# Universal GPS Tracker Emulator - Professional Edition

![Version](https://img.shields.io/badge/version-5.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)
![Windows](https://img.shields.io/badge/Windows-3.13%2B-blue.svg)
![Linux](https://img.shields.io/badge/Linux-3.10--3.11-orange.svg)
![License](https://img.shields.io/badge/license-Commercial-blue.svg)
![Protocols](https://img.shields.io/badge/protocols-87-success.svg)

---

## 🎯 Two Versions Available

Choose the version that fits your needs:

| | 🖥️ Windows Local | 🌐 DigitalOcean Production |
|---|---|---|
| **Best For** | Development & Testing | Production & 24/7 Operation |
| **Platform** | Windows 10/11 | Ubuntu Linux |
| **Python** | 3.13+ | 3.10-3.11 |
| **Setup** | One-click `install.bat` | Automated `install.sh` |

{% hint style="info" %}
**Need help choosing?** See the complete [Version Comparison Guide](getting-started/version-comparison.md)
{% endhint %}

**Quick Links:**
- 📖 [Windows Local Installation Guide](getting-started/windows-local.md)
- 📖 [DigitalOcean Production Guide](getting-started/digitalocean-production.md)

---

## 🎬 See It In Action

{% hint style="info" %}
**Quick Demo**: Watch how easy it is to simulate GPS devices in under 2 minutes!
{% endhint %}

{% embed url="https://www.youtube.com/watch?v=_i59hUqqzRk" %}
Complete Tutorial: Creating and Managing GPS Devices
{% endembed %}

---

## 📸 Application Preview

### Dashboard Overview

![Dashboard Overview](/.gitbook/assets/screenshots/first_launch.png)

**Main dashboard showing:**
- Active protocols and devices
- Real-time status monitoring
- Quick device creation interface
- Performance metrics

---

### Multi-Device Management

![Multi-Device Management](/.gitbook/assets/screenshots/see_It_In_action_multi_devices_management.png)

**Manage multiple devices simultaneously:**
- Create up to 100+ devices
- Start/stop individual devices
- View real-time position updates
- Track multiple protocols at once

---

### Real-Time Map Visualization

<!-- PLACEHOLDER: Screenshot - Interactive map with device markers -->
![Real-Time Map](/.gitbook/assets/screenshots/see_It_In_action_real_time_map_visualization.png)

**Track devices on interactive maps:**
- Leaflet.js integration
- Real-time position updates
- Multiple device tracking
- Custom route visualization

---

## ✨ Key Features

### 🌍 87 GPS Protocols Supported

<!-- PLACEHOLDER: Graphic showing protocol logos/icons in a grid -->
```
┌─────────────────────────────────────────────────────────┐
│  TK103  │  GT06  │  Teltonika  │  GL200  │  OsmAnd    │
├─────────────────────────────────────────────────────────┤
│  H02    │  GPS103│  Meiligao   │  Suntech│  Fifotrack │
├─────────────────────────────────────────────────────────┤
│  Watch  │  AIS   │  Navigil    │  Castel │  And 72+   │
└─────────────────────────────────────────────────────────┘
```

Full protocol list: [View All 87 Protocols](protocols/all-protocols.md)

---

### 🎯 Modern Web Interface

<!-- PLACEHOLDER: Screenshot - Web interface highlighting key sections -->
![Web Interface](/.gitbook/assets/screenshots/preview.png)

**Professional dashboard featuring:**
- Bootstrap 5 responsive design
- Real-time WebSocket updates
- Interactive charts and metrics
- Mobile-friendly interface

---

### 🔌 Complete REST API

<!-- PLACEHOLDER: Screenshot - Swagger/OpenAPI documentation -->
<!-- TODO: Create screenshot of API documentation page -->
<!-- TEMPORARY PLACEHOLDER -->
```
📋 35+ API Endpoints Available
├── System Status (4 endpoints)
├── Device Management (8 endpoints)
├── Traccar Integration (5 endpoints)
├── Route Management (4 endpoints)
├── Vehicle Data (2 endpoints)
├── Commands & Control (4 endpoints)
├── Protocol Information (4 endpoints)
└── Legacy Endpoints (6 endpoints)
```

**Full API documentation:** [REST API Reference](api-reference/rest-api-detailed.md)

---

### 🚀 Multi-Device Simulation

![Device Creation](/.gitbook/assets/screenshots/see_It_In_action_multi_devices_simulation.png)

**Simulate multiple devices:**
- Up to 100+ concurrent devices
- Each device runs independently
- Realistic GPS behavior
- Custom routes and speeds

{% hint style="success" %}
**Performance**: Each device uses <1% CPU and ~20MB RAM
{% endhint %}

---

## 🎓 Who Is This For?

### 👨‍💻 Developers

Build and test GPS tracking applications without physical hardware:
- Integration testing for Traccar/GPS platforms
- API development and testing
- Load testing tracking servers
- Protocol implementation validation

### 🔬 QA Teams

Professional testing environment:
- Automated testing workflows
- Edge case simulation
- Performance benchmarking
- Multi-protocol compatibility testing

### 🎓 Educators & Students

Learning GPS protocols and tracking systems:
- Protocol analysis and reverse engineering
- Real-time data streaming
- Full source code included
- Educational documentation

---

## 📊 Technical Specifications

### Architecture

<!-- PLACEHOLDER: System architecture diagram -->
<!-- TODO: Create architecture diagram (see IMAGES_DOCUMENTATION.md) -->
<!-- TEMPORARY PLACEHOLDER -->
```
┌─────────────────────────────────────────────────────────┐
│                    Web Browser                          │
│              (Dashboard + Map View)                     │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/WebSocket
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Flask Application                          │
│   ┌──────────────────────────────────────────────┐     │
│   │  REST API (32 endpoints)  │  WebSocket       │     │
│   └──────────────────────────────────────────────┘     │
│   ┌──────────────────────────────────────────────┐     │
│   │  Device Manager  │  Protocol Registry        │     │
│   └──────────────────────────────────────────────┘     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           87 Protocol Implementations                   │
│  (GPS103, TK103, GT06, Teltonika, etc.)                │
└────────────────────┬────────────────────────────────────┘
                     │ TCP/UDP/HTTP
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Traccar Server / GPS Platform              │
└─────────────────────────────────────────────────────────┘
```

### Technology Stack by Version

#### 🖥️ Windows Local Version

- **Backend**: Python 3.13+, Flask 3.0.0, Flask-SocketIO 5.3.5
- **Async Mode**: Threading + Eventlet 0.33.3
- **Server**: Flask development server
- **Frontend**: HTML5, Bootstrap 5, jQuery, Leaflet.js 1.9.4
- **Database**: SQLite (vehicle attributes persistence)
- **API**: RESTful (35+ endpoints) + WebSocket (Socket.IO 4.6.0)
- **Protocols**: TCP/UDP/HTTP
- **Routing**: OSRM (Open Source Routing Machine)
- **Dependencies**: `requirements-windows.txt` (no gevent)

#### 🌐 DigitalOcean Production Version

- **Backend**: Python 3.10-3.11, Flask 3.0.0, Flask-SocketIO 5.3.5
- **Async Mode**: Gevent 24.2.1 (high-performance async I/O)
- **Server**: Gunicorn 21.2.0 (production WSGI server)
- **Frontend**: HTML5, Bootstrap 5, jQuery, Leaflet.js 1.9.4
- **Database**: SQLite (vehicle attributes persistence)
- **API**: RESTful (35+ endpoints) + WebSocket (Socket.IO 4.6.0)
- **Protocols**: TCP/UDP/HTTP
- **Routing**: OSRM (Open Source Routing Machine)
- **Service**: Systemd (auto-start on boot)
- **Dependencies**: `requirements.txt` (includes gevent)
- **Configuration**: YAML/JSON with hot-reload support (watchdog)

### Performance

<!-- PLACEHOLDER: Performance metrics chart/graph -->
<!-- TODO: Create performance chart -->
<!-- TEMPORARY PLACEHOLDER -->
| Metric | Value |
|--------|-------|
| **Max Concurrent Devices** | 100+ |
| **CPU per Device** | <1% |
| **Memory per Device** | ~20 MB |
| **Startup Time** | <5 seconds |
| **Position Update Rate** | 10-30 seconds (configurable) |

---

## 🎬 Quick Start Tutorial

<!-- PLACEHOLDER: Step-by-step visual guide -->

Choose your installation path based on your needs:

### 🖥️ Quick Start - Windows Local

**Perfect for:** Local development, testing, and Windows environments

**Quick setup:**
1. Extract ZIP → Run `install.bat` → Run `start.bat`
2. Access: http://localhost:5000

📖 **Full Installation Guide**: [Windows Local Installation](getting-started/windows-local.md)

---

### 🌐 Quick Start - DigitalOcean Production

**Perfect for:** Production servers, 24/7 operation, team access

**Quick setup:**
1. Upload to Linux server → Run `install.sh`
2. Service starts automatically
3. Access: http://YOUR_SERVER_IP:5000

📖 **Full Installation Guide**: [DigitalOcean Production Deployment](getting-started/digitalocean-production.md)

---

### Step 2: Create Your First Device

![Create Device](/.gitbook/assets/gifs/create_your_first_device.gif)

**Quick creation via Web UI** (both versions):
1. Open browser to dashboard (http://localhost:5000 or http://YOUR_SERVER_IP:5000)
2. Select protocol (e.g., TK103)
3. Choose device model
4. Select route (Paris, London, NYC, etc.)
5. Click "Add Device"

**Or use the API:**

![Create Device via API](/.gitbook/assets/gifs/create_device_api.gif)

{% tabs %}
{% tab title="Linux / macOS" %}
```bash
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "paris",
    "speed": 50.0
  }'
```
{% endtab %}

{% tab title="Windows (PowerShell)" %}
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
{% endtab %}

{% tab title="Windows (CMD)" %}
```cmd
curl -X POST http://localhost:5000/api/multidevice/devices ^
  -H "Content-Type: application/json" ^
  -d "{\"protocol\":\"tk103\",\"device_model\":\"TK103-2B\",\"route\":\"paris\",\"speed\":50.0}"
```
{% endtab %}

{% tab title="Python" %}
```python
import requests

response = requests.post(
    "http://localhost:5000/api/multidevice/devices",
    json={
        "protocol": "tk103",
        "device_model": "TK103-2B",
        "route": "paris",
        "speed": 50.0
    }
)
print(response.json())
```
{% endtab %}
{% endtabs %}

---

### Step 3: Start Simulation

![Device Running](/.gitbook/assets/gifs/start_simulation.gif)

**Monitor in real-time:**
- Current GPS position (lat/lon)
- Speed and heading
- Vehicle attributes (fuel, battery, odometer)
- Packets transmitted counter

---

### Step 4: View in Traccar

![Traccar Device View](/.gitbook/assets/screenshots/view_in_traccar.png)

**📍 Device visible in Traccar:**
- **Device ID:** TELTONIKA_FMB965_357938502775402601882000
- **Status:** Online
- **Position:** 48.8566°N, 2.3522°E
- **Speed:** 11.88 kn
- **Last update:** Just now

**Traccar integration is automatic!**
- Devices auto-created in Traccar
- Position updates synchronized
- Commands supported

{% content-ref url="user-guide/traccar-integration.md" %}
[traccar-integration.md](user-guide/traccar-integration.md)
{% endcontent-ref %}

---

## 🎯 Use Cases

### Integration Testing

<!-- PLACEHOLDER: Diagram - Testing workflow -->
```
Developer → GPS Emulator → Tracking Platform → Test Results
```

Test your GPS tracking platform without hardware:
- Protocol compatibility testing
- API endpoint validation
- Database schema verification
- Performance benchmarking

---

### Load Testing

<!-- PLACEHOLDER: Screenshot - 50+ devices running -->
<!-- TODO: Create screenshot showing many active devices -->

Simulate heavy traffic:
- 100+ concurrent devices
- Multiple protocols simultaneously
- Configurable update rates
- Resource monitoring

---

### Development & Debugging

<!-- PLACEHOLDER: Screenshot - Logs/debug view -->
<!-- TODO: Create screenshot of logging interface -->

Debug protocol implementations:
- View raw packet data
- Inspect protocol messages
- Monitor communication flow
- Test edge cases

---

## 📚 Documentation

{% hint style="info" %}
**Complete guides available** for every feature and protocol
{% endhint %}

### Getting Started
{% content-ref url="getting-started/installation.md" %}
[installation.md](getting-started/installation.md)
{% endcontent-ref %}

{% content-ref url="getting-started/quick-start.md" %}
[quick-start.md](getting-started/quick-start.md)
{% endcontent-ref %}

### User Guides
{% content-ref url="user-guide/creating-devices.md" %}
[creating-devices.md](user-guide/creating-devices.md)
{% endcontent-ref %}

{% content-ref url="user-guide/configuration.md" %}
[configuration.md](user-guide/configuration.md)
{% endcontent-ref %}

### API Documentation
{% content-ref url="api-reference/rest-api-detailed.md" %}
[rest-api-detailed.md](api-reference/rest-api-detailed.md)
{% endcontent-ref %}

### Protocols
{% content-ref url="protocols/all-protocols.md" %}
[all-protocols.md](protocols/all-protocols.md)
{% endcontent-ref %}

---

## ❓ FAQ

<details>
<summary><strong>Q: Do I need GPS hardware?</strong></summary>

**A:** No! This is a pure software emulator. No hardware needed at all. The emulator generates realistic GPS data and transmits it using actual GPS protocols.
</details>

<details>
<summary><strong>Q: Does it work with Traccar?</strong></summary>

**A:** Yes! Fully compatible with Traccar and most GPS tracking platforms. Devices are automatically created and synchronized. See our [Traccar Integration Guide](user-guide/traccar-integration.md).
</details>

<details>
<summary><strong>Q: Can I modify the code?</strong></summary>

**A:** Yes! Full source code included. You can customize protocols, add new features, and extend functionality. We encourage customization for your specific needs.
</details>

<details>
<summary><strong>Q: Does it run on Windows?</strong></summary>

**A:** Yes! Works on Windows, Linux, and macOS. We provide detailed installation guides for all platforms.
</details>

<details>
<summary><strong>Q: How many devices can I simulate?</strong></summary>

**A:** The system can handle 100+ concurrent devices depending on your hardware. Each device uses minimal resources (<1% CPU, ~20MB RAM).
</details>

<details>
<summary><strong>Q: Can I create custom routes?</strong></summary>

**A:** Yes! You can define custom GPS routes, use predefined city routes (Paris, London, NYC, etc.), or import routes from GPX files. See [Custom Routes Guide](user-guide/custom-routes.md).
</details>

{% content-ref url="support/faq.md" %}
[faq.md](support/faq.md)
{% endcontent-ref %}

---

## 🎁 What's Included

### ✅ Full Package Contents

- ✅ **Source Code**: Complete Python application
- ✅ **86 GPS Protocols**: Production-ready implementations
- ✅ **Web Dashboard**: Modern, responsive interface
- ✅ **REST API**: 32+ endpoints with Swagger docs
- ✅ **Documentation**: Comprehensive guides (200+ pages)
- ✅ **Example Routes**: 8 predefined city routes
- ✅ **Test Suite**: Unit and integration tests
- ✅ **Configuration**: YAML-based configuration system
- ✅ **License System**: Demo and full license support
- ✅ **Updates**: Free updates for purchased version

---

## 🚀 Get Started Today!

Ready to revolutionize your GPS testing workflow?

{% hint style="success" %}
**No GPS hardware required • Works with Traccar • 87+ protocols • Full source code • Two versions available**
{% endhint %}

### ⚙️ Which Version Should You Choose?

| Question | Answer | Recommended Version |
|----------|--------|---------------------|
| Testing on Windows PC? | Local development | 🖥️ [Windows Local](getting-started/windows-local.md) |
| Need Python 3.13 support? | Latest Python version | 🖥️ [Windows Local](getting-started/windows-local.md) |
| Learning GPS protocols? | Simple setup | 🖥️ [Windows Local](getting-started/windows-local.md) |
| Deploying for production? | Cloud server | 🌐 [DigitalOcean Production](getting-started/digitalocean-production.md) |
| Need 24/7 availability? | Auto-start service | 🌐 [DigitalOcean Production](getting-started/digitalocean-production.md) |
| Maximum performance? | Gevent async I/O | 🌐 [DigitalOcean Production](getting-started/digitalocean-production.md) |
| 100+ concurrent devices? | Production server | 🌐 [DigitalOcean Production](getting-started/digitalocean-production.md) |

### Quick Steps:

#### 🖥️ For Windows Local:

1. **Extract** the ZIP to `/local/` folder
2. **Run** `install.bat` for automatic setup
3. **Start** with `start.bat`
4. **Access** http://localhost:5000

{% content-ref url="getting-started/windows-local.md" %}
[windows-local.md](getting-started/windows-local.md)
{% endcontent-ref %}

#### 🌐 For DigitalOcean Production:

1. **Create** Ubuntu droplet on DigitalOcean
2. **Upload** files to `/opt/gps-emulator/`
3. **Run** `install.sh` for automatic setup
4. **Access** http://YOUR_SERVER_IP:5000

{% content-ref url="getting-started/digitalocean-production.md" %}
[digitalocean-production.md](getting-started/digitalocean-production.md)
{% endcontent-ref %}

---

{% content-ref url="getting-started/quick-start.md" %}
[quick-start.md](getting-started/quick-start.md)
{% endcontent-ref %}

---

## 💬 Support & Community

### Need Help?

{% content-ref url="support/troubleshooting.md" %}
[troubleshooting.md](support/troubleshooting.md)
{% endcontent-ref %}

{% content-ref url="support/contact.md" %}
[contact.md](support/contact.md)
{% endcontent-ref %}

### Stay Updated

- 📧 Email support included
- 📖 Regular documentation updates
- 🐛 Bug fixes and improvements
- ✨ New features and protocols

---

## 📋 System Requirements

**Quick Reference:**

| Component | Windows Local | DigitalOcean Production |
|-----------|---------------|-------------------------|
| **OS** | Windows 10/11 | Ubuntu 22.04+ |
| **Python** | 3.13+ | 3.10 - 3.11 |
| **RAM** | 2-4 GB | 2-4 GB |
| **Storage** | 500 MB - 1 GB | 10-20 GB |

{% hint style="info" %}
**Need detailed requirements?** See [Complete System Requirements Guide](getting-started/system-requirements.md)
{% endhint %}

{% content-ref url="getting-started/system-requirements.md" %}
[system-requirements.md](getting-started/system-requirements.md)
{% endcontent-ref %}

---

## 📜 License

This software is available in multiple versions:

**Available Versions:**
- **Demo Version**: Limited devices for testing and evaluation
- **Commercial Unlimited Version**: Unlimited devices with all features included

**Configuration:**
- License type and device limits are configured in the `.env` file
- Commercial version: `LICENSE_TYPE=COMMERCIAL` with `MAX_DEVICES=-1` (unlimited)

{% content-ref url="resources/license.md" %}
[license.md](resources/license.md)
{% endcontent-ref %}

---

## 📊 Version History

### Version 5.0 (Current - November 2025)
- ✅ 87 GPS protocols supported
- ✅ Modern web interface (Bootstrap 5)
- ✅ REST API (35+ endpoints)
- ✅ Multi-device simulation (100+ devices)
- ✅ Real-time WebSocket updates (Socket.IO 4.6.0)
- ✅ Vehicle attributes database (SQLite)
- ✅ OSRM realistic routing engine
- ✅ Traccar auto-sync integration
- ✅ Windows 10/11 + Ubuntu deployment
- ✅ Python 3.13 support
- ✅ Commercial unlimited version
- ✅ Advanced configuration system with hot-reload
- ✅ Eventlet 0.33.3 async server

{% content-ref url="resources/changelog.md" %}
[changelog.md](resources/changelog.md)
{% endcontent-ref %}

---

## 🎯 Coming Soon

- 🔄 PostgreSQL support
- 🌐 MQTT protocol support
- 📱 Mobile app for monitoring
- 🔌 More protocol plugins
- 📊 Advanced analytics dashboard

---

*Last updated: November 2025 | Version: 2.0.0*

**Questions? Contact us anytime!**

{% content-ref url="support/contact.md" %}
[contact.md](support/contact.md)
{% endcontent-ref %}
