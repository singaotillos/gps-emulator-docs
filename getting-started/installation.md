# Installation Guide - Universal GPS Tracker Emulator

Complete step-by-step installation guide for both deployment versions.

---

## Choose Your Installation

The GPS Emulator is available in **two versions** optimized for different use cases:

{% hint style="info" %}
**Not sure which version to choose?** See our detailed [Version Comparison Guide](version-comparison.md)
{% endhint %}

### 🖥️ Windows Local (Development)

{% hint style="info" %}
**Best for:** Local development, testing, debugging on Windows 10/11
{% endhint %}

- ✅ **Python 3.13** compatible
- ✅ **Localhost only** (127.0.0.1)
- ✅ **Quick setup** with batch scripts
- ✅ **Threading mode** (no gevent)
- 📦 **Use:** `requirements-windows.txt`

{% content-ref url="windows-local.md" %}
[windows-local.md](windows-local.md)
{% endcontent-ref %}

---

### 🌐 DigitalOcean Production (Server)

{% hint style="success" %}
**Best for:** Production deployment on Ubuntu servers (DigitalOcean, AWS, etc.)
{% endhint %}

- ✅ **Ubuntu 22.04/24.04** optimized
- ✅ **Public access** (0.0.0.0)
- ✅ **Systemd service** (auto-start)
- ✅ **Gunicorn + Gevent** (high performance)
- 📦 **Use:** `requirements.txt`

{% content-ref url="digitalocean-production.md" %}
[digitalocean-production.md](digitalocean-production.md)
{% endcontent-ref %}

---

{% content-ref url="version-comparison.md" %}
[version-comparison.md](version-comparison.md)
{% endcontent-ref %}

---

## Quick Comparison

| Feature | Windows Local | DigitalOcean Production |
|---------|--------------|------------------------|
| **Platform** | Windows 10/11 | Ubuntu 22.04/24.04 |
| **Python** | 3.10 - 3.13+ | 3.10 - 3.11 |
| **Setup** | `install.bat` | `install.sh` |
| **Start** | `start.bat` | `systemctl start` |
| **Async** | Threading | Gevent |
| **Server** | Flask dev | Gunicorn |
| **Access** | Localhost | Network/Internet |
| **Auto-start** | No | Yes (systemd) |
| **Use Case** | Development | Production |

---

## Table of Contents

