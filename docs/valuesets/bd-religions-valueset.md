# Bangladesh Religions ValueSet

Religions value set according to CCDS guideline

## Overview

- **ID**: `bd-religions-valueset`
- **Name**: BDReligionsVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-religions-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-religions`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-religions",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
