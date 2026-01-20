## Endpoints

### Subcontest tree (each endpoint goes one level deeper)

- `GET /subcontest` → subjects (abbrev + full name)
- `GET /subcontest/{subject_abbrev}` → seasons (format `YYYY-YYYY`)
- `GET /subcontest/{subject_abbrev}/{season}` → contest types
- `GET /subcontest/{subject_abbrev}/{season}/{contest_type}` → age groups
- `GET /subcontest/{subject_abbrev}/{season}/{contest_type}/{age_group}` → results (`format=json|csv`)

Examples:

```bash
curl 'http://localhost:8000/subcontest' | jq
curl 'http://localhost:8000/subcontest/efo' | jq
curl 'http://localhost:8000/subcontest/efo/2023-2024' | jq
curl 'http://localhost:8000/subcontest/efo/2023-2024/lahtine' | jq
curl 'http://localhost:8000/subcontest/efo/2023-2024/lahtine/12.%20klass' | jq
curl -L 'http://localhost:8000/subcontest/efo/2023-2024/lahtine/12.%20klass?format=csv'
```

### Subjects (with 3-letter abbreviations)

- `GET /subjects`

```bash
curl 'http://localhost:8000/subjects' | jq
```
