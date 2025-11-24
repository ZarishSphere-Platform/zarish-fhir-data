# Bangladesh Medication Dose Form ValueSet

Medication dose form value set according to CCDS guideline

## Overview

- **ID**: `bd-dose-form-valueset`
- **Name**: BDMedicationDoseFormVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-dose-form-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-dose-form`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-dose-form",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
