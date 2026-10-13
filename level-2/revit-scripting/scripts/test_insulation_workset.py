"""Execute the canonical Markdown fence; native behavior is mocked, not claimed."""
import pathlib
import re
import types
import unittest
import sys
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]


def block():
    path = ROOT / 'assets/blocks/mep/insulation-workset.md'
    fences = re.findall(r'```python\n(.*?)\n```', path.read_text(), re.S)
    if len(fences) != 1:
        raise AssertionError('One canonical implementation fence required')
    namespace = {}
    exec(compile(fences[0], str(path), 'exec'), namespace)
    return namespace


class Id:
    def __init__(self, value): self.IntegerValue = value


class Host:
    def __init__(self, doc, ident, workset):
        self.Document = doc; self.Id = Id(ident); self.UniqueId = 'H' + str(ident)
        self.WorksetId = Id(workset); self.readonly = False
        self.failure = None; self.writes = []; self.parameter_reads = 0
    def get_Parameter(self, bip):
        self.parameter_reads += 1
        def write(value):
            self.writes.append(value)
            if self.failure == 'restore' and len(self.writes) == 2:
                return False
            self.WorksetId = Id(value)
            return self.failure != 'mutate_then_false'
        return types.SimpleNamespace(IsReadOnly=self.readonly, StorageType='Integer', Set=write)


class Cover:
    def __init__(self, doc, ident, host, workset):
        self.Document = doc; self.Id = Id(ident); self.UniqueId = 'I' + str(ident)
        self.HostElementId = host.Id; self.WorksetId = Id(workset)
        self.type_id = 24139; self.Thickness = 16.0 / 304.8
    def GetTypeId(self): return Id(self.type_id)
    def get_Parameter(self, bip): raise AssertionError('Do not write insulation workset')


class PipeCover(Cover):
    pass


class Doc:
    IsFamilyDocument = False
    IsWorkshared = True
    IsReadOnly = False
    IsModifiable = True
    def __init__(self):
        self.items = {}; self.regenerations = 0; self.regeneration_states = []
        self.fail_regeneration = False; self.rollback_failure = None
        self.commit_result = 'Committed'; self.current_result = 'Committed'
        self.subtransactions = []
    def Equals(self, other): return self is other
    def GetElement(self, ident): return self.items.get(ident.IntegerValue)
    def Regenerate(self):
        self.regenerations += 1
        self.regeneration_states.append({k:e.WorksetId.IntegerValue for k,e in self.items.items()})
        if self.fail_regeneration: raise RuntimeError('Regeneration failed')
    def outer_commit(self, propagate=True):
        self.IsModifiable = False
        if propagate:
            for e in self.items.values():
                if isinstance(e, Cover): e.WorksetId = self.items[e.HostElementId.IntegerValue].WorksetId


class Sub:
    def __init__(self, doc):
        self.doc = doc; self.state = 'Uninitialized'; self.disposed = False
        doc.subtransactions.append(self)
    def Start(self):
        self.saved = {k:e.WorksetId.IntegerValue for k,e in self.doc.items.items()}
        self.state = 'Started'; return self.state
    def GetStatus(self): return self.state
    def Commit(self): self.state = self.doc.current_result; return self.doc.commit_result
    def RollBack(self):
        if self.doc.rollback_failure == 'raise': raise RuntimeError('Rollback failed')
        if self.doc.rollback_failure == 'unfinished': return 'Started'
        for k,value in self.saved.items(): self.doc.items[k].WorksetId = Id(value)
        self.state = 'RolledBack'; return self.state
    def Dispose(self): self.disposed = True


API = types.SimpleNamespace(ElementId=Id, DuctInsulation=Cover, PipeInsulation=PipeCover,
                            SubTransaction=Sub, BuiltInParameter=types.SimpleNamespace(ELEM_PARTITION_PARAM='workset'),
                            StorageType=types.SimpleNamespace(Integer='Integer'),
                            TransactionStatus=types.SimpleNamespace(Uninitialized='Uninitialized', Started='Started',
                                Committed='Committed', RolledBack='RolledBack', Pending='Pending'))


