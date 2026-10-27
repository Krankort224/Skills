"""Offline protocol tests of canonical fences, with no CLR/native runtime claim."""
import unittest
from test_core_blocks import load, Obj, Type, Element, Id, install_clr_mock, PropertyMetadata


class Descriptor(object):
    def __init__(self, value=None, error=None):
        self.value = value
        self.error = error
        self.calls = 0
    def GetValue(self, owner):
        self.calls += 1
        if self.error is not None:
            raise self.error
        return self.value


def contract(descriptor, readable=True):
    return type('Contract', (object,), {
        '__clr_property_test_metadata__': {'Name': readable},
        'Name': descriptor})


class ClrPropertyTests(unittest.TestCase):
    def setUp(self):
        install_clr_mock(self)
        self.read = load('clr-property-access')['read_clr_property']

    def test_explicit_selection_ignores_shadowed_and_wrong_dynamic_value(self):
        for dynamic in ('error', 'wrong'):
            descriptor = Descriptor('base name')
            base = contract(descriptor)
            class Derived(base):
                direct_calls = 0
                @property
                def Name(self):
                    self.direct_calls += 1
                    if dynamic == 'error':
                        raise AttributeError('unreadable derived property')
                    return 'wrong dynamic name'
            owner = Derived()
            result = self.read(owner, 'Name', base)
            self.assertEqual(result['status'], 'declared_getter_value')
            self.assertEqual(result['value'], 'base name')
            self.assertTrue(result['access_path'].endswith('.Name.GetValue'))
            self.assertIn('Contract', result['access_path'])
            self.assertEqual(owner.direct_calls, 0)
            self.assertEqual(descriptor.calls, 1)

    def test_direct_attribute_error_is_uncertain_and_called_once(self):
        class Broken(object):
            calls = 0
            @property
            def Name(self):
                self.calls += 1
                raise AttributeError('getter internal error or binder error')
        owner = Broken()
        result = self.read(owner, 'Name')
        self.assertEqual(result['status'], 'direct_access_error')
        self.assertEqual(result['error_type'], 'AttributeError')
        self.assertIn('getter internal error', result['error_text'])
        self.assertEqual(owner.calls, 1)
        self.assertEqual(self.read(Obj(), 'absent')['status'], 'direct_access_error')

    def test_absence_unavailable_and_throwing_getter_are_distinct(self):
        descriptor = Descriptor(error=AttributeError('native getter failed'))
        base = contract(descriptor)
        owner = base()
        self.assertEqual(self.read(owner, 'Absent', base)['status'], 'property_missing')
        result = self.read(owner, 'Name', base)
        self.assertEqual(result['status'], 'getter_error')
        self.assertEqual(result['stage'], 'getter_invocation')
        self.assertEqual(result['error_type'], 'AttributeError')
        for descriptor, readable in ((Descriptor(), False), (Obj(), True),
                                     (Obj(GetValue=None), True)):
            base = contract(descriptor, readable)
            self.assertEqual(self.read(base(), 'Name', base)['status'], 'getter_unavailable')

    def test_metadata_descriptor_lookup_and_configuration_errors(self):
        class BrokenMetadata(dict):
            def __contains__(self, key): raise RuntimeError('metadata unavailable')
        base = type('BadMetadata', (object,), {
            '__clr_property_test_metadata__': BrokenMetadata()})
        result = self.read(base(), 'Name', base)
        self.assertEqual(result['status'], 'metadata_error')
        self.assertEqual(result['stage'], 'metadata')
        base = type('NoDescriptor', (object,), {'__clr_property_test_metadata__': {'Name': True}})
        result = self.read(base(), 'Name', base)
        self.assertEqual(result['status'], 'metadata_error')
        self.assertEqual(result['stage'], 'descriptor_lookup')
        for args in ((None, 'Name'), (Obj(), ''), (Obj(), 3),
                     (Obj(), 'Name', 1), (Obj(), 'Name', Type)):
            self.assertEqual(self.read(*args)['status'], 'configuration_error')

    def test_values_and_no_fallback_after_explicit_failure(self):
        for value in (None, '', 0, False):
            base = contract(Descriptor(value))
            result = self.read(base(), 'Name', base)
            self.assertEqual(result['status'], 'returned_null' if value is None else 'declared_getter_value')
            self.assertIs(result['value'], value)
            result = self.read(Obj(Name=value), 'Name')
            self.assertEqual(result['status'], 'returned_null' if value is None else 'direct_value')
        base = contract(Descriptor(error=RuntimeError('unavailable now')))
        class Derived(base):
            @property
            def Name(self): raise AssertionError('Direct fallback is forbidden')
        result = self.read(Derived(), 'Name', base)
        self.assertEqual(result['status'], 'getter_error')
        self.assertEqual(result['error_type'], 'RuntimeError')


