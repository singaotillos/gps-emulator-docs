# Custom Routes

Learn how to create custom GPS routes for your simulated devices.

---

## Overview

The GPS Emulator includes **5 predefined routes**, but you can also create **custom routes** with your own waypoints.

{% hint style="success" %}
**Why custom routes?**
- Test specific locations
- Simulate actual delivery routes
- Test geofencing
- Reproduce real-world scenarios
{% endhint %}

---

## Predefined Routes

The emulator includes 5 built-in city routes:

| Route ID | City | Country | Distance | Points | Description |
|----------|------|---------|----------|--------|-------------|
| `paris` | Paris | France | 12.5 km | 4 | Central Paris tour |
| `london` | London | UK | 15.0 km | 4 | London city tour |
| `berlin` | Berlin | Germany | 18.0 km | 4 | Berlin tour |
| `tokyo` | Tokyo | Japan | 20.0 km | 4 | Tokyo tour |
| `newyork` | New York | USA | 22.0 km | 4 | NYC tour |

### Using Predefined Routes

{% tabs %}
{% tab title="Web Interface" %}
1. Create new device
2. Select route from dropdown:
   - Paris
   - London
   - Berlin
   - Tokyo
   - New York
3. Click "Create Device"
{% endtab %}

{% tab title="API" %}
```bash
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "paris"
  }'
```
{% endtab %}
{% endtabs %}

---

## Creating Custom Routes

### Method 1: API (Recommended)

**Create device with custom waypoints:**

```bash
curl -X POST http://localhost:5000/api/device/DEVICE_ID/route \
  -H "Content-Type: application/json" \
  -d '{
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
        "speed": 40.0,
        "altitude": 32.0
      },
      {
        "latitude": 48.8738,
        "longitude": 2.2950,
        "speed": 50.0,
        "altitude": 30.0
      },
      {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "speed": 30.0,
        "altitude": 35.0
      }
    ]
  }'
```

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `latitude` | float | ✅ Yes | Latitude in decimal degrees (-90 to 90) |
| `longitude` | float | ✅ Yes | Longitude in decimal degrees (-180 to 180) |
| `speed` | float | ❌ No | Speed at this point (km/h), default: 50.0 |
| `altitude` | float | ❌ No | Altitude at this point (meters), default: 35.0 |

**Response:**
```json
{
  "success": true,
  "message": "Custom route set successfully",
  "route": {
    "points": 4,
    "distance_km": 8.2
  }
}
```

{% hint style="warning" %}
**Important:** Device must be **stopped** to change route!
{% endhint %}

---

### Method 2: Configuration File

**Edit `config.yaml`:**

```yaml
routes:
  custom_delivery:
    name: "Delivery Route A"
    description: "Morning delivery route"
    points:
      - latitude: 48.8566
        longitude: 2.3522
        speed: 40.0
        altitude: 35.0
      - latitude: 48.8606
        longitude: 2.3376
        speed: 45.0
        altitude: 32.0
      - latitude: 48.8738
        longitude: 2.2950
        speed: 50.0
        altitude: 30.0

  custom_patrol:
    name: "Security Patrol Route"
    description: "Night patrol route"
    points:
      - latitude: 40.7128
        longitude: -74.0060
        speed: 30.0
      - latitude: 40.7614
        longitude: -73.9776
        speed: 35.0
      - latitude: 40.7489
        longitude: -73.9680
        speed: 30.0
```

**Use custom route:**

```bash
curl -X POST http://localhost:5000/api/multidevice/devices \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "custom_delivery"
  }'
```

---

### Method 3: Python Script

**Complete example:**

```python
import requests

BASE_URL = "http://localhost:5000"

# Define custom route
custom_route = {
    "points": [
        {"latitude": 48.8566, "longitude": 2.3522, "speed": 40.0},
        {"latitude": 48.8606, "longitude": 2.3376, "speed": 45.0},
        {"latitude": 48.8738, "longitude": 2.2950, "speed": 50.0},
        {"latitude": 48.8566, "longitude": 2.3522, "speed": 40.0}
    ]
}

# Create device
device_data = {
    "protocol": "tk103",
    "device_model": "TK103-2B"
}

response = requests.post(f"{BASE_URL}/api/multidevice/devices", json=device_data)
device_id = response.json()["device"]["device_id"]
print(f"Created device: {device_id}")

# Set custom route
response = requests.post(
    f"{BASE_URL}/api/device/{device_id}/route",
    json=custom_route
)
print(f"Route set: {response.json()['message']}")

# Start device
response = requests.post(f"{BASE_URL}/api/multidevice/devices/{device_id}/start")
print(f"Device started: {response.json()['message']}")
```

