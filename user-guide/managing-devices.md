# Managing Devices

Complete guide to device management operations.

---

## Starting Devices

![Device List with Start Button](/.gitbook/assets/screenshots/device-list-start-button.png)

**Via Web Interface:**
1. Locate your device in the **Active Protocols** section
2. Click the green **Play icon** (▶️) button on the device card
3. Device status changes to "active" and begins sending data

**Via API:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
```

---

## Stopping Devices

![Device Running with Stop Button](/.gitbook/assets/screenshots/device-running-stop-button.png)

**Via Web Interface:**
1. Locate the running device (green indicator shows "active")
2. Click the blue **Stop icon** (⏸️) button on the device card
3. Device status changes to "stopped" and stops sending data

**Via API:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/stop
```

---

## Updating Configuration

![Device Edit Configuration Dialog](/.gitbook/assets/screenshots/device-edit-config-dialog.png)

**Steps:**
1. Click the blue **Settings icon** (⚙️) on the device card
2. A modal dialog "Device Configuration" opens
3. Modify settings:
   - **Route**: Select from dropdown (Paris, London, etc.)
   - **Send frequency (seconds)**: Adjust update interval
4. Click **"Save"** to apply changes or **"Cancel"** to discard

{% hint style="info" %}
You can configure a device while it's running or stopped.
{% endhint %}

---

## Deleting Devices

![Device Delete Confirmation](/.gitbook/assets/screenshots/device-delete-confirmation.png)

**Steps:**
1. Click the red **Delete icon** (🗑️) on the device card
2. A confirmation dialog appears
3. Confirm deletion by clicking the delete button

{% hint style="info" %}
You can delete a device whether it's running or stopped.
{% endhint %}

---

## Bulk Operations

### Creating Multiple Devices at Once

You can create multiple devices simultaneously using the **Quick Device Addition** section.

**Steps:**
1. In the **Quick Device Addition** section, select a tab:
   - **By Protocol**: Select protocol first, then device model
   - **By Device**: Select device model directly
2. Choose the **Route** (Paris, London, Berlin, Tokyo, New York)
3. Set the **Count** field to the number of devices you want to create (1-10)
4. Click the green **"+ Add"** button
5. Multiple devices will be created with the same configuration

{% hint style="success" %}
**Example**: Set Count to 5 and select TK103 protocol → Creates 5 TK103 devices instantly!
{% endhint %}

---

## Monitoring

![Real-time Device Monitoring](/.gitbook/assets/screenshots/device-monitoring-realtime.png)

{% hint style="info" %}
**📸 IMAGE À CAPTURER:**
- Dashboard montrant device en cours d'exécution
- Position actuelle (latitude, longitude, speed) visible et en cours de mise à jour
- Statistiques: packets sent, uptime, distance
- Indicateur de mise à jour en temps réel (animation ou timestamp récent)
- Graphe ou historique de speed/position si disponible
- Résolution: 1920x1080
{% endhint %}

![Device Management Workflow](/.gitbook/assets/gifs/device-management-workflow.gif)

{% hint style="info" %}
**📸 GIF ANIMÉ À CRÉER:**
- Animation 15-20 secondes montrant le workflow complet
- Séquence: Start device → Monitor updates → Stop device → Edit config → Restart
- Montrer les changements en temps réel (position updates)
- Ajouter annotations pour chaque étape
- Format: GIF optimisé < 5MB
- FPS: 10-15
{% endhint %}

**Real-time updates:**
- Position updates every 10 seconds (default)
- Status changes instant
- Statistics updated live

---

*Last updated: October 2025*
