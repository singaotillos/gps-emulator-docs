# System Requirements

Hardware and software requirements for running the GPS Emulator.

---

## Minimum Requirements

### Hardware

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | 2 cores @ 2.0 GHz | 4 cores @ 2.5+ GHz |
| **RAM** | 4 GB | 8 GB or more |
| **Storage** | 2 GB free space | 5 GB free space |
| **Network** | 10 Mbps | 100 Mbps or faster |

{% hint style="info" %}
**Memory calculation:** Each device uses ~20-30 MB RAM
- 5 devices: ~512 MB
- 50 devices: ~2 GB
- 100 devices: ~4 GB
{% endhint %}

---

## Software Requirements

### Operating System

{% tabs %}
{% tab title="Windows" %}
**Supported versions:**
- ✅ Windows 11
- ✅ Windows 10 (64-bit)
- ✅ Windows Server 2019/2022
- ⚠️ Windows 8.1 (may work, not officially supported)

**Recommended:** Windows 10/11 64-bit
{% endtab %}

{% tab title="Linux" %}
**Supported distributions:**
- ✅ Ubuntu 20.04 LTS or newer
- ✅ Debian 11 (Bullseye) or newer
- ✅ CentOS 8 / Rocky Linux 8
- ✅ Fedora 35+
- ✅ Arch Linux

**Recommended:** Ubuntu 22.04 LTS
{% endtab %}

{% tab title="macOS" %}
**Supported versions:**
- ✅ macOS 13 (Ventura)
- ✅ macOS 12 (Monterey)
- ✅ macOS 11 (Big Sur)
- ⚠️ macOS 10.15 (Catalina) - may work

**Recommended:** macOS 12 or newer
{% endtab %}

{% tab title="Docker" %}
**Supported:**
- ✅ Docker 20.10+
- ✅ Docker Compose 2.0+
- ✅ Kubernetes 1.21+

Works on any OS with Docker support.
{% endtab %}
{% endtabs %}

---

### Python

{% hint style="warning" %}
**Important:** Python version requirements differ between deployment versions!
{% endhint %}

{% tabs %}
{% tab title="🖥️ Windows Local" %}
### Windows Local Version

**Required:** Python 3.13 or newer

