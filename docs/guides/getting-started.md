# Getting Started

Welcome to the Zarish FHIR Data documentation! This guide will help you get started with using FHIR terminologies in your applications.

## Prerequisites

- Basic understanding of FHIR (Fast Healthcare Interoperability Resources)
- Familiarity with JSON or XML
- Development environment with Go 1.23+ (for using the terminology package)

## Installation

### Clone the Repository

```bash
git clone https://github.com/ZarishSphere-Platform/zarish-fhir-data.git
cd zarish-fhir-data
```

### Install Dependencies

```bash
go mod download
```

## Quick Start

### Loading a Code System

```go
package main

import (
    "fmt"
    "encoding/json"
    "os"
)

func main() {
    // Load Bangladesh Blood Groups CodeSystem
    data, err := os.ReadFile("terminology/bd-core/package/CodeSystem-bd-blood-groups.json")
    if err != nil {
        panic(err)
    }
    
    var codeSystem map[string]interface{}
    json.Unmarshal(data, &codeSystem)
    
    fmt.Println("Code System:", codeSystem["title"])
    fmt.Println("Concepts:", codeSystem["count"])
}
```

### Using in FHIR Resources

#### Patient with Blood Group

```json
{
  "resourceType": "Patient",
  "id": "example-patient",
  "extension": [{
    "url": "http://zarishsphere.org/fhir/StructureDefinition/blood-group",
    "valueCodeableConcept": {
      "coding": [{
        "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
        "code": "1",
        "display": "O Positive"
      }]
    }
  }],
  "identifier": [{
    "type": {
      "coding": [{
        "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-identifier-type",
        "code": "NID",
        "display": "National ID"
      }]
    },
    "value": "1234567890123"
  }],
  "name": [{
    "family": "Rahman",
    "given": ["Abdul"]
  }],
  "gender": "male",
  "address": [{
    "extension": [{
      "url": "http://zarishsphere.org/fhir/StructureDefinition/bd-divisions",
      "valueCodeableConcept": {
        "coding": [{
          "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-geocodes",
          "code": "10",
          "display": "Dhaka"
        }]
      }
    }],
    "city": "Dhaka",
    "country": "BD"
  }]
}
```

## Directory Structure

```
zarish-fhir-data/
├── terminology/
│   ├── bangladesh/
│   │   ├── districts.json
│   │   └── divisions.json
│   └── bd-core/
│       └── package/
│           ├── CodeSystem-*.json
│           ├── ValueSet-*.json
│           └── StructureDefinition-*.json
├── docs/
│   ├── codesystems/
│   ├── valuesets/
│   └── guides/
└── mkdocs.yml
```

## Common Use Cases

### 1. Patient Demographics

Use Bangladesh Core code systems for:
- Blood groups
- Religions
- Occupations
- Geographic locations (divisions, districts, upazilas)

### 2. Clinical Observations

Use LOINC for:
- Vital signs (heart rate, blood pressure, temperature)
- Laboratory results
- Clinical measurements

### 3. Diagnoses

Use ICD-10 or SNOMED CT for:
- Disease coding
- Condition documentation
- Clinical findings

### 4. Medications

Use RxNorm or Bangladesh Medication codes for:
- Medication orders
- Prescriptions
- Drug databases

## Validation

### Validating Codes

```go
func validateCode(system, code string) bool {
    // Load the code system
    data, _ := os.ReadFile(fmt.Sprintf("terminology/bd-core/package/CodeSystem-%s.json", system))
    
    var cs map[string]interface{}
    json.Unmarshal(data, &cs)
    
    // Check if code exists
    concepts := cs["concept"].([]interface{})
    for _, c := range concepts {
        concept := c.(map[string]interface{})
        if concept["code"] == code {
            return true
        }
    }
    return false
}
```

## Best Practices

!!! tip "Use Appropriate Terminologies"
    - Use international standards (SNOMED CT, LOINC, ICD-10) for interoperability
    - Use Bangladesh Core for local context and requirements
    - Combine multiple code systems when needed

!!! warning "Version Management"
    Always track which version of a code system you're using. Code meanings can change between versions.

!!! info "Multiple Codings"
    FHIR supports multiple codings for the same concept. Use this to provide both local and international codes.

## Next Steps

- [Learn about Code Systems](../codesystems/index.md)
- [Explore Value Sets](../valuesets/index.md)
- [Using Terminologies Guide](using-terminologies.md)
- [API Reference](api-reference.md)

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/ZarishSphere-Platform/zarish-fhir-data/issues)
- **Documentation**: [Full documentation](https://zarishsphere-platform.github.io/zarish-fhir-data/)
- **FHIR Specification**: [HL7 FHIR](https://www.hl7.org/fhir/)
