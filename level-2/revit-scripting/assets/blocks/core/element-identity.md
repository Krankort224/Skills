# Element identity and exact type lookup

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
| id | element-identity |
| group | core |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 CLR requires separate verification |
| verification | offline |
| dependencies | clr-property-access |
| mutation | read-only |

## Purpose

Read native identity without localized display labels. Resolve a family/type pair only when exactly one supplied type matches; never select an arbitrary first match.

## Inputs and outputs

`element_identity(doc, element, api=None)` returns native element, family and type names, IDs and warnings. `resolve_exact_type(doc, types, family_name, type_name, api=None)` accepts an explicit candidate collection and returns `unique`, `missing`, `ambiguous`, or `indeterminate`, matching IDs, incomplete candidate identities, and a type only for `unique`. Any unreadable required family/type metadata makes the result indeterminate; successful empty/null names are known values and remain distinct from read failures. `name_results` preserves the structured property/parameter results behind the string convenience fields. Load the [clr-property-access](clr-property-access.md) fence first in the same namespace. Names are exact, case-sensitive Unicode strings; no substring or normalization matching.

## Implementation

```python
# -*- coding: utf-8 -*-
def _identity_text(value):
    try:
        return unicode(value) if value is not None else u''
    except NameError:
        return str(value) if value is not None else ''


def _identity_id(value):
    if value is None:
        return None
    if hasattr(value, 'Value'):
        return int(value.Value)
    if hasattr(value, 'IntegerValue'):
        return int(value.IntegerValue)
    raise ValueError('Native ID has no Value or IntegerValue')


def _identity_name_result(value, path):
    return {'status': 'returned_null' if value is None else 'parameter_value',
            'value': value, 'access_path': path, 'stage': 'name_read',
            'error_type': None, 'error_text': None}


def _identity_warn(result, warnings, label):
    if result['status'] not in ('direct_value', 'declared_getter_value', 'parameter_value', 'returned_null'):
        warnings.append(label + ': ' + result['status'] + ': ' +
                        _identity_text(result['error_text']))


def _identity_declared_name(element, api):
    try:
        declaration = api.Element
        if declaration is None:
            raise ValueError('api.Element must identify the declaring type')
    except Exception as error:
        return _clr_result('configuration_error', 'declaring_type.GetValue',
                           'configuration', error=error)
    return read_clr_property(element, 'Name', declaration)


def _identity_native_name(element, bip, warnings, api):
    attempts = []
    if bip is not None:
        try:
            parameter = element.get_Parameter(bip)
            if parameter is not None:
                name = parameter.AsString()
                if name:
                    return _identity_name_result(name, 'SYMBOL_NAME_PARAM')
        except Exception as error:
            failure = _clr_result('parameter_error', 'SYMBOL_NAME_PARAM',
                                  'parameter_read', error=error)
            attempts.append(failure)
            _identity_warn(failure, warnings, 'name_parameter')
    result = _identity_declared_name(element, api)
    result['attempts'] = attempts
    _identity_warn(result, warnings, 'native_name')
    return result


def _identity_family_name(type_element, warnings):
    family = read_clr_property(type_element, 'Family')
    attempts = [family]
    if family['status'] == 'direct_value':
        result = read_clr_property(family['value'], 'Name')
        if result['status'] in ('direct_value', 'declared_getter_value', 'parameter_value', 'returned_null'):
            return result
        attempts.append(result)
        _identity_warn(result, warnings, 'family_name')
    elif family['status'] != 'returned_null':
        _identity_warn(family, warnings, 'family')
    result = read_clr_property(type_element, 'FamilyName')
    result['attempts'] = attempts
    _identity_warn(result, warnings, 'family_name')
    return result


def element_identity(doc, element, api=None):
    if api is None:
        import Autodesk.Revit.DB as api
    if doc is None or element is None or element.Document != doc:
        raise ValueError('Element must belong to supplied document')
    warnings = []
    element_id = _identity_id(element.Id)
    type_element = None
    type_error = None
    try:
        if isinstance(element, api.ElementType):
            type_element = element
        else:
            type_element = doc.GetElement(element.GetTypeId())
    except Exception as error:
        type_error = error
        warnings.append('type_resolution: ' + _identity_text(error))
    if type_element is not None and type_element.Document != doc:
        raise ValueError('Resolved type belongs to another document')
    if type_element is None:
        unavailable = _clr_result('type_unavailable', 'type_resolution',
                                  'type_resolution', error=type_error)
        names = {'family_name': dict(unavailable),
                 'type_name': dict(unavailable)}
        if type_error is None:
            warnings.append('type_resolution: no type was returned')
    else:
        names = {'family_name': _identity_family_name(type_element, warnings),
                 'type_name': _identity_native_name(
                     type_element, api.BuiltInParameter.SYMBOL_NAME_PARAM,
                     warnings, api)}
    names['element_name'] = _identity_native_name(element, None, warnings, api)
    return {'element_id': element_id,
            'unique_id': _identity_text(getattr(element, 'UniqueId', '')),
            'element_name': _identity_text(names['element_name']['value']),
            'type_id': None if type_element is None else
                       _identity_id(type_element.Id),
            'family_name': _identity_text(names['family_name']['value']),
            'type_name': _identity_text(names['type_name']['value']),
            'name_results': names, 'warnings': warnings}


def resolve_exact_type(doc, types, family_name, type_name, api=None):
    family_name = _identity_text(family_name)
    type_name = _identity_text(type_name)
    if not family_name or not type_name:
        raise ValueError('Both exact names are required')
    matches = []
    incomplete = []
    seen = set()
    for candidate in types:
        identity = element_identity(doc, candidate, api)
        if any(identity['name_results'][key]['status'] not in
               ('direct_value', 'declared_getter_value', 'parameter_value', 'returned_null') for key in ('family_name', 'type_name')):
            incomplete.append(identity)
            continue
        if (identity['family_name'] != family_name or
                identity['type_name'] != type_name):
            continue
        key = identity['type_id']
        if key is None:
            raise ValueError('Matching type has no usable native ID')
        if key not in seen:
            seen.add(key)
            matches.append(candidate)
    status = 'indeterminate' if incomplete else (
        'missing' if not matches else (
            'unique' if len(matches) == 1 else 'ambiguous'))
    return {'status': status, 'match_ids': sorted(seen),
            'incomplete': incomplete,
            'type': matches[0] if status == 'unique' else None}

```

