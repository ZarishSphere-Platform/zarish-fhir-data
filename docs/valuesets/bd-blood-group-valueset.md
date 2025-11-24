# Bangladesh Blood Group ValueSet

Blood group value set according to CCDS guideline

## Overview

- **ID**: `bd-blood-group-valueset`
- **Name**: BDBloodGroupVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-blood-group-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
