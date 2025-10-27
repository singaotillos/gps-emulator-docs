# Managing Devices

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
