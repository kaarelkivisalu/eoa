## Endpoints

### Competition (subcontest) results (JSON for frontend rendering)

This provides the same data as the `https://eoa.ee/?id=...` results table, but as JSON (rendering is up to the frontend).

- `GET /subcontests/1/results`

Examples:

```bash
curl 'http://localhost:8000/subcontests/1/results' | jq
```

CSV export:

```bash
curl -L 'http://localhost:8000/subcontests/1/results?format=csv'
```

### List valid `subcontest_id` values (with metadata)

- `GET /subcontest-ids`
- `GET /subcontest-ids?subject_abbrev=efo`

```bash
curl 'http://localhost:8000/subcontest-ids' | jq
```

### Subjects (with 3-letter abbreviations)

- `GET /subjects`

```bash
curl 'http://localhost:8000/subjects' | jq
```