- [Quick Installation](#quick-installation)
- [Detailed Installation](#detailed-installation)
  - [Windows](#windows-installation)
  - [Linux/Ubuntu](#linux-installation)
- [Post-Installation](#post-installation)
- [Troubleshooting](#troubleshooting)
- [Uninstallation](#uninstallation)

---

## Quick Installation

{% hint style="warning" %}
**Important:** Choose the correct requirements file for your platform:
- Windows: `requirements-windows.txt`
- Linux/Ubuntu: `requirements.txt`
{% endhint %}

### Windows Quick Start

```cmd
REM 1. Extract files
cd C:\path\to\universal-gps-emulator\local

REM 2. Run automated installer
install.bat

REM 3. Start application
start.bat

REM 4. Open browser
REM http://localhost:5000
```

### Linux/Ubuntu Quick Start

```bash
# 1. Extract files
cd /opt/universal-gps-emulator

# 2. Run automated installer
sudo chmod +x install.sh
sudo ./install.sh

# 3. Application auto-started via systemd
# http://YOUR_SERVER_IP:5000
```

Done! Continue to [Post-Installation](#post-installation) for configuration.

---

## Detailed Installation

### Windows Installation

#### Prerequisites

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - During installation, **check "Add Python to PATH"**
   - Verify installation:
     ```cmd
     python --version
     ```

2. **Extract the Archive**
   - Right-click `universal-gps-emulator.zip`
   - Select "Extract All..."
   - Choose destination folder

#### Installation Steps

1. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - Navigate to extracted folder:
     ```cmd
     cd C:\Users\YourName\Downloads\universal-gps-emulator
     ```

2. **Install Dependencies**

   {% hint style="danger" %}
   **CRITICAL**: Windows users must use `requirements-windows.txt` (NOT `requirements.txt`)!
   {% endhint %}

   ```cmd
   pip install -r requirements-windows.txt
   ```

   If you get an error, try:
   ```cmd
   python -m pip install --upgrade pip
   python -m pip install -r requirements-windows.txt
   ```

3. **Configure Application (Optional)**
   ```cmd
   copy .env.example .env
   notepad .env
   ```
   Edit configuration as needed (see [Configuration Guide](../user-guide/configuration.md))

4. **Start Application**
   ```cmd
   python app.py
   ```

5. **Access Web Interface**
   - Open browser
   - Go to: http://localhost:5000
   - You should see the dashboard!

---

### Linux Installation

#### Prerequisites

1. **Python 3.8+**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip python3-venv

   # CentOS/RHEL
   sudo yum install python3 python3-pip

   # Arch Linux
   sudo pacman -S python python-pip
   ```

2. **Extract Archive**
   ```bash
   unzip universal-gps-emulator.zip
   cd universal-gps-emulator
   ```

#### Installation Steps

1. **Create Virtual Environment (Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Application**
   ```bash
   cp .env.example .env
   nano .env  # or vim, gedit, etc.
   ```

4. **Start Application**
   ```bash
   python app.py
   ```

5. **Access Web Interface**
   Open browser: http://localhost:5000

#### Run as System Service (Optional)

Create `/etc/systemd/system/gps-emulator.service`:

```ini
[Unit]
Description=GPS Tracker Emulator
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/universal-gps-emulator
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable gps-emulator
sudo systemctl start gps-emulator
sudo systemctl status gps-emulator
```

---

## Post-Installation

### 1. Verify Installation

Access http://localhost:5000

You should see the dashboard with:
- List of 86 protocols
- "Create Device" button
- Clean interface

### 2. Create Test Device

1. Click "Create Device"
2. Select protocol: **TK103**
3. Enter model: **TK103-2B**
4. Device ID: Leave auto-generated
5. Route: **Paris**
6. Click "Create"

### 3. Start Simulation

1. Find your device in the list
2. Click "Start" button
3. Status should change to "Running"
4. Device is now sending GPS data!

### 4. Test with Traccar (Optional)

If you have Traccar installed:

1. Create device in Traccar:
   - Protocol: **tk103**
   - Unique ID: Copy from emulator
   - Port: **5002**

2. Start emulator device
3. Check Traccar - positions should appear!

---

## Troubleshooting

### "Python not found"

**Windows:**
- Reinstall Python
- Check "Add to PATH" during installation

**Linux/Mac:**
```bash
sudo apt install python3  # Ubuntu
brew install python@3.10  # macOS
```

### "Permission denied"

**Linux/Mac:**
```bash
chmod +x app.py
sudo chown -R $USER:$USER .
```

### "Port 5000 already in use"

Change port in `.env`:
```
WEB_PORT=5001
```

Or kill process using port:
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "Module not found"

Reinstall dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### "Database locked"

Stop all instances:
```bash
# Linux/Mac
pkill -f app.py

# Windows
taskkill /IM python.exe /F
```

Delete lock file:
```bash
rm /tmp/osmand_gps_emulator.lock
```

### Dependencies Installation Fails

Try with `--user` flag:
```bash
pip install --user -r requirements.txt
```

Or create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## Uninstallation

### Windows

1. Stop application (Ctrl+C in command prompt)
2. Delete installation folder
3. Delete virtual environment (if created)

### Linux/Mac

```bash
# Stop service (if installed)
sudo systemctl stop gps-emulator
sudo systemctl disable gps-emulator
sudo rm /etc/systemd/system/gps-emulator.service

# Remove files
cd ..
rm -rf universal-gps-emulator

# Remove virtual environment
rm -rf venv
```

### Docker

```bash
docker stop gps-emulator
docker rm gps-emulator
docker rmi gps-emulator
```

---

## Next Steps

1. Read [Configuration Guide](../user-guide/configuration.md) for customization
2. Check [REST API Reference](../api-reference/rest-api.md) for API usage
3. See [Protocols Overview](../protocols/overview.md) for protocol list
4. Review [FAQ](../support/faq.md) for common questions

---

## Need Help?

- Check [Troubleshooting Guide](../support/troubleshooting.md)
- Read [FAQ](../support/faq.md)
- Email: support@your-domain.com
- Response time: 24-48 hours

---

*Installation guide updated: October 2025*
