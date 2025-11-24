# Bangladesh Vaccine Code System

Vaccine codes used in Bangladesh EPI and immunization program.

## Overview

- **ID**: `bd-vaccine-code`
- **Name**: BDVaccineCS
- **System URL**: `https://fhir.dghs.gov.bd/core/CodeSystem/bd-vaccine-code`
- **Total Concepts**: 10
- **Status**: active

## Concepts

| Code | Display Name |
|------|-------------|
| `BCG` | BCG Vaccine |
| `OPV` | Oral Polio Vaccine (OPV) |
| `IPV` | Inactivated Polio Vaccine (IPV) |
| `PENTA` | Pentavalent Vaccine |
| `MR` | Measles-Rubella (MR) Vaccine |
| `TT` | Tetanus Toxoid (TT) Vaccine |
| `PCV10` | Pneumococcal Conjugate Vaccine |
| `ROTA` | Rotavirus Vaccine |
| `HPV` | Human Papillomavirus (HPV) Vaccine |
| `COVID19` | COVID-19 Vaccine |


## Usage in FHIR

### Example

```json
{
  "resourceType": "CodeableConcept",
  "coding": [{
    "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-vaccine-code",
    "code": "BCG",
    "display": "BCG Vaccine"
  }]
}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
