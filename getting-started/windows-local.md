# Windows Local Installation - Python 3.13 Compatible

Complete installation guide for running the GPS Emulator locally on Windows with Python 3.13.

---

## Overview

This guide covers the **Windows Local Development Version** of the Universal GPS Tracker Emulator, specifically optimized for:

- ✅ **Python 3.13.2** compatibility
- ✅ **Windows 10/11** operating systems
- ✅ **Localhost development** (127.0.0.1)
- ✅ **Threading mode** (no gevent dependency)
- ✅ **Quick setup** with automated batch scripts

{% hint style="info" %}
**Production Deployment?** For Linux server deployment (DigitalOcean, AWS, etc.), see [DigitalOcean Production Guide](digitalocean-production.md)
{% endhint %}

---

## Prerequisites

### 1. Python 3.10+ Required

{% hint style="warning" %}
**Important**: Python 3.13 is fully supported. The Windows version uses threading mode instead of gevent.
{% endhint %}

**Download Python:**
1. Visit: https://www.python.org/downloads/
2. Download Python 3.10 or higher (Python 3.13.2 recommended)
3. **During installation:**
   - ✅ **Check "Add Python to PATH"** (CRITICAL!)
   - ✅ Check "Install pip"
   - ✅ Click "Install Now"

**Verify Installation:**
```cmd
python --version
```

Expected output: `Python 3.13.2` (or your installed version)

---

## Installation Methods

### Method 1: Automated Installation (Recommended)

The easiest way to install on Windows:

#### Step 1: Extract Files

