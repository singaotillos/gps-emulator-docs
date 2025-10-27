# Creating Devices

Learn how to create and manage GPS devices in the emulator.

---

## Overview

The GPS Emulator allows you to create **virtual GPS tracking devices** that simulate real hardware. This guide covers all methods of creating and managing devices.

{% hint style="success" %}
**Quick Start:** Create a device in 30 seconds using the web interface!
{% endhint %}

---

## Methods to Create Devices

There are three ways to create devices:

1. **Web Interface** - Visual, user-friendly (recommended for beginners)
2. **REST API** - Programmatic, automation-friendly
3. **Configuration File** - Bulk creation, pre-configuration

---

## Method 1: Web Interface

### Step-by-Step Guide

**1. Open Web Dashboard**

Navigate to:
```
http://localhost:5000
```

**2. Click "Create New Device"**

Find the button on the dashboard homepage.

**3. Fill Device Information**

{% tabs %}
{% tab title="Required Fields" %}
**Protocol:** Select from dropdown
- TK103 (recommended for first device)
- GT06
- Teltonika
- OsmAnd
- ... 82 more protocols

**Device Model:** Enter device model
- Example: TK103-2B
- Example: GT06N
- Example: FMB920
{% endtab %}

{% tab title="Optional Fields" %}
**Device ID:** Unique identifier
- Leave empty for auto-generation
- Or enter custom ID (IMEI format for most protocols)

**Route:** Predefined route
- Paris (default)
- London
- New York
- Tokyo
- Berlin

**Speed:** Vehicle speed in km/h
- Default: 50 km/h
- Range: 0-120 km/h

**Description:** Human-readable description
- Example: "Test vehicle 1"
- Example: "Fleet truck #45"
{% endtab %}
{% endtabs %}

**4. Click "Create Device"**

Device is created and appears in device list.

**5. Start Device**

Click "Start" button next to the device to begin simulation.

{% hint style="info" %}
**Device ID Format:** Most protocols use IMEI format (15 digits). Leave empty for auto-generation.
{% endhint %}

---

### Video Tutorial

{% hint style="success" %}
**Watch:** Creating your first device (2 minutes)
{% endhint %}

---

## Method 2: REST API

### Basic Device Creation

**Request:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "device_model": "TK103-2B",
       "route": "paris"
     }'
```

**Response:**
```json
{
  "success": true,
  "device": {
    "device_id": "dev_tk103_357938506404024",
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "unique_id": "357938506404024",
    "route": "paris",
    "status": "stopped",
    "created_at": "2025-10-25T14:30:00Z"
  },
  "message": "Device created successfully"
}
```

---

### Advanced Device Creation

**With Custom Configuration:**

```bash
curl -X POST http://localhost:5000/api/multidevice/devices \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "device_model": "TK103-2B",
       "device_id": "357938506404024",
       "route": "paris",
       "speed": 80.0,
       "update_interval": 5.0,
       "description": "High-speed test vehicle"
     }'
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `protocol` | string | ✅ Yes | Protocol name (see [Protocols](../protocols/overview.md)) |
| `device_model` | string | ✅ Yes | Device model name |
| `device_id` | string | ❌ No | Unique identifier (auto-generated if omitted) |
| `route` | string | ❌ No | Route name: `paris`, `london`, `newyork`, `tokyo`, `berlin` |
| `speed` | float | ❌ No | Speed in km/h (default: 50.0) |
| `update_interval` | float | ❌ No | Seconds between updates (default: 10.0) |
| `description` | string | ❌ No | Human-readable description |

---

### Python Example

```python
import requests

BASE_URL = "http://localhost:5000"

def create_device(protocol, model, route="paris", speed=50.0):
    """Create a new GPS device"""

    device_data = {
        "protocol": protocol,
        "device_model": model,
        "route": route,
        "speed": speed
    }

    response = requests.post(
        f"{BASE_URL}/api/multidevice/devices",
        json=device_data
    )

    if response.status_code == 201:
        device = response.json()["device"]
        print(f"✅ Created: {device['device_id']}")
        return device["device_id"]
    else:
        print(f"❌ Error: {response.json()['error']}")
        return None

# Create device
device_id = create_device("tk103", "TK103-2B", route="london", speed=60.0)

# Start device
if device_id:
    start_response = requests.post(
        f"{BASE_URL}/api/multidevice/devices/{device_id}/start"
    )
    print(f"✅ Started: {start_response.json()['message']}")
```

