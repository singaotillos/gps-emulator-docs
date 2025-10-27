# Configuration

Complete guide to configuring your GPS Emulator installation.

---

## Overview

The Universal GPS Tracker Emulator uses two configuration systems:

1. **config.yaml** - Main configuration file (auto-generated)
2. **.env** - Environment variables (you create from template)

{% hint style="info" %}
**Environment variables** in `.env` override settings in `config.yaml`
{% endhint %}

---

## Quick Start

{% tabs %}
{% tab title="Windows" %}
### Windows Setup

```powershell
# Copy environment template
copy .env.example .env

# Edit settings
notepad .env

# Restart application
python app.py
```
{% endtab %}

{% tab title="Linux / macOS" %}
### Linux / macOS Setup

```bash
# Copy environment template
cp .env.example .env

# Edit settings
nano .env

# Restart application
python app.py
```
{% endtab %}

{% tab title="Docker" %}
### Docker Setup

```bash
# Copy environment template
cp .env.example .env

# Edit settings
nano .env

# Restart container
docker-compose restart
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Important:** Never commit `.env` to version control! It contains sensitive data.
{% endhint %}

---

## Configuration Files

### config.yaml

**Location:** `config.yaml` in project root

**Purpose:** Primary configuration with all settings organized by section

**Format:** YAML

**Auto-generated:** Yes, created on first run with defaults

**Example:**
```yaml
web_interface:
  host: 0.0.0.0
  port: 5000
  debug: false

api:
  enabled: true
  version: v2
  enable_authentication: false
```

### .env File

**Location:** `.env` in project root (create from `.env.example`)

**Purpose:** Environment-specific settings and sensitive data

**Format:** KEY=VALUE pairs

**Auto-generated:** No, you must create from template

**Example:**
```bash
WEB_PORT=5000
TRACCAR_HOST=localhost
API_KEY=your-secret-key
```

{% hint style="success" %}
**Pro Tip:** Use `.env` for passwords and API keys, use `config.yaml` for everything else.
{% endhint %}

---

## Web Interface Settings

Controls the web dashboard and UI.

### Configuration Options

```yaml
web_interface:
  enabled: true           # Enable/disable web interface
  host: 0.0.0.0          # Listen address (0.0.0.0 = all interfaces)
  port: 5000             # Web server port
  debug: false           # Flask debug mode (disable in production!)
  theme: light           # UI theme: light or dark
  auto_refresh_interval: 1   # Dashboard auto-refresh (seconds)
```

### Environment Variables

```bash
WEB_HOST=0.0.0.0
WEB_PORT=5000
WEB_DEBUG=false
WEB_THEME=light
```

### Options Explained

**host options:**
- `0.0.0.0` - Listen on all network interfaces (accessible from network)
- `127.0.0.1` - Only localhost (most secure)
- `192.168.1.100` - Specific IP address

**port:**
- Default: `5000`
- Change if port conflicts with other services
- Remember to update firewall rules

**debug mode:**
- `true` - Development mode (detailed errors, auto-reload)
- `false` - Production mode (**required for production**)

{% hint style="danger" %}
**Never** use `debug: true` in production! This exposes sensitive information.
{% endhint %}

---

## API Settings

Configure the REST API functionality.

### Configuration Options

```yaml
api:
  enabled: true                    # Enable/disable API
  version: v2                      # API version
  enable_cors: true                # Allow cross-origin requests
  enable_authentication: false     # Require API key
  api_key: ''                      # API key (if auth enabled)
  rate_limiting: false             # Enable rate limiting
  max_requests_per_minute: 100    # Rate limit threshold
```

### Environment Variables

```bash
API_ENABLED=true
API_VERSION=v2
API_ENABLE_CORS=true
API_ENABLE_AUTHENTICATION=false
API_KEY=your-secret-api-key-here
API_RATE_LIMITING=false
API_MAX_REQUESTS_PER_MINUTE=100
```

### Generating API Keys

```bash
# Generate strong random key
openssl rand -hex 32
```

### Example API Request with Authentication

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     http://localhost:5000/api/multidevice/devices
```

{% hint style="warning" %}
Enable authentication for production deployments!
{% endhint %}

---

## Traccar Integration

Settings for automatic Traccar server integration.

### Configuration Options

```yaml
traccar:
  default_host: localhost     # Traccar server host
  default_port: 8082          # Traccar web interface port
  username: admin             # Traccar admin username
  password: admin             # Traccar admin password
  auto_create_devices: true   # Auto-add devices to Traccar
  device_prefix: EMU_         # Device name prefix in Traccar
```

### Environment Variables

```bash
TRACCAR_HOST=localhost
TRACCAR_PORT=8082
TRACCAR_USERNAME=admin
TRACCAR_PASSWORD=admin
TRACCAR_AUTO_CREATE_DEVICES=true
TRACCAR_DEVICE_PREFIX=EMU_
```

