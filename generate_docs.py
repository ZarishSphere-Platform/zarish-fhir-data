#!/usr/bin/env python3
"""
Generate comprehensive MkDocs documentation from Bangladesh FHIR Core resources
"""

import json
import os
from pathlib import Path

# Directories
BASE_DIR = Path("/home/ariful/Desktop/ZarishSphere-Platform/zarish-fhir-data")
TERMINOLOGY_DIR = BASE_DIR / "terminology/bd-core/package"
DOCS_DIR = BASE_DIR / "docs"
CS_DOCS_DIR = DOCS_DIR / "codesystems"
VS_DOCS_DIR = DOCS_DIR / "valuesets"

# Create directories
CS_DOCS_DIR.mkdir(parents=True, exist_ok=True)
VS_DOCS_DIR.mkdir(parents=True, exist_ok=True)

def generate_codesystem_page(cs_data):
    """Generate markdown page for a CodeSystem"""
    cs_id = cs_data.get('id', '')
    name = cs_data.get('name', '')
    title = cs_data.get('title', '')
    description = cs_data.get('description', '')
    url = cs_data.get('url', '')
    count = cs_data.get('count', 0)
    concepts = cs_data.get('concept', [])
    
    # Create markdown content
    md = f"""# {title}

{description}

## Overview

- **ID**: `{cs_id}`
- **Name**: {name}
- **System URL**: `{url}`
- **Total Concepts**: {count}
- **Status**: {cs_data.get('status', 'draft')}

## Concepts

"""
    
    if concepts:
        md += "| Code | Display Name |\n"
        md += "|------|-------------|\n"
        for concept in concepts[:50]:  # Limit to first 50 for readability
            code = concept.get('code', '')
            display = concept.get('display', '')
            md += f"| `{code}` | {display} |\n"
        
        if len(concepts) > 50:
            md += f"\n*...and {len(concepts) - 50} more concepts*\n"
    
    md += f"""

## Usage in FHIR

### Example

```json
{{
  "resourceType": "CodeableConcept",
  "coding": [{{
    "system": "{url}",
    "code": "{concepts[0].get('code', '') if concepts else ''}",
    "display": "{concepts[0].get('display', '') if concepts else ''}"
  }}]
}}
```

## Related Resources

- [Back to Code Systems](index.md)
- [View Value Sets](../valuesets/index.md)
"""
    
    return md

def generate_valueset_page(vs_data):
    """Generate markdown page for a ValueSet"""
    vs_id = vs_data.get('id', '')
    name = vs_data.get('name', '')
    title = vs_data.get('title', '')
    description = vs_data.get('description', '')
    url = vs_data.get('url', '')
    compose = vs_data.get('compose', {})
    includes = compose.get('include', [])
    
    md = f"""# {title}

{description}

## Overview

- **ID**: `{vs_id}`
- **Name**: {name}
- **URL**: `{url}`
- **Status**: {vs_data.get('status', 'draft')}

## Composition

This value set includes codes from the following code systems:

"""
    
    for include in includes:
        system = include.get('system', '')
        md += f"- `{system}`\n"
    
    md += f"""

## Usage in FHIR

### Example

```json
{{
  "resourceType": "CodeableConcept",
  "coding": [{{
    "system": "{includes[0].get('system', '') if includes else ''}",
    "code": "example-code",
    "display": "Example Display"
  }}]
}}
```

## Related Resources

- [Back to Value Sets](index.md)
- [View Code Systems](../codesystems/index.md)
"""
    
    return md

# Process all CodeSystems
codesystems = []
for file in TERMINOLOGY_DIR.glob("CodeSystem-*.json"):
    with open(file) as f:
        data = json.load(f)
        codesystems.append(data)
        
        # Generate page
        md_content = generate_codesystem_page(data)
        output_file = CS_DOCS_DIR / f"{data['id']}.md"
        with open(output_file, 'w') as out:
            out.write(md_content)
        print(f"Created: {output_file}")

# Process all ValueSets
valuesets = []
for file in TERMINOLOGY_DIR.glob("ValueSet-*.json"):
    with open(file) as f:
        data = json.load(f)
        valuesets.append(data)
        
        # Generate page
        md_content = generate_valueset_page(data)
        output_file = VS_DOCS_DIR / f"{data['id']}.md"
        with open(output_file, 'w') as out:
            out.write(md_content)
        print(f"Created: {output_file}")

print(f"\n✅ Generated {len(codesystems)} CodeSystem pages")
print(f"✅ Generated {len(valuesets)} ValueSet pages")
