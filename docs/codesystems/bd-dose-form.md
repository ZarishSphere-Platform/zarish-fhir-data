# Bangladesh Medication Dose Form CodeSystem

Medication dose form codes according to CCDS guideline

## Overview

- **ID**: `bd-dose-form`
- **Name**: BDMedicationDoseForm
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-dose-form`
- **Total Concepts**: 10
- **Status**: draft

## Concepts

| Code | Display Name |
|------|-------------|
| `TAB` | Tablet |
| `DTAB` | Dispersible Tablet |
| `CAP` | Capsule |
| `SYP` | Syrup |
| `SUSP` | Suspension |
| `PFS` | Powder for Suspension |
| `INJ` | Injection |
| `SOL` | Solution |
| `CRM` | Cream |
| `LOT` | Lotion |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-dose-form",
    "code": "TAB",
    "display": "Tablet"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
