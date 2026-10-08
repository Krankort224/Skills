"""Offline tests: execute the exact Python fences shipped in MEP blocks."""
import copy
import pathlib
import re
import sys
from unittest import mock
import types
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def block(name):
    path = ROOT / 'assets' / 'blocks' / 'mep' / (name + '.md')
    fences = re.findall(r'```python\n(.*?)\n```', path.read_text(), re.S)
    if len(fences) != 1:
        raise AssertionError('Expected exactly one implementation fence: ' + name)
    namespace = {'__name__': 'offline_' + name.replace('-', '_')}
    exec(compile(fences[0], str(path), 'exec'), namespace)
    return namespace


class MepReadTests(unittest.TestCase):
    def test_cover_both_directions_and_missing_reference(self):
        m = block('host-cover-map')
        covers = [types.SimpleNamespace(Id=10, HostElementId=1),
                  types.SimpleNamespace(Id=11, HostElementId=1)]
        result = m['cover_maps']([1, 2], covers, lambda i: object(),
                                  {1: 'MISSING_REFERENCE'}, True)
        self.assertEqual(result['host_to_covers'][1]['cover_ids'], [10,11])
        self.assertEqual(result['cover_to_host'], {10:1,11:1})
        self.assertEqual(result['host_to_covers'][1]['actual_status'], 'PRESENT')
        self.assertEqual(result['host_to_covers'][2]['actual_status'], 'ABSENT')

    def test_partial_cover_scope_cannot_prove_absence(self):
        m = block('host-cover-map')
        self.assertEqual(m['cover_maps']([1], [], lambda i: None)
                         ['host_to_covers'][1]['actual_status'], 'UNKNOWN_SCOPE')

    def test_cover_unavailable_host_and_duplicates(self):
        m = block('host-cover-map')
        cover = types.SimpleNamespace(Id=10, HostElementId=99)
        r = m['cover_maps']([1], [cover, cover], lambda i: None, complete_scope=True)
        self.assertEqual(len(r['issues']), 1)
        self.assertIsNone(r['cover_to_host'][10])
        self.assertEqual(r['host_to_covers'][1]['actual_status'], 'UNKNOWN_SCOPE')

    def test_nested_roots_parents_and_cycle(self):
        m = block('nested-hierarchy')
        graph = {1:[2,3], 2:[4], 3:[4], 4:[1], 9:[4]}
        r = m['trace_nested']([1,9], lambda i:i, lambda i:graph[i])
        rows = {row['id']:row for row in r['records']}
        self.assertEqual(rows[4]['roots'], [1,9])
        self.assertEqual(rows[4]['parents'], [2,3,9])
        self.assertTrue(rows[4]['multiple_parents'])
        self.assertTrue(r['cycles'])
        self.assertFalse(r['complete'])

    def test_nested_supplement_and_limits(self):
        m = block('nested-hierarchy')
        r = m['trace_nested']([1], lambda i:i, lambda i:[], [(1,2),(2,3)], max_nodes=2)
        self.assertEqual(len(r['records']), 2)
        self.assertEqual(r['issues'][0]['status'], 'NODE_LIMIT')
        r = m['trace_nested']([1], lambda i:i, lambda i:[i+1], max_depth=1)
        self.assertEqual(r['issues'][0]['status'], 'DEPTH_LIMIT')
        with self.assertRaises(ValueError):
            m['trace_nested']([], lambda i:i, lambda i:[], max_nodes=0)

    def test_nested_api_missing_and_error(self):
        m = block('nested-hierarchy')
        r = m['trace_nested']([1], lambda i:None, lambda i:[])
        self.assertFalse(r['complete'])
        self.assertEqual(r['issues'][0]['status'], 'API_ERROR')

    def test_signature_canonical_dedupe_area(self):
        m = block('connector-size-signature')
        r = m['size_signatures']([
            {'id':1,'shape':'Rectangular','width_mm':100,'height_mm':200},
            {'id':2,'shape':'Rectangular','width_mm':200.05,'height_mm':100},
            {'id':3,'shape':'Round','diameter_mm':50}])
        self.assertEqual([x['shape'] for x in r['signatures']], ['Round','Rectangular'])
        self.assertEqual(r['signatures'][1]['connector_ids'], [1,2])
        self.assertEqual(r['signatures'][1]['dimensions_mm'], [200,100])

    def test_signature_filters_axes_and_invalid(self):
        m = block('connector-size-signature')
        r = m['size_signatures']([
            {'shape':'Oval'}, {'shape':'Round','diameter_mm':-1},
            {'shape':'Round','diameter_mm':float('nan')},
            {'shape':'Round','diameter_mm':2,'logical':True}])
        self.assertEqual(len(r['rejected']), 4)
        records = [{'shape':'Rectangular','width_mm':100,'height_mm':200},
                   {'shape':'Rectangular','width_mm':200,'height_mm':100}]
        self.assertEqual(len(m['size_signatures'](records, preserve_axes=True)['signatures']),2)

    def test_connector_adapter_unsupported_and_api_failure(self):
        m = block('connector-size-signature')
        c = types.SimpleNamespace(Id=1,Shape='Round',ConnectorType='End',
                                  Domain='DomainHvac',Radius=1)
        e = types.SimpleNamespace(ConnectorManager=types.SimpleNamespace(Connectors=[c,object()]))
        r = m['connector_size_records'](e)
        self.assertAlmostEqual(r['records'][0]['diameter_mm'],609.6)
        self.assertEqual(len(r['issues']),1)
        self.assertEqual(m['connector_size_records'](object())['issues'],['NO_CONNECTOR_MANAGER'])

    def target(self):
        return {'point_mm':[0,0,0],'family':'F','type':'T','system':'S','size_mm':[100,200]}

    def candidate(self, ident=1, x=0):
        r = self.target();r.update(id=ident,point_mm=[x,0,0]);return r

    def test_position_semantics_and_id_provenance(self):
        m = block('positional-resolution');t = self.target();t['element_id']=99
        wrong = self.candidate(99);wrong['system']='OTHER'
        r = m['resolve_position'](t,[wrong,self.candidate(1,3)])
        self.assertEqual((r['status'],r['id']),('FOUND',1))
        self.assertEqual(r['method'],'POINT_DISTANCE_AND_EXACT_FILTERS')

    def test_position_ambiguous_missing_occupied(self):
        m = block('positional-resolution');fn = m['resolve_position'];t = self.target()
        self.assertEqual(fn(t,[self.candidate(1),self.candidate(2,1)])['status'],'AMBIGUOUS')
        self.assertEqual(fn(t,[self.candidate(1,6)])['status'],'NOT_FOUND')
        self.assertEqual(fn(t,[self.candidate(1)],{1})['status'],'OCCUPIED')
        del t['system'];self.assertEqual(fn(t,[])['status'],'INVALID_TARGET')

    def test_position_occupancy_size_and_bad_index(self):
        m = block('positional-resolution');t = self.target();c = self.candidate()
        original=set();r=m['resolve_positions']([t,t],[c],original)
        self.assertEqual([x['status'] for x in r['results']],['FOUND','OCCUPIED'])
        self.assertEqual(original,set())
        c['size_mm']=[200,100]
        self.assertEqual(m['resolve_position'](t,[c])['status'],'NOT_FOUND')
        self.assertEqual(m['resolve_position'](t,[c,c])['status'],'INVALID_CANDIDATES')
        with self.assertRaises(ValueError):m['resolve_position'](t,[],tolerance_mm=-1)


