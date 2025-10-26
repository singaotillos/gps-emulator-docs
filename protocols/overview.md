# Protocols Overview

Learn about the 86 GPS tracking protocols supported by the emulator.

---

## What are GPS Protocols?

GPS tracking protocols are communication standards that define how GPS devices send location data to servers. Each manufacturer often has their own protocol format.

The Universal GPS Tracker Emulator supports **86 different protocols**, making it the most comprehensive GPS emulation solution available.

---

## Protocol Categories

### By Data Format

| Category | Count | Examples | Description |
|----------|-------|----------|-------------|
| **Binary** | 45 | TK103, GT06, Teltonika | Compact binary data format |
| **Text** | 28 | GPS103, H02, TAIP | Human-readable ASCII format |
| **HTTP** | 13 | OsmAnd, GPSGate | HTTP-based REST APIs |

### By Popularity

{% tabs %}
{% tab title="Most Popular" %}
### Top 10 Most Used Protocols

1. **TK103** - Most common GPS tracker protocol
2. **GT06** - Widely used in Chinese devices
3. **Teltonika** - Professional fleet tracking
4. **OsmAnd** - Mobile app tracking
5. **H02** - Simple text-based protocol
6. **GPS103** - Legacy but still popular
7. **Meiligao** - Common in Asia
8. **GT02** - Variant of GT06
9. **Concox** - Budget-friendly devices
10. **Suntech** - Commercial fleet devices

{% hint style="success" %}
**Quick Start:** Begin with TK103 or GT06 - they're the most widely supported!
{% endhint %}
{% endtab %}

{% tab title="By Region" %}
### Regional Distribution

**Asia (35 protocols)**
- TK103, GT06, Meiligao, Concox, H02, JT600, JT808, Huabao, etc.
- Dominant in consumer market

**Europe (25 protocols)**
- Teltonika, Galileo, Arnavi, Retranslator, etc.
- Focus on professional fleet management

**Americas (15 protocols)**
- CalAmp, Suntech, Queclink, etc.
- Commercial and enterprise focus

**Global (11 protocols)**
- OsmAnd, GPSGate, Wialon, etc.
- Platform-agnostic solutions
{% endtab %}

{% tab title="By Use Case" %}
### Common Use Cases

**Personal Tracking**
- OsmAnd, GPS103, TK102, Watch

**Fleet Management**
- Teltonika, CalAmp, Queclink, Suntech

**Asset Tracking**
- Concox, Meitrack, iStartek

**Pet Tracking**
- TK103, Watch protocols

**Marine Tracking**
- AIS, Navigil

**Cold Chain**
- Teltonika (with temperature sensors)
{% endtab %}
{% endtabs %}

---

## Complete Protocol List

### A-D

| Protocol | Port | Type | Manufacturer | Popularity |
|----------|------|------|--------------|------------|
| ADM | 5015 | Binary | ADM | ⭐⭐ |
| AIS | 5175 | Text | Marine | ⭐⭐ |
| Aplicom | 5121 | Binary | Aplicom | ⭐⭐ |
| AppTrack | 5182 | HTTP | Various | ⭐⭐ |
| Arnavi | 5047 | Binary | Arnavi | ⭐⭐⭐ |
| Atrack | 5001 | Binary | Atrack | ⭐⭐⭐ |
| AutoFon | 5046 | Binary | AutoFon | ⭐⭐ |
| AVL301 | 5164 | Binary | SeeMe | ⭐ |
| BCM | 5022 | Binary | BCM | ⭐ |
| BlackKite | 5141 | Binary | BlackKite | ⭐⭐ |
| CalAmp | 5082 | Binary | CalAmp | ⭐⭐⭐⭐ |
| CarTrack | 5006 | Binary | CarTrack | ⭐⭐ |
| Castel | 5116 | Binary | Castel | ⭐⭐⭐ |
| CellocatorX | 5097 | Binary | Cellocator | ⭐⭐ |
| CITEC | 5160 | Binary | CITEC | ⭐⭐ |
| Concox | 5158 | Binary | Concox | ⭐⭐⭐⭐ |
| Disha | 5190 | Binary | Disha | ⭐ |
| DMT | 5191 | Binary | DMT | ⭐⭐ |

