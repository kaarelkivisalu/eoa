## Endpoints

### Competition (subcontest) results (JSON for frontend rendering)

This provides the same data as the `https://eoa.ee/?id=...` results table, but as JSON (rendering is up to the frontend).

- `GET /results?id=1`
- `GET /subcontests/1/results`

Examples:

```bash
curl 'http://localhost:8000/results?id=1'

curl 'http://localhost:8000/subcontests/1/results' | jq
```
