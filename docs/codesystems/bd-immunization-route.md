# Bangladesh Immunization Route Code System

Codes for routes of vaccine administration in Bangladesh.

## Overview

- **ID**: `bd-immunization-route`
- **Name**: BDImmunizationRouteCS
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-route`
- **Total Concepts**: 5
- **Status**: active

## Concepts

| Code | Display Name |
|------|-------------|
| `IM` | Intramuscular |
| `SC` | Subcutaneous |
| `ID` | Intradermal |
| `ORAL` | Oral |
| `IN` | Intranasal |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-route",
    "code": "IM",
    "display": "Intramuscular"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
