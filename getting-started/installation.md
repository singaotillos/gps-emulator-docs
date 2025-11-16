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

## Need More Details?

For detailed comparison of both versions, see:

{% content-ref url="version-comparison.md" %}
[version-comparison.md](version-comparison.md)
{% endcontent-ref %}

---

## Table of Contents

- [Quick Installation](#quick-installation)
- [Post-Installation](#post-installation)
- [Next Steps](#next-steps)

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

{% hint style="success" %}
**Installation complete!** Continue to [Post-Installation](#post-installation) for next steps.
{% endhint %}

**Need detailed installation steps?**

- **Windows Users:** See the complete [Windows Local Installation Guide](windows-local.md)
- **Linux/Server Users:** See the complete [DigitalOcean Production Guide](digitalocean-production.md)

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

Having issues during installation? See our comprehensive troubleshooting guide:

{% content-ref url="../support/troubleshooting.md" %}
[troubleshooting.md](../support/troubleshooting.md)
{% endcontent-ref %}

**Common issues:**
- **Python not found** → [Solution](../support/troubleshooting.md#python-not-found)
- **Port already in use** → [Solution](../support/troubleshooting.md#port-already-in-use)
- **Module not found** → [Solution](../support/troubleshooting.md#module-not-found)
- **Gevent build fails** → [Solution](../support/troubleshooting.md#gevent-build-fails-python-313)
- **Permission denied** → [Solution](../support/troubleshooting.md#permission-denied)

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
- Email: singaotillos@gmail.com
- Response time: 24-48 hours

---

*Installation guide updated: October 2025*