class Parameter(object):
    def __init__(self, value, storage):
        self.value=value;self.StorageType=storage;self.IsReadOnly=False
    def AsElementId(self):return self.value
    def Set(self,value):self.value=value;return True


class Level(object):
    def __init__(self, ident, elevation):self.Id=ident;self.Elevation=elevation


class FamilyInstance(object):
    def __init__(self):
        self.Id=10;self.UniqueId='U10';self.Pinned=False;self.GroupId=-1
        self.Location=types.SimpleNamespace(Point=types.SimpleNamespace(X=1,Y=2,Z=15))
        self.params={'level':Parameter(1,'ElementId'),'offset':Parameter(15,'Double')}
    def get_Parameter(self,bip):return self.params[bip]


class SubTransaction(object):
    def __init__(self,doc):self.doc=doc;doc.last_tx=self
    def GetStatus(self):return getattr(self,'status','Uninitialized')
    def Start(self):
        self.saved=copy.deepcopy({k:v for k,v in self.doc.element.__dict__.items() if k!='Document'})
        self.status='Started';return 'Started'
    def Commit(self):self.status='Committed';return 'Committed'
    def RollBack(self):
        self.doc.element.__dict__.update(self.saved)
        self.status='RolledBack';return 'RolledBack'
    def Dispose(self):self.disposed=True


class Doc(object):
    def __init__(self):
        self.element=FamilyInstance();self.levels={1:Level(1,0),2:Level(2,10)}
        self.IsModifiable=True;self.changed_z=False
        self.ProjectInformation=types.SimpleNamespace(UniqueId="PROJECT_UID")
        self.element.Document=self
        for level in self.levels.values():level.Document=self
    def GetElement(self,ident):return self.element if ident==10 else self.levels.get(ident)
    def Regenerate(self):
        if self.changed_z:self.element.Location.Point.Z=999