**Why Python 3.13?**
- Uses threading-based concurrency
- Compatible with Flask's built-in development server
- No gevent dependency (which doesn't support Python 3.13+)
- Uses `requirements-windows.txt`

**Install Python 3.13:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ CHECK "Add Python to PATH"

**Check version:**
```bash
python --version
# Should output: Python 3.13.x
```
{% endtab %}

{% tab title="🌐 DigitalOcean Production" %}
### DigitalOcean Production Version

**Required:** Python 3.10 or 3.11

**Why Python 3.10-3.11?**
- Uses gevent for high-performance async operations
- Gevent currently supports Python 3.10 and 3.11
- Uses Gunicorn with gevent workers
- Uses `requirements.txt`

**Install Python (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

**Check version:**
```bash
python3 --version
# Should output: Python 3.10.x or 3.11.x
```

**Recommended:** Python 3.11 for best performance
{% endtab %}
{% endtabs %}

---

### Python Packages

**Installed automatically from requirements.txt:**

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.0+ | Web framework |
| Flask-SocketIO | 5.3.0+ | WebSocket support |
| Flask-CORS | 4.0.0+ | CORS handling |
| requests | 2.31.0+ | HTTP client |
| SQLAlchemy | 2.0.0+ | Database ORM |
| psutil | 5.9.0+ | System monitoring |

**Total disk space:** ~150 MB for all dependencies

---

## Network Requirements

### Ports Required

| Port | Protocol | Purpose | Required |
|------|----------|---------|----------|
| 5000 | HTTP | Web interface | ✅ Yes |
| 5001-5232 | TCP/UDP/HTTP | GPS protocols | ✅ Yes (per protocol) |
| 8082 | HTTP | Traccar (if used) | Optional |

{% hint style="warning" %}
**Firewall:** Allow inbound connections on required ports
{% endhint %}

### Port Configuration

**Change web interface port:**
```bash
# .env
WEB_PORT=5000  # Change to avoid conflicts
```

**Protocol ports configured in:**
- `config.yaml` - Protocol server settings
- Must match Traccar configuration

---

## Additional Software

### Optional but Recommended

**Traccar Server (for GPS tracking):**
- Version: 5.0 or newer
- Download: [traccar.org](https://www.traccar.org/download/)
- RAM: 1 GB minimum
- Ports: 8082 (web), 5001-5232 (protocols)

**Database (for production):**
- SQLite (included, default)
- PostgreSQL 12+ (recommended for production)
- MySQL 8.0+ (supported)

**Reverse Proxy (for production):**
- Nginx 1.18+
- Apache 2.4+
- Caddy 2.0+

**Version Control:**
- Git (for updates and deployment)

---

## Performance Considerations

### Device Limits by Hardware

| Hardware | Max Devices | Recommended |
|----------|-------------|-------------|
| **Basic** (2 cores, 4 GB RAM) | 20 devices | 5-10 devices |
| **Standard** (4 cores, 8 GB RAM) | 100 devices | 50 devices |
| **High-end** (8+ cores, 16 GB RAM) | 200+ devices | 100+ devices |
| **Server** (16+ cores, 32 GB RAM) | 500+ devices | 200+ devices |

{% hint style="info" %}
**Factors affecting performance:**
- Update interval (lower = more CPU)
- Number of protocols enabled
- Advanced simulation features
- Monitoring enabled
{% endhint %}

---

## Cloud Deployment

### Recommended Cloud Specs

{% tabs %}
{% tab title="AWS" %}
**Amazon EC2:**
- **Small:** t3.medium (2 vCPU, 4 GB) - 20 devices
- **Medium:** t3.large (2 vCPU, 8 GB) - 50 devices
- **Large:** c5.2xlarge (8 vCPU, 16 GB) - 100+ devices

**Storage:** 20 GB EBS
{% endtab %}

{% tab title="Google Cloud" %}
**Compute Engine:**
- **Small:** e2-medium (2 vCPU, 4 GB) - 20 devices
- **Medium:** e2-standard-2 (2 vCPU, 8 GB) - 50 devices
- **Large:** n2-standard-4 (4 vCPU, 16 GB) - 100+ devices

**Storage:** 20 GB Persistent Disk
{% endtab %}

{% tab title="DigitalOcean" %}
**Droplets:**
- **Small:** Basic 4 GB ($24/mo) - 20 devices
- **Medium:** Basic 8 GB ($48/mo) - 50 devices
- **Large:** CPU-Optimized 16 GB ($119/mo) - 100+ devices

**Storage:** 80-160 GB SSD
{% endtab %}

{% tab title="Azure" %}
**Virtual Machines:**
- **Small:** B2s (2 vCPU, 4 GB) - 20 devices
- **Medium:** B2ms (2 vCPU, 8 GB) - 50 devices
- **Large:** D4s v3 (4 vCPU, 16 GB) - 100+ devices

**Storage:** 128 GB Premium SSD
{% endtab %}
{% endtabs %}

---

## Compatibility Matrix

### Browser Compatibility

**Web Interface:**

| Browser | Minimum Version | Recommended |
|---------|-----------------|-------------|
| Chrome | 90+ | Latest |
| Firefox | 88+ | Latest |
| Safari | 14+ | Latest |
| Edge | 90+ | Latest |
| Opera | 76+ | Latest |

{% hint style="success" %}
**Best experience:** Latest Chrome or Firefox
{% endhint %}

### Python Version Compatibility

{% tabs %}
{% tab title="🖥️ Windows Local" %}
| Python | Status | Notes |
|--------|--------|-------|
| 3.13 | ✅ Required | Uses threading mode |
| 3.14+ | ✅ Should work | Future versions |
| 3.12 | ⚠️ May work | Not tested |
| 3.11 | ❌ Not compatible | Use Production version instead |
| 3.10 | ❌ Not compatible | Use Production version instead |
{% endtab %}

{% tab title="🌐 DigitalOcean Production" %}
| Python | Status | Notes |
|--------|--------|-------|
| 3.11 | ✅ Recommended | Best performance with gevent |
| 3.10 | ✅ Recommended | Stable with gevent |
| 3.9 | ⚠️ May work | Gevent support limited |
| 3.8 | ⚠️ Not tested | May work |
| 3.13+ | ❌ Not compatible | Gevent doesn't support yet |
{% endtab %}
{% endtabs %}

---

## Testing Your System

### Quick System Check

```bash
# Check CPU cores
# Linux/Mac:
nproc
# Windows PowerShell:
Get-WmiObject -Class Win32_Processor | Select-Object NumberOfCores

# Check RAM
# Linux:
free -h
# Mac:
sysctl hw.memsize
# Windows PowerShell:
Get-WmiObject -Class Win32_ComputerSystem | Select-Object TotalPhysicalMemory

# Check disk space
# Linux/Mac:
df -h
# Windows:
Get-PSDrive
```

### Performance Test Script

```python
# test_system.py
import psutil
import platform

print("=== System Information ===")
print(f"OS: {platform.system()} {platform.release()}")
print(f"CPU Cores: {psutil.cpu_count()}")
print(f"RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")
print(f"Disk: {psutil.disk_usage('/').free / (1024**3):.2f} GB free")
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"RAM Usage: {psutil.virtual_memory().percent}%")

# Estimate capacity
ram_gb = psutil.virtual_memory().total / (1024**3)
estimated_devices = int(ram_gb * 20)  # ~20 devices per GB
print(f"\n✅ Estimated capacity: {estimated_devices} devices")
```

---

## Special Environments

### Raspberry Pi

**Models supported:**
- ✅ Raspberry Pi 4 (4 GB or 8 GB)
- ⚠️ Raspberry Pi 3 B+ (limited to 5-10 devices)
- ❌ Raspberry Pi Zero (not recommended)

**OS:** Raspberry Pi OS (64-bit recommended)

**Capacity:** 10-20 devices on Pi 4

### WSL (Windows Subsystem for Linux)

**Supported:**
- ✅ WSL 2 (recommended)
- ⚠️ WSL 1 (may have limitations)

**Notes:**
- Use Ubuntu 22.04 from Microsoft Store
- Docker integration works
- Network ports accessible from Windows

### Virtual Machines

**Works on:**
- ✅ VMware Workstation/ESXi
- ✅ VirtualBox
- ✅ Hyper-V
- ✅ Parallels (macOS)

**Recommendations:**
- Allocate at least 2 vCPU, 4 GB RAM
- Use bridged networking
- Enable nested virtualization (for Docker)

---

## Troubleshooting

### Not Enough RAM

{% hint style="danger" %}
**Error:** Out of memory or system slowdown
{% endhint %}

**Solutions:**
1. Reduce number of devices
2. Increase update interval (less frequent updates)
3. Disable monitoring features
4. Add swap space (Linux)
5. Upgrade RAM

### CPU Bottleneck

{% hint style="warning" %}
**Symptom:** High CPU usage, slow updates
{% endhint %}

**Solutions:**
1. Increase update interval
2. Disable advanced simulation features
3. Use performance mode: `efficient`
4. Reduce concurrent devices
5. Upgrade CPU

### Port Conflicts

{% hint style="danger" %}
**Error:** Port already in use
{% endhint %}

**Solutions:**
1. Change web port in `.env`
2. Stop conflicting services
3. Use different protocol ports

---

## Next Steps

{% content-ref url="installation.md" %}
[installation.md](installation.md)
{% endcontent-ref %}

{% content-ref url="docker-setup.md" %}
[docker-setup.md](docker-setup.md)
{% endcontent-ref %}

{% content-ref url="quick-start.md" %}
[quick-start.md](quick-start.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