### E-K

| Protocol | Port | Type | Manufacturer | Popularity |
|----------|------|------|--------------|------------|
| EasyTrack | 5113 | Binary | EasyTrack | ⭐⭐ |
| EelLink | 5192 | Binary | EelLink | ⭐⭐ |
| Enfora | 5008 | Text | Enfora | ⭐⭐ |
| Fifotrack | 5198 | Binary | Fifotrack | ⭐⭐⭐ |
| Fox | 5118 | Binary | Fox | ⭐⭐ |
| Galileo | 5024 | Binary | Galileo | ⭐⭐⭐ |
| GL100 | 5003 | Binary | Queclink | ⭐⭐⭐ |
| GL200 | 5004 | Binary | Queclink | ⭐⭐⭐⭐ |
| GlobalSat | 5060 | Binary | GlobalSat | ⭐⭐ |
| GoSafe | 5140 | Binary | GoSafe | ⭐⭐ |
| GPS103 | 5001 | Text | Various | ⭐⭐⭐⭐⭐ |
| GPSGate | 5026 | HTTP | GateHouse | ⭐⭐⭐ |
| GPSMarker | 5065 | Text | GPSMarker | ⭐⭐ |
| GpsWay | 5195 | Binary | GpsWay | ⭐ |
| GT02 | 5022 | Binary | Various | ⭐⭐⭐⭐ |
| GT06 | 5023 | Binary | Various | ⭐⭐⭐⭐⭐ |
| Gurtam | 5067 | Binary | Gurtam | ⭐⭐⭐ |
| H02 | 5013 | Text | Various | ⭐⭐⭐⭐⭐ |
| Huabao | 5015 | Binary | Huabao | ⭐⭐⭐ |
| Huashi | 5126 | Binary | Huashi | ⭐⭐ |
| iStartek | 5148 | Binary | iStartek | ⭐⭐ |
| JT600 | 5014 | Binary | JiMi | ⭐⭐⭐ |
| JT808 | 5016 | Binary | JiMi | ⭐⭐⭐⭐ |
| Kenji | 5193 | Binary | Kenji | ⭐ |
| KHD | 5188 | Binary | KHD | ⭐⭐ |

### L-Z

| Protocol | Port | Type | Manufacturer | Popularity |
|----------|------|------|--------------|------------|
| Laipac | 5161 | Binary | Laipac | ⭐⭐ |
| M2C | 5178 | Binary | M2C | ⭐ |
| M2M | 5184 | Binary | M2M | ⭐⭐ |
| Maestro | 5196 | Binary | Maestro | ⭐ |
| Megastek | 5024 | Binary | Megastek | ⭐⭐⭐ |
| Meiligao | 5009 | Binary | Meiligao | ⭐⭐⭐⭐ |
| Meitrack | 5020 | Binary | Meitrack | ⭐⭐⭐⭐ |
| MXT | 5167 | Binary | MXT | ⭐⭐ |
| Navis | 5019 | Binary | Navis | ⭐⭐⭐ |
| Navigil | 5025 | Binary | Navigil | ⭐⭐ |
| Noran | 5189 | Binary | Noran | ⭐⭐ |
| OsmAnd | 5055 | HTTP | OsmAnd | ⭐⭐⭐⭐⭐ |
| Piligrim | 5194 | Binary | Piligrim | ⭐ |
| Position | 5187 | Binary | Position | ⭐ |
| Progress | 5012 | Binary | Progress | ⭐⭐ |
| PT502 | 5017 | Binary | Xexun | ⭐⭐⭐ |
| Queclink | 5174 | Binary | Queclink | ⭐⭐⭐⭐ |
| Retranslator | 5068 | Binary | Retranslator | ⭐⭐ |
| S168 | 5153 | Binary | S168 | ⭐⭐ |
| SafeRoute | 5186 | Binary | SafeRoute | ⭐ |
| Sanav | 5197 | Binary | Sanav | ⭐ |
| Skypatrol | 5021 | Binary | Skypatrol | ⭐⭐⭐ |
| Suntech | 5011 | Text | Suntech | ⭐⭐⭐⭐ |
| T55 | 5005 | Text | Coban | ⭐⭐⭐⭐ |
| TAIP | 5048 | Text | Trimble | ⭐⭐⭐ |
| Teltonika | 5027 | Binary | Teltonika | ⭐⭐⭐⭐⭐ |
| TK102 | 5002 | Text | Xexun | ⭐⭐⭐⭐ |
| TK103 | 5002 | Text | Xexun | ⭐⭐⭐⭐⭐ |
| Totem | 5007 | Text | Totem | ⭐⭐⭐ |
| TR20 | 5018 | Binary | TR20 | ⭐⭐ |
| TRV | 5010 | Binary | TRV | ⭐⭐ |
| TZone | 5145 | Binary | TZone | ⭐⭐ |
| UlboTech | 5180 | Binary | UlboTech | ⭐⭐ |
| V680 | 5016 | Binary | Jointech | ⭐⭐ |
| Visiontek | 5181 | Binary | Visiontek | ⭐⭐ |
| Watch | 5093 | Binary | Various | ⭐⭐⭐ |
| Wialon | 5081 | Text | Wialon | ⭐⭐⭐⭐ |
| Xexun | 5006 | Text | Xexun | ⭐⭐⭐ |

