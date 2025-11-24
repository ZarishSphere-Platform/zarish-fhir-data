# Bangladesh district ValueSet

Bangladesh district Codes (only two-digit codes)

## Overview

- **ID**: `bd-district-code-valueset`
- **Name**: BDDistrictsVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-district-code-valueset`
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