### Options Explained

**default_host:**
- IP or hostname of Traccar server
- Use `localhost` if running locally
- Use IP/domain if remote: `traccar.example.com`

**default_port:**
- Traccar **web interface** port (not protocol port!)
- Default Traccar port: `8082`
- Check Traccar's `traccar.xml` configuration

**auto_create_devices:**
- `true` - Automatically add emulator devices to Traccar
- `false` - Manual device creation required

**device_prefix:**
- Prefix added to device names in Traccar
- Example: `EMU_` creates devices like "EMU_TK103_001"
- Helps identify emulator devices

{% hint style="success" %}
With `auto_create_devices: true`, new devices appear in Traccar automatically!
{% endhint %}

---

## Simulation Parameters

Control GPS simulation behavior and realism.

### Basic Settings

```yaml
simulation:
  update_interval: 10.0              # Seconds between position updates
  heartbeat_interval: 30.0           # Seconds between heartbeat packets
  default_speed: 50.0                # Default vehicle speed (km/h)
  gps_accuracy: 5.0                  # GPS accuracy in meters
  simulation_speed: 1.0              # Time multiplier (1.0 = real-time)
```

### Advanced Features

```yaml
  # Advanced features (CPU intensive)
  enable_traffic_simulation: false    # Simulate traffic delays
  enable_weather_effects: false       # Weather affects speed
  enable_fuel_consumption: false      # Track fuel levels
  enable_driver_behavior: false       # Simulate driver patterns
  simulate_acceleration: false        # Smooth acceleration/deceleration
  simulate_engine_data: false         # RPM, engine load, etc.
  simulate_temperature: false         # Engine/ambient temperature
```

### Environment Variables

```bash
SIMULATION_UPDATE_INTERVAL=10.0
SIMULATION_DEFAULT_SPEED=50.0
SIMULATION_GPS_ACCURACY=5.0
SIMULATION_SPEED_MULTIPLIER=1.0
SIMULATION_HEARTBEAT_INTERVAL=30.0

SIMULATION_ENABLE_TRAFFIC=false
SIMULATION_ENABLE_WEATHER=false
SIMULATION_ENABLE_FUEL_CONSUMPTION=false
```

### Options Explained

**update_interval:**
- How often position is updated and sent
- Lower = more frequent updates, higher CPU usage
- Typical values: 5-30 seconds
- 10 seconds = 360 updates/hour

**simulation_speed:**
- Time multiplier for faster testing
- `1.0` = real-time
- `2.0` = 2x speed (1 hour in 30 minutes)
- `10.0` = 10x speed (good for testing)

**gps_accuracy:**
- Simulated GPS error in meters
- `5m` = typical consumer GPS
- `0m` = perfect GPS (unrealistic)
- Higher = more position variation

{% hint style="info" %}
**Fast Testing:** Set `simulation_speed: 10.0` and `update_interval: 5.0`

**Realistic:** Set `simulation_speed: 1.0` and enable advanced features
{% endhint %}

### Example Configurations

{% tabs %}
{% tab title="Fast Testing" %}
```yaml
simulation:
  update_interval: 5.0      # More frequent updates
  simulation_speed: 10.0    # 10x faster
  default_speed: 80.0       # Highway speeds
  enable_traffic_simulation: false
  enable_weather_effects: false
```
{% endtab %}

{% tab title="Realistic Simulation" %}
```yaml
simulation:
  update_interval: 10.0
  simulation_speed: 1.0
  enable_traffic_simulation: true
  enable_fuel_consumption: true
  simulate_acceleration: true
  simulate_engine_data: true
```
{% endtab %}

{% tab title="Production" %}
```yaml
simulation:
  update_interval: 30.0
  simulation_speed: 1.0
  gps_accuracy: 5.0
  enable_traffic_simulation: false
  enable_weather_effects: false
```
{% endtab %}
{% endtabs %}

---

## Protocol Servers

Configure individual GPS protocol listening servers.

### Configuration Options

```yaml
servers:
  tk103:
    enabled: true            # Enable this protocol server
    host: localhost          # Listen address
    port: 5002              # Port number (must match Traccar!)
    protocol: tcp           # tcp, udp, or http
    timeout: 30             # Connection timeout (seconds)
    max_connections: 10     # Max simultaneous connections

  gt06:
    enabled: true
    host: localhost
    port: 5023
    protocol: tcp
    timeout: 30
    max_connections: 10

  osmand:
    enabled: true
    host: localhost
    port: 5055
    protocol: http
    timeout: 30
    max_connections: 10
```

### Port Numbers Reference

{% hint style="danger" %}
**CRITICAL:** Port numbers **must match** your Traccar configuration!
{% endhint %}

