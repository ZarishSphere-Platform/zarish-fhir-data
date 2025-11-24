# BD Encounter Class Subset

Subset of EncounterClass limited to inpatient, ambulatory, and emergency.

## Overview

- **ID**: `bd-encounter-class-subset`
- **Name**: BDEncounterClassSubsetVS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-encounter-class-subset`
- **Status**: active

## Composition

This value set includes codes from the following code systems:

- `http://terminology.hl7.org/CodeSystem/v3-ActCode`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
