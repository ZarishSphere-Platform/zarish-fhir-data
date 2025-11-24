# API Reference

This guide provides reference information for programmatically accessing and using FHIR terminologies.

## Terminology Services

### Code System Lookup

Retrieve information about a specific code from a code system.

**Request:**
```http
GET /CodeSystem/$lookup?system=https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups&code=1
```

**Response:**
```json
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "name",
      "valueString": "BDBloodGroupCS"
    },
    {
      "name": "display",
      "valueString": "O Positive"
    },
    {
      "name": "system",
      "valueUri": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups"
    }
  ]
}
```

### Value Set Expansion

Expand a value set to get all included codes.

**Request:**
```http
GET /ValueSet/$expand?url=https://fhir.dghs.gov.bd/core/ValueSet/bd-blood-group-valueset
```

**Response:**
```json
{
  "resourceType": "ValueSet",
  "expansion": {
    "contains": [
      {
        "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
        "code": "1",
        "display": "O Positive"
      },
      {
        "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
        "code": "2",
        "display": "O Negative"
      }
      // ... more codes
    ]
  }
}
```

### Value Set Validation

Validate whether a code is in a value set.

**Request:**
```http
GET /ValueSet/$validate-code?url=https://fhir.dghs.gov.bd/core/ValueSet/bd-blood-group-valueset&system=https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups&code=1
```

**Response:**
```json
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "result",
      "valueBoolean": true
    },
    {
      "name": "display",
      "valueString": "O Positive"
    }
  ]
}
```

## Go Package Usage

### Loading Code Systems

```go
package main

import (
    "encoding/json"
    "os"
)

type CodeSystem struct {
    ResourceType string `json:"resourceType"`
    ID           string `json:"id"`
    Name         string `json:"name"`
    Title        string `json:"title"`
    URL          string `json:"url"`
    Concept      []Concept `json:"concept"`
}

type Concept struct {
    Code    string `json:"code"`
    Display string `json:"display"`
}

func LoadCodeSystem(path string) (*CodeSystem, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, err
    }
    
    var cs CodeSystem
    err = json.Unmarshal(data, &cs)
    return &cs, err
}

func main() {
    cs, _ := LoadCodeSystem("terminology/bd-core/package/CodeSystem-bd-blood-groups.json")
    
    for _, concept := range cs.Concept {
        println(concept.Code, concept.Display)
    }
}
```

### Validating Codes

```go
func (cs *CodeSystem) ValidateCode(code string) bool {
    for _, concept := range cs.Concept {
        if concept.Code == code {
            return true
        }
    }
    return false
}

// Usage
valid := cs.ValidateCode("1")  // true
invalid := cs.ValidateCode("99")  // false
```

### Looking Up Display Names

```go
func (cs *CodeSystem) GetDisplay(code string) string {
    for _, concept := range cs.Concept {
        if concept.Code == code {
            return concept.Display
        }
    }
    return ""
}

// Usage
display := cs.GetDisplay("1")  // "O Positive"
```

## REST API Endpoints

### Code Systems

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/CodeSystem` | GET | Search code systems |
| `/CodeSystem/{id}` | GET | Read a code system |
| `/CodeSystem/$lookup` | GET/POST | Look up a code |
| `/CodeSystem/$subsumes` | GET/POST | Test subsumption |

### Value Sets

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ValueSet` | GET | Search value sets |
| `/ValueSet/{id}` | GET | Read a value set |
| `/ValueSet/$expand` | GET/POST | Expand a value set |
| `/ValueSet/$validate-code` | GET/POST | Validate a code |

## Search Parameters

### Code System Search

```http
# Search by name
GET /CodeSystem?name=BDBloodGroupCS

# Search by URL
GET /CodeSystem?url=https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups

# Search by status
GET /CodeSystem?status=active
```

### Value Set Search

```http
# Search by name
GET /ValueSet?name=BDBloodGroupVS

# Search by URL
GET /ValueSet?url=https://fhir.dghs.gov.bd/core/ValueSet/bd-blood-group-valueset

# Search by reference
GET /ValueSet?reference=https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups
```

## Code Examples

### JavaScript/TypeScript

```typescript
interface Coding {
  system: string;
  code: string;
  display?: string;
}

interface CodeableConcept {
  coding?: Coding[];
  text?: string;
}

function createBloodGroupCoding(code: string, display: string): Coding {
  return {
    system: "https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
    code,
    display
  };
}

// Usage
const bloodGroup = createBloodGroupCoding("1", "O Positive");
```

### Python

```python
from typing import List, Dict

class Coding:
    def __init__(self, system: str, code: str, display: str = None):
        self.system = system
        self.code = code
        self.display = display
    
    def to_dict(self) -> Dict:
        result = {
            "system": self.system,
            "code": self.code
        }
        if self.display:
            result["display"] = self.display
        return result

# Usage
blood_group = Coding(
    system="https://fhir.dghs.gov.bd/core/CodeSystem/bd-blood-groups",
    code="1",
    display="O Positive"
)
```

## Error Handling

### Invalid Code

```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "code-invalid",
    "details": {
      "text": "The code '99' is not valid in the code system 'bd-blood-groups'"
    }
  }]
}
```

### Unknown Code System

```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "not-found",
    "details": {
      "text": "Code system 'unknown-system' not found"
    }
  }]
}
```

## Performance Tips

!!! tip "Cache Expansions"
    Value set expansions can be expensive. Cache them when possible.

!!! tip "Use Filters"
    When expanding large value sets, use filters to limit results.

!!! warning "Rate Limiting"
    Implement rate limiting for terminology service calls.

## Next Steps

- [Code Systems Reference](../codesystems/index.md)
- [Value Sets Reference](../valuesets/index.md)
- [Using Terminologies Guide](using-terminologies.md)
- [Contributing Guide](contributing.md)
