# Traccar Integration

Complete guide to integrating the GPS Emulator with Traccar server.

---

## Overview

The GPS Emulator provides **seamless integration** with Traccar, the world's leading open-source GPS tracking platform.

{% hint style="success" %}
**100% Compatible** - All 86 protocols work perfectly with Traccar!
{% endhint %}

**What you get:**
- ✅ Automatic device creation in Traccar
- ✅ Real-time position updates
- ✅ Full device management
- ✅ Historical data tracking
- ✅ Geofencing and alerts

---

## Prerequisites

### 1. Traccar Server Running

**Check if Traccar is running:**

{% tabs %}
{% tab title="Web Interface" %}
Open browser and go to:
```
http://localhost:8082
```

You should see the Traccar login page.
{% endtab %}

{% tab title="Command Line" %}
```bash
# Test Traccar web interface
curl http://localhost:8082

# Should return HTML content
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Traccar not installed?** Download from [traccar.org](https://www.traccar.org/download/)
{% endhint %}

### 2. Traccar Credentials

You need admin credentials (default is `admin`/`admin`):

```bash
# Default credentials
Username: admin
Password: admin
```

{% hint style="danger" %}
**Production:** Change default password immediately in production!
{% endhint %}

---

## Quick Setup (5 Minutes)

![Traccar Integration Overview](/.gitbook/assets/diagrams/traccar-integration-overview.svg)

{% hint style="info" %}
**📸 DIAGRAMME À CRÉER:**
- Diagramme d'architecture montrant:
  - GPS Emulator (à gauche)
  - Flèche avec "GPS Protocol Data (TK103, GT06, etc.)" vers Traccar Server
  - Traccar Server (au milieu)
  - Traccar Web Interface (à droite)
  - Ports: 5002, 5023, etc. pour protocols
  - Port: 8082 pour web interface
- Style: Architecture diagram propre et professionnel
- Format: SVG vectoriel
- Couleurs: Bleu/Vert pour flux de données
{% endhint %}

### Step 1: Configure Emulator

Edit your `.env` file:

```bash
# Traccar Configuration
TRACCAR_HOST=localhost
TRACCAR_PORT=8082
TRACCAR_USERNAME=admin
TRACCAR_PASSWORD=admin
TRACCAR_AUTO_CREATE_DEVICES=true
TRACCAR_DEVICE_PREFIX=EMU_
```

### Step 2: Restart Emulator

```bash
# Stop emulator if running
# Then restart
python app.py
```

### Step 3: Create Device

{% tabs %}
{% tab title="Web Interface" %}
1. Go to http://localhost:5000
2. Click "Create New Device"
3. Select protocol: **TK103**
4. Device model: **TK103-2B**
5. Route: **paris**
6. Click "Create Device"
7. Click "Start"
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

# Start device
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
```
{% endtab %}
{% endtabs %}

### Step 4: View in Traccar

![Device in Traccar Map View](/.gitbook/assets/screenshots/traccar-device-map-view.png)

