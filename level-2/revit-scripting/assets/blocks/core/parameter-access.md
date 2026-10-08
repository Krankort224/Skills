# Explicit parameter access and verified writes

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
| id | parameter-access |
| group | core |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host |
| verification | offline |
| dependencies | none |
| mutation | document-write |

## Purpose

Resolve exactly one parameter in an explicit instance or type scope. Read and convert values by storage type, then report planned, unchanged, changed, read-only, missing, ambiguous or verification failure. Never fall through to another scope for writes.

## Inputs and outputs

`access_parameter(doc, element, scope, selector, operation='read', value=None, unit=None, internal_units=False, dry_run=True, tolerance=1e-9, api=None)` accepts selector `{'kind':'bip'|'guid'|'name', 'value':...}`. `unit` is a compatible Forge unit ID; `internal_units=True` is an explicit alternative for Double values. Results contain status, scope, storage, data type, unit metadata, previous/requested/readback values and writable/changed flags. Writes require a caller-owned open native transaction; use transaction-receipt to coordinate rollback after failed readback.

## Implementation

```python
# -*- coding: utf-8 -*-
def access_parameter(doc, element, scope, selector, operation='read',
                     value=None, unit=None, internal_units=False,
                     dry_run=True, tolerance=1e-9, api=None):
    if api is None:
        import Autodesk.Revit.DB as api
    if scope not in ('instance', 'type') or operation not in ('read', 'write'):
        raise ValueError('Explicit scope and read/write operation required')
    import math
    def finite(number):
        number = float(number)
        if math.isnan(number) or math.isinf(number):
            raise ValueError('Nonfinite numeric value')
        return number
    tolerance = finite(tolerance)
    if tolerance < 0:
        raise ValueError('Negative tolerance')
    if doc is None or element is None or element.Document != doc:
        raise ValueError('Element must belong to the supplied document')
    if unit is not None and internal_units:
        raise ValueError('Choose external unit or explicit internal units')
    owner = element
    if scope == 'type':
        owner = (element if isinstance(element, api.ElementType) else
                 doc.GetElement(element.GetTypeId()))
    elif isinstance(element, api.ElementType):
        raise ValueError('An ElementType requires scope=type')
    result = {'scope': scope, 'status': 'missing', 'writable': False,
              'changed': False, 'previous': None, 'requested': value,
              'readback': None, 'owner': owner}
    if owner is None:
        return result
    if owner.Document != doc:
        raise ValueError('Parameter owner must belong to supplied document')
    kind = selector.get('kind')
    key = selector.get('value')
    if kind == 'name':
        parameters = list(owner.GetParameters(key))
    elif kind == 'bip':
        try:
            key_is_text = isinstance(key, basestring)
        except NameError:
            key_is_text = isinstance(key, str)
        if key_is_text:
            key = getattr(api.BuiltInParameter, key)
        parameter = owner.get_Parameter(key)
        parameters = [] if parameter is None else [parameter]
    elif kind == 'guid':
        from System import Guid
        parameter = owner.get_Parameter(Guid(str(key)))
        parameters = [] if parameter is None else [parameter]
    else:
        raise ValueError('selector kind must be bip, guid or name')
    if len(parameters) != 1:
        result['status'] = 'ambiguous' if parameters else 'missing'
        result['match_count'] = len(parameters)
        return result
    parameter = parameters[0]
    storage = str(parameter.StorageType)
    try:
        data_type = parameter.Definition.GetDataType()
    except AttributeError:
        data_type = None
    try:
        native_unit = parameter.GetUnitTypeId()
    except Exception:
        native_unit = None
    result.update({'storage': storage, 'data_type': str(data_type),
                   'native_unit': str(native_unit), 'parameter': parameter,
                   'writable': not parameter.IsReadOnly})
    if storage == 'Double':
        if unit is None and not internal_units:
            raise ValueError('Double requires unit or internal_units=True')
        if unit is not None:
            if data_type is None or not api.UnitUtils.IsValidUnit(data_type, unit):
                raise ValueError('Unit incompatible with parameter data type')
        def read():
            raw = finite(parameter.AsDouble())
            return finite(raw if unit is None else
                          api.UnitUtils.ConvertFromInternalUnits(raw, unit))
        converted = (None if operation == 'read' else finite(value))
        if converted is not None and unit is not None:
            converted = finite(api.UnitUtils.ConvertToInternalUnits(converted, unit))
    elif storage == 'Integer':
        if unit is not None:
            raise ValueError('Integer does not accept a unit')
        def read():
            return parameter.AsInteger()
        converted = None if operation == 'read' else int(value)
        if operation == 'write' and float(value) != converted:
            raise ValueError('Integer value must be exact; no rounding')
    elif storage == 'String':
        if unit is not None:
            raise ValueError('String does not accept a unit')
        def read():
            return parameter.AsString()
        try:
            string_types = (basestring,)
        except NameError:
            string_types = (str,)
        if operation == 'write' and not isinstance(value, string_types):
            raise ValueError('String requires text, not implicit coercion')
        converted = value
    elif storage == 'ElementId':
        if unit is not None:
            raise ValueError('ElementId does not accept a unit')
        def read():
            element_id = parameter.AsElementId()
            if hasattr(element_id, 'Value'):
                return int(element_id.Value)
            if hasattr(element_id, 'IntegerValue'):
                return int(element_id.IntegerValue)
            raise ValueError('Native ID has no Value or IntegerValue')
        converted = None if operation == 'read' else api.ElementId(int(value))
        if operation == 'write' and float(value) != int(value):
            raise ValueError('ElementId requires an exact integer')
    else:
        result['status'] = 'unsupported_storage'
        return result
    def equal(a, b):
        if storage == 'Double':
            return abs(float(a) - float(b)) <= tolerance
        if storage == 'ElementId':
            return a == int(b)
        return a == b
    previous = read()
    result.update({'previous': previous, 'readback': previous})
    if operation == 'read':
        result['status'] = 'read'
    elif equal(previous, value):
        result['status'] = 'unchanged'
    elif not result['writable']:
        result['status'] = 'read_only'
    elif dry_run:
        result['status'] = 'planned'
    else:
        if not doc.IsModifiable:
            raise ValueError('A caller-owned transaction is required')
        accepted = parameter.Set(converted)
        readback = read()
        result.update({'readback': readback,
                       'changed': not equal(previous, readback)})
        result['status'] = ('changed' if accepted and equal(readback, value)
                            else 'verification_failed')
    return result
```

## Adaptation and limits

Name lookup rejects duplicate localized names; use BIP or shared parameter GUID where possible. GUIDs require .NET System. Double conversions use the parameter data type, not project name heuristics. Pass compatible units explicitly; do not use formatted display strings as numeric inputs. Type writes affect all instances of that type and require deliberate caller policy. `Set` errors propagate for transaction rollback; this function does not open or commit a transaction. Native worksharing ownership and formula constraints remain host validation concerns.

## Verification

Native validation pending. Offline mocks exercise ambiguous name resolution, explicit type scope, read-only/unchanged/planned writes, unit conversions, changed/readback rejection, unsupported storage, missing transaction, exact integer validation, document ownership, 64-bit ID access and nonfinite conversion/readback rejection. They do not validate live Forge type IDs, .NET GUID overload binding or worksharing.

## Provenance

Adapted from [CFD parameter fill at 6f6ff374](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/20_VRU_FillParameters.py), `get_data_type_text`, `get_unit_type_text`, `to_internal_value`, `from_internal_value`, `values_equal`, and its parameter write/readback loop. Replaced parameter-name unit rules and `LookupParameter` with explicit scope, unique selector resolution, compatible unit validation and caller-controlled transactions.
