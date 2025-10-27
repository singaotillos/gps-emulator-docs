# Frequently Asked Questions

Quick answers to common questions about the Universal GPS Tracker Emulator.

---

## General Questions

### What is a GPS Tracker Emulator?

A GPS tracker emulator is a **software tool that simulates real GPS tracking devices** without needing physical hardware. It sends GPS positions to tracking platforms just like a real device would.

{% hint style="success" %}
**Save money** - No need to buy expensive GPS hardware

**Test faster** - Instant setup vs waiting for hardware

**Scale easily** - Simulate 100+ devices simultaneously
{% endhint %}

### Why do I need this?

**Common use cases:**
- 💰 **Save money** - No need to buy expensive GPS hardware
- ⚡ **Test faster** - Instant setup vs waiting for hardware
- 🔧 **Develop easier** - Perfect for app development
- 📊 **Load testing** - Simulate 100+ devices simultaneously
- 🎓 **Learn** - Understand GPS protocols without investment

### Is this legal to use?

**Yes!** The emulator is for **legitimate testing and development purposes**:

✅ **Allowed uses:**
- Testing your GPS tracking application
- Developing fleet management systems
- Training and demonstrations
- Quality assurance and QA testing

❌ **NOT allowed:**
- Spoofing real vehicle locations
- Fraudulent purposes
- Illegal tracking

{% hint style="warning" %}
Use this tool responsibly for testing and development only.
{% endhint %}

---

## Installation & Setup

### Do I need GPS hardware?

**No!** That's the whole point - this is a **pure software solution**. No GPS device, no SIM card, no hardware needed.

### What are the system requirements?

**Minimum:**
- Python 3.8+
- 4GB RAM
- 2GB disk space
- Windows/Linux/macOS

**Recommended:**
- Python 3.10+
- 8GB RAM
- For 50+ devices simultaneously

### How long does installation take?

**3-5 minutes** on average:

1. Extract files (30 seconds)
2. Install Python dependencies (2-3 minutes)
3. Start application (10 seconds)
4. Done!

{% hint style="info" %}
See [Installation Guide](../getting-started/installation.md) for detailed steps
{% endhint %}

### Can I run this on a server?

**Absolutely!** Works great on:
- ✅ VPS (DigitalOcean, Linode, etc.)
- ✅ Cloud (AWS, Google Cloud, Azure)
- ✅ Dedicated servers
- ✅ Raspberry Pi (for lighter loads)

### Do I need internet connection?

**For basic use:** No - can run offline for local testing

**For Traccar integration:** Yes - if Traccar server is remote

---

## Usage & Features

### How many devices can I simulate?

**Depends on your license and hardware:**

| Edition | Device Limit | Recommended |
|---------|--------------|-------------|
| **Community Edition** | 5 devices | Testing only |
| **Regular License** | 50 devices | Small projects |
| **Extended License** | 100+ devices | Production use |

**Performance:**
- Each device uses ~20MB RAM
- 50 devices ≈ 1GB RAM
- 100 devices ≈ 2-3GB RAM

### How realistic is the simulation?

**Very realistic!** Features include:

- ✅ Accurate GPS coordinates
- ✅ Realistic vehicle movement
- ✅ Proper speed/altitude/course
- ✅ Correct timestamps
- ✅ Ignition on/off behavior
- ✅ Speed = 0 when vehicle stopped
- ✅ Multiple predefined routes

### Can I create custom routes?

**Yes!** Three ways:

1. **Predefined routes** - Paris, London, NYC, Tokyo, Berlin
2. **Custom routes** - Define your own waypoints in config
3. **API** - Create routes programmatically via REST API

{% hint style="success" %}
Custom routes can be created with latitude/longitude waypoints
{% endhint %}

### Can I control devices in real-time?

**Yes!** via Web Interface or API:

- Start/Stop devices
- Change routes
- Modify speed
- Turn ignition on/off
- Send commands (protocol-dependent)

### Does it work offline?

**Yes**, for local testing:
- Emulator runs on localhost
- No internet needed for basic operation
- Internet needed only for remote Traccar connections

---

## Protocols

### How many protocols are supported?

**86 GPS protocols** including:
- TK103, GT06, Teltonika (most popular)
- And 83 more!

{% content-ref url="../protocols/overview.md" %}
[overview.md](../protocols/overview.md)
{% endcontent-ref %}

### Which protocol should I use?

**Popular choices:**

| Protocol | Best For | Difficulty |
|----------|----------|------------|
| **TK103** | First-time users | ⭐ Easy |
| **OsmAnd** | Mobile apps | ⭐ Easy |
| **Teltonika** | Professional fleet | ⭐⭐ Medium |
| **GT06** | Common devices | ⭐ Easy |

{% hint style="info" %}
**Recommendation:** Start with TK103 - it's the most widely compatible
{% endhint %}

### Can I use multiple protocols at once?

**Yes!** Simulate different devices with different protocols simultaneously:

- 10 TK103 devices
- 5 GT06 devices
- 3 Teltonika devices
- All at the same time!

### Can I add my own custom protocol?

**Yes!** The system is extensible:

1. Source code included
2. Create new protocol in `protocols/` directory
3. Implement message format
4. Register protocol
5. Done!

---

## Integration

### Does it work with Traccar?

**Yes! 100% compatible** with Traccar:

- ✅ All 86 protocols supported by Traccar
- ✅ Automatic device creation
- ✅ Real-time position updates
- ✅ Full integration guide included

