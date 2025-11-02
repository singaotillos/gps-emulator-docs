# Sending Commands to GPS Devices

Send commands to your emulated GPS devices to control various functions like engine stop/resume, position requests, configuration changes, and more.

---

## 🎯 Overview

The GPS Tracker Emulator supports **sending commands** to devices through the Traccar platform. Commands allow you to:

- 🛑 **Control engine** (stop/resume)
- 📍 **Request positions** (single or periodic)
- 🔒 **Lock/unlock doors**
- ⚙️ **Configure device settings**
- 🔔 **Set alarms and geofences**
- 📱 **Send custom commands**

Commands are sent via the **Traccar API** and are protocol-specific.

---

## 📋 Supported Command Types

### Standard Commands

| Command Type | Description | Protocols |
|--------------|-------------|-----------|
| **ENGINE_STOP** | Stop the vehicle engine | TK103, GT06, Teltonika, Castel, H02 |
| **ENGINE_RESUME** | Resume the vehicle engine | TK103, GT06, Teltonika, Castel, H02 |
| **POSITION_SINGLE** | Request current position | Most protocols |
| **POSITION_PERIODIC** | Set position reporting interval | TK103, GT06, Teltonika |
| **POSITION_STOP** | Stop position reporting | TK103, Teltonika |
| **ALARM_ARM** | Arm the alarm system | TK103, Watch |
| **ALARM_DISARM** | Disarm the alarm system | TK103, Watch |
| **REBOOT_DEVICE** | Reboot the GPS device | TK103, GT06, Teltonika |
| **OUTPUT_CONTROL** | Control device outputs | GT06, Teltonika, H02 |
| **SET_TIMEZONE** | Set device timezone | Multiple protocols |
| **CUSTOM** | Send custom protocol command | All protocols |

---

## 🚀 Sending Commands via Web Interface

### Step 1: Access Device Commands

1. Navigate to your device in the **Active Protocols** section
2. Click the **Commands** button (command icon) on the device card
3. A command dialog will open showing available commands for the protocol

### Step 2: Select Command

1. Choose a command from the dropdown list
2. Available commands depend on the device protocol
3. Each command shows:
   - **Icon** - Visual indicator
   - **Description** - What the command does
   - **Type** - Traccar command type

### Step 3: Configure Command (if needed)

Some commands require additional parameters:

**Example: Position Periodic**
- **Frequency:** 30 seconds (how often to report position)

**Example: Output Control**
- **Index:** 1 (which output to control)
- **Data:** ON/OFF

**Example: Custom Command**
- **Data:** Your custom command string

### Step 4: Send Command

1. Click **Send Command** button
2. Command is sent to Traccar
3. Traccar forwards command to the device
4. Response appears in the result area

---

## 💻 Sending Commands via API

### Get Available Commands for Protocol

**Endpoint:** `GET /api/protocol/<protocol>/commands`

**Example:**
```bash
curl http://localhost:5000/api/protocol/tk103/commands
```

**Response:**
```json
{
  "success": true,
  "protocol": "tk103",
  "commands": [
    {
      "id": "engineStop",
      "type": "Command.TYPE_ENGINE_STOP",
      "description": "Stop Engine",
      "icon": "fas fa-stop",
      "commandString": "**,imei:STOP#"
    },
    {
      "id": "engineResume",
      "type": "Command.TYPE_ENGINE_RESUME",
      "description": "Resume Engine",
      "icon": "fas fa-play",
      "commandString": "**,imei:RESUME#"
    }
  ]
}
```

---

### Send Command to Device

**Endpoint:** `POST /api/send-command`

**Request Body:**
```json
{
  "protocol": "tk103",
  "deviceId": "357938506404024",
  "command": "engineStop",
  "commandType": "Command.TYPE_ENGINE_STOP",
  "commandData": ""
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "deviceId": "357938506404024",
    "command": "engineStop",
    "commandType": "Command.TYPE_ENGINE_STOP"
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "Command sent successfully",
  "traccar_response": {
    "id": 123,
    "deviceId": 5,
    "type": "engineStop",
    "sent": true
  }
}
```

---

### Get Command Result

**Endpoint:** `GET /api/command-result?deviceId=<id>&commandId=<cmd_id>`

**Example:**
```bash
curl "http://localhost:5000/api/command-result?deviceId=357938506404024&commandId=123"
```

**Response:**
```json
{
  "success": true,
  "result": {
    "id": 123,
    "deviceId": 5,
    "type": "engineStop",
    "sent": true,
    "delivered": true,
    "response": "OK"
  }
}
```

---

### Get Command History

**Endpoint:** `GET /api/command-history?deviceId=<id>`

**Example:**
```bash
curl "http://localhost:5000/api/command-history?deviceId=357938506404024"
```

