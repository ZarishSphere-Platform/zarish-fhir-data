# Bangladesh ICD-11 MMS ValueSet

ValueSet that includes the ICD-11 MMS CodeSystem for Condition.code

## Overview

- **ID**: `bd-condition-icd11-valueset`
- **Name**: BDConditionICD11VS
- **URL**: `https://fhir.dghs.gov.bd/core/ValueSet/bd-condition-icd11-valueset`
- **Status**: draft

## Composition

This value set includes codes from the following code systems:

- `http://id.who.int/icd/release/11/mms`


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "http://id.who.int/icd/release/11/mms",
    "code": "example-code",
    "display": "Example Display"
  }]
}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
