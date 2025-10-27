# Performance Tuning

Optimize emulator performance for your use case.

---

## Maximum Performance

**For 100+ devices:**

```yaml
# config.yaml
simulation:
  update_interval: 5.0
  enable_traffic_simulation: false

advanced:
  max_concurrent_emulators: 200
  performance_mode: fast
  
monitoring:
  enabled: false
```

---

## Low Resource Mode

**For Raspberry Pi / minimal hardware:**

```yaml
simulation:
  update_interval: 30.0

advanced:
  max_concurrent_emulators: 10
  performance_mode: efficient
  memory_limit_mb: 256
```

---

## Monitoring

**Check CPU/Memory:**
```bash
docker stats gps-emulator
```

---

*Last updated: October 2025*
