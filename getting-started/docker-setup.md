# Docker Setup

Run the GPS Emulator using Docker containers.

---

## Why Docker?

{% hint style="success" %}
**Benefits of using Docker:**
- ✅ No Python installation needed
- ✅ Isolated environment
- ✅ Easy deployment
- ✅ Consistent across platforms
- ✅ Easy scaling
{% endhint %}

---

## Prerequisites

### Install Docker

{% tabs %}
{% tab title="Windows" %}
**Docker Desktop for Windows:**

1. Download from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Run installer
3. Enable WSL 2 backend (recommended)
4. Restart computer

**Verify installation:**
```powershell
docker --version
docker-compose --version
```
{% endtab %}

{% tab title="Linux" %}
**Ubuntu/Debian:**
```bash
# Update packages
sudo apt update

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install docker-compose-plugin

# Verify
docker --version
docker compose version
```
{% endtab %}

{% tab title="macOS" %}
**Docker Desktop for Mac:**

1. Download from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Drag to Applications folder
3. Open Docker.app
4. Wait for Docker to start

**Verify:**
```bash
docker --version
docker-compose --version
```
{% endtab %}
{% endtabs %}

---

## Quick Start with Docker

### Method 1: Docker Run

**Single command to start:**

```bash
docker run -d \
  --name gps-emulator \
  -p 5000:5000 \
  -p 5001-5232:5001-5232 \
  -v gps-emulator-data:/app/data \
  your-dockerhub-username/gps-emulator:latest
```

**Access web interface:**
```
http://localhost:5000
```

---

### Method 2: Docker Compose (Recommended)

**Create `docker-compose.yml`:**

```yaml
version: '3.8'

services:
  gps-emulator:
    image: your-dockerhub-username/gps-emulator:latest
    container_name: gps-emulator
    restart: unless-stopped
    ports:
      - "5000:5000"
      - "5001-5232:5001-5232"
    volumes:
      - ./data:/app/data
      - ./config.yaml:/app/config.yaml
      - ./.env:/app/.env
    environment:
      - WEB_PORT=5000
      - TRACCAR_HOST=traccar
      - TRACCAR_PORT=8082
    networks:
      - gps-network

  traccar:
    image: traccar/traccar:latest
    container_name: traccar
    restart: unless-stopped
    ports:
      - "8082:8082"
      - "5001-5232:5001-5232"
    volumes:
      - traccar-data:/opt/traccar/data
    networks:
      - gps-network

networks:
  gps-network:
    driver: bridge

volumes:
  traccar-data:
```

**Start services:**
```bash
docker-compose up -d
```

**Stop services:**
```bash
docker-compose down
```

---

## Building from Source

### Create Dockerfile

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose ports
EXPOSE 5000
EXPOSE 5001-5232

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV WEB_HOST=0.0.0.0
ENV WEB_PORT=5000

# Create data directory
RUN mkdir -p /app/data

# Run application
CMD ["python", "app.py"]
```

### Build Image

```bash
# Build image
docker build -t gps-emulator:latest .

# Tag for Docker Hub
docker tag gps-emulator:latest your-username/gps-emulator:latest

# Push to Docker Hub (optional)
docker push your-username/gps-emulator:latest
```

---

## Configuration

### Environment Variables

**Pass via docker run:**
```bash
docker run -d \
  -e WEB_PORT=5000 \
  -e TRACCAR_HOST=localhost \
  -e TRACCAR_PORT=8082 \
  -e API_KEY=your-api-key \
  gps-emulator:latest
```

**Or use .env file:**
```bash
docker run -d \
  --env-file .env \
  gps-emulator:latest
```

### Volume Mounts

**Persistent data:**
```bash
docker run -d \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/config.yaml:/app/config.yaml \
  -v $(pwd)/.env:/app/.env \
  gps-emulator:latest
```

**What to mount:**
- `./data` - Database and logs
- `./config.yaml` - Configuration file
- `./.env` - Environment variables

---

## Docker Compose Examples

### Example 1: Basic Setup

```yaml
version: '3.8'

services:
  gps-emulator:
    image: gps-emulator:latest
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

### Example 2: With Traccar

```yaml
version: '3.8'

services:
  gps-emulator:
    image: gps-emulator:latest
    container_name: gps-emulator
    ports:
      - "5000:5000"
    environment:
      - TRACCAR_HOST=traccar
      - TRACCAR_PORT=8082
    depends_on:
      - traccar
    networks:
      - gps-network

  traccar:
    image: traccar/traccar:latest
    container_name: traccar
    ports:
      - "8082:8082"
      - "5001-5232:5001-5232"
    volumes:
      - traccar-data:/opt/traccar/data
    networks:
      - gps-network

networks:
  gps-network:

volumes:
  traccar-data:
```

### Example 3: Production with PostgreSQL

