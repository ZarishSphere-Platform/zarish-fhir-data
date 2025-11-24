# Bangladesh Upazila ValueSet

Bangladesh Upazila Codes (only two-digit codes)

## Overview

- **ID**: `bd-upazilla-code-valueset`
- **Name**: BDUpazillasVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-upazilla-code-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-geocodes`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-geocodes",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