1. Locate the downloaded ZIP file
2. Right-click → "Extract All..."
3. Choose destination (e.g., `C:\universal-gps-emulator_digitalocean\local\`)

#### Step 2: Run Installation Script

1. Navigate to the extracted folder
2. **Double-click**: `install.bat`
3. Wait for installation to complete (2-3 minutes)

**What the script does:**
- ✅ Checks Python installation
- ✅ Creates virtual environment
- ✅ Installs Windows-compatible dependencies
- ✅ Configures `.env` file for localhost
- ✅ Creates necessary folders

**Expected output:**
```
================================================================
   Universal GPS Tracker Emulator - Windows Installation
   COMMERCIAL UNLIMITED VERSION
================================================================

   UNLIMITED Devices
   86 GPS Protocols
   Production Ready

================================================================

[1/6] Checking Python...
Python 3.13.2 detected

[2/6] Checking pip...
pip is available

[3/6] Creating Python virtual environment...
Virtual environment created

[4/6] Installing Python dependencies...
    (This may take 2-3 minutes, please wait...)
Dependencies installed

[5/6] Configuring application...
.env file created
Configuration adapted for Windows localhost

[6/6] Creating folders...
Folders created

================================================================
   INSTALLATION COMPLETED!
================================================================

URL: http://localhost:5000
Version: Commercial Unlimited (UNLIMITED devices)
Routes: Laayoune, Dakhla, Smara, Guergarat
Protocols: 86 GPS protocols supported

To start the application:
   1. Double-click: start.bat
   OR
   2. Run: python app.py
```

#### Step 3: Start Application

**Double-click**: `start.bat`

Or manually:
```cmd
venv\Scripts\activate.bat
python app.py
```

#### Step 4: Access Web Interface

The script will automatically open your browser to:
```
http://localhost:5000
```

Or manually open: `open-browser.bat`

---

### Method 2: Manual Installation

For advanced users who prefer manual setup:

#### Step 1: Extract and Navigate

```cmd
cd C:\path\to\universal-gps-emulator\local
```

#### Step 2: Create Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### Step 3: Install Dependencies

```cmd
python -m pip install --upgrade pip
pip install -r requirements-windows.txt
```

{% hint style="warning" %}
**IMPORTANT**: Use `requirements-windows.txt` (NOT `requirements.txt`)

The Windows version excludes gevent which is incompatible with Python 3.13.
{% endhint %}

#### Step 4: Configure Environment

```cmd
copy .env.example .env
notepad .env
```

**Required settings for Windows:**
```env
# Flask Configuration (Windows Localhost)
FLASK_ENV=development
HOST=127.0.0.1
PORT=5000
WERKZEUG_RUN_MAIN=false

# Traccar Configuration
TRACCAR_SERVER=http://localhost:8082
TRACCAR_AUTO_CREATE_DEVICES=true
```

{% hint style="danger" %}
**Critical**: `WERKZEUG_RUN_MAIN=false` must be set to avoid WERKZEUG_SERVER_FD errors on Windows.
{% endhint %}

#### Step 5: Create Folders

```cmd
mkdir templates
mkdir static
mkdir .route_cache
```

#### Step 6: Start Application

```cmd
python app.py
```

---

## Python 3.13 Compatibility

### Why a Special Windows Version?

The original server version uses **gevent**, which has compatibility issues with Python 3.13:

```
❌ ERROR: Failed to build gevent
   undeclared name not builtin: long
```

**Solution**: The Windows version uses **Flask-SocketIO in threading mode**, which:
- ✅ Works perfectly with Python 3.13
- ✅ No external async library needed
- ✅ Sufficient performance for development/testing
- ✅ Fully compatible with all 86 GPS protocols

### Dependencies Comparison

**Server Version (requirements.txt):**
```txt
Flask==3.0.0
Flask-SocketIO==5.3.5
gunicorn==21.2.0
gevent==24.2.1  ❌ Not compatible with Python 3.13
```

**Windows Version (requirements-windows.txt):**
```txt
Flask==3.0.0
Flask-SocketIO==5.3.5
Flask-CORS==4.0.0
python-socketio==5.10.0
eventlet==0.33.3  ✅ Installed but threading mode used
requests==2.31.0
python-dotenv==1.0.0
pytz==2023.3
psutil==5.9.6
```

---

## File Structure

After installation, your directory structure:

```
C:\universal-gps-emulator_digitalocean\local\
├── app.py                          # Main application
├── install.bat                     # Installation script
├── start.bat                       # Start script
├── open-browser.bat                # Browser launcher
├── .env                            # Configuration (localhost)
├── requirements-windows.txt        # Windows dependencies
├── README.txt                      # Quick start guide
├── PROJECT-STRUCTURE.txt           # File documentation
├── config_cloud.json               # GPS routes
├── venv\                           # Python virtual environment
├── protocols\                      # 86 GPS protocol implementations
│   ├── tk103\
│   ├── gt06\
│   ├── teltonika\
│   └── ... (83 more)
├── templates\                      # Web interface
├── static\                         # CSS, JS, images
└── .route_cache\                   # Route cache
```

---

## Starting the Application

### Option 1: Batch Script (Easiest)

Double-click: **start.bat**

The script will:
1. Activate virtual environment
2. Start Flask application
3. Display URL: http://localhost:5000

### Option 2: Command Line

```cmd
cd C:\path\to\local
venv\Scripts\activate.bat
python app.py
```

### Option 3: Open Browser Automatically

Double-click: **open-browser.bat**

Or run:
```cmd
start http://localhost:5000
```

---

## Verification

### 1. Check Application Startup

Expected console output:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

### 2. Access Dashboard

Open browser to: http://localhost:5000

You should see:
- ✅ Dashboard with 86 protocols listed
- ✅ "Create Device" button
- ✅ Empty device list (initially)
- ✅ No error messages

### 3. Create Test Device

**Via Web Interface:**
1. Click "Create Device"
2. Select protocol: **TK103**
3. Model: **TK103-2B**
4. Route: **Paris**
5. Click "Add Device"
6. Device appears in list
7. Click "Start" → Status changes to "Running"

**Via API:**
```powershell
$body = @{
    protocol = "tk103"
    device_model = "TK103-2B"
    route = "paris"
    speed = 50.0
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/multidevice/devices" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

---

## Troubleshooting

### Error: "Python is not installed"

**Solution:**
1. Download Python from https://www.python.org/downloads/
2. **Check "Add Python to PATH"** during installation
3. Restart Command Prompt
4. Verify: `python --version`

---

### Error: "Failed to build gevent"

**Cause**: Using wrong requirements file

**Solution:**
```cmd
pip install -r requirements-windows.txt
```

NOT `requirements.txt` (that's for Linux servers)

---

### Error: "KeyError: 'WERKZEUG_SERVER_FD'"

**Cause**: Missing environment variable

**Solution:**

Edit `.env` and add:
```env
WERKZEUG_RUN_MAIN=false
```

Or run:
```cmd
powershell -Command "(Get-Content .env) -replace 'WERKZEUG_RUN_MAIN=true', 'WERKZEUG_RUN_MAIN=false' | Set-Content .env"
```

---

### Error: "Port 5000 already in use"

**Check what's using the port:**
```cmd
netstat -ano | findstr :5000
```

**Kill the process:**
```cmd
taskkill /PID <PID> /F
```

**Or change port in `.env`:**
```env
PORT=5001
```

---

### Error: "Module not found"

**Solution:**
```cmd
venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements-windows.txt --force-reinstall
```

---

### Error: "Virtual environment not found"

**Solution:**
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements-windows.txt
```

---

## Configuration

### Environment Variables (.env)

Key Windows-specific settings:

```env
# Flask Configuration
FLASK_ENV=development           # Development mode
HOST=127.0.0.1                  # Localhost only
PORT=5000                       # Web interface port
WERKZEUG_RUN_MAIN=false        # Required for Windows!

# Traccar Integration
TRACCAR_SERVER=http://localhost:8082
TRACCAR_AUTO_CREATE_DEVICES=true

# Logging
LOG_LEVEL=INFO
```

### Allowing Network Access

By default, the application only accepts connections from localhost (`127.0.0.1`).

**To allow network access:**

1. Edit `.env`:
   ```env
   HOST=0.0.0.0
   ```

2. Configure Windows Firewall:
   - Open: Control Panel → Windows Defender Firewall
   - Click: Advanced Settings
   - Inbound Rules → New Rule
   - Rule Type: Port
   - Protocol: TCP
   - Port: 5000
   - Action: Allow the connection
   - Profile: Select appropriate (Domain/Private/Public)
   - Name: GPS Emulator

---

## Stopping the Application

### Method 1: Keyboard

Press **Ctrl+C** in the Command Prompt window

### Method 2: Kill Process

```cmd
taskkill /IM python.exe /F
```

---

## Uninstallation

### Complete Removal

1. **Stop application** (Ctrl+C)
2. **Delete folder**:
   ```cmd
   cd ..
   rmdir /s /q local
   ```

### Keep Configuration

Delete only virtual environment:
```cmd
rmdir /s /q venv
```

---

## Differences from Production Version

| Feature | Windows Local | DigitalOcean Production |
|---------|---------------|------------------------|
| **Platform** | Windows 10/11 | Ubuntu 22.04/24.04 |
| **Python** | 3.13+ | 3.10+ |
| **Async Mode** | Threading | Gevent |
| **Web Server** | Flask dev server | Gunicorn |
| **Service** | Manual start | Systemd service |
| **Host** | 127.0.0.1 | 0.0.0.0 |
| **Port** | 5000 | 5000 |
| **SSL** | No | Optional |
| **Auto-start** | No | Yes |
| **Use Case** | Development/Testing | Production |

{% content-ref url="digitalocean-production.md" %}
[digitalocean-production.md](digitalocean-production.md)
{% endcontent-ref %}

---

## Next Steps

1. **Create devices** - [Creating Devices Guide](../user-guide/creating-devices.md)
2. **Configure Traccar** - [Traccar Integration](../user-guide/traccar-integration.md)
3. **Use the API** - [REST API Reference](../api-reference/rest-api.md)
4. **Explore protocols** - [All Protocols](../protocols/all-protocols.md)

---

## Need Help?

- [Troubleshooting Guide](../support/troubleshooting.md)
- [FAQ](../support/faq.md)
- [Common Issues](../support/common-issues.md)
- [Contact Support](../support/contact.md)

---

*Windows Local Installation Guide - Updated: November 2025*