{% content-ref url="../user-guide/traccar-integration.md" %}
[traccar-integration.md](../user-guide/traccar-integration.md)
{% endcontent-ref %}

### What about other GPS platforms?

**Works with:**
- ✅ Traccar
- ✅ GPSGate
- ✅ Wialon
- ✅ Any platform supporting standard protocols
- ✅ Your custom platform (via standard protocols)

### Can I integrate with my application?

**Yes!** Multiple integration methods:

1. **Direct Protocol** - Your app listens on port
2. **REST API** - Control emulator via API
3. **WebSocket** - Real-time updates
4. **Database** - Read from SQLite database

### Is there an API?

**Yes!** Complete REST API:

- Create/start/stop devices
- Get status and positions
- Manage routes
- WebSocket for real-time updates

{% content-ref url="../api-reference/rest-api.md" %}
[rest-api.md](../api-reference/rest-api.md)
{% endcontent-ref %}

---

## Licensing

### What's the difference between Regular and Extended License?

| Feature | Regular ($69) | Extended ($349) |
|---------|---------------|-----------------|
| **Projects** | 1 project | Unlimited |
| **Support** | 6 months | 12 months |
| **SaaS use** | ❌ No | ✅ Yes |
| **White-label** | ❌ No | ✅ Yes |
| **Devices** | 50 recommended | Unlimited |
| **Priority support** | ❌ No | ✅ Yes |

### Can I modify the code?

**Yes!** Both licenses allow:

- ✅ Modify source code
- ✅ Customize for your needs
- ✅ Add features
- ✅ Fix bugs
- ❌ Cannot resell source code as-is

### Can I use it commercially?

**Yes!** Both Regular and Extended licenses:

- ✅ Commercial use allowed
- ✅ Use in your business
- ✅ Include in your product (Extended only for SaaS)

### Do I get updates?

**Yes!**

- **Regular License:** 6 months free updates
- **Extended License:** 12 months free updates
- Minor updates (2.0.x) are free
- Major updates (3.0) may require upgrade fee

---

## Technical

### What programming language is it written in?

**Python 3.8+**

- Backend: Flask framework
- Frontend: HTML/CSS/JavaScript (Bootstrap 5)
- Database: SQLite (can use PostgreSQL)

### Can I run it in Docker?

**Yes!** Docker support included:

{% tabs %}
{% tab title="Docker" %}
```bash
docker build -t gps-emulator .
docker run -p 5000:5000 gps-emulator
```
{% endtab %}

{% tab title="Docker Compose" %}
```bash
docker-compose up -d
```
{% endtab %}
{% endtabs %}

### Does it support HTTPS?

**Yes!** HTTPS/SSL supported:

- Configure reverse proxy (Nginx/Caddy)
- Use Let's Encrypt for free SSL
- Instructions in documentation

### What database does it use?

**Default:** SQLite (file-based, no setup)

**Production:** Can use PostgreSQL, MySQL

### Can I use it in CI/CD?

**Absolutely!** Perfect for:

- ✅ Automated testing
- ✅ Jenkins/GitHub Actions/GitLab CI
- ✅ Regression tests
- ✅ Integration tests
- Example configs included

---

## Troubleshooting

### Application won't start

{% hint style="danger" %}
**Quick checks:**
{% endhint %}

1. **Python 3.8+ installed?**
   ```bash
   python --version
   ```

2. **Dependencies installed?**
   ```bash
   pip install -r requirements.txt
   ```

3. **Port 5000 available?**
   ```bash
   # Change port in .env if needed
   WEB_PORT=5001
   ```

### "Module not found" error

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Devices not sending data

**Check:**

1. ✅ Device status = "running"?
2. ✅ Correct protocol selected?
3. ✅ Correct port configured?
4. ✅ Firewall not blocking?

### Can't connect to Traccar

**Checklist:**

1. ✅ Traccar server running?
2. ✅ Device created in Traccar?
3. ✅ Correct protocol in Traccar?
4. ✅ Correct port (e.g., 5002 for TK103)?
5. ✅ Firewall allows connection?

{% content-ref url="troubleshooting.md" %}
[troubleshooting.md](troubleshooting.md)
{% endcontent-ref %}

### Performance is slow

**Solutions:**

1. Reduce number of devices
2. Increase update interval in config
3. Use more powerful hardware
4. Close other applications

### Database locked error

**Solution:**
```bash
# Stop all instances
# Linux/Mac
pkill -f app.py

# Windows
taskkill /IM python.exe /F

# Remove lock file
rm /tmp/osmand_gps_emulator.lock
```

---

## Quick Start Reminder

```bash
# 1. Extract files
unzip universal-gps-emulator.zip

# 2. Install
pip install -r requirements.txt

# 3. Run
python app.py

# 4. Open browser
http://localhost:5000

# 5. Create device and start!
```

---

## Still Have Questions?

### Contact Support

{% hint style="info" %}
**Email:** support@your-domain.com

**Response time:** 24-48 hours (business days)

**Include:**
- Error messages
- Screenshots
- Configuration files
- What you've already tried
{% endhint %}

### Additional Resources

{% content-ref url="../getting-started/installation.md" %}
[installation.md](../getting-started/installation.md)
{% endcontent-ref %}

{% content-ref url="../user-guide/configuration.md" %}
[configuration.md](../user-guide/configuration.md)
{% endcontent-ref %}

{% content-ref url="troubleshooting.md" %}
[troubleshooting.md](troubleshooting.md)
{% endcontent-ref %}

---

*FAQ last updated: October 2025*
