# Named table payload validation

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
| id | table-payload |
| group | core |
| status | reviewed |
| runtime | Python 2.7 or 3 |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Turn a header-first table or a `[report, table]` envelope into a named table contract. Invalid shape, duplicated headers and ambiguous envelopes are errors, not empty results.

## Inputs and outputs

`table_payload(payload, table_name, required_headers=None, allow_extra=True)` returns `{'name', 'headers', 'rows', 'records', 'report', 'source_shape'}`. Headers are nonempty distinct strings. Rows must be rectangular and cannot be strings or dictionaries. Empty data with a valid header is accepted; empty payload without a header is rejected. `[report, table]` accepts a text string or a sequence of text report lines. Required headers preserve caller-supplied names and order is explicit in `headers`.

## Implementation

```python
# -*- coding: utf-8 -*-
def table_payload(payload, table_name, required_headers=None, allow_extra=True):
    try:
        text_types = (basestring,)
    except NameError:
        text_types = (str,)
    def sequence(value):
        return isinstance(value, (list, tuple))
    def header(value):
        return (sequence(value) and len(value) > 0 and
                all(isinstance(item, text_types) and item.strip()
                    for item in value) and len(set(value)) == len(value))
    def is_table(value):
        if not sequence(value) or not value or not header(value[0]):
            return False
        width = len(value[0])
        return all(sequence(row) and len(row) == width for row in value[1:])
    def is_report(value):
        return (isinstance(value, text_types) or
                sequence(value) and all(isinstance(line, text_types)
                                        for line in value))
    if not isinstance(table_name, text_types) or not table_name.strip():
        raise ValueError('Explicit table name required')
    direct = is_table(payload)
    envelope = (sequence(payload) and len(payload) == 2 and
                is_report(payload[0]) and is_table(payload[1]))
    if direct and envelope:
        raise ValueError('Ambiguous table envelope')
    if not direct and not envelope:
        raise ValueError('Invalid table/envelope shape or headers')
    table = payload[1] if envelope else payload
    headers = list(table[0])
    if required_headers is not None and not sequence(required_headers):
        raise ValueError('Required headers must be a list or tuple')
    required = [] if required_headers is None else list(required_headers)
    if required and not header(required):
        raise ValueError('Invalid required headers')
    missing = [name for name in required if name not in headers]
    if missing:
        raise ValueError('Missing required headers: %s' % missing)
    if not allow_extra and set(headers) != set(required):
        raise ValueError('Unexpected headers')
    rows = [list(row) for row in table[1:]]
    records = [dict(zip(headers, row)) for row in rows]
    report = payload[0] if envelope else []
    if isinstance(report, text_types):
        report = [report]
    return {'name': table_name, 'headers': headers, 'rows': rows,
            'records': records, 'report': list(report),
            'source_shape': 'report_table' if envelope else 'table'}


def table_column(table, name):
    headers = table.get('headers', [])
    if headers.count(name) != 1:
        raise ValueError('Column must exist exactly once')
    index = headers.index(name)
    rows = table.get('rows')
    if not isinstance(rows, (list, tuple)):
        raise ValueError('Invalid normalized table rows')
    result = []
    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) != len(headers):
            raise ValueError('Nonrectangular normalized table')
        result.append(row[index])
    return result
```

## Adaptation and limits

This strict adapter intentionally accepts Python list/tuple, not arbitrary iterables or DesignScript dictionaries. Convert known host collection types explicitly before calling and retain source shape errors. It preserves values without type coercion, units, model identity resolution or automatic parameter mapping. Validate data cells against the consumer schema before writes. Table metadata is named; positional whole-Core OUT contracts are outside this block.

## Verification

Offline cases cover direct and enveloped payloads, header-only empty data, report lines, missing/duplicate/empty headers, string rows, ragged rows, strict extra-header policy and named column extraction. Native Dynamo collection conversion remains pending; no Revit runtime claim.

## Provenance

Generalized from [Revit raster block at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_2/block_2_current.py), `run` header-first `candidate_rows` output. The validation and envelope decoder are new generalized adaptation code, not a verbatim extraction. Replaced project column positions with named, rectangular, explicit contracts. Does not reuse legacy Core index contracts.
