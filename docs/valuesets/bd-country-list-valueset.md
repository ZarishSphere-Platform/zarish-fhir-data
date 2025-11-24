# Nationality ValueSet

Nationality value set

## Overview

- **ID**: `bd-country-list-valueset`
- **Name**: BDCountryListVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-country-list-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-country-list`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-country-list",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
