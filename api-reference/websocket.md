# WebSocket API

Real-time communication using Socket.IO WebSocket.

---

## Overview

The GPS Emulator provides **real-time updates** via WebSocket using Socket.IO protocol.

{% hint style="success" %}
**Perfect for:**
- Real-time dashboards
- Live tracking displays
- Monitoring applications
- Event-driven updates
{% endhint %}

**Features:**
- ✅ Real-time device updates
- ✅ Device status events
- ✅ Bidirectional communication
- ✅ Room-based subscriptions
- ✅ Automatic reconnection

---

## Connection

### JavaScript/Browser

```javascript
// Include Socket.IO client library
<script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>

<script>
  // Connect to emulator
  const socket = io('http://localhost:5000');

  socket.on('connect', () => {
    console.log('Connected to GPS Emulator');
    console.log('Socket ID:', socket.id);
  });

  socket.on('disconnect', () => {
    console.log('Disconnected from emulator');
  });

  socket.on('connect_error', (error) => {
    console.error('Connection error:', error);
  });
</script>
```

### Node.js

```javascript
const io = require('socket.io-client');

const socket = io('http://localhost:5000', {
  transports: ['websocket'],
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  reconnectionAttempts: 5
});

socket.on('connect', () => {
  console.log('Connected to GPS Emulator');
});

socket.on('disconnect', (reason) => {
  console.log('Disconnected:', reason);
});
```

### Python

```python
import socketio

# Create Socket.IO client
sio = socketio.Client()

@sio.event
def connect():
    print('Connected to GPS Emulator')
    print('Socket ID:', sio.sid)

@sio.event
def disconnect():
    print('Disconnected from emulator')

@sio.event
def connect_error(data):
    print('Connection error:', data)

# Connect
sio.connect('http://localhost:5000')

# Keep connection open
sio.wait()
```

---

## Events - Receiving

### Event: connect

Emitted when client successfully connects.

**Listener:**
```javascript
socket.on('connect', () => {
  console.log('Connected');
  console.log('Socket ID:', socket.id);
});
```

**No data payload**

---

### Event: disconnect

Emitted when client disconnects.

**Listener:**
```javascript
socket.on('disconnect', (reason) => {
  console.log('Disconnected:', reason);

  // Reasons:
  // - "io server disconnect" - Server disconnected client
  // - "io client disconnect" - Client disconnected
  // - "ping timeout" - Connection timeout
  // - "transport close" - Connection lost
  // - "transport error" - Transport error
});
```

---

### Event: device_update

Emitted when device position or status updates.

**Frequency:** Every update interval (default: 10 seconds)

**Listener:**
```javascript
socket.on('device_update', (data) => {
  console.log('Device update:', data);
});
```

