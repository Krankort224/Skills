# CLR property access through an explicit declaration

## Contents

- [Contract](#contract)
- [Purpose](#purpose)
- [Inputs and outputs](#inputs-and-outputs)
- [Implementation](#implementation)
- [Adaptation and limits](#adaptation-and-limits)
- [Verification](#verification)
- [Provenance](#provenance)

## Contract

| Field | Value |
|---|---|
| id | clr-property-access |
| group | core |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 CLR requires separate verification |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Read one CLR property while preserving the distinction between a dynamic access failure, confirmed absence on a selected declaration, unavailable getter and native getter failure. An explicit declaring type selects its descriptor immediately, including when a derived object's dynamic `Name` is inaccessible or misleading.

## Inputs and outputs

`read_clr_property(owner, property_name, declaring_type=None)` returns `status`, `value`, `access_path`, `stage`, `error_type` and `error_text`. A successful non-null value has status `direct_value` or `declared_getter_value` according to the selected path; only a successful `None` is `returned_null`. Empty strings, zero and `False` remain successful values. Errors retain no value. Invalid owner, empty/non-string property name or incompatible declaring type returns `configuration_error`.

Without a declaring type, access the requested attribute exactly once. Any exception, including `AttributeError`, is `direct_access_error`; it proves neither missing metadata nor a binder defect. With a declaring type, inspect only that exact type's declared property metadata, then call its descriptor's `GetValue(owner)`. Never try dynamic owner access or fall back after an explicit-path failure.

`property_missing` requires absent metadata on that selected declaration. `getter_unavailable` means existing metadata has no supported public instance, non-indexed getter, or its descriptor has no callable `GetValue`. `getter_error` records an exception from invocation. `metadata_error` records failures resolving metadata or the selected descriptor. `stage` separates metadata, descriptor lookup, getter lookup and invocation.

## Implementation

```python
# -*- coding: utf-8 -*-
def _clr_error_text(error):
    try:
        return unicode(error)
    except NameError:
        return str(error)


def _clr_result(status, path, stage, value=None, error=None):
    return {'status': status, 'value': value, 'access_path': path,
            'stage': stage,
            'error_type': None if error is None else type(error).__name__,
            'error_text': None if error is None else _clr_error_text(error)}


def read_clr_property(owner, property_name, declaring_type=None):
    path = 'direct' if declaring_type is None else 'declaring_type.GetValue'
    try:
        try:
            string_types = (basestring,)
        except NameError:
            string_types = (str,)
        if owner is None:
            raise ValueError('A non-null owner is required')
        if not isinstance(property_name, string_types) or not property_name:
            raise ValueError('A non-empty property name is required')
        if declaring_type is not None:
            if not isinstance(declaring_type, type):
                raise ValueError('Declaring type must be a type')
            if not isinstance(owner, declaring_type):
                raise ValueError('Owner is incompatible with declaring type')
    except Exception as error:
        return _clr_result('configuration_error', path, 'configuration', error=error)
    path = ('direct.' + property_name if declaring_type is None else
            _clr_error_text(declaring_type) + '.' + property_name + '.GetValue')
    if declaring_type is None:
        try:
            value = getattr(owner, property_name)
        except Exception as error:
            return _clr_result('direct_access_error', path, 'direct_access', error=error)
        return _clr_result('returned_null' if value is None else 'direct_value',
                           path, 'direct_access', value=value)
    try:
        import clr
        from System.Reflection import BindingFlags
        native_type = clr.GetClrType(declaring_type)
        flags = (BindingFlags.DeclaredOnly | BindingFlags.Public |
                 BindingFlags.NonPublic | BindingFlags.Instance |
                 BindingFlags.Static)
        metadata = native_type.GetProperty(property_name, flags)
        present = metadata is not None
        readable = (present and metadata.GetGetMethod() is not None and
                    not metadata.GetGetMethod().IsStatic and
                    len(metadata.GetIndexParameters()) == 0)
    except Exception as error:
        return _clr_result('metadata_error', path, 'metadata', error=error)
    if not present:
        return _clr_result('property_missing', path, 'metadata')
    if not readable:
        return _clr_result('getter_unavailable', path, 'metadata')
    try:
        descriptor = getattr(declaring_type, property_name)
    except Exception as error:
        return _clr_result('metadata_error', path, 'descriptor_lookup', error=error)
    try:
        getter = getattr(descriptor, 'GetValue')
        if not callable(getter):
            raise TypeError('Selected descriptor GetValue is not callable')
    except Exception as error:
        return _clr_result('getter_unavailable', path, 'getter_lookup', error=error)
    try:
        value = getter(owner)
    except Exception as error:
        return _clr_result('getter_error', path, 'getter_invocation', error=error)
    return _clr_result('returned_null' if value is None else 'declared_getter_value',
                       path, 'getter_invocation', value=value)
```

## Adaptation and limits

The bounded CLR adapter uses `clr.GetClrType` and `BindingFlags.DeclaredOnly | Public | NonPublic | Instance | Static`; it rejects non-public, static and indexed getters and does not scan the MRO, search alternate types, invoke setters, resolve arbitrary overloads or reflect its way around a failed getter. Select the actual declaration, for example `read_clr_property(element, 'Name', api.Element)` to invoke `api.Element.Name.GetValue(element)`. Inherited properties require their declaring type. A metadata failure is not absence. Native exceptions remain diagnostic errors, never an empty successful value.

Offline tests replace `clr.GetClrType`, `BindingFlags` and property metadata with a scoped Python test model, while executing this exact implementation path. The Python descriptor test model supplies `GetValue(owner)` only to exercise lookup/invocation control flow. It is neither a general Python descriptor contract nor evidence that Python 3 CLR engines implement IronPython's descriptor API. Production calls require CLR metadata and the documented IronPython descriptor API.

## Verification

Offline tests execute this fence, exercising shadowing, misleading dynamic names, zero dynamic calls on the explicit path, uncertain direct errors, absence, unavailable getters, metadata/descriptor failures, invocation errors, invalid inputs and falsey/null values. Revit execution is pending. Validate with an actual `ElementType` whose dynamic `Name` raises `AttributeError`, compare `api.Element.Name.GetValue(owner)`, and exercise an unavailable/throwing getter in Revit 2022 / Dynamo 2.12 / IronPython 2.7. Record Python 3 CLR behavior separately. Original source runtime results do not validate this replacement.

## Provenance

The explicit descriptor operation follows [IronPython .NET integration documentation](https://ironpython.net/documentation/dotnet/dotnet.html), including its documented property `GetValue` API. Motivation and separation of element, type and family metadata follow [Revit-automatization DEC-027 at e15c0cae](https://github.com/Krankort224/Revit-automatization/blob/e15c0caebe8e582119c984eba1cef95e9c736ab3/knowledge/06_DECISIONS.md#dec-027--metadata-имена-элемента-типа-и-семейства-разделяются). The bounded result contract, metadata checks and offline test model are adaptations in this library, with no inherited native verification claim.
