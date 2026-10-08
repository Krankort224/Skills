"""Offline branch tests of canonical Markdown implementations; no native API run."""
import os
import re
import unittest

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'assets', 'blocks', 'core')

def load(name):
    with open(os.path.join(ROOT, name + '.md'), 'r') as stream:
        content = stream.read()
    code = re.findall(r'```python\n(.*?)\n```', content, re.S)
    if len(code) != 1:
        raise AssertionError('Exactly one implementation required: ' + name)
    namespace = {}
    exec(compile(code[0], name + '.md', 'exec'), namespace)
    return namespace

class Obj(object):
    def __init__(self, **values): self.__dict__.update(values)

class Id(object):
    def __init__(self, value): self.IntegerValue = value

class Type(object):
    def __init__(self, value, family='Fan', name='A'):
        self.Id = Id(value); self.FamilyName = family; self.Name = name
    def get_Parameter(self, key): return Obj(AsString=lambda: self.Name)

class Parameter(object):
    def __init__(self, value, storage='Integer', readonly=False, broken=False):
        self.value = value; self.StorageType = storage
        self.IsReadOnly = readonly; self.broken = broken
        self.Definition = Obj(GetDataType=lambda: 'length')
    def GetUnitTypeId(self): return 'native'
    def AsInteger(self): return self.value
    def AsDouble(self): return self.value
    def AsString(self): return self.value
    def AsElementId(self): return Id(self.value)
    def Set(self, value):
        if not self.broken: self.value = value
        return True

