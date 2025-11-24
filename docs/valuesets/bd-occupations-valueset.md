# Bangladesh Occupations ValueSet

Occupations value set according to CCDS guideline

## Overview

- **ID**: `bd-occupations-valueset`
- **Name**: BDOccupationsVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-occupations-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-occupations`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-occupations",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
