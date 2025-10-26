# Quick Start

Get your first GPS device running in under 5 minutes!

---

## Prerequisites

Before starting, ensure you have:

* ✅ Installed the emulator ([Installation Guide](installation.md))
* ✅ Emulator running at http://localhost:5000
* ✅ (Optional) Traccar server running

---

## Step 1: Access the Dashboard

Open your browser and navigate to:

```
http://localhost:5000
```

You should see the **Universal GPS Tracker Emulator** dashboard.

{% hint style="success" %}
**Tip:** Bookmark this URL for quick access!
{% endhint %}

---

## Step 2: Create Your First Device

### Method 1: Using the Web Interface

1. **Click** on the "By Protocol" tab
2. **Select** a protocol from the dropdown (e.g., `TK103`)
3. **Select** a device model (e.g., `TK103-2B`)
4. **Choose** a route (e.g., `Paris`)
5. **Click** the green "+ Add" button

{% hint style="info" %}
The Device ID is auto-generated if you leave it empty.
{% endhint %}

### Method 2: Using the API

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

**Response:**
```json
{
  "success": true,
  "device": {
    "device_id": "dev_tk103_357938506404024",
    "protocol": "tk103",
    "status": "stopped"
  }
}
```

---

## Step 3: Start the Device

### Using Web Interface

1. Find your device in the "Active Protocols" section
2. Click the green **Play** button (▶️)
3. Watch the status change to "1 active"

### Using API

```bash
curl -X POST http://localhost:5000/api/multidevice/devices/dev_tk103_001/start
```

{% hint style="success" %}
**Device Started!** Your virtual GPS tracker is now sending data.
{% endhint %}

---

## Step 4: View in Traccar (Optional)

If you have Traccar running:

1. Open Traccar web interface (usually http://localhost:8082)
2. Login with your credentials
3. You should see your device online with GPS data

{% hint style="warning" %}
**Traccar Not Configured?** See [Traccar Integration](../user-guide/traccar-integration.md)
{% endhint %}

---

## Step 5: Monitor Real-time Data

Back in the emulator dashboard, you can see:

* **Current Position**: Latitude, Longitude, Speed
* **Vehicle Data**: Fuel (%), Battery (%), Odometer
* **Status**: Active, Stopped, or Error
* **Packets Sent**: Number of data packets transmitted

The dashboard updates automatically via WebSocket!

---

## Common First-Time Actions

### View All Devices

```bash
curl http://localhost:5000/api/multidevice/devices
```

### Stop a Device

**Web Interface:**
- Click the yellow **Stop** button (⏸️)

**API:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/dev_tk103_001/stop
```

### Delete a Device

**Web Interface:**
- Click the red **Delete** button (🗑️)

**API:**
```bash
curl -X DELETE http://localhost:5000/api/multidevice/devices/dev_tk103_001
```

### Configure Device Settings

**Web Interface:**
- Click the **Settings** button (⚙️)
- Modify speed, update interval, etc.
- Click "Save"

---

## Quick Examples

### Example 1: Create 3 Devices with Different Protocols

```bash
# TK103 device
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{"protocol": "tk103", "device_model": "TK103-2B", "route": "paris"}'

# GT06 device
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{"protocol": "gt06", "device_model": "GT06N", "route": "london"}'

# Teltonika device
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{"protocol": "teltonika", "device_model": "FMB920", "route": "berlin"}'
```

### Example 2: Start All Devices

Use the web interface "Refresh" button to see all devices, then start them individually.

### Example 3: Monitor with Python

```python
import requests
import time

BASE_URL = "http://localhost:5000"

# Create device
device_data = {
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "paris"
}
response = requests.post(f"{BASE_URL}/api/multidevice/devices", json=device_data)
device_id = response.json()["device"]["device_id"]

# Start device
requests.post(f"{BASE_URL}/api/multidevice/devices/{device_id}/start")

# Monitor for 60 seconds
for i in range(6):
    time.sleep(10)
    response = requests.get(f"{BASE_URL}/api/multidevice/devices/{device_id}")
    pos = response.json()["device"]["current_position"]
    print(f"Position: {pos['latitude']:.6f}, {pos['longitude']:.6f} @ {pos['speed']} km/h")

# Stop device
requests.post(f"{BASE_URL}/api/multidevice/devices/{device_id}/stop")
```

---

## Troubleshooting

### Device Won't Start

**Check:**
1. Is the protocol server enabled in `config.yaml`?
2. Are you within device limits? (CE: 5 devices, EE: unlimited)
3. Is the port already in use?

**Solution:**
```bash
# Check logs
tail -f emulator.log

# Check status
curl http://localhost:5000/api/status
```

### Can't See Device in Traccar

**Check:**
1. Is Traccar running? `curl http://localhost:8082`
2. Is auto-create enabled in configuration?
3. Does the Device ID match in both systems?

**Solution:**
See [Traccar Integration](../user-guide/traccar-integration.md)

### Dashboard Not Loading

**Check:**
1. Is the emulator running? `python app.py`
2. Is port 5000 free? `netstat -an | grep 5000`
3. Is firewall blocking access?

---

## What's Next?

Now that you have your first device running, explore more features:

{% content-ref url="../user-guide/creating-devices.md" %}
[creating-devices.md](../user-guide/creating-devices.md)
{% endcontent-ref %}

{% content-ref url="../user-guide/routes-and-tracking.md" %}
[routes-and-tracking.md](../user-guide/routes-and-tracking.md)
{% endcontent-ref %}

{% content-ref url="../protocols/popular-protocols.md" %}
[popular-protocols.md](../protocols/popular-protocols.md)
{% endcontent-ref %}

{% content-ref url="../api-reference/rest-api.md" %}
[rest-api.md](../api-reference/rest-api.md)
{% endcontent-ref %}

---

## Video Tutorial

{% hint style="info" %}
**Coming Soon:** Video tutorial showing the complete quick start process!
{% endhint %}

---

## Feedback

Found this guide helpful? Have suggestions?

{% content-ref url="../support/contact.md" %}
[contact.md](../support/contact.md)
{% endcontent-ref %}
