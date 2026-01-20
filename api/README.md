## Endpoints

### Competition (subcontest) results (JSON for frontend rendering)

This provides the same data as the `https://eoa.ee/?id=...` results table, but as JSON (rendering is up to the frontend).

- `GET /subcontests/1/results`

Examples:

```bash
curl 'http://localhost:8000/subcontests/1/results' | jq
```

### List valid `subcontest_id` values

- `GET /subcontest-ids`

```bash
curl 'http://localhost:8000/subcontest-ids' | jq
```