```yaml
version: '3.8'

services:
  gps-emulator:
    image: gps-emulator:latest
    container_name: gps-emulator
    restart: unless-stopped
    ports:
      - "5000:5000"
      - "5001-5232:5001-5232"
    environment:
      - DATABASE_URL=postgresql://user:pass@postgres:5432/gps_emulator
      - TRACCAR_HOST=traccar
    depends_on:
      - postgres
      - traccar
    networks:
      - gps-network

  postgres:
    image: postgres:15
    container_name: gps-postgres
    restart: unless-stopped
    environment:
      - POSTGRES_DB=gps_emulator
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - gps-network

  traccar:
    image: traccar/traccar:latest
    container_name: traccar
    restart: unless-stopped
    ports:
      - "8082:8082"
    volumes:
      - traccar-data:/opt/traccar/data
    networks:
      - gps-network

networks:
  gps-network:

volumes:
  postgres-data:
  traccar-data:
```

---

## Management Commands

### Start/Stop Containers

```bash
# Start
docker-compose up -d

# Stop
docker-compose stop

# Restart
docker-compose restart

# Stop and remove
docker-compose down

# Stop and remove with volumes
docker-compose down -v
```

### View Logs

```bash
# All services
docker-compose logs

# Follow logs
docker-compose logs -f

# Specific service
docker-compose logs gps-emulator

# Last 100 lines
docker-compose logs --tail=100
```

### Access Container Shell

```bash
# Interactive bash
docker exec -it gps-emulator bash

# Run single command
docker exec gps-emulator ls -la

# Check Python version
docker exec gps-emulator python --version
```

### Monitor Resources

```bash
# Container stats
docker stats gps-emulator

# All containers
docker stats
```

---

## Scaling

### Multiple Emulator Instances

```yaml
version: '3.8'

services:
  gps-emulator-1:
    image: gps-emulator:latest
    container_name: gps-emulator-1
    ports:
      - "5000:5000"
    environment:
      - INSTANCE_ID=1

  gps-emulator-2:
    image: gps-emulator:latest
    container_name: gps-emulator-2
    ports:
      - "5001:5000"
    environment:
      - INSTANCE_ID=2

  gps-emulator-3:
    image: gps-emulator:latest
    container_name: gps-emulator-3
    ports:
      - "5002:5000"
    environment:
      - INSTANCE_ID=3
```

### Using Docker Compose Scale

```yaml
version: '3.8'

services:
  gps-emulator:
    image: gps-emulator:latest
    deploy:
      replicas: 3
    ports:
      - "5000-5002:5000"
```

**Scale command:**
```bash
docker-compose up -d --scale gps-emulator=5
```

---

## Kubernetes Deployment

### Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gps-emulator
spec:
  replicas: 3
  selector:
    matchLabels:
      app: gps-emulator
  template:
    metadata:
      labels:
        app: gps-emulator
    spec:
      containers:
      - name: gps-emulator
        image: gps-emulator:latest
        ports:
        - containerPort: 5000
        env:
        - name: WEB_PORT
          value: "5000"
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "2000m"
---
apiVersion: v1
kind: Service
metadata:
  name: gps-emulator
spec:
  selector:
    app: gps-emulator
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer
```

**Deploy:**
```bash
kubectl apply -f deployment.yaml
```

---

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs gps-emulator

# Check container status
docker ps -a

# Inspect container
docker inspect gps-emulator
```

### Port Already in Use

```bash
# Find process using port
# Linux/Mac:
lsof -i :5000

# Windows PowerShell:
netstat -ano | findstr :5000

# Change port in docker-compose.yml
ports:
  - "5001:5000"  # Use 5001 instead
```

### Permission Issues

```bash
# Fix volume permissions
sudo chown -R $USER:$USER ./data

# Or run as root (not recommended)
docker run --user root ...
```

### Can't Connect to Traccar

```bash
# Check network
docker network ls
docker network inspect gps-network

# Ping from container
docker exec gps-emulator ping traccar

# Check Traccar is running
docker ps | grep traccar
```

---

## Best Practices

{% hint style="success" %}
**Production recommendations:**
{% endhint %}

1. **Use specific tags:**
   ```yaml
   image: gps-emulator:2.0.0  # Not :latest
   ```

2. **Set resource limits:**
   ```yaml
   deploy:
     resources:
       limits:
         cpus: '2.0'
         memory: 2G
   ```

3. **Use health checks:**
   ```yaml
   healthcheck:
     test: ["CMD", "curl", "-f", "http://localhost:5000/api/status"]
     interval: 30s
     timeout: 10s
     retries: 3
   ```

4. **Persist data:**
   ```yaml
   volumes:
     - ./data:/app/data
   ```

5. **Use secrets for passwords:**
   ```yaml
   secrets:
     - db_password
   ```

---

## Next Steps

{% content-ref url="quick-start.md" %}
[quick-start.md](quick-start.md)
{% endcontent-ref %}

{% content-ref url="../advanced/docker.md" %}
[docker.md](../advanced/docker.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