**Data payload:**
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
    "battery": 12.6,
    "temperature": 22.0,
    "odometer": 125500.0
  }
}
```

**Example usage:**
```javascript
socket.on('device_update', (data) => {
  // Update map marker
  updateMarker(data.device_id, data.position.latitude, data.position.longitude);

  // Update speed display
  document.getElementById('speed').textContent = `${data.position.speed} km/h`;

  // Update fuel gauge
  document.getElementById('fuel').textContent = `${data.vehicle_data.fuel}%`;
});
```

---

### Event: device_started

Emitted when device starts.

**Listener:**
```javascript
socket.on('device_started', (data) => {
  console.log('Device started:', data);
});
```

**Data payload:**
```json
{
  "device_id": "dev_tk103_001",
  "protocol": "tk103",
  "started_at": "2025-10-25T14:35:00Z"
}
```

**Example usage:**
```javascript
socket.on('device_started', (data) => {
  // Show notification
  showNotification(`Device ${data.device_id} started`);

  // Update UI
  document.getElementById(`device-${data.device_id}`).classList.add('running');
});
```

---

### Event: device_stopped

Emitted when device stops.

**Listener:**
```javascript
socket.on('device_stopped', (data) => {
  console.log('Device stopped:', data);
});
```

**Data payload:**
```json
{
  "device_id": "dev_tk103_001",
  "stopped_at": "2025-10-25T14:40:00Z",
  "stats": {
    "packets_sent": 1523,
    "uptime_seconds": 15230,
    "distance_km": 125.5,
    "avg_speed": 48.2
  }
}
```

---

### Event: device_created

Emitted when new device is created.

**Listener:**
```javascript
socket.on('device_created', (data) => {
  console.log('New device created:', data);
});
```

**Data payload:**
```json
{
  "device_id": "dev_tk103_002",
  "protocol": "tk103",
  "device_model": "TK103-2B",
  "created_at": "2025-10-25T14:30:00Z"
}
```

---

### Event: device_deleted

Emitted when device is deleted.

**Listener:**
```javascript
socket.on('device_deleted', (data) => {
  console.log('Device deleted:', data);
});
```

**Data payload:**
```json
{
  "device_id": "dev_tk103_002",
  "deleted_at": "2025-10-25T14:45:00Z"
}
```

---

### Event: system_status

Emitted periodically with system status.

**Frequency:** Every 30 seconds

**Listener:**
```javascript
socket.on('system_status', (data) => {
  console.log('System status:', data);
});
```

**Data payload:**
```json
{
  "uptime": "2h 15m 30s",
  "cpu_percent": 15.2,
  "memory_percent": 45.8,
  "devices_running": 5,
  "devices_total": 12,
  "packets_sent_total": 45230,
  "timestamp": "2025-10-25T14:32:15Z"
}
```

---

## Events - Sending

### Emit: start_emulator

Start a device remotely.

**Emit:**
```javascript
socket.emit('start_emulator', {
  device_id: 'dev_tk103_001'
});
```

**Response event:** `emulator_started`

```javascript
socket.on('emulator_started', (data) => {
  console.log('Emulator started:', data);
});
```

**Response data:**
```json
{
  "success": true,
  "device_id": "dev_tk103_001",
  "message": "Device started successfully"
}
```

---

### Emit: stop_emulator

Stop a device remotely.

**Emit:**
```javascript
socket.emit('stop_emulator', {
  device_id: 'dev_tk103_001'
});
```

**Response event:** `emulator_stopped`

```javascript
socket.on('emulator_stopped', (data) => {
  console.log('Emulator stopped:', data);
});
```

**Response data:**
```json
{
  "success": true,
  "device_id": "dev_tk103_001",
  "message": "Device stopped successfully"
}
```

---

### Emit: get_device_status

Get current device status.

**Emit:**
```javascript
socket.emit('get_device_status', {
  device_id: 'dev_tk103_001'
});
```

**Response event:** `device_status`

```javascript
socket.on('device_status', (data) => {
  console.log('Device status:', data);
});
```

---

## Complete Examples

### Example 1: Real-Time Dashboard

```html
<!DOCTYPE html>
<html>
<head>
  <title>GPS Tracker Dashboard</title>
  <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
