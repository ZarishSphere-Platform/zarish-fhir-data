# Bangladesh Immunization Site Code System

Codes for anatomical site of vaccine administration in Bangladesh.

## Overview

- **ID**: `bd-immunization-site`
- **Name**: BDImmunizationSiteCS
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-site`
- **Total Concepts**: 5
- **Status**: active

## Concepts

| Code | Display Name |
|------|-------------|
| `LA` | Left Arm |
| `RA` | Right Arm |
| `LT` | Left Thigh |
| `RT` | Right Thigh |
| `ORAL` | Oral |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-site",
    "code": "LA",
    "display": "Left Arm"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
