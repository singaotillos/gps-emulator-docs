# Authentication

API authentication and security.

---

## Overview

API authentication is **optional** but recommended for production.

---

## Enabling Authentication

**In `.env` file:**
```bash
API_ENABLE_AUTHENTICATION=true
API_KEY=your-secret-api-key-here
```

---

## Generating API Key

```bash
# Generate secure random key
openssl rand -hex 32
```

---

## Using API Key

**Header method (recommended):**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY"      http://localhost:5000/api/status
```

**Query parameter:**
```bash
curl "http://localhost:5000/api/status?api_key=YOUR_API_KEY"
```

---

## Python Example

```python
import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.get("http://localhost:5000/api/status", headers=headers)
```

---

*Last updated: October 2025*
