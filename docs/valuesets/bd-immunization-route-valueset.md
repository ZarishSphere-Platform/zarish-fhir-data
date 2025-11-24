# Bangladesh Immunization Route Value Set

Allowed administration routes for vaccines in Bangladesh.

## Overview

- **ID**: `bd-immunization-route-valueset`
- **Name**: BDImmunizationRouteVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-immunization-route-valueset`
- **Status**: active

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-route`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-route",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
