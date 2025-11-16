# DigitalOcean Production Deployment

Complete guide for deploying the GPS Emulator on DigitalOcean (or any Ubuntu server) for production use.

---

## Overview

This guide covers the **Production Server Version** deployed on DigitalOcean, optimized for:

- ✅ **Ubuntu 22.04/24.04 LTS**
- ✅ **Production environment** (Gunicorn + Gevent)
- ✅ **Systemd service** (auto-start on boot)
- ✅ **Public access** (0.0.0.0)
- ✅ **High performance** (gevent async workers)

{% hint style="info" %}
**Local Development?** For Windows localhost installation, see [Windows Local Installation](windows-local.md)
{% endhint %}

---

## Server Requirements

### Minimum Specifications

- **OS**: Ubuntu 22.04 or 24.04 LTS
- **RAM**: 2 GB
- **CPU**: 1 vCPU
- **Storage**: 10 GB SSD
- **Network**: Public IP address

### Recommended Specifications

- **RAM**: 4 GB (for 50+ devices)
- **CPU**: 2 vCPUs
- **Storage**: 20 GB SSD
- **Network**: 100 Mbps+

---

## DigitalOcean Droplet Setup

### 1. Create Droplet

1. **Login** to DigitalOcean: https://cloud.digitalocean.com/
2. Click **"Create"** → **"Droplets"**
3. **Choose an image**:
   - Distribution: **Ubuntu 24.04 LTS x64**
4. **Choose Size**:
   - Basic Plan: $6/month (1 GB RAM, 1 vCPU)
   - Recommended: $12/month (2 GB RAM, 2 vCPUs)
5. **Choose datacenter region**:
   - Select closest to your Traccar server
6. **Authentication**:
   - SSH keys (recommended) or Password
7. **Hostname**: `gps-emulator-production`
8. Click **"Create Droplet"**

### 2. Connect via SSH

```bash
ssh root@YOUR_DROPLET_IP
```

Example:
```bash
ssh root@157.245.236.143
```

---

## Installation

### Method 1: Automated Installation (Recommended)

The server includes an automated installation script.

#### Step 1: Upload Files

**From your local machine:**

```bash
# Using SCP
scp -r universal-gps-emulator root@YOUR_DROPLET_IP:/opt/

# Or using SFTP
sftp root@YOUR_DROPLET_IP
put -r universal-gps-emulator /opt/
```

**Or clone from repository** (if you have it in Git):

```bash
cd /opt
git clone https://github.com/yourusername/universal-gps-emulator.git
cd universal-gps-emulator
```

#### Step 2: Run Installation Script

```bash
cd /opt/universal-gps-emulator
chmod +x install.sh
sudo ./install.sh
```

**What the script does:**

1. ✅ Updates system packages
2. ✅ Installs Python 3.10+ and pip
3. ✅ Creates virtual environment
4. ✅ Installs production dependencies (including gevent)
5. ✅ Configures `.env` for production
6. ✅ Creates systemd service
7. ✅ Configures UFW firewall
8. ✅ Starts the service

**Expected output:**

```
================================================================
   Universal GPS Tracker Emulator - Ubuntu Installation
   COMMERCIAL UNLIMITED VERSION
================================================================

[1/8] Updating system packages...
[2/8] Installing Python 3.10+...
[3/8] Installing pip...
[4/8] Creating virtual environment...
[5/8] Installing dependencies...
[6/8] Configuring application...
[7/8] Creating systemd service...
[8/8] Configuring firewall...

================================================================
   INSTALLATION COMPLETED!
================================================================

Service Status: ● gps-emulator.service - active (running)
Web Interface: http://YOUR_SERVER_IP:5000
Protocols: 86 GPS protocols supported

Service Commands:
  Start:   sudo systemctl start gps-emulator
  Stop:    sudo systemctl stop gps-emulator
  Restart: sudo systemctl restart gps-emulator
  Status:  sudo systemctl status gps-emulator
  Logs:    sudo journalctl -u gps-emulator -f
```