**Response:**
```json
{
  "success": true,
  "history": [
    {
      "id": 123,
      "timestamp": "2025-11-02T10:30:00Z",
      "type": "engineStop",
      "sent": true,
      "delivered": true
    },
    {
      "id": 122,
      "timestamp": "2025-11-02T09:15:00Z",
      "type": "positionSingle",
      "sent": true,
      "delivered": true
    }
  ]
}
```

---

## 📱 Protocol-Specific Commands

### TK103 Protocol

**Available Commands:**
- **Engine Stop:** `**,imei:STOP#`
- **Engine Resume:** `**,imei:RESUME#`
- **Get Position:** `**,imei:GETLOCATION#`
- **Reboot:** `**,imei:RESET#`
- **Arm Alarm:** `**,imei:ARM#`
- **Disarm Alarm:** `**,imei:DISARM#`

**Example:**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "deviceId": "357938506404024",
    "command": "getPosition",
    "commandType": "Command.TYPE_POSITION_SINGLE"
  }'
```

---

### GT06 Protocol

**Available Commands:**
- **Engine Stop:** Binary command with relay control
- **Engine Resume:** Binary command with relay control
- **Position Single:** Request immediate position
- **Reboot Device:** Restart the tracker

**Example:**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "gt06",
    "deviceId": "123456789012345",
    "command": "engineStop",
    "commandType": "Command.TYPE_ENGINE_STOP"
  }'
```

---

### Teltonika Protocol

**Available Commands:**
- **Get Version:** Get firmware version
- **Get I/O:** Request I/O element values
- **Set Digital Output:** Control digital outputs
- **Position Single:** Request position
- **Custom Command:** Send AT commands

**Example:**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "teltonika",
    "deviceId": "357938502775402",
    "command": "getVersion",
    "commandType": "Command.TYPE_GET_VERSION"
  }'
```

---

### H02 Protocol

**Available Commands:**
- **Engine Stop:** `#CUT#`
- **Engine Resume:** `#RESUME#`
- **Position Single:** `#POSITION#`
- **Custom Command:** Send custom H02 command

**Example:**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "h02",
    "deviceId": "H02123456789",
    "command": "positionSingle",
    "commandType": "Command.TYPE_POSITION_SINGLE"
  }'
```

---

## 🔧 Custom Commands

Send protocol-specific custom commands:

**Example: TK103 Custom Command**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "deviceId": "357938506404024",
    "command": "custom",
    "commandType": "Command.TYPE_CUSTOM",
    "commandData": "**,imei:TRACKER,120#"
  }'
```

**Example: Teltonika Custom AT Command**
```bash
curl -X POST http://localhost:5000/api/send-command \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "teltonika",
    "deviceId": "357938502775402",
    "command": "custom",
    "commandType": "Command.TYPE_CUSTOM",
    "commandData": "setparam 2000:60"
  }'
```

---

## 🔄 Command Flow

```
┌─────────────────────────────────────────────────────────┐
│              Your Application / Web UI                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         GPS Tracker Emulator (/api/send-command)        │
│   • Validates command                                   │
│   • Converts device ID for protocol                     │
│   • Forwards to Traccar                                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Traccar Server (API)                       │
│   • Queues command                                      │
│   • Waits for device connection                         │
│   • Sends command when device reports                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           Emulated GPS Device                           │
│   • Receives command                                    │
│   • Processes command (simulated)                       │
│   • Sends response/acknowledgment                       │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Configuration Requirements

### Traccar Configuration

Commands require Traccar to be configured:

1. **Traccar Server Running:**
   ```bash
   http://localhost:8082
   ```

2. **Traccar Credentials Set:**
   - Username: `admin`
   - Password: Your Traccar password

3. **Device Created in Traccar:**
   - Devices are auto-created by the emulator
   - Verify device exists before sending commands

### Emulator Configuration

Update `config.yaml` with Traccar settings:

```yaml
traccar:
  server: "localhost:8082"
  username: "admin"
  password: "your_password"
  auto_create_devices: true
```

Or use the web interface:
1. Go to **Settings** → **Traccar Integration**
2. Enter server URL, username, and password
3. Click **Save Configuration**

---

## 📊 Command Response Codes

### Success Codes

| Code | Status | Description |
|------|--------|-------------|
| **200** | OK | Command sent successfully |
| **201** | Created | Command queued in Traccar |

### Error Codes

| Code | Status | Description |
|------|--------|-------------|
| **400** | Bad Request | Invalid command or parameters |
| **404** | Not Found | Device not found in Traccar |
| **401** | Unauthorized | Invalid Traccar credentials |
| **500** | Server Error | Traccar connection error |

---

## 🧪 Testing Commands

### Test with Single Device

1. **Create a device:**
   ```bash
   curl -X POST http://localhost:5000/api/multidevice/devices \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "device_model": "TK103-2B",
       "route": "paris"
     }'
   ```

2. **Start the device:**
   ```bash
   curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
   ```

3. **Send a test command:**
   ```bash
   curl -X POST http://localhost:5000/api/send-command \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "deviceId": "DEVICE_ID",
       "command": "positionSingle",
       "commandType": "Command.TYPE_POSITION_SINGLE"
     }'
   ```

4. **Check command result:**
   ```bash
   curl "http://localhost:5000/api/command-result?deviceId=DEVICE_ID&commandId=123"
   ```

---

## 🔍 Troubleshooting

### Command Not Sent

**Problem:** Command returns error "Device not found"

**Solution:**
- Verify device exists in Traccar: `http://localhost:8082`
- Check device ID matches exactly (case-sensitive)
- Ensure device has connected at least once

