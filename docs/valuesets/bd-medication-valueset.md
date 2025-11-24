# Bangladesh Medication ValueSet

Bangladesh Medication ValueSet

## Overview

- **ID**: `bd-medication-valueset`
- **Name**: BDMedicationVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-medication-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-medication-code`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-medication-code",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
