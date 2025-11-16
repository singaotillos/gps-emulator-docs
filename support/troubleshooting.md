# Troubleshooting Guide - Universal GPS Tracker Emulator

Common issues and solutions for the GPS emulator.

---

## Table of Contents

- [Installation Issues](#installation-issues)
- [Startup Problems](#startup-problems)
- [Device Issues](#device-issues)
- [Traccar Integration](#traccar-integration)
- [Network & Connectivity](#network--connectivity)
- [Performance Issues](#performance-issues)
- [Database Issues](#database-issues)
- [API Problems](#api-problems)
- [Platform-Specific](#platform-specific)
- [Error Messages](#error-messages)
- [Debug Mode](#debug-mode)
- [Getting Help](#getting-help)

---

## Installation Issues

### Python Not Found

**Problem:** `python: command not found` or `'python' is not recognized`

**Solution (Windows):**
```bash
# Download Python from python.org
# During installation, CHECK "Add Python to PATH"

# Verify installation
python --version

# Or use python launcher
py --version
```

**Solution (Linux/Ubuntu):**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Verify
python3 --version
```

---

### Gevent Build Fails (Python 3.13+)

{% hint style="danger" %}
**Windows + Python 3.13**: This is a known compatibility issue. Use the Windows-specific installation method.
{% endhint %}

**Problem:**
```
error: subprocess-exited-with-error
undeclared name not builtin: long
Failed to build 'gevent' when getting requirements to build wheel
```

**Cause:** Gevent is not compatible with Python 3.13 (uses deprecated `long` type from Python 2)

**Solution (Windows):**

{% hint style="success" %}
Use `requirements-windows.txt` instead of `requirements.txt`
{% endhint %}

```cmd
# Use Windows-specific requirements file
pip install -r requirements-windows.txt

# This installs Flask-SocketIO in threading mode (no gevent)
```

**What's different:**
- ❌ `requirements.txt` - Uses gevent (Linux/production only)
- ✅ `requirements-windows.txt` - Uses threading mode (Windows compatible)

**See:** [Windows Local Installation Guide](../getting-started/windows-local.md)

**Solution (Linux Production):**

Use Python 3.10 or 3.11 (not 3.13):

```bash
# Install Python 3.10
sudo apt install python3.10 python3.10-venv python3-pip

# Create virtual environment with Python 3.10
python3.10 -m venv venv
source venv/bin/activate

# Install with gevent
pip install -r requirements.txt
```

**See:** [DigitalOcean Production Guide](../getting-started/digitalocean-production.md)

---

### Pip Install Fails

**Problem:** `pip install -r requirements.txt` fails with errors

**Solution 1 - Check Python version:**
```bash
python --version

# Python 3.13 on Windows? Use requirements-windows.txt instead!
pip install -r requirements-windows.txt
```

**Solution 2 - Upgrade pip:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Solution 3 - Use user directory:**
```bash
pip install --user -r requirements.txt
```

**Solution 4 - Virtual environment:**
```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux:
source venv/bin/activate

# Install correct requirements file
# Windows:
pip install -r requirements-windows.txt
# Linux:
pip install -r requirements.txt
```

**Solution 5 - Install individually:**
```bash
# Install packages one by one to find problematic package
pip install flask==3.0.0
pip install flask-socketio==5.3.5
pip install flask-cors==4.0.0
# ... continue with each package
```

---

### Permission Denied

**Problem:** Permission errors during installation/execution

**Solution (Linux/Mac):**
```bash
# Make script executable
chmod +x app.py

# Fix ownership
sudo chown -R $USER:$USER .

# Or install with --user
pip install --user -r requirements.txt
```

**Solution (Windows):**
```bash
# Run Command Prompt as Administrator
# Right-click CMD > "Run as administrator"
```

---

### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Ensure you're in correct environment
which python  # Linux/Mac
where python  # Windows

# If using virtual environment, activate it first
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

---

---

### WERKZEUG_SERVER_FD Error (Windows)

{% hint style="danger" %}
**Windows-specific**: This error only occurs on Windows with certain configurations.
{% endhint %}

**Problem:**
```
KeyError: 'WERKZEUG_SERVER_FD'
at File "werkzeug\serving.py", line 1091, in run_simple
```

**Cause:** Flask's Werkzeug reloader expects an environment variable that doesn't exist on Windows

**Solution:**

Add to your `.env` file:

```env
WERKZEUG_RUN_MAIN=false
```

**Or set via PowerShell:**

```powershell
(Get-Content .env) -replace 'WERKZEUG_RUN_MAIN=true', 'WERKZEUG_RUN_MAIN=false' | Set-Content .env
```

**Restart application:**

```cmd
venv\Scripts\activate.bat
python app.py
```

**See:** [Windows Local Installation Guide](../getting-started/windows-local.md#troubleshooting)

---

## Startup Problems

### Port Already in Use

**Problem:** `Address already in use` or `Port 5000 is already allocated`

**Solution 1 - Change port:**
```bash
# Edit .env
WEB_PORT=5001

# Or config.yaml
web_interface:
  port: 5001
```

**Solution 2 - Kill existing process:**

**Linux/Mac:**
```bash
# Find process using port 5000
lsof -ti:5000

# Kill process
lsof -ti:5000 | xargs kill -9

# Or use fuser
fuser -k 5000/tcp
```

**Windows:**
```cmd
# Find process
netstat -ano | findstr :5000

# Note the PID (last column)
# Kill process (replace PID)
taskkill /PID 12345 /F
```

---

### Application Already Running

**Problem:** `Another instance of the application is already running`

**Solution:**
```bash
# Remove lock file
# Linux/Mac
rm /tmp/osmand_gps_emulator.lock

# Windows
del %TEMP%\osmand_gps_emulator.lock

# Or kill all Python processes
# Linux/Mac
pkill -f app.py

# Windows
taskkill /IM python.exe /F
```

---

### Flask Debug Mode Warning

**Problem:** `WARNING: This is a development server. Do not use it in a production deployment.`

**Solution:**

This is a warning, not an error. For production:

**Option 1 - Use production WSGI server:**
```bash
# Install gunicorn (Linux/Mac)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Install waitress (Windows)
pip install waitress
waitress-serve --listen=*:5000 app:app
```

**Option 2 - Ignore for small deployments:**
```bash
# Disable debug mode in .env
WEB_DEBUG=false

# Run normally
python app.py
```

---

### Import Errors on Startup

**Problem:** Various import errors when starting

**Solution:**
```bash
# Ensure all dependencies installed
pip install -r requirements.txt --upgrade

# Check Python version (needs 3.8+)
python --version

# Clear Python cache
find . -type d -name __pycache__ -exec rm -rf {} +  # Linux/Mac
# Windows: delete __pycache__ folders manually

# Reinstall from scratch
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## Device Issues

### Device Won't Start

**Problem:** Device status remains "stopped" after clicking Start

**Check 1 - License limit:**
```bash
# CE limited to 5 devices
# Check how many running:
curl http://localhost:5000/api/status | jq '.system.devices_running'

# Stop other devices or upgrade to EE
```

**Check 2 - Protocol port availability:**
```bash
# Verify protocol port not in use
# Linux/Mac
lsof -i :5002  # TK103 port

# Windows
netstat -ano | findstr :5002
```

**Check 3 - Logs:**
```bash
# Check emulator.log for errors
tail -f emulator.log  # Linux/Mac
type emulator.log     # Windows

# Look for:
# - Port binding errors
# - Protocol initialization failures
# - Permission issues
```

---

### Device Immediately Stops

**Problem:** Device starts but immediately stops

**Cause:** Usually protocol initialization failure

**Solution:**
```bash
# Enable debug logging
# .env
LOG_LEVEL=DEBUG

# Restart and check logs
python app.py

# Common causes:
# 1. Port already in use
# 2. Invalid device ID format
# 3. Missing protocol files
# 4. Firewall blocking
```

---

### Invalid Device ID

**Problem:** `Invalid device ID format` error

**Solution:**

Each protocol has specific ID format:

```python
# TK103: 15-digit IMEI
"357938506404024"

# GT06: 10-15 digit number
"8888888888"

# OsmAnd: any identifier
"mobile-001"

# Navigil: special format
"123456789012345"
```

**Let emulator auto-generate:**
```json
{
  "protocol": "tk103",
  "device_model": "TK103-2B"
  // Omit device_id - will be generated
}
```

---

### Device Not Sending Data

**Problem:** Device shows "running" but no data sent

**Check 1 - Target host/port:**
```bash
# Verify Traccar is listening
curl http://localhost:8082

# Check protocol port open
nc -zv localhost 5002  # TK103
telnet localhost 5002
```

**Check 2 - Firewall:**
```bash
# Linux: Allow port
sudo ufw allow 5002/tcp

# Windows: Add firewall rule
netsh advfirewall firewall add rule name="GPS TK103" dir=in action=allow protocol=TCP localport=5002
```

**Check 3 - Configuration:**
```yaml
# config.yaml
servers:
  tk103:
    enabled: true      # Must be true
    host: localhost    # Correct host
    port: 5002        # Must match Traccar
```

---

### Device Data Not Updating

**Problem:** Position/stats not updating in dashboard

**Solution:**
```bash
# Check update_interval not too high
curl http://localhost:5000/api/multidevice/devices/dev_tk103_001 | jq '.device.config.update_interval'

# Should be 5-30 seconds
# Update if needed:
curl -X PUT http://localhost:5000/api/multidevice/devices/dev_tk103_001/config \
  -H "Content-Type: application/json" \
  -d '{"update_interval": 10.0}'

# Check WebSocket connection
# Open browser console (F12)
# Should see: "Connected to emulator"
```

---

## Traccar Integration

### Traccar Not Receiving Data

**Problem:** Emulator running but Traccar shows no positions

**Solution:**

**Step 1 - Verify Traccar running:**
```bash
# Check Traccar web interface
curl http://localhost:8082

# Check Traccar logs
tail -f /opt/traccar/logs/tracker-server.log
```

**Step 2 - Verify port configuration:**
```xml
<!-- Check traccar.xml -->
<!-- TK103 must use port 5002 -->
<entry key='tk103.port'>5002</entry>
```

**Step 3 - Check device exists in Traccar:**
```bash
# Login to Traccar web interface
# Go to Settings > Devices
# Verify device with correct unique ID exists

# Protocol: tk103
# Unique ID: 357938506404024 (must match emulator)
```

**Step 4 - Test connectivity:**
```bash
# Send test packet to Traccar port
echo -e "(123456789012345BP00123456789012345260925A1234.5678N01234.5678E000.0120000123.4500000000L00000000)" | nc localhost 5002
```

---

### Device Offline in Traccar

**Problem:** Device appears in Traccar but shows "offline"

**Causes & Solutions:**

**1. Device ID mismatch:**
```bash
# Emulator device ID must EXACTLY match Traccar unique ID
# Check emulator:
curl http://localhost:5000/api/multidevice/devices/dev_tk103_001 | jq '.device.unique_id'

# Check Traccar:
# Settings > Devices > Click device > Unique ID field
```

**2. Protocol mismatch:**
```bash
# Emulator protocol must match Traccar device protocol
# Emulator: tk103
# Traccar device protocol: tk103 (not tk102, not tk104)
```

**3. Not sending data:**
```bash
# Verify device started in emulator
curl http://localhost:5000/api/status | jq '.devices[] | select(.device_id=="dev_tk103_001").status'
# Should be "running"
```

**4. Firewall blocking:**
```bash
# Check firewall logs
sudo tail -f /var/log/ufw.log  # Linux

# Temporarily disable to test
sudo ufw disable
```

---

### Traccar Connection Timeout

**Problem:** `Failed to connect to Traccar` error

**Solution:**
```bash
# Check Traccar is running
systemctl status traccar  # Linux
# Or check Windows Services

# Check Traccar web port
curl http://localhost:8082

# Update emulator config
# .env
TRACCAR_HOST=localhost     # or IP address
TRACCAR_PORT=8082          # Traccar WEB port (not protocol port!)
TRACCAR_USERNAME=admin
TRACCAR_PASSWORD=admin

# Test connection
curl -X POST http://localhost:5000/api/traccar/test
```

---

### Traccar Authentication Failed

**Problem:** `Authentication failed` when adding devices to Traccar

**Solution:**
```bash
# Verify Traccar credentials
# .env
TRACCAR_USERNAME=admin
TRACCAR_PASSWORD=admin

# Test login manually
curl -X POST http://localhost:8082/api/session \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=admin&password=admin"

# If fails, reset Traccar password:
# Login to Traccar web > Account > Change password
```

---

## Network & Connectivity

### Can't Access Web Interface

**Problem:** Can't open `http://localhost:5000`

**Solution 1 - Check application running:**
```bash
# Verify process running
ps aux | grep app.py  # Linux/Mac
tasklist | findstr python  # Windows

# Check logs
tail -f emulator.log
```

**Solution 2 - Check firewall:**
```bash
# Linux
sudo ufw allow 5000/tcp

# Windows
netsh advfirewall firewall add rule name="GPS Emulator" dir=in action=allow protocol=TCP localport=5000
```

**Solution 3 - Check binding address:**
```yaml
# config.yaml
web_interface:
  host: 0.0.0.0  # Listen on all interfaces
  port: 5000

# Restart application
```

**Solution 4 - Try different browsers:**
```bash
# Try:
http://localhost:5000
http://127.0.0.1:5000
http://[your-ip]:5000
```

---

### Can't Access from Network

**Problem:** Works on localhost but not from other computers

**Solution:**
```bash
# 1. Set host to 0.0.0.0
# config.yaml
web_interface:
  host: 0.0.0.0  # Not 127.0.0.1

# 2. Allow firewall
sudo ufw allow 5000/tcp

# 3. Get your IP address
# Linux/Mac
hostname -I
ip addr show

# Windows
ipconfig

# 4. Access from other computer
http://192.168.1.100:5000  # Use your IP
```

---

### API Requests Timeout

**Problem:** API requests take too long or timeout

**Solution:**
```bash
# Check server load
curl http://localhost:5000/api/status | jq '.system.cpu_percent'

# Reduce concurrent devices
# .env
ADVANCED_MAX_CONCURRENT_EMULATORS=20

# Disable resource-intensive features
# config.yaml
simulation:
  enable_traffic_simulation: false
  enable_weather_effects: false
  simulate_acceleration: false
```

---

### CORS Errors

**Problem:** Browser console shows CORS errors

**Solution:**
```bash
# Enable CORS in .env
API_ENABLE_CORS=true

# Restart application

# For specific origin only
# Modify app.py:
# CORS(app, origins=["http://example.com"])
```

---

## Performance Issues

### High CPU Usage

**Problem:** Emulator using 80%+ CPU

**Causes & Solutions:**

**1. Too many devices:**
```bash
# Check device count
curl http://localhost:5000/api/status | jq '.system.devices_running'

# Stop unnecessary devices
curl -X POST http://localhost:5000/api/multidevice/devices/{device_id}/stop
```

**2. Short update interval:**
```yaml
# config.yaml
simulation:
  update_interval: 30.0  # Increase from 5 to 30 seconds
```

**3. Advanced features enabled:**
```yaml
simulation:
  enable_traffic_simulation: false
  enable_weather_effects: false
  simulate_acceleration: false
  simulate_engine_data: false
```

**4. Monitoring overhead:**
```yaml
monitoring:
  enabled: false  # Disable if not needed
```

---

### High Memory Usage

**Problem:** RAM usage constantly increasing

**Solution:**
```bash
# 1. Check current usage
curl http://localhost:5000/api/status | jq '.system.memory_percent'

# 2. Reduce concurrent devices
# .env
ADVANCED_MAX_CONCURRENT_EMULATORS=20

# 3. Reduce metrics retention
# config.yaml
monitoring:
  metrics_retention_hours: 24  # Instead of 168

# 4. Restart periodically
# Use system cron/Task Scheduler to restart daily

# 5. Check for memory leaks
# Monitor over time:
watch -n 30 'curl -s http://localhost:5000/api/status | jq .system.memory_percent'
```

---

### Slow Web Interface

**Problem:** Dashboard loads slowly or freezes

**Solution:**
```bash
# 1. Reduce auto-refresh rate
# config.yaml
web_interface:
  auto_refresh_interval: 5  # Increase from 1 to 5 seconds

# 2. Disable advanced metrics
web_interface:
  show_advanced_metrics: false

# 3. Use API instead of web UI for bulk operations

# 4. Clear browser cache
# Chrome: Ctrl+Shift+Delete
# Firefox: Ctrl+Shift+Delete
```

---

### Disk Space Issues

**Problem:** Running out of disk space

**Solution:**
```bash
# Check disk usage
df -h .  # Linux/Mac

# 1. Clean old logs
rm -f *.log.1 *.log.2 *.log.3

# 2. Reduce log retention
# config.yaml
logging:
  max_size_mb: 5         # Reduce from 10
  backup_count: 2        # Reduce from 5

# 3. Reduce monitoring data
monitoring:
  metrics_retention_hours: 24  # Reduce from 168

# 4. Clean database
rm -f vehicle_attributes.db
# Database will be recreated on next start
```

---

## Database Issues

### Database Locked

**Problem:** `database is locked` error

**Solution:**
```bash
# 1. Stop all emulator instances
pkill -f app.py  # Linux/Mac
taskkill /IM python.exe /F  # Windows

# 2. Remove lock file
rm /tmp/osmand_gps_emulator.lock

# 3. Check for orphaned processes
ps aux | grep app.py  # Linux/Mac
tasklist | findstr python  # Windows

# 4. Restart application
python app.py
```

---

### Database Corruption

**Problem:** `database disk image is malformed` error

**Solution:**
```bash
# Backup database
cp vehicle_attributes.db vehicle_attributes.db.backup

# Try to repair
sqlite3 vehicle_attributes.db "PRAGMA integrity_check;"

# If repair fails, delete and recreate
rm vehicle_attributes.db
# Database will be recreated on next start with fresh data

# Note: Vehicle attribute history will be lost
```

---

### Missing Database Tables

**Problem:** `no such table` error

**Solution:**
```bash
# Database schema will be auto-created on first start
# If missing, delete and recreate:

rm vehicle_attributes.db
python app.py

# Database will initialize automatically
```

---

## API Problems

### API Returns 404

**Problem:** All API requests return 404 Not Found

**Solution:**
```bash
# Check API enabled
# .env
API_ENABLED=true

# Verify correct URL format
# WRONG:
curl http://localhost:5000/api/v2/devices
curl http://localhost:5000/devices

# CORRECT:
curl http://localhost:5000/api/multidevice/devices
curl http://localhost:5000/api/status

# Check application started correctly
curl http://localhost:5000/
# Should return HTML page, not 404
```

---

### API Returns 401 Unauthorized

**Problem:** `Authentication required` error

**Solution:**
```bash
# Check if authentication enabled
# .env
API_ENABLE_AUTHENTICATION=false  # Set to false for testing

# Or provide API key
# .env
API_KEY=your-secret-key

# Use in request:
curl -H "Authorization: Bearer your-secret-key" \
     http://localhost:5000/api/status
```

---

### API Returns 400 Bad Request

**Problem:** `Invalid request` error

**Solution:**
```bash
# Check request format
# WRONG - missing Content-Type:
curl -X POST http://localhost:5000/api/multidevice/devices \
  -d '{"protocol":"tk103"}'

# CORRECT - with Content-Type:
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{"protocol":"tk103","device_model":"TK103-2B"}'

# Check required fields present
# device_model is REQUIRED!
```

---

### API Returns 500 Internal Server Error

**Problem:** Server error

**Solution:**
```bash
# Check logs for error details
tail -f emulator.log

# Enable debug mode
# .env
WEB_DEBUG=true
LOG_LEVEL=DEBUG

# Restart and check error message
python app.py

# Common causes:
# - Database errors
# - Missing dependencies
# - Configuration errors
# - Python syntax errors
```

---

## Platform-Specific

### Windows: 'cp' is not recognized

**Problem:** Commands from Linux/Mac guides don't work

**Solution:**
```cmd
# Use Windows equivalents:
# cp -> copy
# rm -> del
# mkdir -> md
# ls -> dir

# Or install Git Bash (includes Unix tools)
# Download from: git-scm.com

# Or use PowerShell which has aliases:
# cp = Copy-Item
# rm = Remove-Item
# ls = Get-ChildItem
```

---

### Linux: Permission Denied on Port 80/443

**Problem:** Can't bind to port 80 or 443

**Solution:**
```bash
# Option 1 - Use port > 1024
# .env
WEB_PORT=5000  # or 8080

# Option 2 - Use sudo (not recommended)
sudo python app.py

# Option 3 - Use setcap (best)
sudo setcap 'cap_net_bind_service=+ep' $(which python3)
```

---

### macOS: SSL Certificate Errors

**Problem:** SSL certificate verification failed

**Solution:**
```bash
# Install certificates
/Applications/Python\ 3.x/Install\ Certificates.command

# Or disable SSL verification (not recommended)
export PYTHONHTTPSVERIFY=0

# Or update certifi
pip install --upgrade certifi
```

---

### Docker: Can't Connect to Host Network

**Problem:** Container can't reach host services (Traccar)

**Solution:**
```bash
# Use host network mode
docker run --network=host gps-emulator

# Or use host.docker.internal
# .env
TRACCAR_HOST=host.docker.internal

# Linux: add extra host
docker run --add-host=host.docker.internal:host-gateway gps-emulator
```

---

## Error Messages

### "Protocol not found"

**Cause:** Invalid protocol name

**Solution:**
```bash
# Get list of valid protocols
curl http://localhost:5000/api/protocols | jq '.protocols[].name'

# Use exact name (lowercase)
"protocol": "tk103"  # NOT "TK103" or "tk-103"
```

---

### "Device limit reached"

**Cause:** Community Edition limit (5 devices)

**Solution:**
```bash
# Check current count
curl http://localhost:5000/api/status | jq '.system.devices_running'

# Stop unused devices
curl -X POST http://localhost:5000/api/multidevice/devices/{device_id}/stop

# Or upgrade to Enterprise Edition (unlimited)
# .env
UGTE_LICENSE_KEY=EE-XXXX-XXXX-XXXX-XXXX
```

---

### "Port already allocated"

**Cause:** Protocol port in use

**Solution:**
```bash
# Find what's using the port
lsof -i :5002  # Linux/Mac
netstat -ano | findstr :5002  # Windows

# Kill process or change port
# config.yaml
servers:
  tk103:
    port: 5102  # Different port
```

---

### "Failed to start simulator"

**Cause:** Various initialization errors

**Solution:**
```bash
# Enable debug logging
# .env
LOG_LEVEL=DEBUG

# Check logs for specific error
tail -f emulator.log

# Common causes:
# - Invalid device ID format
# - Port unavailable
# - Missing protocol files
# - Configuration error
```

---

## Debug Mode

### Enable Full Debug Logging

```bash
# .env
LOG_LEVEL=DEBUG
LOG_ENABLE_CONSOLE=true
LOG_ENABLE_FILE=true
WEB_DEBUG=true
```

### View Real-Time Logs

```bash
# Linux/Mac
tail -f emulator.log

# Windows
Get-Content emulator.log -Wait  # PowerShell
```

### Test Individual Components

```python
# Test protocol ID conversion
python -c "from protocol_id_converter import convert_id_for_protocol; print(convert_id_for_protocol('tk103', '357938506404024'))"

# Test database
python -c "from vehicle_attributes_db import get_vehicle_attributes; print(get_vehicle_attributes('test'))"

# Test Traccar connection
curl -X POST http://localhost:5000/api/traccar/test
```

---

## Getting Help

### Before Asking for Help

1. **Check logs:**
   ```bash
   tail -100 emulator.log
   ```

2. **Check system status:**
   ```bash
   curl http://localhost:5000/api/status | jq
   ```

3. **Test basic functionality:**
   ```bash
   # Can you create a device?
   curl -X POST http://localhost:5000/api/multidevice/devices \
     -H "Content-Type: application/json" \
     -d '{"protocol":"tk103","device_model":"TK103-2B"}'
   ```

4. **Gather version info:**
   ```bash
   python --version
   pip list | grep -i flask
   uname -a  # Linux/Mac
   systeminfo  # Windows
   ```

### Contact Support

**Email:** support@your-domain.com

**Include:**
- Description of problem
- Error messages (full text)
- Last 50 lines of log file
- Your configuration (.env and config.yaml - remove passwords!)
- Steps to reproduce
- Operating system and Python version

**Response Time:**
- Community Edition: 24-48 hours
- Enterprise Edition: 4-24 hours (priority)

### Community Resources

- Documentation: See all `.md` files in project
- FAQ: [FAQ.md](FAQ.md)
- API Reference: [API_REFERENCE.md](API_REFERENCE.md)
- Configuration: [CONFIGURATION.md](CONFIGURATION.md)
- Installation: [INSTALLATION.md](INSTALLATION.md)

---

## Common Solutions Summary

**Quick Fixes:**
```bash
# Restart application
pkill -f app.py && python app.py

# Clear lock file
rm /tmp/osmand_gps_emulator.lock

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Clear Python cache
find . -name __pycache__ -exec rm -rf {} +

# Check port not in use
lsof -i :5000

# View logs
tail -f emulator.log

# Test API
curl http://localhost:5000/api/status
```

---

*Troubleshooting guide updated: October 2025*
