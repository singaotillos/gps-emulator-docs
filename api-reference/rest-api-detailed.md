# API Reference - Universal GPS Tracker Emulator

Complete REST API documentation for integrating with the GPS emulator.

---

## Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Base URL](#base-url)
- [Response Format](#response-format)
- [Error Codes](#error-codes)
- [Rate Limiting](#rate-limiting)
- [API Endpoints](#api-endpoints)
  - [System & Status](#system--status)
  - [Device Management](#device-management)
  - [Device Control](#device-control)
  - [Protocol Information](#protocol-information)
  - [Routes & Tracking](#routes--tracking)
  - [Traccar Integration](#traccar-integration)
  - [Device Commands](#device-commands)
  - [Configuration](#configuration)
  - [WebSocket Events](#websocket-events)
- [Code Examples](#code-examples)
- [Postman Collection](#postman-collection)

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

```bash
# .env
API_ENABLE_AUTHENTICATION=true
API_KEY=your-secret-api-key-here
```

**Generate Strong Key:**
```bash
openssl rand -hex 32
```

**Using API Key:**

```bash
# Header method (recommended)
curl -H "Authorization: Bearer YOUR_API_KEY" \
     http://localhost:5000/api/status

# Query parameter method (less secure)
curl http://localhost:5000/api/status?api_key=YOUR_API_KEY
```

**Example with Python:**
```python
import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.get("http://localhost:5000/api/status", headers=headers)
print(response.json())
```

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

Standard HTTP status codes with custom error codes:

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
| `DEVICE_ALREADY_RUNNING` | Device already started | Stop device first |
| `DEVICE_NOT_RUNNING` | Device not active | Start device first |

---

## Rate Limiting

Rate limiting protects the API from abuse.

**Default Limits:**
- 100 requests per minute per IP
- Applies when `API_RATE_LIMITING=true`

**Headers:**
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

**Disable Rate Limiting:**
```bash
# .env
API_RATE_LIMITING=false
```

---

## API Endpoints

### System & Status

#### GET /api/status

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

#### GET /api/protocols

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
    },
    {
      "name": "gt06",
      "display_name": "GT06",
      "port": 5023,
      "type": "tcp",
      "manufacturer": "Various",
      "description": "GT06/CRX1 protocol",
      "popular": true
    }
  ],
  "count": 86,
  "categories": {
    "popular": ["tk103", "gt06", "teltonika", "osmand"],
    "binary": ["tk103", "gt06", "teltonika", "meiligao"],
    "text": ["gps103", "h02", "watch"],
    "http": ["osmand", "gpsgate"]
  }
}
```

---

#### GET /api/protocol_info/:protocol

Get detailed information about specific protocol.

**Request:**
```bash
curl http://localhost:5000/api/protocol_info/tk103
```

**Response:**
```json
{
  "success": true,
  "protocol": {
    "name": "tk103",
    "display_name": "TK103",
    "port": 5002,
    "type": "tcp",
    "manufacturer": "Xexun",
    "models": ["TK103-2B", "TK103A", "TK103B"],
    "features": ["gps", "gsm", "alarms", "geofence"],
    "id_format": "15-digit IMEI",
    "id_example": "357938506404024",
    "documentation_url": "https://docs.traccar.org/devices/tk103/"
  }
}
```

---

### Device Management

#### POST /api/multidevice/devices

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
  "route": "paris",              // Optional: paris, london, berlin, tokyo, newyork, or custom
  "speed": 50.0,                 // Optional: Speed in km/h (default: 50.0)
  "update_interval": 10.0,       // Optional: Seconds between updates (default: 10.0)
  "description": "Test vehicle"  // Optional: Human-readable description
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

**Error Responses:**

400 Bad Request - Missing required fields:
```json
{
  "success": false,
  "error": "Protocol and device model required"
}
```

409 Conflict - Device already exists:
```json
{
  "success": false,
  "error": "Device already exists with this ID"
}
```

---

#### GET /api/multidevice/devices

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
      },
      "created_at": "2025-10-25T12:00:00Z",
      "started_at": "2025-10-25T12:05:00Z"
    }
  ],
  "count": 12,
  "total": 12
}
```

---

#### GET /api/multidevice/devices/:device_id

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
    "config": {
      "speed": 50.0,
      "update_interval": 10.0,
      "heartbeat_interval": 30.0
    },
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
    },
    "created_at": "2025-10-25T12:00:00Z",
    "started_at": "2025-10-25T12:05:00Z",
    "last_update": "2025-10-25T14:32:15Z"
  }
}
```

---

#### DELETE /api/multidevice/devices/:device_id

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

**Note:** Device must be stopped before deletion. Returns 400 if running.

---

#### PUT /api/multidevice/devices/:device_id/config

Update device configuration.

**Request:**
```bash
curl -X PUT http://localhost:5000/api/multidevice/devices/dev_tk103_001/config \
     -H "Content-Type: application/json" \
     -d '{
       "speed": 80.0,
       "update_interval": 5.0
     }'
```

**Request Body:**
```json
{
  "speed": 80.0,                // Speed in km/h
  "update_interval": 5.0,        // Seconds between updates
  "heartbeat_interval": 30.0,    // Heartbeat interval
  "description": "Updated desc"  // Description
}
```

**Response:**
```json
{
  "success": true,
  "device": {
    "device_id": "dev_tk103_001",
    "config": {
      "speed": 80.0,
      "update_interval": 5.0
    }
  },
  "message": "Configuration updated"
}
```

**Note:** Device must be stopped to update configuration.

---

### Device Control

#### POST /api/multidevice/devices/:device_id/start

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

**Error Response:**

Device already running:
```json
{
  "success": false,
  "error": "Device is already running"
}
```

Device limit reached (CE):
```json
{
  "success": false,
  "error": "Device limit reached",
  "details": "Community Edition limited to 5 devices. Upgrade to Enterprise."
}
```

---

#### POST /api/multidevice/devices/:device_id/stop

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

#### GET /api/multidevice/devices/:device_id/traccar-status

Get Traccar status for device.

**Request:**
```bash
curl http://localhost:5000/api/multidevice/devices/dev_tk103_001/traccar-status
```

**Response:**
```json
{
  "success": true,
  "traccar": {
    "connected": true,
    "device_exists": true,
    "last_position": {
      "latitude": 48.8566,
      "longitude": 2.3522,
      "timestamp": "2025-10-25T14:32:15Z"
    },
    "online": true
  }
}
```

---

### Routes & Tracking

#### GET /api/routes/presets

Get list of preset routes.

**Request:**
```bash
curl http://localhost:5000/api/routes/presets
```

**Response:**
```json
{
  "success": true,
  "routes": {
    "paris": {
      "name": "Paris City Tour",
      "country": "France",
      "distance_km": 12.5,
      "points": 4,
      "description": "Tour of central Paris"
    },
    "london": {
      "name": "London Tour",
      "country": "UK",
      "distance_km": 15.0,
      "points": 4
    },
    "berlin": {
      "name": "Berlin Tour",
      "country": "Germany",
      "distance_km": 18.0,
      "points": 4
    },
    "tokyo": {
      "name": "Tokyo Tour",
      "country": "Japan",
      "distance_km": 20.0,
      "points": 4
    },
    "newyork": {
      "name": "New York Tour",
      "country": "USA",
      "distance_km": 22.0,
      "points": 4
    }
  }
}
```

---

#### GET /api/device/:device_id/route

Get device route details.

**Request:**
```bash
curl http://localhost:5000/api/device/dev_tk103_001/route
```

**Response:**
```json
{
  "success": true,
  "route": {
    "name": "paris",
    "points": [
      {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "speed": 30.0,
        "altitude": 35.0
      },
      {
        "latitude": 48.8606,
        "longitude": 2.3376,
        "speed": 25.0,
        "altitude": 32.0
      }
    ],
    "current_index": 2,
    "distance_km": 12.5
  }
}
```

---

#### POST /api/device/:device_id/route

Set custom route for device.

**Request:**
```bash
curl -X POST http://localhost:5000/api/device/dev_tk103_001/route \
     -H "Content-Type: application/json" \
     -d '{
       "points": [
         {"latitude": 48.8566, "longitude": 2.3522, "speed": 30.0},
         {"latitude": 48.8606, "longitude": 2.3376, "speed": 40.0},
         {"latitude": 48.8738, "longitude": 2.295, "speed": 50.0}
       ]
     }'
```

**Request Body:**
```json
{
  "points": [
    {
      "latitude": 48.8566,    // Required
      "longitude": 2.3522,    // Required
      "speed": 30.0,          // Optional (km/h)
      "altitude": 35.0        // Optional (meters)
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Custom route set successfully",
  "route": {
    "points": 3,
    "distance_km": 8.2
  }
}
```

**Note:** Device must be stopped to change route.

---

### Traccar Integration

#### GET /api/traccar/config

Get current Traccar configuration.

**Request:**
```bash
curl http://localhost:5000/api/traccar/config
```

**Response:**
```json
{
  "success": true,
  "config": {
    "host": "localhost",
    "port": 8082,
    "username": "admin",
    "auto_create_devices": true,
    "device_prefix": "EMU_"
  }
}
```

---

#### POST /api/traccar/config

Update Traccar configuration.

**Request:**
```bash
curl -X POST http://localhost:5000/api/traccar/config \
     -H "Content-Type: application/json" \
     -d '{
       "host": "traccar.example.com",
       "port": 8082,
       "username": "admin",
       "password": "newpassword"
     }'
```

**Request Body:**
```json
{
  "host": "traccar.example.com",
  "port": 8082,
  "username": "admin",
  "password": "newpassword",
  "auto_create_devices": true,
  "device_prefix": "EMU_"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Traccar configuration updated"
}
```

---

#### POST /api/traccar/test

Test Traccar connection.

**Request:**
```bash
curl -X POST http://localhost:5000/api/traccar/test
```

**Response (Success):**
```json
{
  "success": true,
  "message": "Successfully connected to Traccar",
  "server": {
    "version": "5.9",
    "devices": 15,
    "online_devices": 7
  }
}
```

**Response (Failure):**
```json
{
  "success": false,
  "error": "Failed to connect to Traccar",
  "details": "Connection refused to localhost:8082"
}
```

---

#### POST /api/add_traccar_device

Add device to Traccar manually.

**Request:**
```bash
curl -X POST http://localhost:5000/api/add_traccar_device \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "device_id": "357938506404024",
       "device_name": "Test Vehicle 001"
     }'
```

**Request Body:**
```json
{
  "protocol": "tk103",
  "device_id": "357938506404024",
  "device_name": "Test Vehicle 001"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Device added to Traccar",
  "traccar_device": {
    "id": 1523,
    "name": "EMU_Test Vehicle 001",
    "uniqueId": "357938506404024",
    "status": "offline"
  }
}
```

---

#### POST /api/traccar/resync

Resync all devices with Traccar.

**Request:**
```bash
curl -X POST http://localhost:5000/api/traccar/resync
```

**Response:**
```json
{
  "success": true,
  "message": "Devices synced with Traccar",
  "added": 5,
  "updated": 3,
  "failed": 0
}
```

---

### Device Commands

#### GET /api/protocol/:protocol/commands

Get available commands for a specific protocol.

**Request:**
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
    },
    {
      "id": "positionSingle",
      "type": "Command.TYPE_POSITION_SINGLE",
      "description": "Request Single Position",
      "icon": "fas fa-map-marker-alt",
      "commandString": "**,imei:GETLOCATION#"
    }
  ]
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Protocol gt90 not found",
  "available_protocols": ["tk103", "gt06", "teltonika", ...]
}
```

---

#### POST /api/send-command

Send a command to a device via Traccar.

**Request:**
```bash
curl -X POST http://localhost:5000/api/send-command \
     -H "Content-Type: application/json" \
     -d '{
       "protocol": "tk103",
       "deviceId": "357938506404024",
       "command": "engineStop",
       "commandType": "Command.TYPE_ENGINE_STOP",
       "commandData": ""
     }'
```

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

**Parameters:**
- `protocol` (string, required): Protocol name (e.g., "tk103", "gt06")
- `deviceId` (string, required): Device unique identifier
- `command` (string, required): Command ID from protocol commands list
- `commandType` (string, required): Traccar command type (e.g., "Command.TYPE_ENGINE_STOP")
- `commandData` (string, optional): Additional command data for custom commands

**Response (Success):**
```json
{
  "success": true,
  "message": "Command sent successfully",
  "traccar_response": {
    "id": 123,
    "deviceId": 5,
    "type": "engineStop",
    "textChannel": false,
    "sent": true,
    "serverTime": "2025-11-02T10:30:00.000Z"
  }
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Device not found in Traccar",
  "deviceId": "357938506404024"
}
```

**Common Errors:**
- `400`: Invalid request (missing protocol or deviceId)
- `404`: Device not found in Traccar
- `401`: Traccar authentication failed
- `500`: Traccar server connection error

---

#### GET /api/command-result

Get the result of a sent command.

**Request:**
```bash
curl "http://localhost:5000/api/command-result?deviceId=357938506404024&commandId=123"
```

**Query Parameters:**
- `deviceId` (string, required): Device unique identifier
- `commandId` (integer, required): Command ID returned from send-command

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
    "serverTime": "2025-11-02T10:30:00.000Z",
    "deviceTime": "2025-11-02T10:30:15.000Z",
    "response": "OK"
  }
}
```

**Status Fields:**
- `sent`: Command sent from server to device
- `delivered`: Device acknowledged receipt
- `response`: Device response (if available)

---

#### GET /api/command-history

Get command history for a device.

**Request:**
```bash
curl "http://localhost:5000/api/command-history?deviceId=357938506404024&limit=10"
```

**Query Parameters:**
- `deviceId` (string, required): Device unique identifier
- `limit` (integer, optional): Maximum number of results (default: 50)

**Response:**
```json
{
  "success": true,
  "deviceId": "357938506404024",
  "history": [
    {
      "id": 123,
      "type": "engineStop",
      "sent": true,
      "delivered": true,
      "serverTime": "2025-11-02T10:30:00.000Z",
      "deviceTime": "2025-11-02T10:30:15.000Z"
    },
    {
      "id": 122,
      "type": "positionSingle",
      "sent": true,
      "delivered": true,
      "serverTime": "2025-11-02T09:15:00.000Z",
      "deviceTime": "2025-11-02T09:15:10.000Z"
    }
  ],
  "total": 25
}
```

---

### Configuration

#### GET /api/config

Get current emulator configuration.

**Request:**
```bash
curl http://localhost:5000/api/config
```

**Response:**
```json
{
  "success": true,
  "config": {
    "version": "2.0.0",
    "web_interface": {
      "host": "0.0.0.0",
      "port": 5000,
      "debug": false
    },
    "api": {
      "enabled": true,
      "version": "v2",
      "authentication": false
    },
    "simulation": {
      "update_interval": 10.0,
      "default_speed": 50.0,
      "gps_accuracy": 5.0
    },
    "license": {
      "edition": "CE",
      "device_limit": 5,
      "features": ["API_V2", "MULTIDEVICE_UI"]
    }
  }
}
```

---

### WebSocket Events

Real-time updates via Socket.IO WebSocket.

**Connection:**
```javascript
// JavaScript
const socket = io('http://localhost:5000');

socket.on('connect', () => {
  console.log('Connected to emulator');
});
```

**Python:**
```python
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to emulator')

sio.connect('http://localhost:5000')
```

---

#### Event: connect

Emitted when client connects.

**Listen:**
```javascript
socket.on('connect', () => {
  console.log('Connected');
});
```

---

#### Event: device_update

Emitted when device position/status updates.

**Listen:**
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

#### Event: device_started

Emitted when device starts.

**Listen:**
```javascript
socket.on('device_started', (data) => {
  console.log('Device started:', data);
});
```

**Data:**
```json
{
  "device_id": "dev_tk103_001",
  "protocol": "tk103",
  "started_at": "2025-10-25T14:35:00Z"
}
```

---

#### Event: device_stopped

Emitted when device stops.

**Listen:**
```javascript
socket.on('device_stopped', (data) => {
  console.log('Device stopped:', data);
});
```

**Data:**
```json
{
  "device_id": "dev_tk103_001",
  "stopped_at": "2025-10-25T14:40:00Z",
  "stats": {
    "packets_sent": 1523,
    "uptime_seconds": 15230
  }
}
```

---

#### Emit: start_emulator

Start a device remotely.

**Emit:**
```javascript
socket.emit('start_emulator', {
  device_id: 'dev_tk103_001'
});
```

**Response:**
```javascript
socket.on('emulator_started', (data) => {
  console.log('Started:', data);
});
```

---

#### Emit: stop_emulator

Stop a device remotely.

**Emit:**
```javascript
socket.emit('stop_emulator', {
  device_id: 'dev_tk103_001'
});
```

**Response:**
```javascript
socket.on('emulator_stopped', (data) => {
  console.log('Stopped:', data);
});
```

---

## Code Examples

### Python Examples

#### Create and Start Device

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

#### Batch Create Multiple Devices

```python
import requests
import concurrent.futures

BASE_URL = "http://localhost:5000"

def create_device(protocol, model, route_name):
    """Create a single device"""
    device_data = {
        "protocol": protocol,
        "device_model": model,
        "route": route_name
    }
    response = requests.post(f"{BASE_URL}/api/multidevice/devices", json=device_data)
    return response.json()

# Device configurations
devices_to_create = [
    ("tk103", "TK103-2B", "paris"),
    ("gt06", "GT06N", "london"),
    ("teltonika", "FMB920", "berlin"),
    ("osmand", "Mobile", "tokyo"),
    ("gps103", "GPS103", "newyork")
]

# Create devices in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(create_device, *device) for device in devices_to_create]
    results = [f.result() for f in concurrent.futures.as_completed(futures)]

print(f"Created {len(results)} devices")

# Start all devices
for result in results:
    device_id = result["device"]["device_id"]
    requests.post(f"{BASE_URL}/api/multidevice/devices/{device_id}/start")
    print(f"Started: {device_id}")
```

---

#### Monitor All Devices

```python
import requests
import time

BASE_URL = "http://localhost:5000"

def get_all_devices():
    """Get all devices status"""
    response = requests.get(f"{BASE_URL}/api/multidevice/devices")
    return response.json()["devices"]

def display_status(devices):
    """Display device status table"""
    print("\n" + "="*80)
    print(f"{'Device ID':<30} {'Protocol':<15} {'Status':<10} {'Speed':<10}")
    print("="*80)
    for device in devices:
        device_id = device["device_id"]
        protocol = device["protocol"]
        status = device["status"]
        speed = device.get("current_position", {}).get("speed", 0)
        print(f"{device_id:<30} {protocol:<15} {status:<10} {speed:<10.1f} km/h")
    print("="*80)

# Monitor loop
try:
    while True:
        devices = get_all_devices()
        display_status(devices)
        time.sleep(5)
except KeyboardInterrupt:
    print("\nMonitoring stopped")
```

---

### JavaScript/Node.js Examples

#### Create Device

```javascript
const axios = require('axios');

const BASE_URL = 'http://localhost:5000';

async function createDevice() {
  const deviceData = {
    protocol: 'tk103',
    device_model: 'TK103-2B',
    route: 'paris',
    speed: 60.0
  };

  try {
    const response = await axios.post(
      `${BASE_URL}/api/multidevice/devices`,
      deviceData
    );
    console.log('Device created:', response.data);
    return response.data.device.device_id;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

createDevice();
```

---

#### Real-Time Monitoring with WebSocket

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

### cURL Examples

#### Complete Device Lifecycle

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

## Postman Collection

### Import Postman Collection

Create a file `gps-emulator-api.postman_collection.json`:

```json
{
  "info": {
    "name": "GPS Emulator API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "System Status",
      "request": {
        "method": "GET",
        "url": "{{base_url}}/api/status"
      }
    },
    {
      "name": "List Protocols",
      "request": {
        "method": "GET",
        "url": "{{base_url}}/api/protocols"
      }
    },
    {
      "name": "Create Device",
      "request": {
        "method": "POST",
        "url": "{{base_url}}/api/multidevice/devices",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"protocol\": \"tk103\",\n  \"device_model\": \"TK103-2B\",\n  \"route\": \"paris\",\n  \"speed\": 50.0\n}"
        }
      }
    },
    {
      "name": "List Devices",
      "request": {
        "method": "GET",
        "url": "{{base_url}}/api/multidevice/devices"
      }
    },
    {
      "name": "Start Device",
      "request": {
        "method": "POST",
        "url": "{{base_url}}/api/multidevice/devices/{{device_id}}/start"
      }
    },
    {
      "name": "Stop Device",
      "request": {
        "method": "POST",
        "url": "{{base_url}}/api/multidevice/devices/{{device_id}}/stop"
      }
    },
    {
      "name": "Delete Device",
      "request": {
        "method": "DELETE",
        "url": "{{base_url}}/api/multidevice/devices/{{device_id}}"
      }
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:5000"
    },
    {
      "key": "device_id",
      "value": "dev_tk103_001"
    }
  ]
}
```

**Import to Postman:**
1. Open Postman
2. Click "Import"
3. Drag/drop the JSON file
4. Collection appears in sidebar

---

## Support

For API questions or issues:
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Review [FAQ.md](FAQ.md)
- Email: singaotillos@gmail.com
- Response time: 24-48 hours

---

*API Reference updated: October 2025*