---

## Route Planning Tools

### Getting Coordinates

**Method 1: Google Maps**

1. Go to [Google Maps](https://maps.google.com)
2. Right-click on location
3. Click first number (coordinates)
4. Copy latitude, longitude

**Method 2: OpenStreetMap**

1. Go to [OpenStreetMap](https://www.openstreetmap.org)
2. Right-click on location
3. Select "Show address"
4. Copy coordinates

**Method 3: GPS Coordinates Tool**

Online tools:
- https://www.gps-coordinates.net
- https://www.latlong.net
- https://gps-coordinates.org

### Planning a Route

**Steps:**

1. **Start Point** - Where vehicle begins
2. **Waypoints** - Intermediate stops (2-10 points)
3. **End Point** - Where vehicle ends (can be same as start)

**Tips:**

{% hint style="info" %}
**Best practices for routes:**
- Use 3-6 waypoints for realistic movement
- Vary speeds at different points
- Close the loop (end = start) for continuous simulation
- Space points 1-5 km apart
{% endhint %}

---

## Route Examples

### Example 1: Simple Loop

**Paris city loop (4 points):**

```json
{
  "points": [
    {"latitude": 48.8566, "longitude": 2.3522, "speed": 30},
    {"latitude": 48.8606, "longitude": 2.3376, "speed": 40},
    {"latitude": 48.8738, "longitude": 2.2950, "speed": 50},
    {"latitude": 48.8566, "longitude": 2.3522, "speed": 30}
  ]
}
```

**Distance:** ~8 km
**Time:** ~12 minutes at specified speeds
**Use case:** City delivery route

---

### Example 2: Highway Route

**Long-distance route:**

```json
{
  "points": [
    {"latitude": 48.8566, "longitude": 2.3522, "speed": 60},
    {"latitude": 49.2628, "longitude": 4.0347, "speed": 110},
    {"latitude": 49.4944, "longitude": 5.9708, "speed": 120},
    {"latitude": 48.5734, "longitude": 7.7521, "speed": 90},
    {"latitude": 48.8566, "longitude": 2.3522, "speed": 60}
  ]
}
```

**Distance:** ~600 km
**Time:** ~5 hours
**Use case:** Interstate trucking

---

### Example 3: Patrol Route

**Security patrol with stops:**

```json
{
  "points": [
    {"latitude": 40.7128, "longitude": -74.0060, "speed": 30},
    {"latitude": 40.7200, "longitude": -74.0100, "speed": 0},
    {"latitude": 40.7614, "longitude": -73.9776, "speed": 35},
    {"latitude": 40.7650, "longitude": -73.9750, "speed": 0},
    {"latitude": 40.7489, "longitude": -73.9680, "speed": 30},
    {"latitude": 40.7500, "longitude": -73.9700, "speed": 0},
    {"latitude": 40.7128, "longitude": -74.0060, "speed": 30}
  ]
}
```

**Features:**
- Speed = 0 at checkpoint stops
- Slow speeds (30-35 km/h)
- Multiple stops along route

---

### Example 4: Delivery Route

**Multi-stop delivery:**

```json
{
  "points": [
    {"latitude": 51.5074, "longitude": -0.1278, "speed": 40, "description": "Warehouse"},
    {"latitude": 51.5155, "longitude": -0.0922, "speed": 45},
    {"latitude": 51.5205, "longitude": -0.0955, "speed": 0, "description": "Stop 1"},
    {"latitude": 51.5310, "longitude": -0.1260, "speed": 50},
    {"latitude": 51.5350, "longitude": -0.1280, "speed": 0, "description": "Stop 2"},
    {"latitude": 51.5230, "longitude": -0.1545, "speed": 45},
    {"latitude": 51.5200, "longitude": -0.1590, "speed": 0, "description": "Stop 3"},
    {"latitude": 51.5074, "longitude": -0.1278, "speed": 40, "description": "Return"}
  ]
}
```

**Features:**
- Starts and ends at warehouse
- 3 delivery stops (speed = 0)
- Realistic city speeds

---

## Advanced Route Features

### Variable Speeds

**Simulate traffic conditions:**

```python
# Morning rush hour (slow)
morning_route = {
    "points": [
        {"latitude": 48.8566, "longitude": 2.3522, "speed": 20},  # Slow
        {"latitude": 48.8606, "longitude": 2.3376, "speed": 15},  # Very slow
        {"latitude": 48.8738, "longitude": 2.2950, "speed": 25},  # Slow
    ]
}

# Night time (fast)
night_route = {
    "points": [
        {"latitude": 48.8566, "longitude": 2.3522, "speed": 60},  # Fast
        {"latitude": 48.8606, "longitude": 2.3376, "speed": 70},  # Fast
        {"latitude": 48.8738, "longitude": 2.2950, "speed": 65},  # Fast
    ]
}
```

### Altitude Variation

**Simulate hills/mountains:**

```json
{
  "points": [
    {"latitude": 45.8326, "longitude": 6.8652, "altitude": 1000},
    {"latitude": 45.8400, "longitude": 6.8700, "altitude": 1500},
    {"latitude": 45.8500, "longitude": 6.8800, "altitude": 2000},
    {"latitude": 45.8400, "longitude": 6.8700, "altitude": 1500},
    {"latitude": 45.8326, "longitude": 6.8652, "altitude": 1000}
  ]
}
```

### Circular Routes

**Continuous loop (never-ending):**

```python
# Last point = first point (loop)
circular_route = {
    "points": [
        {"latitude": 48.8566, "longitude": 2.3522, "speed": 50},
        {"latitude": 48.8606, "longitude": 2.3376, "speed": 50},
        {"latitude": 48.8738, "longitude": 2.2950, "speed": 50},
        {"latitude": 48.8566, "longitude": 2.3522, "speed": 50}  # Same as first!
    ]
}
```

{% hint style="success" %}
**Pro tip:** For continuous simulation, make last point = first point
{% endhint %}

---

## Managing Routes

### View Current Route

**Get device route:**

```bash
curl http://localhost:5000/api/device/DEVICE_ID/route
```

**Response:**
```json
{
  "success": true,
  "route": {
    "name": "custom",
    "points": [
      {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "speed": 30.0,
        "altitude": 35.0
      }
    ],
    "current_index": 2,
    "distance_km": 12.5
  }
}
```

### Update Route

**Change route while device is running:**

1. **Stop device:**
   ```bash
   curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop
   ```

2. **Set new route:**
   ```bash
   curl -X POST http://localhost:5000/api/device/DEVICE_ID/route \
     -H "Content-Type: application/json" \
     -d '{"points": [...]}'
   ```

3. **Start device:**
   ```bash
   curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
   ```

---

## Route Validation

### Automatic Validation

The emulator automatically validates routes:

✅ **Valid:**
- At least 2 points
- Valid latitude (-90 to 90)
- Valid longitude (-180 to 180)
- Speed >= 0 km/h
- Altitude >= 0 meters

❌ **Invalid:**
- Less than 2 points
- Invalid coordinates
- Negative speed/altitude

### Example Validation Error

```json
{
  "success": false,
  "error": "Invalid route",
  "details": "Latitude must be between -90 and 90 degrees"
}
```

---

## Best Practices

### Route Design

{% hint style="success" %}
**Good route design:**
{% endhint %}

1. **3-6 waypoints** - Enough variation, not too complex
2. **Realistic speeds** - 30-80 km/h for city, 80-120 km/h for highway
3. **Close the loop** - Last point = first point for continuous simulation
4. **Vary speeds** - Simulate realistic traffic
5. **Use real locations** - Test with actual addresses

### Performance

1. **Don't use 100+ waypoints** - Slows down simulation
2. **Keep points 1-5 km apart** - Realistic movement
3. **Use appropriate speeds** - Affects simulation time

### Testing

1. **Test route first** - Create one device with new route
2. **Verify in Traccar** - Check route appears correctly
3. **Adjust if needed** - Modify speeds, waypoints
4. **Then scale up** - Use for multiple devices

---

## Troubleshooting

### Route Not Working

{% hint style="danger" %}
**Problem:** Route set but device not moving correctly
{% endhint %}

**Solutions:**

1. **Verify route format:**
   ```bash
   curl http://localhost:5000/api/device/DEVICE_ID/route
   ```

2. **Check coordinates are valid:**
   - Latitude: -90 to 90
   - Longitude: -180 to 180

3. **Ensure device is running:**
   - Status = "running"

4. **Check update interval:**
   ```yaml
   simulation:
     update_interval: 10.0
   ```

### Device Not Following Route

{% hint style="warning" %}
**Problem:** Device position not matching route
{% endhint %}

**Check:**

1. ✅ Route has at least 2 points
2. ✅ Speed > 0 km/h
3. ✅ Device is started
4. ✅ No errors in logs

---

## Next Steps

{% content-ref url="creating-devices.md" %}
[creating-devices.md](creating-devices.md)
{% endcontent-ref %}

{% content-ref url="traccar-integration.md" %}
[traccar-integration.md](traccar-integration.md)
{% endcontent-ref %}

{% content-ref url="../api-reference/rest-api.md" %}
[rest-api.md](../api-reference/rest-api.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
