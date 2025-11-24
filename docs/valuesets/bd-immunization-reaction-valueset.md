# Bangladesh Immunization Reaction Value Set

Allowed vaccine reactions for immunization in Bangladesh.

## Overview

- **ID**: `bd-immunization-reaction-valueset`
- **Name**: BDImmunizationReactionValueSet
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-immunization-reaction-valueset`
- **Status**: active

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-reaction`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-reaction",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
