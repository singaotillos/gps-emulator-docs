# REST API Reference

---

## Overview

The Universal GPS Tracker Emulator provides a comprehensive REST API for:

- Creating and managing virtual GPS devices
- Starting/stopping simulations
- Configuring routes and behavior
- Integrating with Traccar
- Real-time monitoring via WebSocket

**API Version:** v2
**Protocol:** HTTP/HTTPS
**Data Format:** JSON
**WebSocket:** Socket.IO v4

---

## Authentication

### API Key Authentication

By default, authentication is **disabled**. Enable in configuration:

{% tabs %}
{% tab title=".env Configuration" %}
```bash
# .env
API_ENABLE_AUTHENTICATION=true
API_KEY=your-secret-api-key-here
```
{% endtab %}

{% tab title="Generate Key" %}
```bash
# Generate strong random key
openssl rand -hex 32
```
{% endtab %}

{% tab title="Usage" %}
```bash
# Header method (recommended)
curl -H "Authorization: Bearer YOUR_API_KEY" \
     http://localhost:5000/api/status

# Query parameter (less secure)
curl "http://localhost:5000/api/status?api_key=YOUR_API_KEY"
```
{% endtab %}
{% endtabs %}

### Python Example

```python
import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.get("http://localhost:5000/api/status", headers=headers)
print(response.json())
```

{% hint style="warning" %}
**Production:** Always enable authentication in production environments!
{% endhint %}

---

## Base URL

**Local Development:**
```
http://localhost:5000
```

**Production:**
```
http://your-server-ip:5000
https://gps-emulator.example.com
```

**All API endpoints are prefixed with `/api`:**
```
http://localhost:5000/api/multidevice/devices
http://localhost:5000/api/protocols
http://localhost:5000/api/status
```

---

## Response Format

All API responses use JSON format with consistent structure.

### Success Response

```json
{
  "success": true,
  "data": {
    "device_id": "dev_abc123",
    "status": "running"
  },
  "message": "Device started successfully"
}
```

### Error Response

```json
{
  "success": false,
  "error": "Device not found",
  "code": "DEVICE_NOT_FOUND",
  "details": "No device exists with ID: dev_xyz789"
}
```

### List Response

```json
{
  "success": true,
  "data": [...],
  "count": 15,
  "total": 15
}
```

---

## Error Codes

### HTTP Status Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Successful request |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required/failed |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Resource already exists |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

### Custom Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| `DEVICE_NOT_FOUND` | Device ID doesn't exist | Check device ID |
| `DEVICE_ALREADY_EXISTS` | Device ID already in use | Use different ID or delete existing |
| `PROTOCOL_INVALID` | Invalid protocol name | See `/api/protocols` for list |
| `DEVICE_LIMIT_REACHED` | Max devices reached | Stop/delete devices or upgrade license |
| `VALIDATION_ERROR` | Invalid request parameters | Check required fields |
| `TRACCAR_CONNECTION_ERROR` | Can't connect to Traccar | Verify Traccar is running |

---

## Rate Limiting

Rate limiting protects the API from abuse.

**Default Limits:**
- 100 requests per minute per IP
- Applies when `API_RATE_LIMITING=true`

**Response Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1635350400
```

**Rate Limit Exceeded:**
```json
HTTP/1.1 429 Too Many Requests
{
  "success": false,
  "error": "Rate limit exceeded",
  "retry_after": 60
}
```

{% hint style="info" %}
Disable rate limiting for development: `API_RATE_LIMITING=false`
{% endhint %}

---

## System Endpoints

### GET /api/status

Get system status and all devices overview.

**Request:**
```bash
curl http://localhost:5000/api/status
```

**Response:**
```json
{
  "success": true,
  "system": {
    "uptime": "2h 15m 30s",
    "cpu_percent": 15.2,
    "memory_percent": 45.8,
    "devices_running": 5,
    "devices_total": 12
  },
  "devices": [
    {
      "device_id": "dev_tk103_001",
      "protocol": "tk103",
      "status": "running",
      "current_position": {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "speed": 45.0,
        "altitude": 35.0
      },
      "last_update": "2025-10-25T14:32:15Z"
    }
  ]
}
```

---

### GET /api/protocols

List all available GPS protocols.

**Request:**
```bash
curl http://localhost:5000/api/protocols
```

**Response:**
```json
{
  "success": true,
  "protocols": [
    {
      "name": "tk103",
      "display_name": "TK103",
      "port": 5002,
      "type": "tcp",
      "manufacturer": "Xexun",
      "description": "TK103 GPS tracker protocol",
      "popular": true
    }
  ],
  "count": 86,
  "categories": {
    "popular": ["tk103", "gt06", "teltonika", "osmand"],
    "binary": ["tk103", "gt06", "teltonika"],
    "text": ["gps103", "h02"],
    "http": ["osmand", "gpsgate"]
  }
}
```

---

## Device Management

### POST /api/multidevice/devices

Create a new GPS device.

**Request:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "device_model": "TK103-2B",
       "device_id": "357938506404024",
       "route": "paris",
       "speed": 50.0
     }'
```