---

### JavaScript Example

```javascript
const axios = require('axios');

const BASE_URL = 'http://localhost:5000';

async function createDevice(protocol, model, route = 'paris', speed = 50.0) {
  try {
    const response = await axios.post(
      `${BASE_URL}/api/multidevice/devices`,
      {
        protocol: protocol,
        device_model: model,
        route: route,
        speed: speed
      }
    );

    const device = response.data.device;
    console.log(`✅ Created: ${device.device_id}`);
    return device.device_id;

  } catch (error) {
    console.error('❌ Error:', error.response?.data?.error);
    return null;
  }
}

// Create device
createDevice('tk103', 'TK103-2B', 'london', 60.0)
  .then(deviceId => {
    if (deviceId) {
      // Start device
      return axios.post(`${BASE_URL}/api/multidevice/devices/${deviceId}/start`);
    }
  })
  .then(response => {
    console.log('✅ Started:', response.data.message);
  });
```

---

## Method 3: Bulk Creation

### Create Multiple Devices

**Python Script:**

```python
import requests
import concurrent.futures

BASE_URL = "http://localhost:5000"

# Define devices to create
devices_config = [
    {"protocol": "tk103", "model": "TK103-2B", "route": "paris"},
    {"protocol": "gt06", "model": "GT06N", "route": "london"},
    {"protocol": "teltonika", "model": "FMB920", "route": "berlin"},
    {"protocol": "osmand", "model": "Mobile", "route": "tokyo"},
    {"protocol": "gps103", "model": "GPS103", "route": "newyork"}
]

def create_single_device(config):
    """Create a single device"""
    device_data = {
        "protocol": config["protocol"],
        "device_model": config["model"],
        "route": config["route"]
    }

    response = requests.post(
        f"{BASE_URL}/api/multidevice/devices",
        json=device_data
    )

    if response.status_code == 201:
        device = response.json()["device"]
        return {"success": True, "device_id": device["device_id"]}
    else:
        return {"success": False, "error": response.json()["error"]}

# Create devices in parallel
print("Creating devices...")
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(create_single_device, config)
               for config in devices_config]

    results = [f.result() for f in concurrent.futures.as_completed(futures)]

# Show results
successful = [r for r in results if r["success"]]
print(f"\n✅ Created {len(successful)}/{len(devices_config)} devices")

# Start all devices
print("\nStarting devices...")
for result in successful:
    device_id = result["device_id"]
    response = requests.post(
        f"{BASE_URL}/api/multidevice/devices/{device_id}/start"
    )
    print(f"  ✅ Started: {device_id}")

print("\n🎉 All devices running!")
```

---

## Device Configuration

### Available Routes

The emulator includes predefined routes for major cities:

| Route | City | Distance | Points | Description |
|-------|------|----------|--------|-------------|
| `paris` | Paris, France | 12.5 km | 4 | Tour of central Paris |
| `london` | London, UK | 15.0 km | 4 | London city tour |
| `berlin` | Berlin, Germany | 18.0 km | 4 | Berlin tour |
| `tokyo` | Tokyo, Japan | 20.0 km | 4 | Tokyo tour |
| `newyork` | New York, USA | 22.0 km | 4 | NYC tour |

{% hint style="info" %}
**Custom Routes:** You can also create custom routes via API. See [Custom Routes](custom-routes.md)
{% endhint %}

---

### Protocol Selection

{% hint style="success" %}
**Recommended for beginners:** Start with TK103 - it's the most widely compatible protocol
{% endhint %}

**Popular protocols:**

| Protocol | Best For | Difficulty | Traccar Support |
|----------|----------|------------|-----------------|
| **TK103** | First-time users | ⭐ Easy | ✅ Full |
| **GT06** | Common devices | ⭐ Easy | ✅ Full |
| **OsmAnd** | Mobile apps | ⭐ Easy | ✅ Full |
| **Teltonika** | Professional fleet | ⭐⭐ Medium | ✅ Full |
| **GPS103** | Text-based protocol | ⭐ Easy | ✅ Full |

{% content-ref url="../protocols/overview.md" %}
[overview.md](../protocols/overview.md)
{% endcontent-ref %}

---

## Device Management

### Starting Devices

{% tabs %}
{% tab title="Web Interface" %}
1. Go to dashboard
2. Find device in list
3. Click "Start" button
4. Device status changes to "running"
{% endtab %}

