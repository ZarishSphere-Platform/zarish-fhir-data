# Bangladesh Medication Codes

Bangladesh Medication Codes

## Overview

- **ID**: `bd-medication-code`
- **Name**: BDMedicationCodeSystem
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-medication-code`
- **Total Concepts**: 6
- **Status**: draft

## Concepts

| Code | Display Name |
|------|-------------|
| `394-0010-030` | Tubutol |
| `394-0011-030` | AFDCDT-2 |
| `394-0012-030` | AFDCDT-3 |
| `394-0017-046` | Levetiracetam 250 |
| `394-0021-028` | Donepezil Hydrochloride 5 |
| `355-0065-023` | Cefufine |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-medication-code",
    "code": "394-0010-030",
    "display": "Tubutol"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
