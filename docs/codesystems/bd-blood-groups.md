# Bangladesh Blood Group CodeSystem

Blood group codes according to CCDS guideline

## Overview

- **ID**: `bd-blood-groups`
- **Name**: BDBloodGroupCS
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups`
- **Total Concepts**: 8
- **Status**: draft

## Concepts

| Code | Display Name |
|------|-------------|
| `1` | O Positive |
| `2` | O Negative |
| `3` | A Positive |
| `4` | A Negative |
| `5` | B Positive |
| `6` | B Negative |
| `7` | AB Positive |
| `8` | AB Negative |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
    "code": "1",
    "display": "O Positive"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