---

## Choosing the Right Protocol

### Decision Tree

```
START: What are you testing?

├─ Mobile App Integration?
│  └─ Use: OsmAnd (HTTP-based, easy to integrate)
│
├─ Commercial Fleet System?
│  ├─ Europe → Use: Teltonika
│  ├─ Americas → Use: CalAmp or Suntech
│  └─ Asia → Use: Meitrack or Concox
│
├─ Budget Consumer Devices?
│  └─ Use: TK103, GT06, or H02
│
├─ Maximum Compatibility?
│  └─ Use: TK103 (most widely supported)
│
└─ Testing Multiple Protocols?
   └─ Start with: TK103, GT06, Teltonika, OsmAnd
```

### Recommendations by Scenario

| Scenario | Recommended Protocol | Why |
|----------|---------------------|-----|
| **First Time User** | TK103 | Most common, well-documented |
| **Mobile App** | OsmAnd | HTTP-based, modern |
| **Professional Fleet** | Teltonika | Rich features, reliable |
| **Quick Testing** | GT06 | Simple, fast |
| **Multi-Protocol** | All Top 10 | Best coverage |

---

## Protocol Features Comparison

### Data Fields Support

| Feature | TK103 | GT06 | Teltonika | OsmAnd | H02 |
|---------|-------|------|-----------|---------|-----|
| GPS Position | ✅ | ✅ | ✅ | ✅ | ✅ |
| Speed | ✅ | ✅ | ✅ | ✅ | ✅ |
| Altitude | ✅ | ✅ | ✅ | ✅ | ✅ |
| Heading | ✅ | ✅ | ✅ | ✅ | ✅ |
| Battery | ✅ | ✅ | ✅ | ✅ | ❌ |
| Fuel | ❌ | ❌ | ✅ | ✅ | ❌ |
| Temperature | ❌ | ❌ | ✅ | ✅ | ❌ |
| Odometer | ✅ | ✅ | ✅ | ✅ | ❌ |
| Ignition | ✅ | ✅ | ✅ | ✅ | ✅ |
| Alarms | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Next Steps

{% content-ref url="popular-protocols.md" %}
[popular-protocols.md](popular-protocols.md)
{% endcontent-ref %}

{% content-ref url="all-protocols.md" %}
[all-protocols.md](all-protocols.md)
{% endcontent-ref %}

{% content-ref url="protocol-id-formats.md" %}
[protocol-id-formats.md](protocol-id-formats.md)
{% endcontent-ref %}
