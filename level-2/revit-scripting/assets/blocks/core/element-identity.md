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
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Read native identity without localized display labels. Resolve a family/type pair only when exactly one supplied type matches; never select an arbitrary first match.

## Inputs and outputs

`element_identity(doc, element, api=None)` returns native element, family and type names, IDs and warnings. `resolve_exact_type(doc, types, family_name, type_name, api=None)` accepts an explicit candidate collection and returns `unique`, `missing`, or `ambiguous`, all candidate IDs, and a type only for `unique`. Names are exact, case-sensitive Unicode strings; no substring or normalization matching.

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


def _identity_native_name(element, bip, warnings):
    try:
        parameter = None if bip is None else element.get_Parameter(bip)
        if parameter is not None:
            name = parameter.AsString()
            if name:
                return _identity_text(name)
    except Exception as error:
        warnings.append('name_parameter: ' + _identity_text(error))
    try:
        return _identity_text(element.Name)
    except Exception as error:
        warnings.append('native_name: ' + _identity_text(error))
        return u''


def element_identity(doc, element, api=None):
    if api is None:
        import Autodesk.Revit.DB as api
    if doc is None or element is None or element.Document != doc:
        raise ValueError('Element must belong to supplied document')
    warnings = []
    element_id = _identity_id(element.Id)
    type_element = None
    try:
        if isinstance(element, api.ElementType):
            type_element = element
        else:
            type_element = doc.GetElement(element.GetTypeId())
    except Exception as error:
        warnings.append('type_resolution: ' + _identity_text(error))
    family_name = u''
    if type_element is not None and type_element.Document != doc:
        raise ValueError('Resolved type belongs to another document')
    if type_element is not None:
        try:
            family_name = _identity_text(type_element.Family.Name)
        except AttributeError:
            try:
                family_name = _identity_text(type_element.FamilyName)
            except AttributeError:
                pass
    type_name = (u'' if type_element is None else
                 _identity_native_name(type_element,
                                       api.BuiltInParameter.SYMBOL_NAME_PARAM,
                                       warnings))
    return {'element_id': element_id,
            'unique_id': _identity_text(getattr(element, 'UniqueId', '')),
            'element_name': _identity_native_name(
                element, None, warnings),
            'type_id': None if type_element is None else
                       _identity_id(type_element.Id),
            'family_name': family_name, 'type_name': type_name,
            'warnings': warnings}


def resolve_exact_type(doc, types, family_name, type_name, api=None):
    family_name = _identity_text(family_name)
    type_name = _identity_text(type_name)
    if not family_name or not type_name:
        raise ValueError('Both exact names are required')
    matches = []
    seen = set()
    for candidate in types:
        identity = element_identity(doc, candidate, api)
        if (identity['family_name'] != family_name or
                identity['type_name'] != type_name):
            continue
        key = identity['type_id']
        if key is None:
            raise ValueError('Matching type has no usable native ID')
        if key not in seen:
            seen.add(key)
            matches.append(candidate)
    status = 'missing' if not matches else (
        'unique' if len(matches) == 1 else 'ambiguous')
    return {'status': status, 'match_ids': sorted(seen),
            'type': matches[0] if status == 'unique' else None}
```

## Adaptation and limits

Pass candidates from the intended document/category. IDs are document-scoped, not cross-document identities. This reader does not activate symbols or load families. Injecting `api` exists for offline tests; live calls use Revit types. Type names use `SYMBOL_NAME_PARAM` with native Name fallback; system families use `FamilyName`.

## Verification

Native validation pending. Offline cases cover exact BIP identity, missing and duplicate family/type pairs, and repeated candidates with the same native type ID, mixed-document rejection and 64-bit IDs without legacy access. They do not prove overload binding in IronPython or live family loading behavior.

## Provenance

Adapted from [CFD-modeling tools/py/20_VRU_FillParameters.py at 6f6ff374](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/20_VRU_FillParameters.py), `get_type_name`, `get_family_name`, `get_identity`, `compare_identity`; and [Revit Core at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py), `element_type_name`, `family_name_doc`. Removed implicit document globals and project system normalization; added exact unique resolution and explicit ambiguity.
