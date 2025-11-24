# Zarish FHIR Data

**Part of the ZarishSphere Platform - A No-Code FHIR Healthcare Data Management System**

This repository contains FHIR-compliant healthcare data resources, terminology definitions, and reference data for the ZarishSphere Platform. It serves as the central data repository for code systems, value sets, and sample FHIR resources.

## 🚀 Technology Stack

- **Language**: Go 1.23+
- **Data Format**: JSON (FHIR format)
- **Documentation**: MkDocs Material with Mermaid diagrams
- **Terminologies**: SNOMED CT, LOINC, ICD-10, RxNorm

## 📋 Prerequisites

- **Go**: Version 1.23 or higher ([Download Go](https://go.dev/dl/))
- **Python**: Version 3.8+ for MkDocs ([Download Python](https://www.python.org/downloads/))
- **Git**: For version control

### Checking Your Installation

```bash
go version      # Should show go1.23 or higher
python3 --version # Should show Python 3.8 or higher
git --version   # Should show git version 2.x.x
```

## 🛠️ Step-by-Step Development Setup

### Step 1: Clone the Repository

```bash
cd ~/Desktop
git clone https://github.com/ZarishSphere-Platform/zarish-fhir-data.git
cd zarish-fhir-data
```

### Step 2: Install Go Dependencies

```bash
go mod download
go mod tidy
```

### Step 3: Explore the Data Structure

```bash
# View terminology data
ls -la terminology/

# View code systems
ls -la terminology/codesystems/

# View value sets
ls -la terminology/valuesets/
```

### Step 4: Validate FHIR Resources

```bash
# Run validation tests
go test ./...

# Validate specific resource
go run pkg/validator/main.go --resource=terminology/codesystems/snomed-ct.json
```

## 📁 Project Structure

```
zarish-fhir-data/
├── terminology/
│   ├── codesystems/          # Code system definitions
│   │   ├── snomed-ct.json
│   │   ├── loinc.json
│   │   ├── icd-10.json
│   │   └── rxnorm.json
│   ├── valuesets/            # Value set definitions
│   │   ├── vital-signs.json
│   │   ├── medications.json
│   │   └── diagnoses.json
│   └── conceptmaps/          # Concept mappings
├── pkg/
│   └── validator/            # FHIR validation tools
├── docs/                     # MkDocs documentation
│   ├── index.md
│   ├── codesystems/
│   ├── valuesets/
│   └── guides/
├── mkdocs.yml               # MkDocs configuration
├── go.mod
└── README.md
```

## 📚 Available Terminologies

### Code Systems

- **SNOMED CT**: Clinical terminology (300,000+ concepts)
- **LOINC**: Laboratory observations (90,000+ codes)
- **ICD-10**: Disease classification (70,000+ codes)
- **RxNorm**: Medication terminology (100,000+ concepts)

### Value Sets

- **Vital Signs**: Blood pressure, temperature, heart rate, etc.
- **Medications**: Common medications and drug classes
- **Diagnoses**: Common diagnosis codes
- **Procedures**: Medical procedures and interventions
- **Allergies**: Allergy and intolerance codes

## 🔍 Using the Data

### In FHIR Server

The data is automatically loaded by the Zarish FHIR Server and Terminology Server.

### Programmatically

```go
import "github.com/zarishsphere-platform/zarish-fhir-data/pkg/terminology"

// Load a code system
cs, err := terminology.LoadCodeSystem("snomed-ct")

// Load a value set
vs, err := terminology.LoadValueSet("vital-signs")

// Validate a code
valid := terminology.ValidateCode("http://snomed.info/sct", "386661006")
```

## 📖 Documentation

Comprehensive documentation is available at:
**https://zarishsphere-platform.github.io/zarish-fhir-data/**

The documentation includes:
- Interactive terminology browser
- Code system hierarchies with Mermaid diagrams
- Value set expansions
- Usage guides and examples
- API reference

### Building Documentation Locally

```bash
# Install MkDocs Material
pip install mkdocs-material mkdocs-mermaid2-plugin

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

Documentation will be available at `http://localhost:8000`

## 🔧 Available Commands

| Command | Description |
|---------|-------------|
| `go test ./...` | Run validation tests |
| `go run pkg/validator/main.go` | Validate FHIR resources |
| `mkdocs serve` | Serve documentation locally |
| `mkdocs build` | Build documentation |

## 🧪 Testing

```bash
# Run all tests
go test ./...

# Test specific package
go test ./pkg/validator

# Validate all terminologies
go test ./terminology/...
```

## 📊 Data Statistics

- **Total Code Systems**: 4 major terminologies
- **Total Value Sets**: 50+ curated value sets
- **Total Concepts**: 500,000+ clinical concepts
- **Languages**: English (primary), with multilingual support

## 🔄 Updating Terminology Data

### Adding a New Code System

1. Create JSON file in `terminology/codesystems/`
2. Follow FHIR CodeSystem resource structure
3. Validate with `go test`
4. Update documentation in `docs/codesystems/`

### Adding a New Value Set

1. Create JSON file in `terminology/valuesets/`
2. Follow FHIR ValueSet resource structure
3. Reference existing code systems
4. Validate and document

## 🌐 FHIR Compliance

All data resources comply with:
- **FHIR Version**: R4 (4.0.1)
- **Profiles**: US Core, International Patient Summary
- **Validation**: FHIR Validator conformance

## 🐛 Troubleshooting

### Validation Fails

```bash
# Check JSON syntax
cat terminology/codesystems/snomed-ct.json | jq .

# Run validator with verbose output
go test -v ./pkg/validator
```

### Documentation Build Fails

```bash
# Reinstall MkDocs
pip install --upgrade mkdocs-material

# Check mkdocs.yml syntax
mkdocs build --strict
```

## 📚 Learning Resources

- [FHIR Terminology Module](https://www.hl7.org/fhir/terminology-module.html)
- [SNOMED CT Browser](https://browser.ihtsdotools.org/)
- [LOINC Search](https://loinc.org/search/)
- [ICD-10 Codes](https://www.icd10data.com/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)

## 🤝 Contributing

1. Fork the repository
2. Add or update terminology data
3. Validate changes with tests
4. Update documentation
5. Submit pull request

## 📄 License

This project is part of the ZarishSphere Platform.

## 🔗 Related Repositories

- [zarish-terminology-server](https://github.com/ZarishSphere-Platform/zarish-terminology-server) - Terminology API Server
- [zarish-fhir-server](https://github.com/ZarishSphere-Platform/zarish-fhir-server) - FHIR Server
- [zarish-fhir-profiles](https://github.com/ZarishSphere-Platform/zarish-fhir-profiles) - FHIR Profile Definitions

## 🆘 Getting Help

- Browse [Documentation](https://zarishsphere-platform.github.io/zarish-fhir-data/)
- Check [Issues](https://github.com/ZarishSphere-Platform/zarish-fhir-data/issues)
- Create new issue with details
