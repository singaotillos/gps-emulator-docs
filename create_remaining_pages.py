import os

# Pages à créer avec contenu minimal mais complet
pages = {
    "user-guide/dashboard-overview.md": """# Dashboard Overview

Complete guide to the web dashboard interface.

---

## Interface Layout

The dashboard provides a modern, responsive interface for managing GPS devices.

### Main Components

1. **Top Navigation Bar**
   - Logo and branding
   - System status
   - User menu
   - Settings

2. **Device List**
   - All devices with status
   - Real-time updates
   - Quick actions (Start/Stop/Delete)

3. **Device Details Panel**
   - Current position
   - Speed, fuel, battery
   - Statistics

4. **Map View** (coming soon)
   - Real-time device positions
   - Route visualization

---

## Creating Devices

Click "Create New Device" button to add devices.

See {% content-ref url="creating-devices.md" %}[creating-devices.md](creating-devices.md){% endcontent-ref %}

---

## Device Status Icons

- 🟢 **Running** - Device active and sending data
- 🔴 **Stopped** - Device stopped
- ⚠️ **Error** - Device has errors

---

*Last updated: October 2025*
""",

    "user-guide/managing-devices.md": """# Managing Devices

Complete guide to device management operations.

---

## Starting Devices

**Via Web Interface:**
1. Find device in list
2. Click "Start" button
3. Device begins sending data

**Via API:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
```

---

## Stopping Devices

**Via Web Interface:**
1. Find running device
2. Click "Stop" button
3. Device stops sending data

**Via API:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop
```

---

## Updating Configuration

1. Stop device first
2. Click "Edit" button
3. Modify settings
4. Save changes
5. Restart device

---

## Deleting Devices

{% hint style="warning" %}
Device must be stopped before deletion
{% endhint %}

**Steps:**
1. Stop device
2. Click "Delete" button
3. Confirm deletion

---

## Bulk Operations

**Start multiple devices:**
- Select devices (checkboxes)
- Click "Start Selected"

**Stop multiple devices:**
- Select devices
- Click "Stop Selected"

---

## Monitoring

**Real-time updates:**
- Position updates every 10 seconds (default)
- Status changes instant
- Statistics updated live

---

*Last updated: October 2025*
""",

    "protocols/popular-protocols/tk103.md": """# TK103 Protocol

Complete guide to TK103 GPS tracker protocol.

---

## Overview

TK103 is one of the most popular GPS tracker protocols.

**Manufacturer:** Xexun
**Type:** Binary protocol over TCP
**Port:** 5002 (default in Traccar)
**Popularity:** ⭐⭐⭐⭐⭐ Very High

---

## Device Information

**Models supporting TK103:**
- TK103-2B
- TK103A
- TK103B
- TK102-2
- And many clones

**Features:**
- Real-time GPS tracking
- GSM communication
- Remote commands
- Geofencing
- Alarms and alerts

---

## Configuration

**In emulator:**
```json
{
  "protocol": "tk103",
  "device_model": "TK103-2B",
  "device_id": "357938506404024"
}
```

**Device ID format:**
- IMEI format: 15 digits
- Example: 357938506404024

---

## Traccar Setup

1. **Enable TK103 in traccar.xml:**
```xml
<entry key='tk103.port'>5002</entry>
```

2. **Create device in Traccar:**
   - Protocol: tk103
   - Identifier: Device IMEI

3. **Start emulator device**

---

## Commands

TK103 supports remote commands:
- `tracker` - Get device status
- `apn` - Set APN settings
- `url` - Set server URL
- `adminip` - Set server IP

---

*Last updated: October 2025*
""",

    "protocols/popular-protocols/gt06.md": """# GT06 Protocol

Complete guide to GT06/CRX1 GPS tracker protocol.

---

## Overview

GT06 is a widely used GPS tracker protocol.

**Manufacturer:** Various (Concox, Jimi, etc.)
**Type:** Binary protocol over TCP
**Port:** 5023 (default in Traccar)
**Popularity:** ⭐⭐⭐⭐⭐ Very High

---

## Device Information

**Models:**
- GT06N
- GT02
- GV55
- JM-VL03
- Many clones

---

## Configuration

```json
{
  "protocol": "gt06",
  "device_model": "GT06N",
  "device_id": "868683031234567"
}
```

---

*Last updated: October 2025*
""",

    "protocols/popular-protocols/teltonika.md": """# Teltonika Protocol

Professional GPS tracker protocol.

---

## Overview

Teltonika is a professional-grade GPS tracking protocol.

**Manufacturer:** Teltonika
**Type:** Binary AVL protocol over TCP
**Port:** 5027
**Popularity:** ⭐⭐⭐⭐ High (Professional)

---

## Models

- FMB920
- FMB125
- FMC125
- FMT100

---

*Last updated: October 2025*
""",

    "protocols/popular-protocols/osmand.md": """# OsmAnd Protocol

HTTP-based GPS tracking protocol.

---

## Overview

OsmAnd is a simple HTTP-based GPS protocol.

**Type:** HTTP GET/POST
**Port:** 5055
**Popularity:** ⭐⭐⭐⭐ High

---

## Perfect For

- Mobile applications
- Web-based tracking
- Simple integration

---

*Last updated: October 2025*
"""
}

# Créer les pages
for path, content in pages.items():
    full_path = path
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {path}")

print(f"\nCreated {len(pages)} pages successfully!")