{% hint style="info" %}
**📸 IMAGE À CAPTURER:**
- Screenshot Traccar web interface (http://localhost:8082)
- Map montrant device EMU_TK103_xxx visible et en ligne (vert)
- Position du device sur la carte (Paris par exemple)
- Sidebar gauche montrant le device dans la liste
- Panneau de détails montrant: speed, position, timestamp
- Ajouter flèche vers device sur la carte
- Annotation: "Device automatically created and online"
- Résolution: 1920x1080
{% endhint %}

1. Open Traccar: http://localhost:8082
2. Login with admin/admin
3. Device appears automatically with prefix `EMU_`
4. Click device to see real-time position on map!

{% hint style="success" %}
**That's it!** Device should now be visible and moving in Traccar 🎉
{% endhint %}

---

## Configuration Options

### Traccar Settings

**In `.env` file:**

```bash
# Traccar server address
TRACCAR_HOST=localhost              # Or IP: 192.168.1.100
TRACCAR_PORT=8082                   # Web interface port (not protocol port!)

# Authentication
TRACCAR_USERNAME=admin              # Traccar admin username
TRACCAR_PASSWORD=admin              # Traccar admin password

# Automatic device creation
TRACCAR_AUTO_CREATE_DEVICES=true   # Auto-create devices in Traccar
TRACCAR_DEVICE_PREFIX=EMU_          # Prefix for device names
```

**In `config.yaml` file:**

```yaml
traccar:
  default_host: localhost
  default_port: 8082
  username: admin
  password: admin
  auto_create_devices: true
  device_prefix: EMU_
```

### Options Explained

**TRACCAR_HOST:**
- `localhost` - Traccar running on same machine
- `192.168.1.100` - Traccar on local network
- `traccar.example.com` - Remote Traccar server

**TRACCAR_PORT:**
- Default: `8082` (Traccar web interface)
- **Important:** This is NOT the protocol port!
- Protocol ports are configured separately (e.g., 5002 for TK103)

**TRACCAR_AUTO_CREATE_DEVICES:**
- `true` - Devices automatically created in Traccar
- `false` - Manual device creation required

**TRACCAR_DEVICE_PREFIX:**
- Prefix added to device names in Traccar
- Example: `EMU_` creates "EMU_TK103_001"
- Helps identify emulator devices vs real hardware

---

## Protocol Port Configuration

### Understanding Ports

![Traccar Port Configuration Diagram](/.gitbook/assets/diagrams/traccar-port-configuration.svg)

{% hint style="info" %}
**📸 DIAGRAMME À CRÉER:**
- Diagramme montrant deux types de ports:
  - Web Interface Port: 8082 (HTTP)
  - Protocol Ports: 5001-5232 (TCP/UDP)
- Emulator (gauche) → Protocol Ports → Traccar Server
- User Browser → Port 8082 → Traccar Web Interface
- Annoter chaque type de connexion
- Style: Network diagram clair
- Format: SVG
{% endhint %}

{% hint style="info" %}
**Two types of ports:**
1. **Web Interface Port** (8082) - For API/web access
2. **Protocol Ports** (5001-5232) - For GPS data transmission
{% endhint %}

### Common Protocol Ports

| Protocol | Emulator Port | Traccar Port | Must Match |
|----------|---------------|--------------|------------|
| TK103 | 5002 | 5002 | ✅ Yes |
| GT06 | 5023 | 5023 | ✅ Yes |
| Teltonika | 5027 | 5027 | ✅ Yes |
| OsmAnd | 5055 | 5055 | ✅ Yes |
| GPS103 | 5001 | 5001 | ✅ Yes |
| H02 | 5013 | 5013 | ✅ Yes |

{% hint style="danger" %}
**Critical:** Protocol ports in emulator MUST match Traccar's configuration!
{% endhint %}

### Check Traccar Protocol Ports

**Location:** Traccar's `traccar.xml` file

![Traccar XML Configuration](/.gitbook/assets/screenshots/traccar-xml-config.png)

{% hint style="info" %}
**📸 IMAGE À CAPTURER:**
- Screenshot du fichier traccar.xml ouvert dans un éditeur
- Montrer les lignes de configuration des ports:
  - <entry key='tk103.port'>5002</entry>
  - <entry key='gt06.port'>5023</entry>
  - etc.
- Highlighter (surligner) les entrées de ports en jaune
- Ajouter annotation: "Protocol port configuration"
- Résolution: 1280x720
{% endhint %}

{% tabs %}
{% tab title="Windows" %}
```
C:\Program Files\Traccar\conf\traccar.xml
```
{% endtab %}

{% tab title="Linux" %}
```
/opt/traccar/conf/traccar.xml
```
{% endtab %}

{% tab title="Docker" %}
```bash
docker exec -it traccar cat /opt/traccar/conf/traccar.xml
```
{% endtab %}
{% endtabs %}

**Example traccar.xml:**

```xml
<entry key='tk103.port'>5002</entry>
<entry key='gt06.port'>5023</entry>
<entry key='teltonika.port'>5027</entry>
<entry key='osmand.port'>5055</entry>
```

### Configure Emulator Ports

**In `config.yaml`:**

```yaml
servers:
  tk103:
    enabled: true
    host: localhost
    port: 5002        # Must match Traccar!
    protocol: tcp

  gt06:
    enabled: true
    host: localhost
    port: 5023        # Must match Traccar!
    protocol: tcp
```

---

## Manual Device Creation

If `TRACCAR_AUTO_CREATE_DEVICES=false`, create devices manually:

### Method 1: Traccar Web Interface

![Traccar Add Device Dialog](/.gitbook/assets/screenshots/traccar-add-device-dialog.png)

{% hint style="info" %}
**📸 IMAGE À CAPTURER:**
- Screenshot Traccar "Add Device" dialog ouvert
- Champs visibles:
  - Name: "Test Vehicle 001"
  - Identifier: "357938506404024"
  - Category: dropdown avec "Car" sélectionné
- Bouton "Save" visible
- Ajouter flèches vers les champs importants
- Annotation: "Enter device identifier from emulator"
- Résolution: 1280x720
{% endhint %}

**Step 1: Login to Traccar**
- Go to http://localhost:8082
- Login with admin credentials

**Step 2: Add Device**
1. Click **Settings** → **Devices**
2. Click **+** (Add Device)
3. Fill information:
   - **Name:** Any name (e.g., "Test Vehicle 1")
   - **Identifier:** Device unique ID from emulator
   - **Category:** Vehicle/Car/Truck
4. Click **Save**

**Step 3: Get Device Unique ID**

From emulator:

{% tabs %}
{% tab title="Web Interface" %}
1. Go to emulator dashboard
2. Find device in list
3. Look for "Unique ID" field
4. Copy the ID (e.g., "357938506404024")
{% endtab %}

{% tab title="API" %}
```bash
curl http://localhost:5000/api/multidevice/devices/DEVICE_ID

# Response includes "unique_id" field
```
{% endtab %}
{% endtabs %}

### Method 2: API Call

**Using emulator's API:**

```bash
curl -X POST http://localhost:5000/api/add_traccar_device \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": "tk103",
    "device_id": "357938506404024",
    "device_name": "Test Vehicle 001"
  }'
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

## Viewing Devices in Traccar

### Map View

**Access:**
1. Login to Traccar: http://localhost:8082
2. Main screen shows map with all devices
3. Click device to see details

**Device Status:**
- 🟢 **Online** - Device sending data (green)
- 🔴 **Offline** - No recent data (red/gray)
- 🟡 **Unknown** - Status unknown (yellow)

### Device Information

**Click on device to see:**
- Current position (latitude, longitude)
- Speed (km/h or mph)
- Course/heading (degrees)
- Altitude (meters)
- Last update timestamp
- Address (reverse geocoding)

### Historical Data

**View device history:**
1. Click device
2. Select date/time range
3. Click "Play" to replay route
4. View speed graph and timeline

---

## Testing Integration

### Test Connection

**Check if emulator can connect to Traccar:**

```bash
curl -X POST http://localhost:5000/api/traccar/test
```

**Success response:**
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

**Failure response:**
```json
{
  "success": false,
  "error": "Failed to connect to Traccar",
  "details": "Connection refused to localhost:8082"
}
```

### Verify Device Appears

**Check device status:**

{% tabs %}
{% tab title="Emulator API" %}
```bash
curl http://localhost:5000/api/multidevice/devices/DEVICE_ID/traccar-status
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
{% endtab %}

{% tab title="Traccar API" %}
```bash
curl -u admin:admin http://localhost:8082/api/devices
```

Lists all devices in Traccar.
{% endtab %}
{% endtabs %}

### Monitor Real-Time Updates

![Emulator and Traccar Side by Side](/.gitbook/assets/screenshots/emulator-traccar-side-by-side.png)

{% hint style="info" %}
**📸 IMAGE À CAPTURER:**
- Split screen montrant:
  - Gauche: Emulator dashboard (http://localhost:5000)
  - Droite: Traccar map view (http://localhost:8082)
- Même device visible dans les deux interfaces
- Position synchronisée visible
- Timestamps identiques ou très proches
- Ajouter ligne ou flèche montrant la synchronisation
- Annotation: "Real-time synchronization between emulator and Traccar"
- Résolution: 1920x1080
{% endhint %}

![Traccar Integration Workflow](/.gitbook/assets/gifs/traccar-integration-workflow.gif)

{% hint style="info" %}
**📸 GIF ANIMÉ À CRÉER:**
- Animation 20-30 secondes du workflow complet:
  1. Configure emulator (.env file)
  2. Create device in emulator
  3. Start device
  4. Switch to Traccar interface
  5. Device appears automatically
  6. Watch position updates in real-time
- Montrer les deux interfaces (split screen ou alternance)
- Ajouter annotations pour chaque étape
- Format: GIF optimisé < 8MB
- FPS: 10-15
{% endhint %}

**Watch device updates:**

1. Open emulator dashboard: http://localhost:5000
2. Open Traccar: http://localhost:8082
3. Start device in emulator
4. Watch position update in both interfaces
5. Updates every 10 seconds (default)

---

## Troubleshooting

### Device Not Appearing in Traccar

{% hint style="danger" %}
**Problem:** Device created in emulator but not in Traccar
{% endhint %}

**Solutions:**

1. **Check auto-create is enabled:**
   ```bash
   TRACCAR_AUTO_CREATE_DEVICES=true
   ```

2. **Verify Traccar is running:**
   ```bash
   curl http://localhost:8082
   ```

3. **Check credentials:**
   ```bash
   TRACCAR_USERNAME=admin
   TRACCAR_PASSWORD=admin
   ```

4. **Test connection:**
   ```bash
   curl -X POST http://localhost:5000/api/traccar/test
   ```

5. **Create device manually** in Traccar

### Device Shows Offline in Traccar

{% hint style="warning" %}
**Problem:** Device exists but shows offline/no position
{% endhint %}

**Checklist:**

1. ✅ **Device started in emulator?**
   - Status must be "running"

2. ✅ **Correct protocol port?**
   - TK103: Port 5002
   - GT06: Port 5023
   - Check `config.yaml` and `traccar.xml`

3. ✅ **Firewall not blocking?**
   ```bash
   # Linux - Allow port
   sudo ufw allow 5002/tcp
   ```

4. ✅ **Traccar protocol enabled?**
   - Check `traccar.xml` has protocol entry
   - Restart Traccar after config changes

### Wrong Position or Not Moving

{% hint style="warning" %}
**Problem:** Position incorrect or device not moving
{% endhint %}

**Solutions:**

1. **Check device is running:**
   - Dashboard status = "running"

2. **Verify route is set:**
   ```bash
   curl http://localhost:5000/api/device/DEVICE_ID/route
   ```

3. **Check update interval:**
   ```yaml
   simulation:
     update_interval: 10.0  # Seconds
   ```

4. **Monitor device in emulator:**
   - Position should update every 10 seconds
   - Speed should be > 0 when moving

5. **Check Traccar last update:**
   - Should be recent (< 1 minute)

### Connection Timeout

{% hint style="danger" %}
**Error:** Connection timeout or refused
{% endhint %}

**Solutions:**

1. **Traccar running on different machine?**
   ```bash
   TRACCAR_HOST=192.168.1.100  # Use actual IP
   ```

2. **Firewall blocking connection?**
   - Allow port 8082 (web interface)
   - Allow protocol ports (5001-5232)

3. **Network issues?**
   ```bash
   ping 192.168.1.100
   telnet 192.168.1.100 8082
   ```

---

## Advanced Configuration

### Remote Traccar Server

**For Traccar on different machine:**

```bash
# .env
TRACCAR_HOST=192.168.1.100      # Traccar server IP
TRACCAR_PORT=8082
```

**Or domain name:**

```bash
TRACCAR_HOST=traccar.example.com
TRACCAR_PORT=8082
```

### Multiple Traccar Instances

**Route different devices to different Traccar servers:**

Not directly supported, but can be achieved by:
1. Running multiple emulator instances
2. Each configured for different Traccar server
3. Different web ports (5000, 5001, 5002...)

### HTTPS/SSL Traccar

**For Traccar with HTTPS:**

```bash
TRACCAR_HOST=https://traccar.example.com
TRACCAR_PORT=443
```

---

## Best Practices

### Production Deployment

{% hint style="success" %}
**Recommended configuration for production:**
{% endhint %}

```bash
# .env - Production
TRACCAR_HOST=traccar.company.com
TRACCAR_PORT=8082
TRACCAR_USERNAME=api_user          # Dedicated API user
TRACCAR_PASSWORD=SecurePassword123!
TRACCAR_AUTO_CREATE_DEVICES=true
TRACCAR_DEVICE_PREFIX=TEST_        # Identify test devices
```

### Security

1. **Change default password:**
   - Never use admin/admin in production

2. **Create dedicated API user:**
   - Traccar → Settings → Users → Add User
   - Grant only necessary permissions

3. **Use HTTPS:**
   - Enable SSL/TLS on Traccar
   - Secure communication

4. **Restrict network access:**
   - Firewall rules
   - VPN for remote access

### Performance

1. **Adjust update interval:**
   ```yaml
   simulation:
     update_interval: 30.0  # Slower = less load
   ```

2. **Limit active devices:**
   - Don't run 100 devices unnecessarily
   - Stop devices when not needed

3. **Monitor Traccar resources:**
   - CPU, memory, database size
   - Regular maintenance

---

## Next Steps

{% content-ref url="creating-devices.md" %}
[creating-devices.md](creating-devices.md)
{% endcontent-ref %}

{% content-ref url="custom-routes.md" %}
[custom-routes.md](custom-routes.md)
{% endcontent-ref %}

{% content-ref url="../support/troubleshooting.md" %}
[troubleshooting.md](../support/troubleshooting.md)
{% endcontent-ref %}

---

*Last updated: October 2025*
