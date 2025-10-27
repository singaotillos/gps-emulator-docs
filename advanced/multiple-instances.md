# Multiple Instances

Run multiple emulator instances.

---

## Why Multiple Instances?

- Scale beyond single instance limits
- Separate environments (dev/test/prod)
- Load distribution

---

## Method 1: Different Ports

**Instance 1:**
```bash
WEB_PORT=5000 python app.py
```

**Instance 2:**
```bash
WEB_PORT=5001 python app.py
```

---

## Method 2: Docker Compose

```yaml
services:
  emulator-1:
    image: gps-emulator
    ports:
      - "5000:5000"
  
  emulator-2:
    image: gps-emulator
    ports:
      - "5001:5000"
```

---

*Last updated: October 2025*
