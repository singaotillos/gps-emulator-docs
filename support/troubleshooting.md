# Troubleshooting Guide

Common issues and solutions for the GPS Emulator.

---

## Installation Issues

### Python Not Found

{% hint style="danger" %}
**Error:** `python: command not found` or `'python' is not recognized`
{% endhint %}

{% tabs %}
{% tab title="Windows" %}
**Solution:**

1. Download Python from [python.org](https://python.org)
2. During installation, **CHECK "Add Python to PATH"**
3. Restart Command Prompt
4. Verify installation:
   ```bash
   python --version
   ```

Or use the Python launcher:
```bash
py --version
```
{% endtab %}

{% tab title="Linux" %}
**Solution:**

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Verify
python3 --version
pip3 --version
```
{% endtab %}

{% tab title="macOS" %}
**Solution:**

```bash
# Using Homebrew
brew install python@3.10

# Verify
python3 --version
pip3 --version
```
{% endtab %}
{% endtabs %}

---

### Pip Install Fails

{% hint style="danger" %}
**Error:** `pip install -r requirements.txt` fails with errors
{% endhint %}

**Solution 1 - Upgrade pip:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Solution 2 - Use user directory:**
```bash
pip install --user -r requirements.txt
```

**Solution 3 - Virtual environment:**
```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install
pip install -r requirements.txt
```

{% hint style="success" %}
**Recommended:** Always use virtual environments for Python projects
{% endhint %}

---

### Permission Denied

{% hint style="danger" %}
**Error:** Permission errors during installation/execution
{% endhint %}

{% tabs %}
{% tab title="Linux/Mac" %}
```bash
# Make script executable
chmod +x app.py

# Fix ownership
sudo chown -R $USER:$USER .

# Or install with --user
pip install --user -r requirements.txt
```
{% endtab %}

{% tab title="Windows" %}
1. Right-click Command Prompt
2. Select "Run as administrator"
3. Run installation commands
{% endtab %}
{% endtabs %}

---

### Module Not Found

{% hint style="danger" %}
**Error:** `ModuleNotFoundError: No module named 'flask'`
{% endhint %}

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

## Startup Problems

### Port Already in Use

{% hint style="danger" %}
**Error:** `Address already in use` or `Port 5000 is already allocated`
{% endhint %}

**Solution 1 - Change port:**

```bash
# Edit .env
WEB_PORT=5001

# Or config.yaml
web_interface:
  port: 5001
```

**Solution 2 - Kill existing process:**

{% tabs %}
{% tab title="Linux/Mac" %}
```bash
# Find process using port 5000
lsof -ti:5000

# Kill process
lsof -ti:5000 | xargs kill -9

# Or use fuser
fuser -k 5000/tcp
```
{% endtab %}

{% tab title="Windows" %}
```cmd
# Find process
netstat -ano | findstr :5000

# Note the PID (last column)
# Kill process (replace PID)
taskkill /PID 12345 /F
```
{% endtab %}
{% endtabs %}

---

### Application Already Running

{% hint style="danger" %}
**Error:** `Another instance of the application is already running`
{% endhint %}

**Solution:**

{% tabs %}
{% tab title="Linux/Mac" %}
```bash
# Remove lock file
rm /tmp/osmand_gps_emulator.lock

# Or kill all Python processes
pkill -f app.py
```
{% endtab %}

{% tab title="Windows" %}
```cmd
# Remove lock file
del %TEMP%\osmand_gps_emulator.lock

# Or kill all Python processes
taskkill /IM python.exe /F
```
{% endtab %}
{% endtabs %}

---

### Database Locked Error

{% hint style="danger" %}
**Error:** `database is locked` or `OperationalError: database is locked`
{% endhint %}

**Solution:**

```bash
# Stop all running instances
# Linux/Mac:
pkill -f app.py

# Windows:
taskkill /IM python.exe /F

# Remove lock file
# Linux/Mac:
rm /tmp/osmand_gps_emulator.lock

# Windows:
del %TEMP%\osmand_gps_emulator.lock

# Restart application
python app.py
```

{% hint style="info" %}
**Cause:** Multiple instances trying to access SQLite database simultaneously
{% endhint %}

---

## Device Issues

### Device Not Sending Data

{% hint style="warning" %}
**Problem:** Device created but not sending data to Traccar
{% endhint %}

**Checklist:**

1. ✅ **Device status = "running"?**
   ```bash
   # Check status in web interface or API
   curl http://localhost:5000/api/multidevice/devices
   ```

2. ✅ **Correct protocol selected?**
   - Protocol must match Traccar configuration
   - Example: TK103 in emulator → TK103 in Traccar

3. ✅ **Correct port configured?**
   - TK103: Port 5002
   - GT06: Port 5023
   - Check `config.yaml` and Traccar's `traccar.xml`

4. ✅ **Firewall not blocking?**
   ```bash
   # Linux - Allow port
   sudo ufw allow 5002/tcp

   # Windows - Check firewall settings
   ```

---

### Device Shows "Error" Status

{% hint style="danger" %}
**Problem:** Device status shows "error" in dashboard
{% endhint %}

**Solutions:**

1. **Check logs:**
   ```bash
   # View last 50 lines of log
   tail -n 50 emulator.log
   ```

2. **Common causes:**
   - Invalid protocol port
   - Network connection issues
   - Traccar server not running
   - Invalid device configuration

3. **Restart device:**
   ```bash
   # Stop device
   curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop

   # Start device
   curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
   ```

---

### Device Limit Reached

{% hint style="danger" %}
**Error:** `Device limit reached` - CE limited to 5 devices
{% endhint %}

**Solution:**

**Option 1 - Stop unused devices:**
```bash
# List all devices
curl http://localhost:5000/api/multidevice/devices

# Stop devices you don't need
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop
```

**Option 2 - Upgrade to Enterprise:**
- Enterprise Edition supports unlimited devices
- Contact sales for upgrade

---

## Traccar Integration

### Can't Connect to Traccar

{% hint style="danger" %}
**Problem:** Emulator can't connect to Traccar server
{% endhint %}

**Checklist:**

1. ✅ **Traccar server running?**
   ```bash
   # Test Traccar web interface
   curl http://localhost:8082
   ```

2. ✅ **Correct Traccar credentials?**
   ```bash
   # .env
   TRACCAR_USERNAME=admin
   TRACCAR_PASSWORD=admin
   ```

3. ✅ **Correct Traccar host/port?**
   ```bash
   # .env
   TRACCAR_HOST=localhost
   TRACCAR_PORT=8082  # Web interface port, not protocol port!
   ```

4. ✅ **Network connectivity?**
   ```bash
   # Test connection
   ping localhost
   telnet localhost 8082
   ```

---

### Device Not Appearing in Traccar

{% hint style="warning" %}
**Problem:** Device created in emulator but not visible in Traccar
{% endhint %}

**Solution:**

1. **Check auto-create is enabled:**
   ```bash
   # .env
   TRACCAR_AUTO_CREATE_DEVICES=true
   ```

2. **Manually create device in Traccar:**
   - Go to Traccar web interface (http://localhost:8082)
   - Settings → Devices → Add Device
   - **Name:** Any name
   - **Identifier:** Use device unique ID from emulator
   - **Protocol:** Must match emulator protocol

3. **Check device unique ID:**
   ```bash
   # Get device details
   curl http://localhost:5000/api/multidevice/devices/DEVICE_ID

   # Look for "unique_id" field
   ```

4. **Test Traccar connection:**
   ```bash
   curl -X POST http://localhost:5000/api/traccar/test
   ```

---

### Wrong Location in Traccar

{% hint style="warning" %}
**Problem:** Device shows incorrect location or doesn't move
{% endhint %}

**Solutions:**

1. **Check device is running:**
   - Status must be "running" not "stopped"

2. **Verify route configuration:**
   ```bash
   # Check device route
   curl http://localhost:5000/api/device/DEVICE_ID/route
   ```

3. **Check update interval:**
   ```yaml
   # config.yaml
   simulation:
     update_interval: 10.0  # Seconds between updates
   ```

4. **Monitor device updates:**
   - Open web dashboard
   - Watch "Last Update" timestamp
   - Should update every 10 seconds (default)

---

## Network & Connectivity

### Can't Access Web Interface

{% hint style="danger" %}
**Problem:** Browser can't open http://localhost:5000
{% endhint %}

**Solutions:**

1. **Check application is running:**
   ```bash
   # Should see "Running on http://0.0.0.0:5000"
   ```

2. **Check correct port:**
   ```bash
   # Check .env or config.yaml for port number
   WEB_PORT=5000
   ```

3. **Try 127.0.0.1 instead:**
   ```
   http://127.0.0.1:5000
   ```

4. **Check firewall:**
   ```bash
   # Linux
   sudo ufw allow 5000/tcp

   # Windows - Temporarily disable firewall for testing
   ```

---

### Can't Access from Other Computers

{% hint style="warning" %}
**Problem:** Web interface only works on localhost, not from network
{% endhint %}

**Solution:**

1. **Change host to 0.0.0.0:**
   ```bash
   # .env
   WEB_HOST=0.0.0.0
   ```

2. **Restart application:**
   ```bash
   python app.py
   ```

3. **Allow firewall:**
   ```bash
   # Linux
   sudo ufw allow 5000/tcp

   # Windows - Allow port in Windows Firewall
   ```

4. **Access using server IP:**
   ```
   http://192.168.1.100:5000
   ```

{% hint style="warning" %}
**Security:** Only use `0.0.0.0` in trusted networks!
{% endhint %}

---

## Performance Issues

### High CPU Usage

{% hint style="warning" %}
**Problem:** Application using too much CPU
{% endhint %}

**Solutions:**

1. **Reduce number of devices:**
   ```bash
   # Stop unused devices
   ```

2. **Increase update interval:**
   ```yaml
   # config.yaml
   simulation:
     update_interval: 30.0  # Slower updates = less CPU
   ```

3. **Disable advanced features:**
   ```yaml
   simulation:
     enable_traffic_simulation: false
     enable_weather_effects: false
     simulate_acceleration: false
   ```

4. **Disable monitoring:**
   ```yaml
   monitoring:
     enabled: false
   ```

---

### High Memory Usage

{% hint style="warning" %}
**Problem:** Application using too much RAM
{% endhint %}

**Solutions:**

1. **Reduce concurrent devices:**
   ```bash
   # .env
   ADVANCED_MAX_CONCURRENT_EMULATORS=20
   ```

2. **Lower metrics retention:**
   ```yaml
   monitoring:
     metrics_retention_hours: 24  # Keep less history
   ```

3. **Use efficient performance mode:**
   ```bash
   # .env
   ADVANCED_PERFORMANCE_MODE=efficient
   ```

---

### Slow Web Interface

{% hint style="warning" %}
**Problem:** Dashboard loads slowly or freezes
{% endhint %}

**Solutions:**

1. **Reduce auto-refresh rate:**
   ```yaml
   web_interface:
     auto_refresh_interval: 5  # Slower refresh = better performance
   ```

2. **Disable metrics display:**
   ```yaml
   web_interface:
     show_advanced_metrics: false
   ```

3. **Use API instead of web interface:**
   - API is more lightweight
   - Better for managing many devices

---

## API Problems

### 401 Unauthorized Error

{% hint style="danger" %}
**Error:** API returns 401 Unauthorized
{% endhint %}

**Solution:**

1. **Check if authentication is enabled:**
   ```bash
   # .env
   API_ENABLE_AUTHENTICATION=true
   ```

2. **Include API key in request:**
   ```bash
   curl -H "Authorization: Bearer YOUR_API_KEY" \
        http://localhost:5000/api/status
   ```

3. **Verify API key is correct:**
   ```bash
   # Check .env file
   API_KEY=your-secret-key
   ```

4. **Regenerate API key if needed:**
   ```bash
   openssl rand -hex 32
   ```

---

### 429 Rate Limit Exceeded

{% hint style="danger" %}
**Error:** Too Many Requests (429)
{% endhint %}

**Solution:**

1. **Disable rate limiting (development):**
   ```bash
   # .env
   API_RATE_LIMITING=false
   ```

2. **Increase rate limit:**
   ```bash
   API_MAX_REQUESTS_PER_MINUTE=500
   ```

3. **Wait and retry:**
   - Wait 60 seconds
   - Check `retry_after` in response

---

## Platform-Specific

### Windows - UTF-8 Encoding Errors

{% hint style="danger" %}
**Error:** `UnicodeEncodeError` on Windows
{% endhint %}

**Solution:**

```cmd
# Set UTF-8 encoding for Command Prompt
chcp 65001

# Or use PowerShell (better UTF-8 support)
```

---

### Linux - Service Won't Start on Boot

{% hint style="warning" %}
**Problem:** Want to run emulator as systemd service
{% endhint %}

**Solution:**

Create service file:

```bash
sudo nano /etc/systemd/system/gps-emulator.service
```

```ini
[Unit]
Description=GPS Tracker Emulator
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/emulator
ExecStart=/usr/bin/python3 /path/to/emulator/app.py
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

## Debug Mode

### Enable Debug Mode

When troubleshooting, enable debug mode for detailed logs:

```yaml
# config.yaml
web_interface:
  debug: true

logging:
  level: DEBUG
  enable_console: true
```

{% hint style="danger" %}
**Never use debug mode in production!** It exposes sensitive information.
{% endhint %}

---

## Getting Help

### Before Contacting Support

1. ✅ Check this troubleshooting guide
2. ✅ Read the [FAQ](faq.md)
3. ✅ Check application logs
4. ✅ Try restarting the application
5. ✅ Test with a fresh device

### When Contacting Support

**Include:**

- Error message (full text)
- Screenshots
- Log files (`emulator.log`)
- Configuration files (`config.yaml`, `.env`)
- Steps to reproduce
- System information (OS, Python version)

**Contact:**

- Email: support@your-domain.com
- Response time: 24-48 hours

---

## Next Steps

{% content-ref url="faq.md" %}
[faq.md](faq.md)
{% endcontent-ref %}

{% content-ref url="../getting-started/installation.md" %}
[installation.md](../getting-started/installation.md)
{% endcontent-ref %}

{% content-ref url="../user-guide/configuration.md" %}
[configuration.md](../user-guide/configuration.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