</head>
<body>
  <h1>Live GPS Tracking</h1>
  <div id="devices"></div>

  <script>
    const socket = io('http://localhost:5000');
    const devicesContainer = document.getElementById('devices');

    socket.on('connect', () => {
      console.log('Connected to GPS Emulator');
    });

    socket.on('device_update', (data) => {
      updateDevice(data);
    });

    socket.on('device_started', (data) => {
      addDevice(data.device_id);
    });

    socket.on('device_stopped', (data) => {
      markDeviceStopped(data.device_id);
    });

    function updateDevice(data) {
      let deviceDiv = document.getElementById(`device-${data.device_id}`);

      if (!deviceDiv) {
        addDevice(data.device_id);
        deviceDiv = document.getElementById(`device-${data.device_id}`);
      }

      deviceDiv.innerHTML = `
        <h3>${data.device_id}</h3>
        <p>Position: ${data.position.latitude.toFixed(6)}, ${data.position.longitude.toFixed(6)}</p>
        <p>Speed: ${data.position.speed.toFixed(1)} km/h</p>
        <p>Fuel: ${data.vehicle_data.fuel.toFixed(1)}%</p>
        <p>Battery: ${data.vehicle_data.battery.toFixed(1)}V</p>
        <p>Last update: ${new Date(data.position.timestamp).toLocaleTimeString()}</p>
      `;
    }

    function addDevice(deviceId) {
      const div = document.createElement('div');
      div.id = `device-${deviceId}`;
      div.className = 'device';
      devicesContainer.appendChild(div);
    }

    function markDeviceStopped(deviceId) {
      const deviceDiv = document.getElementById(`device-${deviceId}`);
      if (deviceDiv) {
        deviceDiv.classList.add('stopped');
      }
    }
  </script>

  <style>
    .device {
      border: 1px solid #ccc;
      padding: 15px;
      margin: 10px;
      border-radius: 5px;
    }
    .device.stopped {
      background-color: #f0f0f0;
      opacity: 0.6;
    }
  </style>
</body>
</html>
```

---

### Example 2: Node.js Monitor

```javascript
const io = require('socket.io-client');

const socket = io('http://localhost:5000');

const devices = new Map();

socket.on('connect', () => {
  console.log('🟢 Connected to GPS Emulator');
  console.log('Monitoring devices...\n');
});

socket.on('disconnect', () => {
  console.log('🔴 Disconnected from emulator');
});

socket.on('device_update', (data) => {
  devices.set(data.device_id, data);
  displayDevices();
});

socket.on('device_started', (data) => {
  console.log(`\n✅ Device started: ${data.device_id}`);
});

socket.on('device_stopped', (data) => {
  console.log(`\n⏸️  Device stopped: ${data.device_id}`);
  console.log(`   Packets sent: ${data.stats.packets_sent}`);
  console.log(`   Distance: ${data.stats.distance_km.toFixed(2)} km`);
});

socket.on('system_status', (data) => {
  console.log(`\n📊 System: ${data.devices_running}/${data.devices_total} devices running`);
  console.log(`   CPU: ${data.cpu_percent.toFixed(1)}%, Memory: ${data.memory_percent.toFixed(1)}%`);
});

function displayDevices() {
  console.clear();
  console.log('='.repeat(80));
  console.log('GPS EMULATOR - LIVE MONITOR');
  console.log('='.repeat(80));
  console.log();

  if (devices.size === 0) {
    console.log('No devices active');
    return;
  }

  devices.forEach((data, deviceId) => {
    console.log(`Device: ${deviceId}`);
    console.log(`  Position: ${data.position.latitude.toFixed(6)}, ${data.position.longitude.toFixed(6)}`);
    console.log(`  Speed: ${data.position.speed.toFixed(1)} km/h`);
    console.log(`  Fuel: ${data.vehicle_data.fuel.toFixed(1)}%`);
    console.log(`  Battery: ${data.vehicle_data.battery.toFixed(1)}V`);
    console.log(`  Updated: ${new Date(data.position.timestamp).toLocaleTimeString()}`);
    console.log();
  });
}

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('\nShutting down monitor...');
  socket.disconnect();
  process.exit(0);
});
```

---

### Example 3: Python Real-Time Logger

```python
import socketio
import json
from datetime import datetime

sio = socketio.Client()

@sio.event
def connect():
    print('🟢 Connected to GPS Emulator')
    print('Logging device updates...\n')

@sio.event
def disconnect():
    print('🔴 Disconnected from emulator')

