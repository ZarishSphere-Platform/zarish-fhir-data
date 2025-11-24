# Bangladesh Immunization Site Value Set

Allowed administration sites for vaccines in Bangladesh.

## Overview

- **ID**: `bd-immunization-site-valueset`
- **Name**: BDImmunizationSiteVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-immunization-site-valueset`
- **Status**: active

## Composition

This value set includes codes from the following code systems:

- `https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-site`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-site",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
