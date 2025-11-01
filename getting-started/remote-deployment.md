# Remote Server Deployment

Complete guide for deploying Universal GPS Tracker Emulator on a remote server (VPS, Cloud, Dedicated Server).

---

## Overview

The GPS Emulator can be deployed on remote servers for:
- **Production use** - 24/7 availability
- **Team access** - Multiple users accessing the same instance
- **Client demonstrations** - Professional hosting
- **Integration testing** - Continuous testing environments

{% hint style="info" %}
**Local vs Remote**: The application works identically in both modes. Only the network configuration changes.
{% endhint %}

---

## Prerequisites

### Server Requirements

**Minimum Specifications:**
- **OS**: Ubuntu 20.04+ / Debian 11+ / CentOS 8+
- **RAM**: 2GB minimum, 4GB recommended
- **CPU**: 2 cores minimum
- **Storage**: 10GB minimum
- **Network**: Public IP address
- **Ports**: 5000 (web), 5001-5090 (GPS protocols)

**Software Requirements:**
- Python 3.8 or higher
- pip (Python package manager)
- systemd (for service management)
- Optional: Nginx/Apache (reverse proxy)
- Optional: SSL certificate (Let's Encrypt)

---

## Installation Methods

{% tabs %}
{% tab title="Method 1: Standard Installation" %}

### Step 1: Connect to Server

```bash
ssh username@your-server-ip
```

### Step 2: Update System

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 3: Install Python & Dependencies

```bash
sudo apt install -y python3 python3-pip python3-venv git
```

### Step 4: Create Application Directory

```bash
sudo mkdir -p /opt/gps-emulator
sudo chown $USER:$USER /opt/gps-emulator
cd /opt/gps-emulator
```

### Step 5: Upload Application

**Option A: Via SCP (from local machine):**
```bash
scp Universal-GPS-Tracker-Emulator-v2.0.0.zip username@your-server-ip:/opt/gps-emulator/
```

**Option B: Via wget (if downloadable):**
```bash
wget https://your-download-link/Universal-GPS-Tracker-Emulator-v2.0.0.zip
```

**Option C: Via Git (if repository):**
```bash
git clone https://your-repo-url.git .
```

### Step 6: Extract & Install

```bash
unzip Universal-GPS-Tracker-Emulator-v2.0.0.zip
cd Universal-GPS-Tracker-Emulator-v2.0.0
pip3 install -r requirements.txt
```

### Step 7: Configure for Remote Access

Create `.env` file:
```bash
cp .env.example .env
nano .env
```

**Essential settings for remote:**
```bash
# Web Interface - IMPORTANT for remote access
WEB_HOST=0.0.0.0        # Listen on all network interfaces
WEB_PORT=5000           # Web interface port
WEB_DEBUG=false         # NEVER enable debug in production

# Traccar Configuration (if using remote Traccar)
TRACCAR_HOST=localhost  # or traccar.yourserver.com
TRACCAR_PORT=8082
TRACCAR_USERNAME=your_username
TRACCAR_PASSWORD=your_secure_password
TRACCAR_AUTO_CREATE_DEVICES=true
```

{% hint style="warning" %}
**Security**: Never set `WEB_DEBUG=true` in production. This exposes sensitive information.
{% endhint %}

### Step 8: Test Application

```bash
python3 app.py
```

Access from browser: `http://your-server-ip:5000`

If accessible, press `Ctrl+C` to stop and continue to service setup.

{% endtab %}

{% tab title="Method 2: Docker Installation" %}

### Step 1: Install Docker

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Step 2: Prepare Application

```bash
mkdir -p /opt/gps-emulator
cd /opt/gps-emulator

# Upload or extract application files
unzip Universal-GPS-Tracker-Emulator-v2.0.0.zip
cd Universal-GPS-Tracker-Emulator-v2.0.0
```

### Step 3: Configure Environment

```bash
cp .env.example .env
nano .env
```

```bash
WEB_HOST=0.0.0.0
WEB_PORT=5000
TRACCAR_HOST=traccar    # Docker service name
TRACCAR_PORT=8082
```

### Step 4: Start with Docker Compose

```bash
docker-compose up -d
```

### Step 5: Verify

```bash
docker-compose ps
docker-compose logs -f
```

Access: `http://your-server-ip:5000`

{% endtab %}
{% endtabs %}

---

## Firewall Configuration

### UFW (Ubuntu/Debian)

```bash
# Allow SSH (IMPORTANT - don't lock yourself out!)
sudo ufw allow 22/tcp

# Allow web interface
sudo ufw allow 5000/tcp

# Allow GPS protocol ports (adjust as needed)
sudo ufw allow 5001:5090/tcp

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status
```

### firewalld (CentOS/RHEL)

```bash
# Allow web interface
sudo firewall-cmd --permanent --add-port=5000/tcp

# Allow GPS protocol ports
sudo firewall-cmd --permanent --add-port=5001-5090/tcp

# Reload firewall
sudo firewall-cmd --reload

# Check status
sudo firewall-cmd --list-all
```

### Cloud Provider Firewall

Don't forget to configure your cloud provider's security group/firewall:

**AWS Security Group:**
- Inbound: TCP 5000 (Web UI)
- Inbound: TCP 5001-5090 (GPS protocols)
- Inbound: TCP 22 (SSH - restrict to your IP)

**Google Cloud Firewall Rules:**
```bash
gcloud compute firewall-rules create gps-emulator-web \
  --allow tcp:5000 \
  --source-ranges 0.0.0.0/0

gcloud compute firewall-rules create gps-emulator-protocols \
  --allow tcp:5001-5090 \
  --source-ranges 0.0.0.0/0
```

**Azure Network Security Group:**
- Add inbound rule for port 5000
- Add inbound rule for port range 5001-5090

---

## Systemd Service (Auto-Start)

Create systemd service for automatic start on boot and restart on crash.

### Step 1: Create Service File

```bash
sudo nano /etc/systemd/system/gps-emulator.service
```

### Step 2: Service Configuration

```ini
[Unit]
Description=Universal GPS Tracker Emulator
After=network.target

[Service]
Type=simple
User=gpsuser
WorkingDirectory=/opt/gps-emulator/Universal-GPS-Tracker-Emulator-v2.0.0
ExecStart=/usr/bin/python3 /opt/gps-emulator/Universal-GPS-Tracker-Emulator-v2.0.0/app.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

# Environment
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
```

{% hint style="info" %}
Replace `gpsuser` with your actual username, or create a dedicated user for security.
{% endhint %}

### Step 3: Create Dedicated User (Optional but Recommended)

```bash
sudo useradd -r -s /bin/false gpsuser
sudo chown -R gpsuser:gpsuser /opt/gps-emulator
```

### Step 4: Enable & Start Service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start on boot
sudo systemctl enable gps-emulator

# Start service
sudo systemctl start gps-emulator

# Check status
sudo systemctl status gps-emulator
```

### Step 5: Manage Service

```bash
# View logs
sudo journalctl -u gps-emulator -f

# Restart service
sudo systemctl restart gps-emulator

# Stop service
sudo systemctl stop gps-emulator

# Disable auto-start
sudo systemctl disable gps-emulator
```

---

## Reverse Proxy Setup (Nginx)

Use Nginx as reverse proxy for:
- SSL/HTTPS support
- Domain name mapping
- Load balancing
- Better security

### Step 1: Install Nginx

```bash
sudo apt install -y nginx
```

### Step 2: Create Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/gps-emulator
```

**Basic Configuration (HTTP only):**

```nginx
server {
    listen 80;
    server_name gps.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket support (if needed)
    location /socket.io/ {
        proxy_pass http://127.0.0.1:5000/socket.io/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # Increase timeouts for long-running operations
    proxy_connect_timeout 600;
    proxy_send_timeout 600;
    proxy_read_timeout 600;
}
```

### Step 3: Enable Site

```bash
# Create symbolic link
sudo ln -s /etc/nginx/sites-available/gps-emulator /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# Reload Nginx
sudo systemctl reload nginx
```

### Step 4: Update .env for Localhost

Since Nginx proxies to the app, bind to localhost only:

```bash
# .env
WEB_HOST=127.0.0.1    # Only Nginx can access
WEB_PORT=5000
```

### Step 5: Access Application

- Direct: `http://your-server-ip:5000`
- Via Nginx: `http://gps.yourdomain.com`

---

## SSL/HTTPS Setup (Let's Encrypt)

### Step 1: Install Certbot

```bash
sudo apt install -y certbot python3-certbot-nginx
```

### Step 2: Obtain SSL Certificate

```bash
sudo certbot --nginx -d gps.yourdomain.com
```

Follow prompts:
- Enter email address
- Agree to terms
- Choose redirect HTTP to HTTPS (recommended)

### Step 3: Auto-Renewal

Certbot automatically sets up renewal. Verify:

```bash
sudo certbot renew --dry-run
```

### Step 4: Updated Nginx Config

Certbot automatically updates your config. Verify HTTPS works:

```bash
https://gps.yourdomain.com
```

**Final Nginx Configuration (with SSL):**

```nginx
server {
    listen 80;
    server_name gps.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name gps.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/gps.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gps.yourdomain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /socket.io/ {
        proxy_pass http://127.0.0.1:5000/socket.io/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## Apache Reverse Proxy (Alternative)

If you prefer Apache over Nginx:

### Step 1: Install Apache

```bash
sudo apt install -y apache2
```

### Step 2: Enable Required Modules

```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_wstunnel
sudo a2enmod ssl
sudo a2enmod headers
sudo systemctl restart apache2
```

### Step 3: Create Virtual Host

```bash
sudo nano /etc/apache2/sites-available/gps-emulator.conf
```

```apache
<VirtualHost *:80>
    ServerName gps.yourdomain.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

    # WebSocket support
    ProxyPass /socket.io/ ws://127.0.0.1:5000/socket.io/
    ProxyPassReverse /socket.io/ ws://127.0.0.1:5000/socket.io/

    # Timeouts
    ProxyTimeout 600

    ErrorLog ${APACHE_LOG_DIR}/gps-emulator-error.log
    CustomLog ${APACHE_LOG_DIR}/gps-emulator-access.log combined
</VirtualHost>
```

### Step 4: Enable Site

```bash
sudo a2ensite gps-emulator
sudo systemctl reload apache2
```

### Step 5: SSL with Certbot

```bash
sudo certbot --apache -d gps.yourdomain.com
```

---

## Security Best Practices

### 1. Change Default Ports

```bash
# .env
WEB_PORT=8443  # Use non-standard port
```

### 2. Enable Authentication

If the app supports it, enable API authentication:

```bash
# .env
API_ENABLE_AUTHENTICATION=true
API_KEY=your-super-secret-key-here
```

### 3. Restrict SSH Access

```bash
# Only allow SSH from specific IP
sudo ufw allow from YOUR_IP_ADDRESS to any port 22
sudo ufw deny 22
```

### 4. Regular Updates

```bash
# System updates
sudo apt update && sudo apt upgrade -y

# Python dependencies
pip3 install --upgrade -r requirements.txt
```

### 5. Monitor Logs

```bash
# Application logs
sudo journalctl -u gps-emulator -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# System logs
sudo tail -f /var/log/syslog
```

### 6. Backup Configuration

```bash
# Backup script
#!/bin/bash
BACKUP_DIR="/backup/gps-emulator"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/gps-emulator-$DATE.tar.gz \
  /opt/gps-emulator/.env \
  /opt/gps-emulator/config.yaml \
  /opt/gps-emulator/config/

# Keep only last 7 backups
find $BACKUP_DIR -name "gps-emulator-*.tar.gz" -mtime +7 -delete
```

### 7. Rate Limiting (Nginx)

Add to Nginx config to prevent abuse:

```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

server {
    # ... other config

    location /api/ {
        limit_req zone=api burst=20;
        proxy_pass http://127.0.0.1:5000;
    }
}
```

---

## Monitoring & Maintenance

### Resource Monitoring

```bash
# CPU & Memory usage
htop

# Disk usage
df -h

# Application process
ps aux | grep python

# Port usage
sudo netstat -tlnp | grep python
```

### Health Check Script

Create `/opt/gps-emulator/healthcheck.sh`:

```bash
#!/bin/bash
URL="http://localhost:5000"

if curl -f -s -o /dev/null "$URL"; then
    echo "$(date): GPS Emulator is running"
    exit 0
else
    echo "$(date): GPS Emulator is DOWN - Restarting..."
    sudo systemctl restart gps-emulator
    exit 1
fi
```

Add to crontab:
```bash
# Check every 5 minutes
*/5 * * * * /opt/gps-emulator/healthcheck.sh >> /var/log/gps-healthcheck.log 2>&1
```

---

## Troubleshooting

### Application Won't Start

```bash
# Check service status
sudo systemctl status gps-emulator

# View detailed logs
sudo journalctl -u gps-emulator -n 100 --no-pager

# Check if port is already in use
sudo netstat -tlnp | grep 5000

# Test manually
cd /opt/gps-emulator/Universal-GPS-Tracker-Emulator-v2.0.0
python3 app.py
```

### Can't Access Remotely

```bash
# Check if application is listening on all interfaces
sudo netstat -tlnp | grep 5000
# Should show 0.0.0.0:5000, not 127.0.0.1:5000

# Verify .env configuration
cat .env | grep WEB_HOST
# Should be: WEB_HOST=0.0.0.0

# Check firewall
sudo ufw status
curl http://localhost:5000  # From server
curl http://your-server-ip:5000  # From local machine
```

### SSL Certificate Issues

```bash
# Renew certificate manually
sudo certbot renew

# Check certificate expiration
sudo certbot certificates

# Test SSL configuration
openssl s_client -connect gps.yourdomain.com:443
```

### High Memory Usage

```bash
# Check memory usage
free -h

# Restart application
sudo systemctl restart gps-emulator

# Limit memory in systemd service
sudo nano /etc/systemd/system/gps-emulator.service
```

Add under `[Service]`:
```ini
MemoryLimit=2G
```

---

## Cloud Provider Examples

### AWS EC2

1. Launch EC2 instance (Ubuntu 22.04, t3.medium)
2. Configure Security Group (ports 22, 5000, 5001-5090)
3. Allocate Elastic IP
4. Follow standard installation steps
5. Use Route 53 for DNS

### Google Cloud Platform

```bash
# Create VM instance
gcloud compute instances create gps-emulator \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --machine-type=e2-medium \
  --tags=gps-emulator

# Configure firewall (see Firewall section above)
```

### DigitalOcean

1. Create Droplet (Ubuntu 22.04, Basic plan $12/month)
2. Add domain to DNS
3. Follow standard installation
4. Use DigitalOcean firewall rules

### Azure

```bash
# Create VM
az vm create \
  --resource-group gps-emulator-rg \
  --name gps-emulator-vm \
  --image Ubuntu2204 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys
```

---

## Performance Optimization

### 1. Use Production WSGI Server

Install Gunicorn:
```bash
pip3 install gunicorn
```

Update systemd service:
```ini
ExecStart=/usr/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

### 2. Enable Nginx Caching

```nginx
# Add to http block
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=gps_cache:10m max_size=1g inactive=60m;

# Add to location block
proxy_cache gps_cache;
proxy_cache_valid 200 5m;
```

### 3. Optimize Database

If using SQLite, move to PostgreSQL for better concurrent access.

---

## Next Steps

- [Configuration Guide](../user-guide/configuration.md) - Detailed configuration options
- [Traccar Integration](../user-guide/traccar-integration.md) - Connect to Traccar server
- [Managing Devices](../user-guide/managing-devices.md) - Add and manage GPS devices
- [Troubleshooting](../support/troubleshooting.md) - Common issues and solutions

{% hint style="success" %}
**Ready for Production!** Your GPS Emulator is now accessible remotely with professional-grade security and reliability.
{% endhint %}