API=types.SimpleNamespace(FamilyInstance=FamilyInstance,Level=Level,ElementId=lambda i:i,
    BuiltInParameter=types.SimpleNamespace(FAMILY_LEVEL_PARAM='level',INSTANCE_ELEVATION_PARAM='offset'),
    SubTransaction=SubTransaction,TransactionStatus=types.SimpleNamespace(Started='Started',Committed='Committed',
        Pending='Pending',RolledBack='RolledBack',Uninitialized='Uninitialized'))


class ReferenceLevelTests(unittest.TestCase):
    def setUp(self):self.m=block('reference-level');self.doc=Doc()
    def plan(self):return self.m['plan_reference_level'](self.doc.element,list(self.doc.levels.values()),lambda e:True,API)
    def test_unsorted_level_choice_and_below(self):
        levels=[Level(2,10),Level(1,0)]
        level,offset=self.m['choose_reference_level'](15,levels)
        self.assertEqual((level.Id,offset),(2,5))
        level,offset=self.m['choose_reference_level'](-2,levels)
        self.assertEqual((level.Id,offset),(1,-2))
        with self.assertRaises(ValueError):self.m['choose_reference_level'](1,[Level(1,0),Level(2,0)])
    def test_plan_readonly_and_pinned_incompatible(self):
        self.assertEqual(self.plan()['new_offset_ft'],5)
        self.assertEqual(self.doc.element.params['level'].value,1)
        self.doc.element.Pinned=True;self.assertEqual(self.plan()['status'],'SKIP_PINNED')
        self.assertEqual(self.m['plan_reference_level'](self.doc.element,[],lambda e:False,API)['status'],'SKIP_INCOMPATIBLE')
    def test_default_dry_run_and_missing_outer_transaction(self):
        p=self.plan();self.assertEqual(self.m['execute_reference_level'](self.doc,p,lambda e:True,api=API)['status'],'DRY_RUN')
        self.doc.IsModifiable=False
        with self.assertRaises(ValueError):self.m['execute_reference_level'](self.doc,p,lambda e:True,True,api=API)
    def test_native_mock_success(self):
        r=self.m['execute_reference_level'](self.doc,self.plan(),lambda e:True,True,api=API)
        self.assertEqual(r['status'],'STAGED_VERIFIED');self.assertTrue(r['outer_commit_required'])
        self.assertEqual(self.doc.element.params['level'].value,2)
        self.assertEqual(self.doc.element.params['offset'].value,5)
    def test_changed_z_rolls_back(self):
        self.doc.changed_z=True
        r=self.m['execute_reference_level'](self.doc,self.plan(),lambda e:True,True,api=API)
        self.assertEqual(r['status'],'ROLLED_BACK');self.assertEqual(self.doc.element.Location.Point.Z,15)
        self.assertEqual(self.doc.element.params['level'].value,1)
    def test_stale_level_and_unwritable(self):
        p=self.plan();self.doc.levels[2].Elevation=11
        r=self.m['execute_reference_level'](self.doc,p,lambda e:True,True,api=API)
        self.assertEqual(r['status'],'ROLLED_BACK')
        self.doc.element.params['offset'].IsReadOnly=True
        self.assertEqual(self.plan()['status'],'SKIP_ERROR')


