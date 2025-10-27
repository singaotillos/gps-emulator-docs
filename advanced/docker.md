# Docker Deployment

Advanced Docker deployment guide.

---

## Production Docker Setup

See {% content-ref url="../getting-started/docker-setup.md" %}[docker-setup.md](../getting-started/docker-setup.md){% endcontent-ref %} for basic setup.

---

## Docker Swarm

**Deploy as swarm service:**

```bash
docker service create \
  --name gps-emulator \
  --replicas 3 \
  --publish 5000:5000 \
  gps-emulator:latest
```

---

## Kubernetes

See getting-started/docker-setup.md for Kubernetes deployment YAML.

---

*Last updated: October 2025*