class CoreTests(unittest.TestCase):
    def test_identity_unique_ambiguous_missing(self):
        n = load('element-identity'); types = [Type(1), Type(2)]
        api = Obj(ElementType=Type, BuiltInParameter=Obj(
            SYMBOL_NAME_PARAM=1, ALL_MODEL_TYPE_NAME=2))
        doc = Obj(GetElement=lambda value: types[0])
        for item in types: item.Document = doc
        resolve = n['resolve_exact_type']
        self.assertEqual(resolve(doc, types, 'Fan', 'A', api)['status'], 'ambiguous')
        self.assertIsNone(resolve(doc, types, 'Fan', 'A', api)['type'])
        self.assertEqual(resolve(doc, types, 'Fan', 'a', api)['status'], 'missing')
        self.assertEqual(resolve(doc, [types[0], types[0]], 'Fan', 'A', api)['status'], 'unique')

    def parameter_context(self, parameter, duplicate=False):
        owner = Obj(GetParameters=lambda key: [parameter] * (2 if duplicate else 1),
                    get_Parameter=lambda key: parameter, GetTypeId=lambda: Id(1))
        units = Obj(IsValidUnit=lambda spec, unit: unit == 'cm',
                    ConvertToInternalUnits=lambda value, unit: value / 100.0,
                    ConvertFromInternalUnits=lambda value, unit: value * 100.0)
        api = Obj(ElementType=Type, ElementId=Id, UnitUtils=units,
                  BuiltInParameter=Obj(TEST=1))
        doc = Obj(GetElement=lambda key: owner, IsModifiable=True)
        owner.Document = doc
        return doc, owner, api

    def test_parameter_statuses_and_scope(self):
        fn = load('parameter-access')['access_parameter']; p = Parameter(1)
        doc, owner, api = self.parameter_context(p)
        def access(**kw):
            return fn(doc, owner, 'instance', {'kind':'name','value':'x'}, api=api, **kw)
        self.assertEqual(access()['status'], 'read')
        self.assertEqual(access(operation='write', value=1)['status'], 'unchanged')
        self.assertEqual(access(operation='write', value=2)['status'], 'planned')
        self.assertEqual(p.value, 1)
        self.assertEqual(access(operation='write', value=2, dry_run=False)['status'], 'changed')
        p.IsReadOnly = True
        self.assertEqual(access(operation='write', value=3)['status'], 'read_only')
        doc, owner, api = self.parameter_context(p, True)
        self.assertEqual(fn(doc,owner,'type',{'kind':'name','value':'x'},api=api)['status'], 'ambiguous')
        with self.assertRaises(ValueError):
            fn(doc,owner,'both',{'kind':'name','value':'x'},api=api)

    def test_parameter_conversion_failed_readback_and_guards(self):
        fn = load('parameter-access')['access_parameter']; p = Parameter(1.0,'Double')
        doc, owner, api = self.parameter_context(p)
        selector = {'kind':'bip','value':'TEST'}
        self.assertEqual(fn(doc,owner,'instance',selector,unit='cm',api=api)['readback'],100.0)
        self.assertEqual(fn(doc,owner,'instance',selector,'write',200.0,unit='cm',dry_run=False,api=api)['status'],'changed')
        p.broken = True
        self.assertEqual(fn(doc,owner,'instance',selector,'write',300.0,unit='cm',dry_run=False,api=api)['status'],'verification_failed')
        with self.assertRaises(ValueError): fn(doc,owner,'instance',selector,api=api)
        with self.assertRaises(ValueError): fn(doc,owner,'instance',selector,unit='bad',api=api)
        p.StorageType='Integer'; p.broken=False
        with self.assertRaises(ValueError): fn(doc,owner,'instance',selector,'write',1.5,api=api)
        doc.IsModifiable=False
        with self.assertRaises(ValueError): fn(doc,owner,'instance',selector,'write',8,dry_run=False,api=api)
        p.StorageType='None'
        self.assertEqual(fn(doc,owner,'instance',selector,api=api)['status'],'unsupported_storage')

    def test_frames_and_bbox(self):
        n=load('coordinate-frames'); f=n['coordinate_frame']((10,20,30),(0,1,0),(-1,0,0))
        local=n['frame_point'](f,(8,23,34))
        self.assertEqual(local,(3.0,2.0,4.0))
        self.assertEqual(n['frame_world'](f,local),(8.0,23.0,34.0))
        self.assertEqual(n['frame_vector'](f,(0,1,0)),(1.0,0.0,0.0))
        with self.assertRaises(ValueError): n['coordinate_frame']((0,0,0),(1,0,0),(1,1,0))
        xyz=lambda x,y,z:Obj(X=x,Y=y,Z=z)
        bbox=Obj(Min=xyz(0,0,0),Max=xyz(1,2,3),Transform=Obj(OfPoint=lambda p:xyz(p.X+10,p.Y,p.Z)))
        link=Obj(GetTotalTransform=lambda:Obj(OfPoint=lambda p:xyz(-p.Y,p.X,p.Z+5)))
        result=n['linked_bbox_corners'](link,bbox,Obj(XYZ=xyz))
        self.assertEqual(len(result['corners']),8)
        self.assertIn((-2.0,11.0,8.0),result['corners'])
        link.GetTotalTransform=lambda:None
        self.assertEqual(n['linked_bbox_corners'](link,bbox,Obj(XYZ=xyz))['status'],'error')

    def test_graph_cycles_shared_boundaries_caps(self):
        fn=load('bounded-graph')['bounded_graph']
        edges=[{'id':str(i),'from':a,'to':b,'provenance':'proximity'}
               for i,(a,b) in enumerate([('a','b'),('b','c'),('c','a')])]
        result=fn(edges,{'one':['a'],'two':['c']})
        self.assertEqual(len(result['edges']),3)
        self.assertEqual(result['ownership']['b'],['one','two'])
        self.assertTrue(all(e['provenance']=='proximity' for e in result['edges']))
        stopped=fn(edges,{'one':['a']},boundary=lambda node,owner:'stop' if node=='a' else 'expand')
        self.assertEqual(stopped['nodes'],['a'])
        excluded=fn(edges,{'one':['a']},boundary=lambda node,owner:'exclude' if node=='b' else 'expand')
        self.assertNotIn('b',excluded['nodes'])
        for cap in ('max_nodes','max_edges','max_visits'):
            self.assertTrue(fn(edges,{'one':['a']},**{cap:0})['truncated'])
        with self.assertRaises(ValueError): fn(edges+edges[:1],{'one':['a']})
        bad=dict(edges[0]);bad['provenance']=''
        with self.assertRaises(ValueError): fn([bad],{'one':['a']})
        directed=dict(edges[0]);directed['directed']=True
        self.assertEqual(fn([directed],{'one':['b']})['nodes'],['b'])

    def test_tables(self):
        n=load('table-payload'); fn=n['table_payload']
        table=[['id','value'],[1,2],[3,4]]
        result=fn(['report',table],'parameters',['id'])
        self.assertEqual(result['source_shape'],'report_table')
        self.assertEqual(n['table_column'](result,'value'),[2,4])
        self.assertEqual(fn([['id']],'empty')['rows'],[])
        for invalid in ([],[['x','x'],[1,2]],[['x'],[1,2]],[['x'],'a']):
            with self.assertRaises(ValueError): fn(invalid,'bad')
        with self.assertRaises(ValueError): fn(table,'bad',['missing'])
        with self.assertRaises(ValueError): fn(table,'bad',['id'],False)

    def test_connectors(self):
        fn=load('physical-connectors')['physical_hvac_graph']
        class SystemOwner(object): pass
        api=Obj(ConnectorType=Obj(End='End',Curve='Curve',Physical='Physical'),
                Domain=Obj(DomainHvac='HVAC'),MEPSystem=SystemOwner)
        document=Obj()
        a,b=Obj(Id=Id(1),Document=document),Obj(Id=Id(2),Document=document)
        def connector(owner,cid,kind='End',domain='HVAC'):
            return Obj(Owner=owner,Id=cid,Domain=domain,ConnectorType=kind,
                       Origin=Obj(X=1,Y=2,Z=3),IsConnected=True,AllRefs=[])
        p,q=connector(a,1),connector(b,1)
        logical=connector(b,2,'Logical'); electrical=connector(b,3,domain='Electrical')
        unconnected=connector(b,4)
        system=connector(SystemOwner(),5);system.Owner.Id=Id(3);system.Owner.Document=document
        p.AllRefs=[q,logical,electrical,unconnected,system]
        p.IsConnectedTo=lambda c:c is q
        q.AllRefs=[p];q.IsConnectedTo=lambda c:c is p
        unconnected.IsConnectedTo=lambda c:False
        a.ConnectorManager=Obj(Connectors=[p]);b.MEPModel=Obj(ConnectorManager=Obj(Connectors=[q]))
        result=fn([a,b],'doc',api)
        self.assertEqual(len(result['edges']),1)
        self.assertEqual(len(result['ports']),2)
        self.assertEqual(result['ports'][0]['origin'],(1.0,2.0,3.0))
        q.IsConnectedTo=lambda c:False
        self.assertEqual(fn([a],'doc',api)['edges'],[])
        self.assertTrue(fn([Obj(Id=Id(9),Document=document)],'doc',api)['warnings'])

    def test_transaction_receipts(self):
        fn=load('transaction-receipt')['transaction_receipt']; calls=[]
        doc=Obj(IsModifiable=False,IsReadOnly=False,Regenerate=lambda:None)
        status=Obj(Started='Started',Committed='Committed',RolledBack='RolledBack',Pending='Pending')
        class Tx(object):
            def __init__(self,doc,name): self.state='New';self.mode=mode[0]
            def Start(self): self.state='Started';return self.state
            def GetFailureHandlingOptions(self): return Obj(SetClearAfterRollback=lambda value:None)
            def SetFailureHandlingOptions(self,options): pass
            def Commit(self):
                self.state={'ok':'Committed','fail':'RolledBack','pending':'Pending'}[self.mode]
                return self.state
            def GetStatus(self): return self.state
            def RollBack(self): calls.append('rollback');self.state='RolledBack';return self.state
            def Dispose(self): calls.append('dispose')
        mode=['ok'];api=Obj(Transaction=Tx,TransactionStatus=status)
        pre=lambda d:{'ok':True};write=lambda d,p:calls.append('write') or 1
        verify=lambda d,r:calls.append('verify') or True
        self.assertEqual(fn(doc,'test',pre,write,verify,api=api)['status'],'dry_run_ready')
        self.assertEqual(calls,[])
        self.assertEqual(fn(doc,'test',pre,write,verify,False,api)['status'],'committed')
        self.assertEqual(fn(doc,'test',pre,write,lambda d,r:False,False,api)['status'],'rolled_back')
        def broken(d,p): raise RuntimeError('write failed')
        self.assertEqual(fn(doc,'test',pre,broken,verify,False,api)['status'],'rolled_back')
        mode[0]='fail'
        self.assertEqual(fn(doc,'test',pre,write,verify,False,api)['status'],'rolled_back')
        mode[0]='pending';calls[:]=[]
        result=fn(doc,'test',pre,write,verify,False,api)
        self.assertEqual(result['status'],'rollback_unconfirmed')
        self.assertNotIn('rollback',calls);self.assertNotIn('dispose',calls)
        doc.IsModifiable=True;calls[:]=[]
        self.assertEqual(fn(doc,'test',pre,write,verify,False,api)['status'],'external_transaction_active')
        self.assertEqual(calls,[])
        doc.IsModifiable=False
        self.assertEqual(fn(doc,'test',lambda d:{'ok':False},write,verify,False,api)['status'],'preflight_failed')

    def test_document_identity_and_64bit_id(self):
        class LargeId(object):
            Value = 2 ** 40
            @property
            def IntegerValue(self):
                raise OverflowError('Legacy access must never occur')
        n = load('element-identity')
        self.assertEqual(n['_identity_id'](LargeId()), 2 ** 40)
        with self.assertRaises(ValueError): n['_identity_id'](Obj())
        doc = Obj(GetElement=lambda key: None)
        foreign = Obj(Document=Obj(), Id=LargeId())
        api = Obj(ElementType=Type)
        with self.assertRaises(ValueError): n['element_identity'](doc, foreign, api)
        with self.assertRaises(ValueError):
            n['resolve_exact_type'](doc, [foreign], 'Fan', 'A', api)
        p = Parameter(1, 'ElementId')
        p.AsElementId = lambda: LargeId()
        fn = load('parameter-access')['access_parameter']
        doc, owner, api = self.parameter_context(p)
        selector = {'kind':'name','value':'x'}
        self.assertEqual(fn(doc,owner,'instance',selector,api=api)['readback'],2 ** 40)
        with self.assertRaises(ValueError): fn(Obj(),owner,'instance',selector,api=api)
        type_owner = Obj(Document=Obj(), GetParameters=owner.GetParameters)
        doc.GetElement = lambda key: type_owner
        with self.assertRaises(ValueError): fn(doc,owner,'type',selector,api=api)

    def test_nonfinite_tolerance_conversion_and_readback(self):
        fn=load('parameter-access')['access_parameter']; p=Parameter(1.0,'Double')
        doc, owner, api=self.parameter_context(p);selector={'kind':'name','value':'x'}
        for bad in (float('nan'),float('inf'),-1):
            with self.assertRaises(ValueError):
                fn(doc,owner,'instance',selector,unit='cm',tolerance=bad,api=api)
        api.UnitUtils.ConvertFromInternalUnits=lambda value,unit:float('inf')
        with self.assertRaises(ValueError): fn(doc,owner,'instance',selector,unit='cm',api=api)
        api.UnitUtils.ConvertFromInternalUnits=lambda value,unit:value*100.0
        api.UnitUtils.ConvertToInternalUnits=lambda value,unit:float('inf')
        with self.assertRaises(ValueError):
            fn(doc,owner,'instance',selector,'write',200.0,unit='cm',dry_run=False,api=api)
        self.assertEqual(p.value,1.0)
        api.UnitUtils.ConvertToInternalUnits=lambda value,unit:value/100.0
        p.Set=lambda value:setattr(p,'value',float('nan')) or True
        with self.assertRaises(ValueError):
            fn(doc,owner,'instance',selector,'write',200.0,unit='cm',dry_run=False,api=api)
        with self.assertRaises(ValueError): fn(doc,owner,'instance',selector,internal_units=True,api=api)

    def test_physical_graph_mixed_document_and_large_ids(self):
        fn=load('physical-connectors')['physical_hvac_graph']
        api=Obj(ConnectorType=Obj(End='End'),Domain=Obj(DomainHvac='HVAC'),MEPSystem=Type)
        d1,d2=Obj(),Obj()
        with self.assertRaises(ValueError):
            fn([Obj(Id=Id(1),Document=d1),Obj(Id=Id(1),Document=d2)],'same',api)
        class LargeId(object):
            Value=2 ** 40
            @property
            def IntegerValue(self): raise OverflowError('eager legacy access')
        owner=Obj(Id=LargeId(),Document=d1)
        c=Obj(Owner=owner,Id=1,Domain='HVAC',ConnectorType='End',AllRefs=[],
              Origin=Obj(X=0,Y=0,Z=0),IsConnected=False)
        owner.ConnectorManager=Obj(Connectors=[c])
        result=fn([owner],'d1',api)
        self.assertEqual(result['warnings'],[])
        self.assertEqual(result['ports'][0]['owner_id'],2 ** 40)

    def test_throwing_connector_filter_warns_about_partial_graph(self):
        fn=load('physical-connectors')['physical_hvac_graph']
        api=Obj(ConnectorType=Obj(End='End'),Domain=Obj(DomainHvac='HVAC'),MEPSystem=Type)
        class BrokenConnector(object):
            @property
            def Domain(self): raise RuntimeError('Domain inaccessible')
        owner=Obj(Id=Id(1),Document=Obj(),ConnectorManager=Obj(Connectors=[BrokenConnector()]))
        result=fn([owner],'doc',api)
        self.assertEqual(result['ports'],[])
        self.assertTrue(any('connector-filter-read' in warning for warning in result['warnings']))

    def test_failed_rollback_retains_transaction_and_statuses(self):
        fn=load('transaction-receipt')['transaction_receipt'];calls=[]
        doc=Obj(IsModifiable=False,IsReadOnly=False,Regenerate=lambda:None)
        status=Obj(Started='Started',Committed='Committed',RolledBack='RolledBack',Pending='Pending')
        behavior=['throws']
        class Tx(object):
            def __init__(self,d,n): self.state='New'
            def Start(self): self.state='Started';return 'Started'
            def GetStatus(self): return self.state
            def GetFailureHandlingOptions(self): return Obj(SetClearAfterRollback=lambda value:None)
            def SetFailureHandlingOptions(self,o): pass
            def RollBack(self):
                calls.append('rollback')
                if behavior[0]=='throws': raise RuntimeError('rollback failure')
                return 'Started'
            def Dispose(self): calls.append('dispose')
        api=Obj(Transaction=Tx,TransactionStatus=status)
        for mode in ('throws','stays_started'):
            behavior[0]=mode;calls[:]=[]
            result=fn(doc,'test',lambda d:{'ok':True},lambda d,p:1,lambda d,r:False,False,api)
            self.assertIn('unresolved_transaction',result)
            self.assertNotIn('dispose',calls)
            self.assertEqual(result['start_status'],'Started')
            self.assertEqual(result['current_status'],'Started')
            self.assertIsNone(result['commit_status'])

    def test_commit_finalizer_status_is_not_assumed(self):
        fn=load('transaction-receipt')['transaction_receipt'];calls=[]
        doc=Obj(IsModifiable=False,IsReadOnly=False,Regenerate=lambda:None)
        status=Obj(Started='Started',Committed='Committed',RolledBack='RolledBack',Pending='Pending')
        class Tx(object):
            def __init__(self,d,n): self.state='New'
            def Start(self): self.state='Started';return 'Started'
            def GetStatus(self): return self.state
            def GetFailureHandlingOptions(self): return Obj(SetClearAfterRollback=lambda value:None)
            def SetFailureHandlingOptions(self,o): pass
            def Commit(self): self.state='RolledBack';return 'Committed'
            def Dispose(self): calls.append('dispose')
        api=Obj(Transaction=Tx,TransactionStatus=status)
        result=fn(doc,'test',lambda d:{'ok':True},lambda d,p:1,lambda d,r:True,False,api)
        self.assertFalse(result['committed'])
        self.assertEqual(result['status'],'rolled_back')
        self.assertEqual(result['commit_status'],'Committed')
        self.assertEqual(result['current_status'],'RolledBack')

if __name__ == '__main__':
    unittest.main()