class FailureAndScopeTests(unittest.TestCase):
    def setUp(self):
        self.m=block('reference-level');self.doc=Doc()
        self.plan=self.m['plan_reference_level'](self.doc.element,list(self.doc.levels.values()),lambda e:True,API)
    def execute(self, transaction_class):
        api=types.SimpleNamespace(**API.__dict__);api.SubTransaction=transaction_class
        return self.m['execute_reference_level'](self.doc,self.plan,lambda e:True,True,api=api)
    def test_start_rejection_is_transaction_failed(self):
        class RejectStart(SubTransaction):
            def Start(self):return 'Uninitialized'
        r=self.execute(RejectStart)
        self.assertEqual(r['status'],'TRANSACTION_FAILED')
        self.assertEqual(r['start_status'],'Uninitialized')
        self.assertIsNone(r['rollback_status']);self.assertTrue(r['disposed'])
    def test_unconfirmed_rollback_keeps_active_handle(self):
        class RejectRollback(SubTransaction):
            def RollBack(self):return 'Started'
        self.doc.changed_z=True;r=self.execute(RejectRollback)
        self.assertEqual(r['status'],'ROLLBACK_UNCONFIRMED')
        self.assertEqual(r['rollback_status'],'Started')
        self.assertEqual(r['current_status'],'Started')
        self.assertIn('transaction_handle',r)
        self.assertFalse(getattr(self.doc.last_tx,'disposed',False))
    def test_rollback_exception_keeps_handle_and_error(self):
        class ThrowRollback(SubTransaction):
            def RollBack(self):raise RuntimeError('rollback failure fixture')
        self.doc.changed_z=True;r=self.execute(ThrowRollback)
        self.assertEqual(r['status'],'ROLLBACK_FAILED')
        self.assertIn('rollback failure fixture',r['rollback_error'])
        self.assertIn('transaction_handle',r)
        self.assertFalse(getattr(self.doc.last_tx,'disposed',False))
    def test_pending_commit_keeps_owner_handle(self):
        class PendingCommit(SubTransaction):
            def Commit(self):self.status='Pending';return 'Pending'
        r=self.execute(PendingCommit)
        self.assertEqual(r['status'],'TRANSACTION_PENDING')
        self.assertEqual(r['commit_status'],'Pending')
        self.assertIn('transaction_handle',r)
        self.assertFalse(getattr(self.doc.last_tx,'disposed',False))
    def test_different_document_with_same_project_uid_rejected(self):
        other=Doc()
        r=self.m['execute_reference_level'](other,self.plan,lambda e:True,True,api=API)
        self.assertEqual(r['status'],'DOCUMENT_MISMATCH')
        self.assertFalse(hasattr(other,'last_tx'))
    def test_foreign_level_rejected_during_plan(self):
        other=Doc()
        r=self.m['plan_reference_level'](self.doc.element,list(other.levels.values()),lambda e:True,API)
        self.assertEqual(r['status'],'SKIP_ERROR')
        self.assertIn('another document',r['error'])
    def test_invalid_candidate_hides_second_match(self):
        m=block('positional-resolution')
        target={'point_mm':[0,0,0],'family':'F','type':'T','system':'S'}
        candidate=dict(target,id=1)
        r=m['resolve_position'](target,[candidate,{'id':2,'point_mm':[0,0]}])
        self.assertEqual(r['status'],'INVALID_CANDIDATES');self.assertNotIn('id',r)
    def test_invalid_candidate_without_match_is_unsafe(self):
        m=block('positional-resolution')
        target={'point_mm':[0,0,0],'family':'F','type':'T','system':'S'}
        self.assertEqual(m['resolve_position'](target,[{'id':2}])['status'],'INVALID_CANDIDATES')
    def test_missing_candidate_identity_is_unsafe(self):
        m=block('positional-resolution')
        target={'point_mm':[0,0,0],'family':'F','type':'T','system':'S'}
        malformed={'id':2,'point_mm':[0,0,0],'family':'F','type':'T'}
        self.assertEqual(m['resolve_position'](target,[dict(target,id=1),malformed])['status'],'INVALID_CANDIDATES')
    def test_unknown_native_status_never_disposes(self):
        class UnknownStatus(SubTransaction):
            def GetStatus(self):raise RuntimeError('unknown native state fixture')
        r=self.execute(UnknownStatus)
        self.assertEqual(r['status'],'ROLLBACK_UNCONFIRMED')
        self.assertIn('transaction_handle',r)
        self.assertFalse(getattr(self.doc.last_tx,'disposed',False))
    def test_native_commit_rollback_is_confirmed(self):
        class CommitRollback(SubTransaction):
            def Commit(self):
                self.RollBack();return 'RolledBack'
        r=self.execute(CommitRollback)
        self.assertEqual(r['status'],'ROLLED_BACK')
        self.assertEqual(r['commit_status'],'RolledBack')
        self.assertEqual(r['current_status'],'RolledBack')
        self.assertTrue(r['disposed'])
    def cover_api_modules(self):
        class Cover(object):pass
        autodesk=types.ModuleType('Autodesk');revit=types.ModuleType('Autodesk.Revit')
        revit.DB=types.SimpleNamespace(InsulationLiningBase=Cover);autodesk.Revit=revit
        return {'Autodesk':autodesk,'Autodesk.Revit':revit},Cover
    def test_native_cover_collector_foreign_host_rejected(self):
        m=block('host-cover-map');mods,Cover=self.cover_api_modules()
        host=types.SimpleNamespace(Id=1,Document=object())
        with mock.patch.dict(sys.modules,mods):
            with self.assertRaisesRegex(ValueError,'Host belongs'):
                m['collect_host_covers'](object(),[host],[])
    def test_native_cover_collector_foreign_cover_rejected(self):
        m=block('host-cover-map');mods,Cover=self.cover_api_modules();doc=object()
        host=types.SimpleNamespace(Id=1,Document=doc);cover=Cover()
        cover.Id=2;cover.Document=object();cover.HostElementId=1
        with mock.patch.dict(sys.modules,mods):
            with self.assertRaisesRegex(ValueError,'Cover belongs'):
                m['collect_host_covers'](doc,[host],[cover])


if __name__=='__main__':unittest.main()