class InsulationWorksetTests(unittest.TestCase):
    def setUp(self):
        self.ns = block(); self.doc = Doc()
        self.h1 = Host(self.doc, 1, 174); self.h2 = Host(self.doc, 2, 36898)
        self.i1 = Cover(self.doc, 21, self.h1, 665); self.i2 = Cover(self.doc, 22, self.h2, 665)
        self.doc.items = {e.Id.IntegerValue:e for e in (self.h1,self.h2,self.i1,self.i2)}
    def plan(self, covers=None):
        return self.ns['plan_insulation_worksets'](self.doc, covers or [self.i1,self.i2], API)
    def stage(self, plan=None, execute=True):
        return self.ns['stage_insulation_worksets'](self.doc, plan or self.plan(), execute, API)
    def verify(self, receipt, commit='Committed', current='Committed'):
        return self.ns['verify_insulation_worksets'](self.doc, receipt, commit, current, API)

    def test_preview_is_read_only(self):
        self.doc.IsModifiable = False
        r = self.stage(execute=False)
        self.assertEqual(r['status'], 'DRY_RUN')
        self.assertEqual(self.doc.subtransactions, [])
        self.assertEqual(self.doc.regenerations, 0)
        self.assertEqual(self.h1.writes + self.h2.writes, [])

    def test_default_native_adapter_uses_actual_mechanical_plumbing_namespaces(self):
        # DB root deliberately has no insulation classes; they live in its
        # Mechanical/Plumbing namespaces in the target API, not the mock facade.
        db = types.ModuleType('Autodesk.Revit.DB')
        for name in ('ElementId','SubTransaction','TransactionStatus','BuiltInParameter','StorageType'):
            setattr(db,name,getattr(API,name))
        mechanical = types.ModuleType('Autodesk.Revit.DB.Mechanical')
        mechanical.DuctInsulation = Cover
        plumbing = types.ModuleType('Autodesk.Revit.DB.Plumbing')
        plumbing.PipeInsulation = PipeCover
        autodesk = types.ModuleType('Autodesk'); revit = types.ModuleType('Autodesk.Revit')
        autodesk.Revit = revit; revit.DB = db
        modules = {'Autodesk':autodesk,'Autodesk.Revit':revit,'Autodesk.Revit.DB':db,
                   'Autodesk.Revit.DB.Mechanical':mechanical,'Autodesk.Revit.DB.Plumbing':plumbing}
        with mock.patch.dict(sys.modules,modules):
            plan = self.ns['plan_insulation_worksets'](self.doc,[self.i1,self.i2])
            r = self.ns['stage_insulation_worksets'](self.doc,plan,execute=True)
            self.doc.outer_commit()
            self.assertTrue(self.ns['verify_insulation_worksets'](self.doc,r,'Committed','Committed')['ok'])
        self.assertFalse(hasattr(db,'DuctInsulation'))

    def test_batch_switches_all_before_one_regeneration_and_restores(self):
        r = self.stage()
        self.assertEqual(r['status'], 'STAGED_PENDING_COMMIT')
        self.assertTrue(r['outer_commit_required'])
        self.assertEqual(self.doc.regenerations, 1)
        self.assertEqual(self.doc.regeneration_states[0][1], 665)
        self.assertEqual(self.doc.regeneration_states[0][2], 665)
        self.assertEqual(self.h1.writes, [665,174])
        self.assertEqual(self.h2.writes, [665,36898])
        self.assertEqual(self.h1.WorksetId.IntegerValue, 174)
        self.assertEqual(self.i1.WorksetId.IntegerValue, 665)
        self.doc.outer_commit()
        result = self.verify(r)
        self.assertEqual(result['status'], 'VERIFIED_AFTER_COMMIT')
        self.assertTrue(result['ok'])
        self.assertEqual([x['actual_insulation_workset_id'] for x in result['rows']], [174,36898])

    def test_matching_hosts_are_never_written(self):
        self.i1.WorksetId = Id(174); self.h1.readonly = True
        r = self.stage()
        self.assertEqual(self.h1.parameter_reads, 0)
        self.assertEqual(self.h1.writes, [])
        self.doc.outer_commit(); self.assertTrue(self.verify(r)['ok'])

    def test_no_mismatches_or_no_worksharing_means_no_transaction(self):
        self.i1.WorksetId = Id(174); self.i2.WorksetId = Id(36898)
        self.assertEqual(self.stage()['status'], 'NO_CHANGE')
        self.doc.IsWorkshared = False; self.i1.WorksetId = Id(665)
        self.assertEqual(self.stage()['status'], 'NO_CHANGE')
        self.assertEqual(self.doc.regenerations, 0)
        self.assertEqual(self.doc.subtransactions, [])

    def test_multiple_same_host_same_temporary_workset_deduplicates_host(self):
        other = Cover(self.doc, 23, self.h1, 665); self.doc.items[23] = other
        p = self.plan([self.i1,other,self.i1])
        self.assertEqual(len(p['rows']), 2); self.assertEqual(len(p['hosts']), 1)
        r = self.stage(p)
        self.assertEqual(self.h1.writes, [665,174])
        self.doc.outer_commit(); self.assertTrue(self.verify(r)['ok'])

    def test_same_host_conflicting_temporary_worksets_rejected(self):
        other = Cover(self.doc, 23, self.h1, 666)
        with self.assertRaises(ValueError): self.plan([self.i1,other])
        self.assertEqual(self.h1.writes, [])

    def test_foreign_cover_document_and_missing_host_rejected(self):
        other = Doc(); self.i1.Document = other
        with self.assertRaises(ValueError): self.plan()
        self.i1.Document = self.doc; del self.doc.items[1]
        with self.assertRaises(ValueError): self.plan()

    def test_noncover_or_family_document_rejected(self):
        with self.assertRaises(ValueError): self.plan([self.h1])
        self.doc.IsFamilyDocument = True
        with self.assertRaises(ValueError): self.plan()

    def test_stale_host_cover_identity_and_worksets_rejected_before_mutation(self):
        for element, field, value in [(self.h1,'UniqueId','NEW_HOST'), (self.i1,'UniqueId','NEW_COVER'),
                                      (self.h1,'WorksetId',Id(333)), (self.i1,'WorksetId',Id(777)),
                                      (self.i1,'type_id',999), (self.i1,'Thickness',1.0)]:
            p = self.plan(); original = getattr(element,field); setattr(element,field,value)
            with self.assertRaises(ValueError): self.stage(p)
            setattr(element,field,original)
        self.assertEqual(self.doc.subtransactions, [])

    def test_plan_document_and_active_transaction_requirements(self):
        p = self.plan(); p['_document'] = Doc()
        with self.assertRaises(ValueError): self.stage(p)
        self.doc.IsModifiable = False
        with self.assertRaises(ValueError): self.stage()
        self.doc.IsModifiable = True; self.doc.IsReadOnly = True
        with self.assertRaises(ValueError): self.stage()

    def test_readonly_host_rolls_back_entire_batch(self):
        self.h2.readonly = True
        r = self.stage()
        self.assertEqual(r['status'], 'ROLLED_BACK')
        self.assertEqual(r['rollback_status'], 'RolledBack')
        self.assertEqual(self.h1.WorksetId.IntegerValue, 174)
        self.assertEqual(self.h2.WorksetId.IntegerValue, 36898)
        self.assertEqual(self.doc.regenerations, 0)
        self.assertTrue(self.doc.subtransactions[0].disposed)

    def test_false_set_after_mutation_and_failed_restoration_roll_back(self):
        for failure in ('mutate_then_false','restore'):
            self.h1.failure = failure; self.h1.writes = []
            r = self.stage()
            self.assertEqual(r['status'], 'ROLLED_BACK')
            self.assertEqual(self.h1.WorksetId.IntegerValue, 174)
            self.assertEqual(self.h2.WorksetId.IntegerValue, 36898)

    def test_regeneration_failure_rolls_back_without_more_model_inspection(self):
        self.doc.fail_regeneration = True
        r = self.stage()
        self.assertEqual(r['status'], 'ROLLED_BACK')
        self.assertEqual(self.doc.regenerations, 1)
        self.assertEqual(self.h1.writes, [665])
        self.assertEqual(self.h1.WorksetId.IntegerValue, 174)

    def test_failed_or_unfinished_rollback_retains_handle(self):
        for failure,status in [('raise','ROLLBACK_FAILED'), ('unfinished','ROLLBACK_UNCONFIRMED')]:
            self.doc.rollback_failure = failure; self.h1.readonly = True
            r = self.stage()
            self.assertEqual(r['status'], status)
            self.assertTrue(r['owner_action_required'])
            self.assertFalse(r['transaction_handle'].disposed)

    def test_pending_subtransaction_is_not_disposed_or_verified(self):
        self.doc.commit_result = self.doc.current_result = 'Pending'
        r = self.stage()
        self.assertEqual(r['status'], 'ROLLBACK_UNCONFIRMED')
        self.assertFalse(r['transaction_handle'].disposed)
        self.doc.IsModifiable = False
        self.assertFalse(self.verify(r)['ok'])

    def test_outer_commit_evidence_required(self):
        r = self.stage()
        self.assertEqual(self.verify(r)['status'], 'OUTER_COMMIT_UNCONFIRMED')
        self.doc.outer_commit()
        for returned,current in [('Pending','Pending'),('Committed','RolledBack'),('RolledBack','Committed')]:
            self.assertFalse(self.verify(r,returned,current)['ok'])

    def test_missing_postcommit_propagation_requests_group_rollback(self):
        r = self.stage(); self.doc.outer_commit(propagate=False)
        result = self.verify(r)
        self.assertEqual(result['status'], 'COMMITTED_READBACK_FAILED')
        self.assertTrue(result['group_rollback_required'])

    def test_both_equal_in_wrong_workset_is_not_success(self):
        r = self.stage(); self.doc.outer_commit()
        self.h1.WorksetId = self.i1.WorksetId = Id(666)
        self.assertFalse(self.verify(r)['ok'])

    def test_postcommit_identity_host_binding_type_and_thickness_readback(self):
        r = self.stage(); self.doc.outer_commit()
        for element,field,value in [(self.h1,'UniqueId','CHANGED'),(self.i1,'UniqueId','CHANGED'),
                                    (self.i1,'HostElementId',Id(2)),(self.i1,'type_id',999),
                                    (self.i1,'Thickness',1.0)]:
            old = getattr(element,field); setattr(element,field,value)
            self.assertFalse(self.verify(r)['ok'])
            setattr(element,field,old)
        del self.doc.items[21]; self.assertFalse(self.verify(r)['ok'])

    def test_verify_foreign_document_is_rejected(self):
        r = self.stage(); self.doc.outer_commit()
        other = Doc(); other.IsModifiable = False
        result = self.ns['verify_insulation_worksets'](other,r,'Committed','Committed',API)
        self.assertEqual(result['status'], 'DOCUMENT_MISMATCH')

    def test_pipe_adapter_with_same_contract_offline_only(self):
        cover = PipeCover(self.doc,23,self.h1,665); self.doc.items[23] = cover
        r = self.stage(self.plan([cover]))
        self.doc.outer_commit(); self.assertTrue(self.verify(r)['ok'])


if __name__ == '__main__':
    unittest.main()
