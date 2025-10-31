# Managing Devices

Complete guide to device management operations.

---

## Starting Devices

![Device List with Start Button](/.gitbook/assets/screenshots/device-list-start-button.png)

**Via Web Interface:**
1. Find device in dropdown **"By Protocol"** or **"By Device"**
2. Click "Start" button
3. Device begins sending data

**Via API:**
```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
```

---

## Stopping Devices

![Device Running with Stop Button](/.gitbook/assets/screenshots/device-running-stop-button.png)

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

![Device Edit Configuration Dialog](/.gitbook/assets/screenshots/device-edit-config-dialog.png)

1. Click "Edit" button (device can be running or stopped)
2. Modify **Device configuration** settings
3. Save changes

---

## Deleting Devices

![Device Delete Confirmation](/.gitbook/assets/screenshots/device-delete-confirmation.png)

**Steps:**
1. Click "Delete" button
2. Confirm deletion

---

## Bulk Operations

![Bulk Device Operations](/.gitbook/assets/screenshots/bulk-device-operations.png)

{% hint style="info" %}
**📸 IMAGE À CAPTURER:**
- Dashboard montrant le champ "Count device to add"
- Interface pour ajouter plusieurs devices en masse
- Montrer le formulaire de création en masse
- Résolution: 1920x1080
{% endhint %}

**Add multiple devices:**
- Use **"Count device to add"** field
- Configure device settings
- Create devices in batch

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