**Request Body:**
```json
{
  "protocol": "tk103",           // Required: Protocol name
  "device_model": "TK103-2B",    // Required: Device model
  "device_id": "357938506404024", // Optional: Auto-generated if omitted
  "route": "paris",              // Optional: paris, london, berlin, tokyo, newyork
  "speed": 50.0,                 // Optional: Speed in km/h (default: 50.0)
  "update_interval": 10.0,       // Optional: Seconds between updates
  "description": "Test vehicle"  // Optional: Description
}
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

{% hint style="success" %}
**Tip:** Leave `device_id` empty for auto-generation of unique IDs
{% endhint %}

---

### GET /api/multidevice/devices

Get list of all devices.

**Request:**
```bash
curl http://localhost:5000/api/multidevice/devices
```

**Query Parameters:**
- `status` - Filter by status: `running`, `stopped`, `error`
- `protocol` - Filter by protocol name
- `limit` - Max results (default: 100)
- `offset` - Pagination offset (default: 0)

**Example with filters:**
```bash
curl "http://localhost:5000/api/multidevice/devices?status=running&protocol=tk103"
```

**Response:**
```json
{
  "success": true,
  "devices": [
    {
      "device_id": "dev_tk103_001",
      "protocol": "tk103",
      "device_model": "TK103-2B",
      "unique_id": "357938506404024",
      "status": "running",
      "route": "paris",
      "current_position": {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "speed": 45.0,
        "altitude": 35.0,
        "heading": 90.0
      },
      "stats": {
        "packets_sent": 1523,
        "uptime_seconds": 15230,
        "distance_km": 125.5
      }
    }
  ],
  "count": 12,
  "total": 12
}
```

---

### GET /api/multidevice/devices/:device_id

Get details of specific device.

**Request:**
```bash
curl http://localhost:5000/api/multidevice/devices/dev_tk103_001
```

**Response:**
```json
{
  "success": true,
  "device": {
    "device_id": "dev_tk103_001",
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "unique_id": "357938506404024",
    "status": "running",
    "route": "paris",
    "current_position": {
      "latitude": 48.8566,
      "longitude": 2.3522,
      "speed": 45.0,
      "altitude": 35.0,
      "heading": 90.0,
      "timestamp": "2025-10-25T14:32:15Z"
    },
    "vehicle_data": {
      "ignition": true,
      "fuel": 75.5,
      "battery": 12.6,
      "temperature": 22.0,
      "odometer": 125500.0
    },
    "stats": {
      "packets_sent": 1523,
      "packets_failed": 2,
      "uptime_seconds": 15230,
      "distance_km": 125.5,
      "avg_speed": 48.2
    }
  }
}
```

---

### DELETE /api/multidevice/devices/:device_id

Delete a device.

**Request:**
```bash
curl -X DELETE http://localhost:5000/api/multidevice/devices/dev_tk103_001
```

**Response:**
```json
{
  "success": true,
  "message": "Device deleted successfully"
}
```

{% hint style="warning" %}
**Note:** Device must be stopped before deletion. Returns 400 if running.
{% endhint %}

---

## Device Control

### POST /api/multidevice/devices/:device_id/start

Start device simulation.

**Request:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/dev_tk103_001/start
```

**Response:**
```json
{
  "success": true,
  "device": {
    "device_id": "dev_tk103_001",
    "status": "running",
    "started_at": "2025-10-25T14:35:00Z"
  },
  "message": "Device started successfully"
}
```

**Error Response (Device Limit):**
```json
{
  "success": false,
  "error": "Device limit reached",
  "details": "Community Edition limited to 5 devices. Upgrade to Enterprise."
}
```

---

### POST /api/multidevice/devices/:device_id/stop

Stop device simulation.

**Request:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/dev_tk103_001/stop
```

**Response:**
```json
{
  "success": true,
  "device": {
    "device_id": "dev_tk103_001",
    "status": "stopped",
    "stopped_at": "2025-10-25T14:40:00Z",
    "final_stats": {
      "packets_sent": 1523,
      "uptime_seconds": 15230,
      "distance_km": 125.5
    }
  },
  "message": "Device stopped successfully"
}
```

---

## Code Examples

### Python - Create and Start Device

```python
import requests
import time

