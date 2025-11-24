# Bangladesh Religions



## Overview

- **ID**: `bd-religions`
- **Name**: BDReligionsCS
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-religions`
- **Total Concepts**: 7
- **Status**: draft

## Concepts

| Code | Display Name |
|------|-------------|
| `1` | Islam |
| `2` | Hinduism |
| `3` | Buddhism |
| `4` | Christianity |
| `8` | Refuse to disclose |
| `9` | Not a believer |
| `0` | Other (specify) |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-religions",
    "code": "1",
    "display": "Islam"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