## Adaptation and limits

Pass candidates from the intended document/category. IDs are document-scoped, not cross-document identities. This reader does not activate symbols or load families. Injecting `api` exists for offline tests; live calls use Revit types. Type names use `SYMBOL_NAME_PARAM` with `api.Element.Name.GetValue` fallback; element names always select the `api.Element` declaration. Family object names take precedence over `FamilyName`, with failed reads retained as warnings. Successful fallback supplies the required family/type metadata; unresolved failures remain in `name_results` and make exact resolution indeterminate.

## Verification

Native validation pending; no Python 3 CLR guarantee. Offline cases load the canonical dependency and cover descriptor shadowing, zero dynamic element-name access, BIP precedence, indeterminate lookup on incomplete metadata, actual empty/null names, and exact BIP identity, missing and duplicate family/type pairs, and repeated candidates with the same native type ID, mixed-document rejection and 64-bit IDs without legacy access. They do not prove overload binding in IronPython or live family loading behavior.

## Provenance

Adapted from [CFD-modeling tools/py/20_VRU_FillParameters.py at 6f6ff374](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/20_VRU_FillParameters.py), `get_type_name`, `get_family_name`, `get_identity`, `compare_identity`; and [Revit Core at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py), `element_type_name`, `family_name_doc`. Removed implicit document globals and project system normalization; added exact unique resolution and explicit ambiguity.

The element `Name` declaration selection and distinction from type/family metadata additionally follow [DEC-027 at e15c0cae](https://github.com/Krankort224/Revit-automatization/blob/e15c0caebe8e582119c984eba1cef95e9c736ab3/knowledge/06_DECISIONS.md#dec-027--metadata-имена-элемента-типа-и-семейства-разделяются) and the [IronPython property descriptor documentation](https://ironpython.net/documentation/dotnet/dotnet.html). This adaptation has offline evidence only.