@sio.event
def device_update(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    device_id = data['device_id']
    position = data['position']

    log_entry = f"[{timestamp}] {device_id} - " \
                f"Lat: {position['latitude']:.6f}, " \
                f"Lng: {position['longitude']:.6f}, " \
                f"Speed: {position['speed']:.1f} km/h"

    print(log_entry)

    # Save to file
    with open('device_log.txt', 'a') as f:
        f.write(log_entry + '\n')

@sio.event
def device_started(data):
    print(f"\n✅ Device started: {data['device_id']}\n")

@sio.event
def device_stopped(data):
    print(f"\n⏸️  Device stopped: {data['device_id']}")
    print(f"   Distance: {data['stats']['distance_km']:.2f} km\n")

# Connect
sio.connect('http://localhost:5000')

try:
    sio.wait()
except KeyboardInterrupt:
    print('\nShutting down logger...')
    sio.disconnect()
```

---

## Advanced Features

### Room-Based Subscriptions

**Subscribe to specific device:**

```javascript
// Join device room
socket.emit('subscribe_device', {
  device_id: 'dev_tk103_001'
});

// Receive updates only for this device
socket.on('device_update', (data) => {
  if (data.device_id === 'dev_tk103_001') {
    console.log('Subscribed device update:', data);
  }
});

// Unsubscribe
socket.emit('unsubscribe_device', {
  device_id: 'dev_tk103_001'
});
```

### Authentication

**Connect with authentication:**

```javascript
const socket = io('http://localhost:5000', {
  auth: {
    token: 'YOUR_API_KEY'
  }
});

socket.on('connect_error', (error) => {
  console.error('Authentication failed:', error.message);
});
```

### Reconnection Logic

```javascript
const socket = io('http://localhost:5000', {
  reconnection: true,
  reconnectionAttempts: 10,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  timeout: 20000
});

let reconnectAttempts = 0;

socket.on('reconnect_attempt', () => {
  reconnectAttempts++;
  console.log(`Reconnection attempt ${reconnectAttempts}...`);
});

socket.on('reconnect', (attemptNumber) => {
  console.log(`Reconnected after ${attemptNumber} attempts`);
  reconnectAttempts = 0;
});

socket.on('reconnect_failed', () => {
  console.error('Failed to reconnect after maximum attempts');
});
```

---

## Best Practices

### Connection Management

{% hint style="success" %}
**Recommended practices:**
{% endhint %}

1. **Handle reconnection:**
   - Enable automatic reconnection
   - Implement exponential backoff
   - Show connection status to user

2. **Clean disconnection:**
   - Always disconnect when done
   - Handle page unload events

3. **Error handling:**
   - Catch connection errors
   - Log disconnection reasons
   - Retry failed connections

### Performance

1. **Limit event listeners:**
   - Don't create multiple listeners for same event
   - Remove listeners when not needed

2. **Throttle updates:**
   - Don't update UI on every event
   - Use requestAnimationFrame for smooth animations

3. **Filter events:**
   - Subscribe only to needed devices
   - Unsubscribe when device not visible

---

## Troubleshooting

### Connection Fails

{% hint style="danger" %}
**Error:** `connect_error` or `connect_timeout`
{% endhint %}

**Solutions:**

1. **Check emulator is running:**
   ```bash
   curl http://localhost:5000
   ```

2. **Verify URL and port:**
   ```javascript
   const socket = io('http://localhost:5000');  // Correct port?
   ```

3. **Check CORS settings:**
   ```bash
   # .env
   API_ENABLE_CORS=true
   ```

4. **Check firewall:**
   - Allow port 5000

### No Updates Received

{% hint style="warning" %}
**Problem:** Connected but no `device_update` events
{% endhint %}

**Check:**

1. ✅ Device is running (status = "running")
2. ✅ Listener registered before device starts
3. ✅ Check browser console for errors
4. ✅ Verify event name is correct

---

## Next Steps

{% content-ref url="rest-api.md" %}
[rest-api.md](rest-api.md)
{% endcontent-ref %}

{% content-ref url="../user-guide/creating-devices.md" %}
[creating-devices.md](../user-guide/creating-devices.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