BASE_URL = "http://localhost:5000"

# 1. Create device
device_data = {
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "paris",
    "speed": 60.0
}

response = requests.post(f"{BASE_URL}/api/multidevice/devices", json=device_data)
device = response.json()
device_id = device["device"]["device_id"]
print(f"Created device: {device_id}")

# 2. Start device
response = requests.post(f"{BASE_URL}/api/multidevice/devices/{device_id}/start")
print(f"Started: {response.json()['message']}")

# 3. Monitor for 60 seconds
for i in range(6):
    time.sleep(10)
    response = requests.get(f"{BASE_URL}/api/multidevice/devices/{device_id}")
    device = response.json()["device"]
    pos = device["current_position"]
    print(f"Position: {pos['latitude']:.6f}, {pos['longitude']:.6f} @ {pos['speed']} km/h")

# 4. Stop device
response = requests.post(f"{BASE_URL}/api/multidevice/devices/{device_id}/stop")
print(f"Stopped: {response.json()['message']}")
```

---

### JavaScript - Real-Time WebSocket

```javascript
const io = require('socket.io-client');

const socket = io('http://localhost:5000');

socket.on('connect', () => {
  console.log('Connected to GPS Emulator');
});

socket.on('device_update', (data) => {
  console.log(`Device ${data.device_id}:`,
    `Lat: ${data.position.latitude}, ` +
    `Lng: ${data.position.longitude}, ` +
    `Speed: ${data.position.speed} km/h`
  );
});

socket.on('device_started', (data) => {
  console.log(`Device started: ${data.device_id}`);
});

socket.on('device_stopped', (data) => {
  console.log(`Device stopped: ${data.device_id}`);
});

// Start a device remotely
function startDevice(deviceId) {
  socket.emit('start_emulator', { device_id: deviceId });
}

// Stop a device remotely
function stopDevice(deviceId) {
  socket.emit('stop_emulator', { device_id: deviceId });
}
```

---

### cURL - Complete Lifecycle

```bash
#!/bin/bash

BASE_URL="http://localhost:5000"

# 1. Create device
echo "Creating device..."
CREATE_RESPONSE=$(curl -s -X POST "$BASE_URL/api/multidevice/devices" \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "paris",
    "speed": 60.0
  }')

DEVICE_ID=$(echo $CREATE_RESPONSE | jq -r '.device.device_id')
echo "Created device: $DEVICE_ID"

# 2. Start device
echo "Starting device..."
curl -s -X POST "$BASE_URL/api/multidevice/devices/$DEVICE_ID/start" | jq

# 3. Wait and monitor
echo "Monitoring for 30 seconds..."
for i in {1..3}; do
  sleep 10
  curl -s "$BASE_URL/api/multidevice/devices/$DEVICE_ID" | jq '.device.current_position'
done

# 4. Stop device
echo "Stopping device..."
curl -s -X POST "$BASE_URL/api/multidevice/devices/$DEVICE_ID/stop" | jq

# 5. Delete device
echo "Deleting device..."
curl -s -X DELETE "$BASE_URL/api/multidevice/devices/$DEVICE_ID" | jq

echo "Complete!"
```

---

## WebSocket Events

Real-time updates via Socket.IO WebSocket.

### Connection

```javascript
const socket = io('http://localhost:5000');

socket.on('connect', () => {
  console.log('Connected to emulator');
});
```

### Event: device_update

Emitted when device position/status updates.

```javascript
socket.on('device_update', (data) => {
  console.log('Device update:', data);
});
```

**Data:**
```json
{
  "device_id": "dev_tk103_001",
  "status": "running",
  "position": {
    "latitude": 48.8566,
    "longitude": 2.3522,
    "speed": 45.0,
    "altitude": 35.0,
    "heading": 90.0,
    "timestamp": "2025-10-25T14:32:15Z"
  },
  "vehicle_data": {
    "ignition": true,
    "fuel": 75.5,
    "battery": 12.6
  }
}
```

---

## Next Steps

{% content-ref url="websocket.md" %}
[websocket.md](websocket.md)
{% endcontent-ref %}

{% content-ref url="../user-guide/creating-devices.md" %}
[creating-devices.md](../user-guide/creating-devices.md)
{% endcontent-ref %}

---

## Need Help?

- See [FAQ](../support/faq.md) for common questions
- Check [Troubleshooting](../support/troubleshooting.md) for issues
- Contact support for API assistance

---

*Last updated: October 2025*
