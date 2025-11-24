# BD Encounter Status Subset

Subset of EncounterStatus limited to planned, in-progress, finished, and cancelled.

## Overview

- **ID**: `bd-encounter-status-subset`
- **Name**: BDEncounterStatusSubsetVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-encounter-status-subset`
- **Status**: active

## Composition

This value set includes codes from the following code systems:

- `http://hl7.org/fhir/encounter-status`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "http://hl7.org/fhir/encounter-status",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
