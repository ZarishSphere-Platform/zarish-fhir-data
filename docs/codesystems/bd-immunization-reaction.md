# Bangladesh Immunization Reaction Code System

Codes for adverse reactions after vaccination in Bangladesh.

## Overview

- **ID**: `bd-immunization-reaction`
- **Name**: BDImmunizationReactionCS
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-reaction`
- **Total Concepts**: 6
- **Status**: active

## Concepts

| Code | Display Name |
|------|-------------|
| `NONE` | No Reaction |
| `FEVER` | Fever |
| `SWELLING` | Swelling |
| `RASH` | Rash |
| `ANAPHYLAXIS` | Anaphylaxis |
| `OTHER` | Other Reaction |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-immunization-reaction",
    "code": "NONE",
    "display": "No Reaction"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