Common protocol ports (must match Traccar):

| Protocol | Port | Type |
|----------|------|------|
| TK103 | 5002 | TCP |
| GT06 | 5023 | TCP |
| Teltonika | 5027 | TCP |
| OsmAnd | 5055 | HTTP |
| GPS103 | 5001 | TCP |
| H02 | 5013 | TCP |
| Meiligao | 5009 | TCP |

---

## Logging

Control application logging behavior.

### Configuration Options

```yaml
logging:
  level: INFO                        # Log level
  enable_console: true               # Log to console/terminal
  enable_file: true                  # Log to file
  file: emulator.log                 # Log file name
  max_size_mb: 10                    # Max file size before rotation
  backup_count: 5                    # Keep 5 old log files
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```

### Log Levels

Available levels (from most to least verbose):
- `DEBUG` - Everything (very detailed, large logs)
- `INFO` - Important events (**recommended**)
- `WARNING` - Only warnings and errors
- `ERROR` - Only errors
- `CRITICAL` - Only critical failures

### Example Configurations

{% tabs %}
{% tab title="Development" %}
```yaml
logging:
  level: DEBUG
  enable_console: true
  enable_file: true
  max_size_mb: 50
  backup_count: 10
```
{% endtab %}

{% tab title="Production" %}
```yaml
logging:
  level: WARNING
  enable_console: false
  enable_file: true
  max_size_mb: 20
  backup_count: 3
```
{% endtab %}
{% endtabs %}

---

## Performance Tuning

### Maximum Performance (100+ devices)

```yaml
# config.yaml
simulation:
  update_interval: 5.0
  enable_traffic_simulation: false
  enable_weather_effects: false

advanced:
  max_concurrent_emulators: 200
  performance_mode: fast
  process_priority: high

monitoring:
  enabled: false
```

```bash
# .env
ADVANCED_MAX_CONCURRENT_EMULATORS=200
ADVANCED_PERFORMANCE_MODE=fast
ADVANCED_MEMORY_LIMIT_MB=4096
LOG_LEVEL=WARNING
```

### Low-Resource Systems (Raspberry Pi)

```yaml
# config.yaml
simulation:
  update_interval: 30.0

advanced:
  max_concurrent_emulators: 10
  performance_mode: efficient
  memory_limit_mb: 256

monitoring:
  metrics_retention_hours: 24
```

---

## Security Settings

### Production Security Checklist

{% hint style="warning" %}
**Before deploying to production, complete ALL items below!**
{% endhint %}

**1. Enable API Authentication:**
```bash
# .env
API_ENABLE_AUTHENTICATION=true
API_KEY=use-openssl-rand-hex-32-to-generate-this
```

**2. Disable Debug Mode:**
```bash
WEB_DEBUG=false
LOG_LEVEL=INFO
```

**3. Restrict Network Access:**
```yaml
# config.yaml
web_interface:
  host: 127.0.0.1  # Only localhost
```

**4. Disable CORS in Production:**
```bash
API_ENABLE_CORS=false
```

**5. Enable Rate Limiting:**
```bash
API_RATE_LIMITING=true
API_MAX_REQUESTS_PER_MINUTE=100
```

**6. Secure Traccar Credentials:**
```bash
# .env (never commit this file!)
TRACCAR_PASSWORD=use-strong-password-here
```

---

## Troubleshooting Configuration

### Configuration Not Loading

**Problem:** Changes to config don't take effect

**Solution:**

1. Restart application after changes
2. Check YAML syntax:
   ```bash
   python -c "import yaml; yaml.safe_load(open('config.yaml'))"
   ```
3. Verify `.env` file exists and has correct format
4. Check file permissions (must be readable)

### Port Already in Use

**Problem:** `Address already in use` error

{% tabs %}
{% tab title="Solution 1: Change Port" %}
```bash
# .env
WEB_PORT=5001
```
{% endtab %}

{% tab title="Solution 2: Kill Process (Linux)" %}
```bash
lsof -ti:5000 | xargs kill -9
```
{% endtab %}

{% tab title="Solution 2: Kill Process (Windows)" %}
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```
{% endtab %}
{% endtabs %}

---

## Next Steps

{% content-ref url="../getting-started/quick-start.md" %}
[quick-start.md](../getting-started/quick-start.md)
{% endcontent-ref %}

{% content-ref url="creating-devices.md" %}
[creating-devices.md](creating-devices.md)
{% endcontent-ref %}

{% content-ref url="../api-reference/rest-api.md" %}
[rest-api.md](../api-reference/rest-api.md)
{% endcontent-ref %}

---

## Need Help?

- See [Troubleshooting](../support/troubleshooting.md) for more issues
- Check [FAQ](../support/faq.md) for common questions
- Contact support for assistance

---

*Last updated: October 2025*