{% tab title="API" %}
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
```
{% endtab %}

{% tab title="Python" %}
```python
import requests

response = requests.post(
    "http://localhost:5000/api/multidevice/devices/DEVICE_ID/start"
)
print(response.json()["message"])
```
{% endtab %}
{% endtabs %}

---

### Stopping Devices

{% tabs %}
{% tab title="Web Interface" %}
1. Go to dashboard
2. Find device in list
3. Click "Stop" button
4. Device status changes to "stopped"
{% endtab %}

{% tab title="API" %}
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop
```
{% endtab %}

{% tab title="Python" %}
```python
import requests

response = requests.post(
    "http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop"
)
print(response.json()["message"])
```
{% endtab %}
{% endtabs %}

---

### Deleting Devices

{% hint style="warning" %}
**Warning:** Devices must be stopped before deletion
{% endhint %}

{% tabs %}
{% tab title="Web Interface" %}
1. Stop device first
2. Click "Delete" button
3. Confirm deletion
{% endtab %}

{% tab title="API" %}
```bash
# Stop device first
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop

# Then delete
curl -X DELETE http://localhost:5000/api/multidevice/devices/DEVICE_ID
```
{% endtab %}
{% endtabs %}

---

## Monitoring Devices

### View Device Status

**Get all devices:**
```bash
curl http://localhost:5000/api/multidevice/devices
```

**Get specific device:**
```bash
curl http://localhost:5000/api/multidevice/devices/DEVICE_ID
```

**Response includes:**
- Current position (lat, lon, speed, altitude)
- Vehicle data (ignition, fuel, battery)
- Statistics (packets sent, uptime, distance)
- Configuration

---

### Real-Time Updates

**WebSocket connection for live updates:**

```javascript
const io = require('socket.io-client');
const socket = io('http://localhost:5000');

socket.on('device_update', (data) => {
  console.log(`Device ${data.device_id}:`);
  console.log(`  Position: ${data.position.latitude}, ${data.position.longitude}`);
  console.log(`  Speed: ${data.position.speed} km/h`);
});

socket.on('device_started', (data) => {
  console.log(`Device started: ${data.device_id}`);
});

socket.on('device_stopped', (data) => {
  console.log(`Device stopped: ${data.device_id}`);
});
```

{% content-ref url="../api-reference/websocket.md" %}
[websocket.md](../api-reference/websocket.md)
{% endcontent-ref %}

---

## Best Practices

### Device Naming

{% hint style="success" %}
**Good naming conventions:**
{% endhint %}

- Use descriptive names: "Delivery Truck 1", "Sales Rep Car"
- Include protocol in description: "TK103 Test Device"
- Use consistent patterns for bulk devices

### Performance Tips

1. **Don't create all devices at once**
   - Create in batches of 10-20
   - Wait between batches

2. **Start devices gradually**
   - Start 5-10 devices at a time
   - Monitor CPU/memory usage

3. **Use appropriate update intervals**
   - Fast testing: 5 seconds
   - Normal: 10 seconds
   - Production: 30 seconds

### Resource Management

**Device limits by edition:**

| Edition | Recommended | Maximum |
|---------|-------------|---------|
| Community | 5 devices | 5 |
| Regular | 50 devices | 50 |
| Extended | 100+ devices | Unlimited |

{% hint style="info" %}
**Memory usage:** Each device uses approximately 20MB RAM
{% endhint %}

---

## Troubleshooting

### Device Creation Fails

**Error:** `Protocol invalid`
- **Solution:** Check protocol name is correct
- **List protocols:** `GET /api/protocols`

**Error:** `Device limit reached`
- **Solution:** Stop/delete unused devices or upgrade license

**Error:** `Device already exists`
- **Solution:** Use different device ID or delete existing device

### Device Won't Start

**Check:**
1. ✅ Device status = "stopped"?
2. ✅ Protocol port configured correctly?
3. ✅ No device limit reached?
4. ✅ Application has network access?

{% content-ref url="../support/troubleshooting.md" %}
[troubleshooting.md](../support/troubleshooting.md)
{% endcontent-ref %}

---

## Next Steps

{% content-ref url="traccar-integration.md" %}
[traccar-integration.md](traccar-integration.md)
{% endcontent-ref %}

{% content-ref url="custom-routes.md" %}
[custom-routes.md](custom-routes.md)
{% endcontent-ref %}

{% content-ref url="../api-reference/rest-api.md" %}
[rest-api.md](../api-reference/rest-api.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
