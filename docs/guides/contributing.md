# Contributing

Thank you for your interest in contributing to Zarish FHIR Data! This guide will help you get started.

## Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features or terminologies
- 📝 Improve documentation
- 🔧 Submit code changes
- ✅ Add or update terminologies

## Getting Started

### 1. Fork the Repository

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/zarish-fhir-data.git
cd zarish-fhir-data
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes

Follow the guidelines below for different types of contributions.

## Adding New Terminologies

### Code Systems

1. Create a new JSON file in `terminology/bd-core/package/`:

```json
{
  "resourceType": "CodeSystem",
  "id": "bd-your-codesystem",
  "url": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-your-codesystem",
  "version": "0.2.0",
  "name": "BDYourCodeSystemCS",
  "title": "Bangladesh Your CodeSystem",
  "status": "draft",
  "experimental": false,
  "publisher": "Directorate General of Health Services (DGHS), Bangladesh",
  "description": "Description of your code system",
  "caseSensitive": true,
  "content": "complete",
  "concept": [
    {
      "code": "1",
      "display": "Concept 1"
    },
    {
      "code": "2",
      "display": "Concept 2"
    }
  ]
}
```

2. Run the documentation generator:

```bash
python3 generate_docs.py
```

3. Update `mkdocs.yml` to include your new code system in the navigation.

### Value Sets

1. Create a new JSON file in `terminology/bd-core/package/`:

```json
{
  "resourceType": "ValueSet",
  "id": "bd-your-valueset",
  "url": "https://fhir.dghs.gov.bd/core/ValueSet/bd-your-valueset",
  "version": "0.2.0",
  "name": "BDYourValueSetVS",
  "title": "Bangladesh Your ValueSet",
  "status": "draft",
  "publisher": "Directorate General of Health Services (DGHS), Bangladesh",
  "description": "Description of your value set",
  "compose": {
    "include": [{
      "system": "https://fhir.dghs.gov.bd/core/CodeSystem/bd-your-codesystem"
    }]
  }
}
```

2. Run the documentation generator and update navigation.

## Documentation

### Writing Documentation

- Use clear, concise language
- Include code examples
- Add diagrams where helpful (using Mermaid)
- Follow the existing documentation structure

### Documentation Style

```markdown
# Page Title

Brief introduction paragraph.

## Section Heading

Content with examples:

\`\`\`json
{
  "example": "code"
}
\`\`\`

!!! tip "Helpful Tip"
    Provide useful information here.
```

## Code Style

### Go Code

```go
// Use clear variable names
func ValidateCode(system, code string) bool {
    // Add comments for complex logic
    for _, concept := range concepts {
        if concept.Code == code {
            return true
        }
    }
    return false
}
```

### JSON Formatting

- Use 2-space indentation
- Include all required FHIR elements
- Follow FHIR naming conventions

## Testing

### Validate FHIR Resources

```bash
# Install FHIR validator
wget https://github.com/hapifhir/org.hl7.fhir.core/releases/latest/download/validator_cli.jar

# Validate a resource
java -jar validator_cli.jar terminology/bd-core/package/CodeSystem-bd-your-codesystem.json
```

### Test Documentation Build

```bash
# Install MkDocs
pip install mkdocs-material mkdocs-mermaid2-plugin

# Build and serve locally
mkdocs serve

# Open http://localhost:8000
```

## Commit Guidelines

### Commit Message Format

```
type(scope): subject

body

footer
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

```bash
git commit -m "feat(codesystem): add Bangladesh education levels code system"
git commit -m "docs(guides): improve getting started guide with more examples"
git commit -m "fix(valueset): correct blood group value set composition"
```

## Pull Request Process

### 1. Update Documentation

- Run `python3 generate_docs.py` if you added/modified terminologies
- Update `mkdocs.yml` if needed
- Test the documentation build

### 2. Create Pull Request

- Push your branch to GitHub
- Create a pull request with a clear title and description
- Link any related issues

### 3. Code Review

- Address reviewer feedback
- Keep the PR focused on a single change
- Update your branch if needed

## Review Checklist

Before submitting, ensure:

- [ ] FHIR resources validate successfully
- [ ] Documentation builds without errors
- [ ] All links work correctly
- [ ] Code examples are tested
- [ ] Commit messages follow guidelines
- [ ] No sensitive information is included

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the code of conduct

## Questions?

- 📧 Open an issue on GitHub
- 💬 Join our discussions
- 📚 Check existing documentation

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Zarish FHIR Data! 🎉
