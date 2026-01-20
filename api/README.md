## Endpoints

### Subcontest tree (each endpoint goes one level deeper)

- `GET /contest` → subjects (abbrev + full name)
- `GET /contest/{subject}` → seasons (format `YYYY-YYYY`)
- `GET /contest/{subject}/{season}` → contest types
- `GET /contest/{subject}/{season}/{type}` → age groups
- `GET /contest/{subject}/{season}/{type}/{age_group}` → results (`format=json|csv`)
- `GET /subcontests/{subcontest_id}` → results (`format=json|csv`)

Examples:

```bash
curl 'http://localhost:8000/contest' | jq
curl 'http://localhost:8000/contest/efo' | jq
curl 'http://localhost:8000/contest/efo/2023-2024' | jq
curl 'http://localhost:8000/contest/efo/2023-2024/lahtine' | jq
curl 'http://localhost:8000/contest/efo/2023-2024/lahtine/12.%20klass' | jq
curl -L 'http://localhost:8000/contest/efo/2023-2024/lahtine/12.%20klass?format=csv'
curl 'http://localhost:8000/subcontests/1' | jq
```

`/subjects` was removed; use `GET /contest` for the subject list (abbrev + full name).

### People

- `GET /contestant/{person_id}` (only for publishable persons)
- `GET /mentor/{mentor_id}` (only for publishable mentors; only includes publishable students)
- `GET /people/search?q=...` (only returns publishable persons)

### Schools

- `GET /schools` (returns `school_id` + `school_name`)
- `GET /schools/search?q=...` (returns `school_id` + `school_name`)
- `GET /schools/{school_id}/students` (only includes publishable students)
- `GET /schools/{school_id}/mentors` (only includes publishable students and mentors)

### Statistics

- `GET /statistics/students`
- `GET /statistics/students?weighted=true`
- `GET /statistics/students?format=csv`
