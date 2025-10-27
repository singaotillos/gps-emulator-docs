# Security Settings

Secure your production deployment.

---

## Production Checklist

{% hint style="success" %}
**Complete ALL items before production:**
{% endhint %}

### 1. Enable API Authentication

```bash
API_ENABLE_AUTHENTICATION=true
API_KEY=use-openssl-rand-hex-32
```

### 2. Disable Debug Mode

```bash
WEB_DEBUG=false
LOG_LEVEL=WARNING
```

### 3. Restrict Network Access

```yaml
web_interface:
  host: 127.0.0.1  # Localhost only
```

### 4. Use HTTPS

Use reverse proxy (Nginx/Caddy) with SSL.

### 5. Secure Traccar Credentials

```bash
TRACCAR_PASSWORD=use-strong-password
```

### 6. Enable Rate Limiting

```bash
API_RATE_LIMITING=true
API_MAX_REQUESTS_PER_MINUTE=100
```

---

*Last updated: October 2025*
