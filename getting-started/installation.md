# Installation Guide - Universal GPS Tracker Emulator

Complete step-by-step installation guide for all platforms.

---

## Table of Contents

- [Quick Installation](#quick-installation)
- [Detailed Installation](#detailed-installation)
  - [Windows](#windows-installation)
  - [Linux/Ubuntu](#linux-installation)
  - [macOS](#macos-installation)
  - [Docker](#docker-installation)
- [Post-Installation](#post-installation)
- [Troubleshooting](#troubleshooting)
- [Uninstallation](#uninstallation)

---

## Quick Installation

For experienced users:

{% tabs %}
{% tab title="Windows" %}
```cmd
# 1. Extract files (Right-click > Extract All)
# Or using PowerShell:
Expand-Archive -Path Universal-GPS-Tracker-Emulator-v2.0.0.zip -DestinationPath .

# 2. Navigate to folder
cd Universal-GPS-Tracker-Emulator-v2.0.0

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Start application
python app.py

# 5. Open browser: http://localhost:5000
```
{% endtab %}

{% tab title="Linux/macOS" %}
```bash
# 1. Extract files
unzip Universal-GPS-Tracker-Emulator-v2.0.0.zip
cd Universal-GPS-Tracker-Emulator-v2.0.0

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start application
python app.py

# 4. Open browser: http://localhost:5000
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Installation takes less than 5 minutes!** Python 3.8+ is the only requirement.
{% endhint %}

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
   ```cmd
   pip install -r requirements.txt
   ```

   If you get an error, try:
   ```cmd
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. **Configure Application (Optional)**

   The `.env` file is **optional** for basic usage. You can start the application without it.

   ```cmd
   copy .env.example .env
   notepad .env
   ```

   **What to configure in .env:**
   - Web server port (default: 5000)
   - API settings
   - Logging preferences

   {% hint style="info" %}
   **Note**: Traccar integration is **NOT** configured in .env file. Configure Traccar later via the web interface (Traccar button).
   {% endhint %}

4. **Start Application**
   ```cmd
   python app.py
   ```

5. **Access Web Interface**
   - Open browser
   - Go to: http://localhost:5000
   - You should see the dashboard!

{% hint style="info" %}
**First Launch** - The dashboard should appear like this:
{% endhint %}

![Dashboard First View](/.gitbook/assets/screenshots/screen1.jpg)

#### Create Desktop Shortcut (Optional)

Create file `start-emulator.bat`:
```batch
@echo off
cd C:\path\to\universal-gps-emulator
python app.py
pause
```

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

### macOS Installation

#### Prerequisites

1. **Install Homebrew** (if not installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python@3.10
   ```

3. **Extract Archive**
   ```bash
   unzip universal-gps-emulator.zip
   cd universal-gps-emulator
   ```

#### Installation Steps

1. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure (Optional)**

   The `.env` file is optional for basic usage.

   ```bash
   cp .env.example .env
   nano .env
   ```

   {% hint style="info" %}
   **Note**: Traccar is configured via the web interface, not in .env
   {% endhint %}

4. **Start Application**
   ```bash
   python app.py
   ```

5. **Access**
   http://localhost:5000

---

### Docker Installation

#### Quick Start

```bash
# Build image
docker build -t gps-emulator .

# Run container
docker run -d -p 5000:5000 --name gps-emulator gps-emulator

# Access
# http://localhost:5000
```

#### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  gps-emulator:
    build: .
    ports:
      - "5000:5000"
    environment:
      - WEB_HOST=0.0.0.0
      - WEB_PORT=5000
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped
```

Run:
```bash
docker-compose up -d
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

### 4. Configure Traccar Integration (Optional)

If you want to use Traccar for GPS tracking:

**Step 1: Ensure Traccar is Running**
- Open http://localhost:8082
- You should see Traccar login page

**Step 2: Configure in Emulator**
1. In the GPS Emulator web interface (http://localhost:5000)
2. Click the **🔧 Traccar** button (top right corner)
3. Enter your Traccar credentials:
   - **Server**: `localhost:8082`
   - **Username**: Your Traccar username (e.g., `admin`)
   - **Password**: Your Traccar password
4. Enable **Auto Sync** ✓
5. Click **Save**

**Step 3: Test**
1. Create a device in the emulator
2. Start the device
3. Open Traccar - the device should appear automatically!

{% hint style="success" %}
**Auto-sync enabled**: Devices created in the emulator are automatically added to Traccar!
{% endhint %}

See [Traccar Integration Guide](../user-guide/traccar-integration.md) for detailed setup.

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

1. Read [CONFIGURATION.md](CONFIGURATION.md) for customization
2. Check [API_REFERENCE.md](API_REFERENCE.md) for API usage
3. See [PROTOCOLS.md](PROTOCOLS.md) for protocol list
4. Review [FAQ.md](FAQ.md) for common questions

---

## Need Help?

- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Read [FAQ.md](FAQ.md)
- Email: support@your-domain.com
- Response time: 24-48 hours

---

*Installation guide updated: October 2025*