class IdentityPropertyTests(unittest.TestCase):
    def setUp(self):
        install_clr_mock(self)
        self.ns = load('element-identity')
        self.api = Obj(Element=Element, ElementType=Type,
                       BuiltInParameter=Obj(SYMBOL_NAME_PARAM=1))
        self.doc = Obj(GetElement=lambda key: None)

    def native_type(self, value=1, family='Fan', name='A'):
        result = Type(value, family, name)
        result.Document = self.doc
        return result

    def test_identity_uses_selected_element_name_and_bip_precedence(self):
        class ShadowType(Type):
            calls = 0
            @property
            def Name(self):
                self.calls += 1
                raise AttributeError('derived Name is write-only')
            @Name.setter
            def Name(self, value): pass
        item = ShadowType(1)
        item.Document = self.doc
        item.get_Parameter = lambda key: Obj(AsString=lambda: 'BIP name')
        identity = self.ns['element_identity'](self.doc, item, self.api)
        self.assertEqual(identity['element_name'], 'A')
        self.assertEqual(identity['type_name'], 'BIP name')
        self.assertEqual(item.calls, 0)
        self.assertEqual(identity['name_results']['type_name']['access_path'], 'SYMBOL_NAME_PARAM')
        item.get_Parameter = lambda key: None
        self.assertEqual(self.ns['element_identity'](self.doc, item, self.api)['type_name'], 'A')
        self.assertEqual(item.calls, 0)

    def test_incomplete_candidate_prevents_unique_and_missing(self):
        good = self.native_type()
        bad = self.native_type(2)
        del bad.FamilyName
        resolve = self.ns['resolve_exact_type']
        for candidates in ([good, bad], [bad]):
            result = resolve(self.doc, candidates, 'Fan', 'A', self.api)
            self.assertEqual(result['status'], 'indeterminate')
            self.assertIsNone(result['type'])
            self.assertEqual(len(result['incomplete']), 1)
            failure = result['incomplete'][0]
            self.assertEqual(failure['name_results']['family_name']['status'], 'direct_access_error')
            self.assertTrue(failure['warnings'])

    def test_failed_type_name_and_parameter_error_are_structured(self):
        item = self.native_type()
        def broken(key): raise RuntimeError('parameter lookup failed')
        item.get_Parameter = broken
        del item._native_name
        identity = self.ns['element_identity'](self.doc, item, self.api)
        result = identity['name_results']['type_name']
        self.assertEqual(result['status'], 'getter_error')
        self.assertEqual(result['attempts'][0]['status'], 'parameter_error')
        self.assertTrue(identity['warnings'])
        self.assertEqual(self.ns['resolve_exact_type'](
            self.doc, [item], 'Fan', 'A', self.api)['status'], 'indeterminate')

    def test_empty_null_and_family_object_precedence(self):
        for value in ('', None):
            item = self.native_type(family=value, name=value)
            item.get_Parameter = lambda key: None
            identity = self.ns['element_identity'](self.doc, item, self.api)
            expected = 'returned_null' if value is None else 'declared_getter_value'
            self.assertEqual(identity['name_results']['type_name']['status'], expected)
            self.assertEqual(identity['name_results']['family_name']['status'],
                             'returned_null' if value is None else 'direct_value')
            self.assertEqual(self.ns['resolve_exact_type'](
                self.doc, [item], 'Fan', 'A', self.api)['status'], 'missing')
        item = self.native_type(family='system fallback')
        item.Family = Obj(Name='object family')
        self.assertEqual(self.ns['element_identity'](
            self.doc, item, self.api)['family_name'], 'object family')

    def test_type_resolution_document_and_64bit_guards(self):
        class LargeId(object):
            Value = 2 ** 40
            @property
            def IntegerValue(self): raise AssertionError('legacy ID access')
        item = self.native_type()
        item.Id = LargeId()
        self.assertEqual(self.ns['element_identity'](self.doc, item, self.api)['type_id'], 2 ** 40)
        foreign = self.native_type()
        foreign.Document = Obj()
        with self.assertRaises(ValueError):
            self.ns['element_identity'](self.doc, foreign, self.api)
        instance = Element()
        instance.Document = self.doc
        instance.Id = Id(9)
        instance._native_name = 'instance'
        instance.GetTypeId = lambda: Id(1)
        self.doc.GetElement = lambda key: foreign
        with self.assertRaises(ValueError):
            self.ns['element_identity'](self.doc, instance, self.api)
        self.doc.GetElement = lambda key: None
        identity = self.ns['element_identity'](self.doc, instance, self.api)
        self.assertEqual(identity['name_results']['type_name']['status'], 'type_unavailable')
        with self.assertRaises(ValueError):
            self.ns['resolve_exact_type'](self.doc, [item], '', 'A', self.api)


if __name__ == '__main__':
    unittest.main()