---

### Command Sent but Not Delivered

**Problem:** Command shows `sent: true` but `delivered: false`

**Solution:**
- Device must be actively connected to Traccar
- Start the device simulation if stopped
- Check Traccar logs for delivery errors

---

### Invalid Command Type

**Problem:** Error "Command not supported for this protocol"

**Solution:**
- Get available commands: `GET /api/protocol/<protocol>/commands`
- Use only commands listed for your protocol
- Check command type matches protocol capabilities

---

### Traccar Connection Error

**Problem:** Error "Cannot connect to Traccar server"

**Solution:**
- Verify Traccar is running: `http://localhost:8082`
- Check Traccar credentials in configuration
- Ensure firewall allows connection to port 8082

---

## 📚 Related Documentation

{% content-ref url="managing-devices.md" %}
[managing-devices.md](managing-devices.md)
{% endcontent-ref %}

{% content-ref url="traccar-integration.md" %}
[traccar-integration.md](traccar-integration.md)
{% endcontent-ref %}

{% content-ref url="../api-reference/rest-api-detailed.md" %}
[rest-api-detailed.md](../api-reference/rest-api-detailed.md)
{% endcontent-ref %}

---

## 💡 Best Practices

### Command Security

1. **Validate commands** before sending to production devices
2. **Test in development** environment first
3. **Monitor command results** to ensure delivery
4. **Log all commands** for audit trail

### Performance Tips

1. **Batch commands** when sending to multiple devices
2. **Use appropriate intervals** for periodic position commands
3. **Avoid flooding** devices with rapid commands
4. **Check delivery status** before sending another command

### Protocol Compatibility

1. **Check protocol support** before sending commands
2. **Use protocol-specific syntax** for custom commands
3. **Refer to protocol documentation** for advanced commands
4. **Test with protocol** to verify command format

---

## 🎓 Examples Library

### Example 1: Emergency Stop All Devices

```bash
#!/bin/bash
# Stop all active devices

# Get all active devices
devices=$(curl -s http://localhost:5000/api/multidevice/devices | jq -r '.devices[] | select(.status=="active") | .device_id')

# Send engine stop to each
for device in $devices; do
  protocol=$(curl -s http://localhost:5000/api/multidevice/devices/$device | jq -r '.protocol')

  curl -X POST http://localhost:5000/api/send-command \
    -H "Content-Type: application/json" \
    -d "{
      \"protocol\": \"$protocol\",
      \"deviceId\": \"$device\",
      \"command\": \"engineStop\",
      \"commandType\": \"Command.TYPE_ENGINE_STOP\"
    }"

  echo "Engine stop sent to $device"
done
```

---

### Example 2: Request Position from All Devices

```python
import requests

emulator_url = "http://localhost:5000"

# Get all devices
response = requests.get(f"{emulator_url}/api/multidevice/devices")
devices = response.json()['devices']

for device in devices:
    protocol = device['protocol']
    device_id = device['device_id']

    # Send position request
    command_data = {
        "protocol": protocol,
        "deviceId": device_id,
        "command": "positionSingle",
        "commandType": "Command.TYPE_POSITION_SINGLE"
    }

    result = requests.post(
        f"{emulator_url}/api/send-command",
        json=command_data
    )

    print(f"Position request sent to {device_id}: {result.json()}")
```

---

### Example 3: Set Periodic Reporting

```javascript
// Set 30-second position reporting for a device

const axios = require('axios');

const sendCommand = async (deviceId, protocol) => {
  const command = {
    protocol: protocol,
    deviceId: deviceId,
    command: 'positionPeriodic',
    commandType: 'Command.TYPE_POSITION_PERIODIC',
    commandData: '30' // 30 seconds
  };

  try {
    const response = await axios.post(
      'http://localhost:5000/api/send-command',
      command
    );
    console.log('Command sent:', response.data);
  } catch (error) {
    console.error('Error:', error.response.data);
  }
};

// Usage
sendCommand('357938506404024', 'tk103');
```

---

**Last updated:** November 2025 | Version: 2.0.0
