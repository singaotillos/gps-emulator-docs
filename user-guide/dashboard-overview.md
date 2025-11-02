# Dashboard Overview

Complete guide to the web dashboard interface.

![Dashboard Overview](/.gitbook/assets/screenshots/dashboard_overview.png)

---

## Interface Layout

The dashboard provides a modern, responsive interface for managing GPS devices.

### Main Components

1. **Top Navigation Bar**
   - Logo and branding
   - System status
   - Settings button (gear icon + Traccar)

2. **Device List**
   - All devices with status
   - Real-time updates
   - Quick actions (Start/Stop/Delete)

![Device List View](/.gitbook/assets/screenshots/device_list.png)

3. **Device Details Panel**
   - Current position
   - Speed, fuel, battery
   - Statistics

4. **Map View**
   - Real-time device positions
   - Route visualization
   - Interactive controls

![Real-Time Map View](/.gitbook/assets/screenshots/Step4_View_Real_time_Map.png)

---

## Traccar Configuration

The dashboard includes a **Traccar** button in the top-right corner for configuring automatic device synchronization with your Traccar server.

### Accessing Traccar Configuration

Click the **Traccar** button (gear icon) in the top navigation bar to open the configuration dialog.

![Traccar Configuration Dialog](/.gitbook/assets/screenshots/traccar_configuration_dialog.png)

### Configuration Options

The Traccar Configuration dialog allows you to:

1. **Traccar Server**
   - Enter your Traccar server address
   - Format: `host:port` (e.g., `localhost:8082`)
   - Default: `localhost:8082`

2. **Login / Email**
   - Your Traccar username or email
   - Default: `admin`

3. **Password**
   - Your Traccar account password
   - Default: `admin`

4. **Automatic Synchronization**
   - ✓ **Enabled**: Devices automatically created in Traccar
   - Unchecked: Manual device creation required

### Quick Setup

{% hint style="info" %}
**Default Credentials:** Use `admin` for both username and password (Traccar defaults)
{% endhint %}

**To configure Traccar integration:**

1. Click **Traccar** button (top-right)
2. Enter server: `localhost:8082`
3. Enter username: `admin`
4. Enter password: `admin`
5. Check **Automatic synchronization**
6. Click **Test Connection** to verify
7. Click **Save**

Configuration is automatically saved to `.env` file.

### Test Connection

Before saving, click **Test Connection** to verify:
- ✅ Server is reachable
- ✅ Credentials are correct
- ✅ API access is working

{% hint style="success" %}
**Automatic Sync Enabled:** All new devices will be automatically created in Traccar!
{% endhint %}

For detailed Traccar integration guide, see:
{% content-ref url="traccar-integration.md" %}
[traccar-integration.md](traccar-integration.md)
{% endcontent-ref %}

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
