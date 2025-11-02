# Popular Protocols

The GPS Tracker Emulator supports over 80 GPS protocols. This section covers the most popular and widely-used protocols for GPS tracking.

---

## Most Popular Protocols

These protocols are recommended for most users due to their widespread adoption, reliability, and ease of use.

### 🌟 TK103 Protocol

**Best for:** Beginners and general-purpose testing

- **Device Type:** Vehicle trackers
- **Difficulty:** ⭐ Easy
- **Traccar Support:** ✅ Full
- **Common Devices:** TK103-2B, TK103A, TK103B+

The TK103 protocol is one of the most popular GPS tracking protocols worldwide. It's simple, reliable, and supported by countless GPS tracker manufacturers.

{% content-ref url="popular-protocols/tk103.md" %}
[tk103.md](popular-protocols/tk103.md)
{% endcontent-ref %}

---

### 🌟 GT06 Protocol

**Best for:** Common Chinese GPS trackers

- **Device Type:** Vehicle trackers, personal trackers
- **Difficulty:** ⭐ Easy
- **Traccar Support:** ✅ Full
- **Common Devices:** GT06N, GT06E, ConcoxGT06

The GT06 protocol is widely used in affordable GPS trackers from Chinese manufacturers. It uses binary communication and supports various features like fuel monitoring, temperature sensors, and relay control.

{% content-ref url="popular-protocols/gt06.md" %}
[gt06.md](popular-protocols/gt06.md)
{% endcontent-ref %}

---

### 🌟 Teltonika Protocol

**Best for:** Professional fleet management

- **Device Type:** Professional fleet trackers
- **Difficulty:** ⭐⭐ Medium
- **Traccar Support:** ✅ Full
- **Common Devices:** FMB920, FMB125, FMB140

Teltonika is a premium GPS tracking solution used in professional fleet management. Their protocol supports advanced features like CAN bus data, driver identification, and extensive I/O capabilities.

{% content-ref url="popular-protocols/teltonika.md" %}
[teltonika.md](popular-protocols/teltonika.md)
{% endcontent-ref %}

---

### 🌟 OsmAnd Protocol

**Best for:** Mobile app testing and development

- **Device Type:** Mobile apps (iOS/Android)
- **Difficulty:** ⭐ Easy
- **Traccar Support:** ✅ Full
- **Common Apps:** OsmAnd, GPS Logger

OsmAnd is an HTTP-based protocol designed for mobile applications. It's simple, uses JSON/URL parameters, and is perfect for testing location-based mobile apps.

{% content-ref url="popular-protocols/osmand.md" %}
[osmand.md](popular-protocols/osmand.md)
{% endcontent-ref %}

---

## Quick Comparison

| Protocol | Difficulty | Use Case | Port | Format |
|----------|-----------|----------|------|--------|
| **TK103** | ⭐ Easy | General-purpose | 5002 | Text |
| **GT06** | ⭐ Easy | Budget trackers | 5023 | Binary |
| **Teltonika** | ⭐⭐ Medium | Professional fleet | 5027 | Binary |
| **OsmAnd** | ⭐ Easy | Mobile apps | 5055 | HTTP/JSON |

---

## Other Notable Protocols

### GPS103
- **Use Case:** Similar to TK103, text-based protocol
- **Port:** 5001
- **Difficulty:** ⭐ Easy

### H02
- **Use Case:** Common in Chinese trackers
- **Port:** 5013
- **Difficulty:** ⭐ Easy

### Watch Protocol
- **Use Case:** GPS watches and wearables
- **Port:** 5093
- **Difficulty:** ⭐ Easy

### Huabao (JT808)
- **Use Case:** Chinese government standard for fleet tracking
- **Port:** 5016
- **Difficulty:** ⭐⭐⭐ Advanced

---

## Choosing the Right Protocol

### For Beginners
**Recommended:** TK103 or OsmAnd
- Simple text-based protocols
- Easy to understand and debug
- Wide device support
- Extensive documentation

### For Mobile Development
**Recommended:** OsmAnd
- HTTP-based (easy to implement)
- JSON format
- No binary parsing required
- Works with any HTTP client

### For Professional Fleet
**Recommended:** Teltonika
- Advanced features (CAN bus, I/O)
- High reliability
- Enterprise-grade
- Extensive sensor support

### For Budget Testing
**Recommended:** GT06 or GPS103
- Low-cost devices available
- Simple implementation
- Good feature set
- Reliable performance

---

## Protocol Features Comparison

| Feature | TK103 | GT06 | Teltonika | OsmAnd |
|---------|-------|------|-----------|--------|
| **Position tracking** | ✅ | ✅ | ✅ | ✅ |
| **Speed/altitude** | ✅ | ✅ | ✅ | ✅ |
| **Engine control** | ✅ | ✅ | ✅ | ❌ |
| **Fuel monitoring** | ❌ | ✅ | ✅ | ❌ |
| **Temperature sensors** | ❌ | ✅ | ✅ | ❌ |
| **CAN bus data** | ❌ | ❌ | ✅ | ❌ |
| **Driver ID** | ❌ | ❌ | ✅ | ❌ |
| **Mobile-friendly** | ❌ | ❌ | ❌ | ✅ |
| **HTTP-based** | ❌ | ❌ | ❌ | ✅ |

---

## Getting Started

### 1. Choose Your Protocol

Based on your use case, select one of the protocols above.

### 2. Create a Device

{% tabs %}
{% tab title="Web Interface" %}
1. Open dashboard: http://localhost:5000
2. Click **Create New Device**
3. Select protocol from dropdown
4. Fill device information
5. Click **Create Device**
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

### 3. Start Simulation

Start the device to begin sending GPS data:

```bash
curl -X POST http://localhost:5000/api/multidevice/devices/DEVICE_ID/start
```

### 4. View in Traccar

Open Traccar (http://localhost:8082) to see your device on the map in real-time.

---

## Learn More

{% content-ref url="overview.md" %}
[overview.md](overview.md)
{% endcontent-ref %}

{% content-ref url="all-protocols.md" %}
[all-protocols.md](all-protocols.md)
{% endcontent-ref %}

{% content-ref url="protocol-id-formats.md" %}
[protocol-id-formats.md](protocol-id-formats.md)
{% endcontent-ref %}

---

## Need Help?

- **Can't find your protocol?** Check [All Protocols A-Z](all-protocols.md)
- **Having issues?** See [Troubleshooting](../support/troubleshooting.md)
- **Need examples?** Check [Code Examples](../api-reference/code-examples.md)

---

*Last updated: November 2025*
