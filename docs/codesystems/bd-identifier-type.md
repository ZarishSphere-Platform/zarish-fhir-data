# Bangladesh Identifier Types

Codes identifying the type of identifiers used in Bangladesh.

## Overview

- **ID**: `bd-identifier-type`
- **Name**: BangladeshIdentifierType
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-identifier-type`
- **Total Concepts**: 3
- **Status**: draft

## Concepts

| Code | Display Name |
|------|-------------|
| `NID` | National ID |
| `BRN` | Birth Registration Number |
| `UHID` | Unique Health ID |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-identifier-type",
    "code": "NID",
    "display": "National ID"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
