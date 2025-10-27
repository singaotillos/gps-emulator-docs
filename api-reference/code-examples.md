# Code Examples

Complete code examples for common tasks.

---

## Python Examples

### Create and Start Device

```python
import requests

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
```

---

## JavaScript Examples

### Monitor Devices

```javascript
const socket = io('http://localhost:5000');

socket.on('device_update', (data) => {
  console.log(`Device ${data.device_id}: ${data.position.speed} km/h`);
});
```

---

## cURL Examples

### Complete Workflow

```bash
# Create device
curl -X POST http://localhost:5000/api/multidevice/devices   -H "Content-Type: application/json"   -d '{"protocol": "tk103", "device_model": "TK103-2B"}'

# Start device
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start

# Get status
curl http://localhost:5000/api/multidevice/devices/DEVICE_ID

# Stop device
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop
```

---

*Last updated: October 2025*