#### Step 3: Verify Installation

```bash
sudo systemctl status gps-emulator
```

Expected output:
```
● gps-emulator.service - Universal GPS Tracker Emulator
     Loaded: loaded (/etc/systemd/system/gps-emulator.service; enabled)
     Active: active (running) since ...
```

#### Step 4: Access Web Interface

Open browser to:
```
http://YOUR_DROPLET_IP:5000
```

Example:
```
http://157.245.236.143:5000
```

---

### Method 2: Manual Installation

For advanced users or custom setups:

#### Step 1: System Updates

```bash
sudo apt update
sudo apt upgrade -y
```

#### Step 2: Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv
python3 --version  # Should be 3.10+
```

#### Step 3: Install Dependencies

```bash
sudo apt install -y build-essential python3-dev
```

#### Step 4: Create Application Directory

```bash
sudo mkdir -p /opt/gps-emulator
cd /opt/gps-emulator
```

#### Step 5: Upload Application Files

Transfer files from local machine:

```bash
# From your local machine
scp -r /path/to/app/* root@YOUR_DROPLET_IP:/opt/gps-emulator/
```

#### Step 6: Create Virtual Environment

```bash
cd /opt/gps-emulator
python3 -m venv venv
source venv/bin/activate
```

#### Step 7: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Production requirements.txt:**
```txt
Flask==3.0.0
Flask-SocketIO==5.3.5
gunicorn==21.2.0
gevent==24.2.1
gevent-websocket==0.10.1
Flask-CORS==4.0.0
requests==2.31.0
python-dotenv==1.0.0
pytz==2023.3
psutil==5.9.6
```

#### Step 8: Configure Environment

```bash
cp .env.example .env
nano .env
```

**Production configuration:**

```env
# ============================================================================
# UNIVERSAL GPS TRACKER EMULATOR - PRODUCTION CONFIGURATION
# ============================================================================

# ----------------------------------------------------------------------------
# TRACCAR SERVER CONFIGURATION
# ----------------------------------------------------------------------------
TRACCAR_SERVER=http://YOUR_TRACCAR_IP:8082
TRACCAR_USERNAME=admin
TRACCAR_PASSWORD=admin
TRACCAR_AUTO_CREATE_DEVICES=true

# ----------------------------------------------------------------------------
# FLASK CONFIGURATION (PRODUCTION)
# ----------------------------------------------------------------------------
FLASK_ENV=production
HOST=0.0.0.0
PORT=5000
SECRET_KEY=your-very-secure-random-secret-key-here
DEBUG=False

# ----------------------------------------------------------------------------
# LOGGING
# ----------------------------------------------------------------------------
LOG_LEVEL=INFO
LOG_FILE=/var/log/gps-emulator/app.log

# ----------------------------------------------------------------------------
# PERFORMANCE
# ----------------------------------------------------------------------------
WORKERS=4
THREADS=2
WORKER_CLASS=gevent
```

#### Step 9: Create Systemd Service

```bash
sudo nano /etc/systemd/system/gps-emulator.service
```

**Service file:**

```ini
[Unit]
Description=Universal GPS Tracker Emulator
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/gps-emulator
Environment="PATH=/opt/gps-emulator/venv/bin"
ExecStart=/opt/gps-emulator/venv/bin/gunicorn \
    --bind 0.0.0.0:5000 \
    --workers 4 \
    --worker-class gevent \
    --timeout 120 \
    --access-logfile /var/log/gps-emulator/access.log \
    --error-logfile /var/log/gps-emulator/error.log \
    app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### Step 10: Create Log Directory

```bash
sudo mkdir -p /var/log/gps-emulator
sudo chown root:root /var/log/gps-emulator
```

#### Step 11: Enable and Start Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable gps-emulator
sudo systemctl start gps-emulator
sudo systemctl status gps-emulator
```

#### Step 12: Configure Firewall

```bash
# Allow SSH (if not already allowed)
sudo ufw allow 22/tcp

# Allow web interface
sudo ufw allow 5000/tcp

# Allow GPS protocol ports (if needed)
sudo ufw allow 5001:5200/tcp
sudo ufw allow 5001:5200/udp

# Enable firewall
sudo ufw enable
sudo ufw status
```

---

## Service Management

### Start Service

```bash
sudo systemctl start gps-emulator
```

### Stop Service

```bash
sudo systemctl stop gps-emulator
```

### Restart Service

```bash
sudo systemctl restart gps-emulator
```

### Check Status

```bash
sudo systemctl status gps-emulator
```

### View Logs (Live)

```bash
sudo journalctl -u gps-emulator -f
```

### View Logs (Last 100 lines)

```bash
sudo journalctl -u gps-emulator -n 100
```

### Enable Auto-Start on Boot

```bash
sudo systemctl enable gps-emulator
```

### Disable Auto-Start

```bash
sudo systemctl disable gps-emulator
```

---

## Architecture

### Production Stack

```
┌─────────────────────────────────────────────────────────┐
│                    Internet Users                        │
│              (http://YOUR_IP:5000)                       │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/WebSocket
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  Gunicorn WSGI Server                    │
│   ┌──────────────────────────────────────────────┐     │
│   │  4 Gevent Workers (async I/O)                │     │
│   └──────────────────────────────────────────────┘     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Flask Application (app.py)                  │
│   ┌──────────────────────────────────────────────┐     │
│   │  REST API  │  WebSocket  │  Device Manager   │     │
│   └──────────────────────────────────────────────┘     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           86 GPS Protocol Implementations                │
│  (TK103, GT06, Teltonika, OsmAnd, etc.)                 │
└────────────────────┬────────────────────────────────────┘
                     │ TCP/UDP/HTTP
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Traccar Server / GPS Platform              │
└─────────────────────────────────────────────────────────┘
```

### Why Gunicorn + Gevent?

**Gunicorn:**
- Production-grade WSGI server
- Process management
- Automatic worker restart
- Load balancing

**Gevent:**
- Asynchronous I/O
- Handles 1000s of concurrent connections
- Perfect for GPS device simulation
- Low memory footprint

---

## Performance Tuning

### Adjust Workers

Edit `/etc/systemd/system/gps-emulator.service`:

```ini
ExecStart=/opt/gps-emulator/venv/bin/gunicorn \
    --bind 0.0.0.0:5000 \
    --workers 8 \              # Increase for more devices
    --worker-class gevent \
    --timeout 120 \
    app:app
```

**Rule of thumb:**
- Workers = (2 × CPU cores) + 1
- 1 core → 3 workers
- 2 cores → 5 workers
- 4 cores → 9 workers

### Increase Timeout

For slow connections or many devices:

```ini
--timeout 300 \
```

### Memory Limits

Monitor memory usage:

```bash
htop
# or
ps aux | grep gunicorn
```

---

## Monitoring

### Real-Time Logs

```bash
sudo journalctl -u gps-emulator -f
```

### Application Logs

```bash
tail -f /var/log/gps-emulator/app.log
tail -f /var/log/gps-emulator/access.log
tail -f /var/log/gps-emulator/error.log
```

### System Resources

```bash
# CPU and Memory
htop

# Disk usage
df -h

# Network connections
netstat -tulpn | grep :5000
```

### Check Running Devices

```bash
curl http://localhost:5000/api/multidevice/devices | jq
```

---

## Security

### Change Default Secret Key

Edit `.env`:

```env
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
```

### Restrict Access by IP

Configure UFW to allow only specific IPs:

```bash
# Remove public access
sudo ufw delete allow 5000/tcp

# Allow specific IP
sudo ufw allow from YOUR_TRACCAR_IP to any port 5000
```

### Use Reverse Proxy (Nginx)

**Install Nginx:**

```bash
sudo apt install nginx
```

**Configure:**

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

**Enable and restart:**

```bash
sudo ln -s /etc/nginx/sites-available/gps-emulator /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Enable SSL (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Updating the Application

### Method 1: Git Pull (if using Git)

```bash
cd /opt/gps-emulator
git pull origin main
sudo systemctl restart gps-emulator
```

### Method 2: Manual Upload

```bash
# From local machine
scp -r /path/to/updated/files/* root@YOUR_DROPLET_IP:/opt/gps-emulator/

# On server
sudo systemctl restart gps-emulator
```

---

## Backup

### Backup Configuration

```bash
sudo tar -czf gps-emulator-backup-$(date +%Y%m%d).tar.gz \
    /opt/gps-emulator/.env \
    /opt/gps-emulator/config_cloud.json \
    /opt/gps-emulator/vehicle_attributes.db
```

### Backup Entire Application

```bash
sudo tar -czf gps-emulator-full-backup-$(date +%Y%m%d).tar.gz \
    /opt/gps-emulator/
```

### Restore Backup

```bash
sudo tar -xzf gps-emulator-backup-20251116.tar.gz -C /
sudo systemctl restart gps-emulator
```

---

## Troubleshooting

### Service Won't Start

**Check logs:**
```bash
sudo journalctl -u gps-emulator -n 50
```

**Common issues:**
- Python dependencies missing
- Port 5000 already in use
- Permission errors

**Solution:**
```bash
sudo systemctl stop gps-emulator
lsof -ti:5000 | xargs kill -9
sudo systemctl start gps-emulator
```

---

### Out of Memory

**Check memory:**
```bash
free -h
```

**Reduce workers:**

Edit service file:
```ini
--workers 2 \
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart gps-emulator
```

---

### Can't Access Web Interface

**Check firewall:**
```bash
sudo ufw status
sudo ufw allow 5000/tcp
```

**Check service:**
```bash
sudo systemctl status gps-emulator
```

**Check port:**
```bash
netstat -tulpn | grep :5000
```

---

## Uninstallation

### Complete Removal

```bash
# Stop and disable service
sudo systemctl stop gps-emulator
sudo systemctl disable gps-emulator
sudo rm /etc/systemd/system/gps-emulator.service
sudo systemctl daemon-reload

# Remove application
sudo rm -rf /opt/gps-emulator

# Remove logs
sudo rm -rf /var/log/gps-emulator

# Remove firewall rules
sudo ufw delete allow 5000/tcp
```

---

## Differences from Windows Version

| Feature | DigitalOcean Production | Windows Local |
|---------|------------------------|---------------|
| **Platform** | Ubuntu 22.04/24.04 | Windows 10/11 |
| **Python** | 3.10+ | 3.13+ |
| **Async Mode** | Gevent | Threading |
| **Web Server** | Gunicorn | Flask dev server |
| **Service** | Systemd service | Manual start |
| **Host** | 0.0.0.0 | 127.0.0.1 |
| **Port** | 5000 | 5000 |
| **SSL** | Optional (Nginx) | No |
| **Auto-start** | Yes | No |
| **Use Case** | Production | Development/Testing |
| **Dependencies** | requirements.txt | requirements-windows.txt |

{% content-ref url="windows-local.md" %}
[windows-local.md](windows-local.md)
{% endcontent-ref %}

---

## Next Steps

1. **Create devices** - [Creating Devices Guide](../user-guide/creating-devices.md)
2. **Configure Traccar** - [Traccar Integration](../user-guide/traccar-integration.md)
3. **Use the API** - [REST API Reference](../api-reference/rest-api.md)
4. **Monitor performance** - [Performance Tuning](../advanced/performance-tuning.md)

---

## Need Help?

- [Troubleshooting Guide](../support/troubleshooting.md)
- [FAQ](../support/faq.md)
- [Common Issues](../support/common-issues.md)
- [Contact Support](../support/contact.md)

---

*DigitalOcean Production Deployment Guide - Updated: November 2025*
