# Bangladesh Vaccine Value Set

Allowed vaccines for immunization in Bangladesh.

## Overview

- **ID**: `bd-vaccine-valueset`
- **Name**: BDVaccineVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-vaccine-valueset`
- **Status**: active

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-vaccine-code`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-vaccine-code",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
