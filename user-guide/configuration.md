# Configuration Guide - Universal GPS Tracker Emulator

Complete configuration reference for customizing your GPS emulator installation.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Configuration Files](#configuration-files)
- [Environment Variables](#environment-variables)
- [Configuration Options](#configuration-options)
  - [Web Interface](#web-interface)
  - [API Settings](#api-settings)
  - [Traccar Integration](#traccar-integration)
  - [Simulation Parameters](#simulation-parameters)
  - [Protocol Servers](#protocol-servers)
  - [Monitoring & Alerts](#monitoring--alerts)
  - [Logging](#logging)
  - [Advanced Settings](#advanced-settings)
  - [License & Features](#license--features)
- [Performance Tuning](#performance-tuning)
- [Security Settings](#security-settings)
- [Examples](#examples)

---

## Quick Start

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit your settings:**
   ```bash
   # Windows
   notepad .env

   # Linux/Mac
   nano .env
   ```

3. **Restart application:**
   ```bash
   python app.py
   ```

---

## Configuration Files

The emulator uses two configuration files:

### 1. config.yaml (Main Configuration)

**Location:** `config.yaml` in project root

**Purpose:** Primary configuration file with all settings organized by section

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

### 2. .env (Environment Variables)

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

**Priority:** Environment variables override config.yaml settings

---

## Environment Variables

### Creating .env File

```bash
# Copy the template
cp .env.example .env

# Edit with your settings
nano .env
```

**IMPORTANT:**
- Never commit `.env` to version control
- Keep `.env.example` as template only
- Environment variables override config.yaml
- Use .env for sensitive data (passwords, API keys)

---

## Configuration Options

### Web Interface

Controls the web dashboard and UI settings.

#### config.yaml Section:
```yaml
web_interface:
  enabled: true           # Enable/disable web interface
  host: 0.0.0.0          # Listen address (0.0.0.0 = all interfaces)
  port: 5000             # Web server port
  debug: false           # Flask debug mode (disable in production)
  theme: light           # UI theme: light or dark
  auto_refresh_interval: 1   # Dashboard auto-refresh (seconds)
  show_advanced_metrics: true  # Show CPU/memory metrics
```

#### Environment Variables:
```bash
WEB_HOST=0.0.0.0         # Override host
WEB_PORT=5000            # Override port
WEB_DEBUG=false          # Override debug mode
WEB_THEME=light          # Override theme
```

#### Options Explained:

**host:**
- `0.0.0.0` - Listen on all network interfaces (accessible from network)
- `127.0.0.1` - Only localhost (most secure)
- `192.168.1.100` - Specific IP address

**port:**
- Default: `5000`
- Change if port conflicts with other services
- Remember to update firewall rules

**debug:**
- `true` - Development mode (detailed errors, auto-reload)
- `false` - Production mode (required for production)

**theme:**
- `light` - Light theme (default)
- `dark` - Dark theme (coming soon)

**auto_refresh_interval:**
- Seconds between dashboard updates
- Lower = more real-time, higher CPU usage
- Default: 1 second

---

### API Settings

Configure the REST API functionality.

#### config.yaml Section:
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

#### Environment Variables:
```bash
API_ENABLED=true
API_VERSION=v2
API_ENABLE_CORS=true
API_ENABLE_AUTHENTICATION=false
API_KEY=your-secret-api-key-here
API_RATE_LIMITING=false
API_MAX_REQUESTS_PER_MINUTE=100
```

#### Options Explained:

**enabled:**
- `true` - API endpoints accessible
- `false` - All API requests return 404

**enable_cors:**
- `true` - Allow requests from any origin (development)
- `false` - Restrict to same origin (more secure)

**enable_authentication:**
- `true` - Require API key in headers
- `false` - Open access (not recommended for production)

**api_key:**
- Generate strong random key: `openssl rand -hex 32`
- Send in header: `Authorization: Bearer YOUR_API_KEY`

**rate_limiting:**
- `true` - Limit requests per IP
- `false` - Unlimited requests

**Example API Request with Auth:**
```bash
curl -H "Authorization: Bearer your-api-key" \
     http://localhost:5000/api/multidevice/devices
```

---

### Traccar Integration

Settings for automatic Traccar server integration.

#### config.yaml Section:
```yaml
traccar:
  default_host: localhost     # Traccar server host
  default_port: 8082          # Traccar web interface port
  username: admin             # Traccar admin username
  password: admin             # Traccar admin password
  auto_create_devices: true   # Auto-add devices to Traccar
  device_prefix: EMU_         # Device name prefix in Traccar
```

#### Environment Variables:
```bash
TRACCAR_HOST=localhost
TRACCAR_PORT=8082
TRACCAR_USERNAME=admin
TRACCAR_PASSWORD=admin
TRACCAR_AUTO_CREATE_DEVICES=true
TRACCAR_DEVICE_PREFIX=EMU_
```

#### Options Explained:

**default_host:**
- IP or hostname of Traccar server
- Use `localhost` if running locally
- Use IP/domain if remote: `traccar.example.com`

**default_port:**
- Traccar web interface port (not protocol port!)
- Default Traccar port: `8082`
- Check Traccar's `traccar.xml`

**username/password:**
- Traccar admin credentials
- Required for auto-device creation
- Create dedicated API user recommended

**auto_create_devices:**
- `true` - Automatically add emulator devices to Traccar
- `false` - Manual device creation in Traccar

**device_prefix:**
- Prefix added to device names in Traccar
- Example: `EMU_` creates devices like "EMU_TK103_001"
- Helps identify emulator devices

**Example Script:**
```python
# Add device to Traccar automatically
device_data = {
    "protocol": "tk103",
    "device_model": "TK103-2B",
    "route": "paris"
}
response = requests.post("http://localhost:5000/api/multidevice/devices",
                         json=device_data)
# Device automatically created in Traccar!
```

---

### Simulation Parameters

Control GPS simulation behavior and realism.

#### config.yaml Section:
```yaml
simulation:
  update_interval: 10.0              # Seconds between position updates
  heartbeat_interval: 30.0           # Seconds between heartbeat packets
  default_speed: 50.0                # Default vehicle speed (km/h)
  gps_accuracy: 5.0                  # GPS accuracy in meters
  simulation_speed: 1.0              # Time multiplier (1.0 = real-time)

  # Advanced features (CPU intensive)
  enable_traffic_simulation: false    # Simulate traffic delays
  enable_weather_effects: false       # Weather affects speed
  enable_fuel_consumption: false      # Track fuel levels
  enable_driver_behavior: false       # Simulate driver patterns
  simulate_acceleration: false        # Smooth acceleration/deceleration
  simulate_engine_data: false         # RPM, engine load, etc.
  simulate_temperature: false         # Engine/ambient temperature

  # Random events
  random_events_enabled: false        # Enable random events
  accident_probability: 0.001         # Accident chance per update
  breakdown_probability: 0.0005       # Breakdown chance per update
```

#### Environment Variables:
```bash
SIMULATION_UPDATE_INTERVAL=10.0
SIMULATION_DEFAULT_SPEED=50.0
SIMULATION_GPS_ACCURACY=5.0
SIMULATION_SPEED_MULTIPLIER=1.0
SIMULATION_HEARTBEAT_INTERVAL=30.0

SIMULATION_ENABLE_TRAFFIC=false
SIMULATION_ENABLE_WEATHER=false
SIMULATION_ENABLE_FUEL_CONSUMPTION=false
SIMULATION_ENABLE_DRIVER_BEHAVIOR=false
SIMULATION_ENABLE_ENGINE_DATA=false
```

#### Options Explained:

**update_interval:**
- How often position is updated and sent
- Lower = more frequent updates, higher CPU
- Typical values: 5-30 seconds
- 10 seconds = 360 updates/hour

**heartbeat_interval:**
- Periodic "I'm alive" messages when stationary
- Used when ignition off or parked
- Should be >= update_interval

**default_speed:**
- Starting speed for vehicles (km/h)
- Actual speed varies by route
- Range: 0-120 km/h typical

**gps_accuracy:**
- Simulated GPS error in meters
- 5m = typical consumer GPS
- 0m = perfect GPS (unrealistic)
- Higher = more position variation

**simulation_speed:**
- Time multiplier for faster testing
- 1.0 = real-time
- 2.0 = 2x speed (1 hour in 30 minutes)
- 10.0 = 10x speed (good for testing)

**Advanced Features:**
All advanced features increase CPU usage. Enable only if needed.

- **traffic_simulation:** Adds random delays like real traffic
- **weather_effects:** Rain/snow reduces speed
- **fuel_consumption:** Tracks fuel level, empty = stops
- **driver_behavior:** Aggressive/cautious driving patterns
- **simulate_acceleration:** Gradual speed changes (realistic)
- **simulate_engine_data:** RPM, throttle, engine load
- **simulate_temperature:** Engine and ambient temperature

**Example - Fast Testing:**
```yaml
simulation:
  update_interval: 5.0      # More frequent updates
  simulation_speed: 10.0    # 10x faster
  default_speed: 80.0       # Highway speeds
```

**Example - Realistic Simulation:**
```yaml
simulation:
  update_interval: 10.0
  simulation_speed: 1.0
  enable_traffic_simulation: true
  enable_fuel_consumption: true
  simulate_acceleration: true
```

---

### Protocol Servers

Configure individual GPS protocol listening servers.

#### config.yaml Section:
```yaml
servers:
  tk103:
    enabled: true            # Enable this protocol server
    host: localhost          # Listen address
    port: 5002              # Port number (must match Traccar)
    protocol: tcp           # tcp, udp, or http
    timeout: 30             # Connection timeout (seconds)
    max_connections: 10     # Max simultaneous connections
    description: ''         # Optional description

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

#### Environment Variables:
```bash
PROTOCOL_DEFAULT_HOST=localhost
PROTOCOL_TIMEOUT=30
PROTOCOL_MAX_CONNECTIONS=10
```

#### Options Explained:

**enabled:**
- `true` - Server starts when emulator starts
- `false` - Server disabled (saves resources)
- Disable unused protocols for better performance

**host:**
- Listen address for this protocol
- Usually `localhost` for local Traccar
- Use `0.0.0.0` to accept remote connections

**port:**
- **CRITICAL:** Must match Traccar configuration!
- Each protocol has default port (see PROTOCOLS.md)
- Check Traccar's `traccar.xml` for correct ports

**protocol:**
- `tcp` - Most binary protocols (TK103, GT06, etc.)
- `udp` - Some protocols use UDP
- `http` - HTTP-based protocols (OsmAnd, etc.)

**timeout:**
- Seconds before idle connection closed
- 30s typical
- Increase for slow networks

**max_connections:**
- Simultaneous devices per protocol
- 10 = good for testing
- Increase for production (50-100)

**Port Numbers Reference:**
Common protocol ports (must match Traccar):
```
TK103:     5002
GT06:      5023
Teltonika: 5027
OsmAnd:    5055
GPS103:    5001
H02:       5013
Meiligao:  5009
```

**Example - Multiple Servers:**
```yaml
servers:
  tk103:
    enabled: true
    port: 5002
  gt06:
    enabled: true
    port: 5023
  teltonika:
    enabled: true
    port: 5027
  osmand:
    enabled: false    # Disabled to save resources
```

---

### Monitoring & Alerts

System monitoring and alert configuration.

#### config.yaml Section:
```yaml
monitoring:
  enabled: true                      # Enable monitoring
  metrics_retention_hours: 168      # Keep metrics for 7 days

  # Alert thresholds
  alert_thresholds:
    cpu_warning: 70.0                # CPU % warning level
    cpu_critical: 90.0               # CPU % critical level
    memory_warning: 80.0             # Memory % warning
    memory_critical: 90.0            # Memory % critical
    disk_warning: 85.0               # Disk % warning
    disk_critical: 95.0              # Disk % critical

  # Email alerts (optional)
  enable_email_alerts: false
  email_smtp_server: ''              # smtp.gmail.com:587
  email_recipients: []               # [admin@example.com]
```

#### Environment Variables:
```bash
MONITORING_ENABLED=true
MONITORING_METRICS_RETENTION_HOURS=168

MONITORING_CPU_WARNING=70.0
MONITORING_CPU_CRITICAL=90.0
MONITORING_MEMORY_WARNING=80.0
MONITORING_MEMORY_CRITICAL=90.0
MONITORING_DISK_WARNING=85.0
MONITORING_DISK_CRITICAL=95.0

MONITORING_ENABLE_EMAIL_ALERTS=false
MONITORING_EMAIL_SMTP_SERVER=smtp.gmail.com:587
MONITORING_EMAIL_RECIPIENTS=admin@example.com,user@example.com
```

#### Options Explained:

**enabled:**
- `true` - Collect metrics (CPU, memory, disk, network)
- `false` - No monitoring (slight performance gain)

**metrics_retention_hours:**
- How long to keep historical metrics
- 168 hours = 7 days
- Higher = more storage used

**Alert Thresholds:**
Set warning and critical levels for each metric:
- **Warning:** Yellow alert, logged
- **Critical:** Red alert, email sent (if enabled)

**cpu_warning/critical:**
- Percentage of total CPU usage
- 70%/90% good defaults
- Adjust based on server capacity

**memory_warning/critical:**
- Percentage of total RAM used
- Emulator uses ~50-200MB typically
- Multiple devices increase usage

**disk_warning/critical:**
- Disk space percentage used
- Mainly affects log files
- Clean logs periodically

**Email Alerts:**
Configure SMTP to send alert emails:

```yaml
enable_email_alerts: true
email_smtp_server: 'smtp.gmail.com:587'
email_recipients:
  - admin@company.com
  - alerts@company.com
```

**Gmail Example:**
1. Enable "App Passwords" in Google Account
2. Use app password instead of regular password
3. Server: `smtp.gmail.com:587`

**Example Alert Email:**
```
Subject: [CRITICAL] GPS Emulator - High CPU Usage

CPU usage exceeded critical threshold:
Current: 92.5%
Threshold: 90.0%
Timestamp: 2025-10-25 14:32:10

Server: emulator-prod-01
Devices running: 47
```

---

### Logging

Control application logging behavior.

#### config.yaml Section:
```yaml
logging:
  level: INFO                        # Log level
  enable_console: true               # Log to console/terminal
  enable_file: true                  # Log to file
  file: osmand_emulator.log          # Log file name
  max_size_mb: 10                    # Max file size before rotation
  backup_count: 5                    # Keep 5 old log files
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```

#### Environment Variables:
```bash
LOG_LEVEL=INFO
LOG_ENABLE_CONSOLE=true
LOG_ENABLE_FILE=true
LOG_FILE=emulator.log
LOG_MAX_SIZE_MB=10
LOG_BACKUP_COUNT=5
```

#### Options Explained:

**level:**
Available levels (from most to least verbose):
- `DEBUG` - Everything (very detailed, large logs)
- `INFO` - Important events (recommended)
- `WARNING` - Only warnings and errors
- `ERROR` - Only errors
- `CRITICAL` - Only critical failures

**enable_console:**
- `true` - Print logs to terminal/console
- `false` - Silent (no console output)
- Useful for development

**enable_file:**
- `true` - Write logs to file
- `false` - No log file
- Recommended for production

**file:**
- Log file path (relative or absolute)
- Examples:
  - `emulator.log` (current directory)
  - `/var/log/emulator.log` (Linux)
  - `C:\Logs\emulator.log` (Windows)

**max_size_mb:**
- Maximum size before log rotation
- When reached, creates new log file
- Old files renamed: emulator.log.1, emulator.log.2, etc.

**backup_count:**
- Number of old log files to keep
- 5 = keep 5 rotated logs + 1 current
- Total disk usage: (max_size_mb × backup_count)

**format:**
Standard Python logging format string:
- `%(asctime)s` - Timestamp
- `%(name)s` - Logger name
- `%(levelname)s` - Level (INFO, WARNING, etc.)
- `%(message)s` - Log message

**Example - Detailed Debugging:**
```yaml
logging:
  level: DEBUG
  enable_console: true
  enable_file: true
  max_size_mb: 50
  backup_count: 10
```

**Example - Production (Minimal):**
```yaml
logging:
  level: WARNING
  enable_console: false
  enable_file: true
  max_size_mb: 20
  backup_count: 3
```

---

### Advanced Settings

Advanced configuration for performance and behavior.

#### config.yaml Section:
```yaml
advanced:
  max_concurrent_emulators: 100      # Max simultaneous devices
  memory_limit_mb: 1024              # RAM limit for emulator
  performance_mode: balanced         # balanced, fast, or efficient
  process_priority: normal           # normal, high, or low
  auto_restart_on_crash: true        # Auto-restart if crash
  enable_plugins: true               # Enable plugin system (EE)
  plugin_directory: plugins          # Plugin folder path
```

#### Environment Variables:
```bash
ADVANCED_MAX_CONCURRENT_EMULATORS=100
ADVANCED_MEMORY_LIMIT_MB=1024
ADVANCED_PERFORMANCE_MODE=balanced
ADVANCED_PROCESS_PRIORITY=normal
ADVANCED_AUTO_RESTART_ON_CRASH=true
ADVANCED_ENABLE_PLUGINS=true
ADVANCED_PLUGIN_DIRECTORY=plugins
```

#### Options Explained:

**max_concurrent_emulators:**
- Maximum devices running simultaneously
- Community Edition (CE): Limited to 5-10 by license
- Enterprise Edition (EE): Up to 100+
- Each device uses ~2-5MB RAM

**memory_limit_mb:**
- Soft RAM limit for application
- 1024MB = 1GB (good for 50-100 devices)
- Alert triggered if exceeded
- System may use more if available

**performance_mode:**
- `balanced` - Balance speed and resource usage (default)
- `fast` - Maximize speed (uses more CPU/RAM)
- `efficient` - Minimize resource usage (slower updates)

**process_priority:**
- OS-level process priority
- `normal` - Standard priority (recommended)
- `high` - Higher priority (use carefully!)
- `low` - Background priority

**auto_restart_on_crash:**
- `true` - Automatically restart if crash detected
- `false` - Manual restart required
- Logs crash details before restart

**enable_plugins:**
- `true` - Load plugins from plugin directory (EE only)
- `false` - Plugin system disabled
- CE: Always disabled

**plugin_directory:**
- Path to plugins folder
- Relative or absolute path
- Plugins must be Python files

**Example - High Performance Server:**
```yaml
advanced:
  max_concurrent_emulators: 200
  memory_limit_mb: 4096
  performance_mode: fast
  process_priority: high
```

**Example - Low-Resource Environment:**
```yaml
advanced:
  max_concurrent_emulators: 20
  memory_limit_mb: 512
  performance_mode: efficient
  process_priority: low
```

---

### License & Features

License and feature flag configuration.

#### Environment Variables:
```bash
# License Configuration
UGTE_LICENSE_KEY=                    # Leave empty for CE
UGTE_CE_DEVICE_LIMIT=5              # CE: Max devices (default 5)

# Feature Flags (0=disabled, 1=enabled)
UGTE_FF_PLUGINS=0                    # Plugin system (EE only)
UGTE_FF_ADVANCED_EXPORTS=0          # PDF/Excel exports (EE only)
UGTE_FF_REPORTS_PDF=0               # PDF reports (EE only)
UGTE_FF_BATCH_OPERATIONS=1          # Batch device operations
UGTE_FF_MAP_VISUALIZATION=0         # Map UI (coming soon)
UGTE_FF_TRAFFIC_SIMULATION=0        # Traffic simulation (EE only)
```

#### Options Explained:

**UGTE_LICENSE_KEY:**
- Community Edition (CE): Leave empty or omit
- Enterprise Edition (EE): Enter license key
- Format: `EE-XXXX-XXXX-XXXX-XXXX`

**UGTE_CE_DEVICE_LIMIT:**
- CE: Maximum simultaneous devices
- Default: 5 devices
- EE: Ignored (unlimited)

**Feature Flags:**
Enable/disable specific features:
- `0` = Disabled
- `1` = Enabled

**CE vs EE Features:**

Community Edition (CE):
- ✓ All 86 protocols
- ✓ Web interface
- ✓ REST API
- ✓ Up to 5-10 devices
- ✓ Basic monitoring
- ✗ Plugins
- ✗ Advanced exports
- ✗ PDF reports
- ✗ Priority support

Enterprise Edition (EE):
- ✓ All CE features
- ✓ Unlimited devices
- ✓ Plugin system
- ✓ Advanced exports (PDF, Excel)
- ✓ PDF reports
- ✓ Traffic simulation
- ✓ CI/CD integrations
- ✓ Priority support
- ✓ Installation assistance

**Example - Community Edition:**
```bash
UGTE_LICENSE_KEY=
UGTE_CE_DEVICE_LIMIT=5
UGTE_FF_PLUGINS=0
UGTE_FF_ADVANCED_EXPORTS=0
UGTE_FF_REPORTS_PDF=0
UGTE_FF_BATCH_OPERATIONS=1
```

**Example - Enterprise Edition:**
```bash
UGTE_LICENSE_KEY=EE-1234-5678-90AB-CDEF
UGTE_FF_PLUGINS=1
UGTE_FF_ADVANCED_EXPORTS=1
UGTE_FF_REPORTS_PDF=1
UGTE_FF_BATCH_OPERATIONS=1
UGTE_FF_TRAFFIC_SIMULATION=1
```

---

## Performance Tuning

Optimize performance for your use case.

### For Maximum Performance

**Goal:** Handle 100+ devices, fastest updates

```yaml
# config.yaml
simulation:
  update_interval: 5.0              # Fast updates
  enable_traffic_simulation: false   # Disable CPU-heavy features
  enable_weather_effects: false
  simulate_acceleration: false

advanced:
  max_concurrent_emulators: 200
  performance_mode: fast
  process_priority: high

monitoring:
  enabled: false                     # Disable monitoring overhead
```

```bash
# .env
ADVANCED_MAX_CONCURRENT_EMULATORS=200
ADVANCED_PERFORMANCE_MODE=fast
ADVANCED_MEMORY_LIMIT_MB=4096
LOG_LEVEL=WARNING                    # Less verbose logging
```

**Hardware Requirements:**
- CPU: 4+ cores
- RAM: 4GB+
- OS: Linux (best performance)

---

### For Low-Resource Systems

**Goal:** Run on minimal hardware, few devices

```yaml
# config.yaml
simulation:
  update_interval: 30.0              # Slower updates
  enable_traffic_simulation: false
  enable_weather_effects: false

advanced:
  max_concurrent_emulators: 10
  performance_mode: efficient
  memory_limit_mb: 256

monitoring:
  enabled: true
  metrics_retention_hours: 24        # Keep less history
```

```bash
# .env
ADVANCED_MAX_CONCURRENT_EMULATORS=10
ADVANCED_PERFORMANCE_MODE=efficient
ADVANCED_MEMORY_LIMIT_MB=256
LOG_LEVEL=WARNING
LOG_MAX_SIZE_MB=5
LOG_BACKUP_COUNT=2
```

**Hardware Requirements:**
- CPU: 1-2 cores
- RAM: 512MB
- OS: Any

---

### For Realistic Simulation

**Goal:** Most realistic behavior, don't care about performance

```yaml
# config.yaml
simulation:
  update_interval: 10.0
  simulation_speed: 1.0               # Real-time
  gps_accuracy: 5.0                   # Realistic GPS error
  enable_traffic_simulation: true     # Real traffic
  enable_weather_effects: true        # Weather affects speed
  enable_fuel_consumption: true       # Track fuel
  enable_driver_behavior: true        # Realistic driving
  simulate_acceleration: true         # Smooth speed changes
  simulate_engine_data: true          # RPM, throttle, etc.
  random_events_enabled: true         # Random events

advanced:
  performance_mode: balanced
```

**Hardware Requirements:**
- CPU: 4+ cores (CPU-intensive)
- RAM: 2GB+
- For 10-20 devices max

---

## Security Settings

Secure your production deployment.

### Production Security Checklist

**1. Enable API Authentication:**
```bash
# .env
API_ENABLE_AUTHENTICATION=true
API_KEY=use-openssl-rand-hex-32-to-generate-this
```

**2. Disable Debug Mode:**
```bash
WEB_DEBUG=false
LOG_LEVEL=INFO  # or WARNING
```

**3. Restrict Network Access:**
```yaml
# config.yaml
web_interface:
  host: 127.0.0.1  # Only localhost
```

Or use firewall:
```bash
# Linux: Allow only specific IP
sudo ufw allow from 192.168.1.0/24 to any port 5000
```

**4. Use HTTPS:**
Place behind reverse proxy (nginx, Apache):
```nginx
# nginx example
server {
    listen 443 ssl;
    server_name gps-emulator.example.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}
```

**5. Secure Traccar Credentials:**
```bash
# .env (never commit this file!)
TRACCAR_PASSWORD=use-strong-password-here
```

**6. Disable CORS in Production:**
```bash
API_ENABLE_CORS=false
```

**7. Enable Rate Limiting:**
```bash
API_RATE_LIMITING=true
API_MAX_REQUESTS_PER_MINUTE=100
```

**8. Separate Environment Files:**
```bash
# Development
.env.development

# Production
.env.production

# Load appropriate file
export ENV=production
python app.py
```

---

## Examples

### Example 1: Development Setup

**Scenario:** Local development, fast iterations, detailed logging

```bash
# .env
WEB_HOST=127.0.0.1
WEB_PORT=5000
WEB_DEBUG=true
WEB_THEME=light

API_ENABLE_AUTHENTICATION=false
API_ENABLE_CORS=true

TRACCAR_HOST=localhost
TRACCAR_PORT=8082

SIMULATION_UPDATE_INTERVAL=5.0
SIMULATION_SPEED_MULTIPLIER=10.0

LOG_LEVEL=DEBUG
LOG_ENABLE_CONSOLE=true

MONITORING_ENABLED=true

UGTE_LICENSE_KEY=
UGTE_CE_DEVICE_LIMIT=5
```

---

### Example 2: Production Server

**Scenario:** Production deployment, 50 devices, secure

```bash
# .env
WEB_HOST=0.0.0.0
WEB_PORT=5000
WEB_DEBUG=false

API_ENABLE_AUTHENTICATION=true
API_KEY=7f9a8b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8
API_ENABLE_CORS=false
API_RATE_LIMITING=true
API_MAX_REQUESTS_PER_MINUTE=100

TRACCAR_HOST=traccar.company.com
TRACCAR_PORT=8082
TRACCAR_USERNAME=api_user
TRACCAR_PASSWORD=SecurePassword123!

SIMULATION_UPDATE_INTERVAL=10.0
SIMULATION_SPEED_MULTIPLIER=1.0

LOG_LEVEL=INFO
LOG_ENABLE_CONSOLE=false
LOG_ENABLE_FILE=true
LOG_FILE=/var/log/gps-emulator/emulator.log

MONITORING_ENABLED=true
MONITORING_ENABLE_EMAIL_ALERTS=true
MONITORING_EMAIL_SMTP_SERVER=smtp.company.com:587
MONITORING_EMAIL_RECIPIENTS=admin@company.com,alerts@company.com

ADVANCED_MAX_CONCURRENT_EMULATORS=50
ADVANCED_PERFORMANCE_MODE=balanced
ADVANCED_AUTO_RESTART_ON_CRASH=true

UGTE_LICENSE_KEY=EE-XXXX-XXXX-XXXX-XXXX
```

---

### Example 3: Testing/QA Environment

**Scenario:** Fast testing, multiple protocols, accelerated time

```bash
# .env
WEB_PORT=5000
WEB_DEBUG=false

API_ENABLE_AUTHENTICATION=false

TRACCAR_HOST=traccar-test.company.local
TRACCAR_PORT=8082

SIMULATION_UPDATE_INTERVAL=5.0
SIMULATION_SPEED_MULTIPLIER=20.0
SIMULATION_DEFAULT_SPEED=80.0

LOG_LEVEL=INFO

ADVANCED_MAX_CONCURRENT_EMULATORS=30
ADVANCED_PERFORMANCE_MODE=fast
```

---

### Example 4: Raspberry Pi / Low Power

**Scenario:** Embedded system, limited resources

```bash
# .env
WEB_PORT=5000
WEB_DEBUG=false

API_ENABLED=true

SIMULATION_UPDATE_INTERVAL=30.0
SIMULATION_ENABLE_TRAFFIC=false
SIMULATION_ENABLE_WEATHER=false

LOG_LEVEL=WARNING
LOG_MAX_SIZE_MB=5
LOG_BACKUP_COUNT=2

MONITORING_ENABLED=false

ADVANCED_MAX_CONCURRENT_EMULATORS=5
ADVANCED_PERFORMANCE_MODE=efficient
ADVANCED_MEMORY_LIMIT_MB=256

UGTE_CE_DEVICE_LIMIT=5
```

---

## Troubleshooting Configuration

### Configuration Not Loading

**Problem:** Changes to config don't take effect

**Solution:**
1. Restart application after changes
2. Check YAML syntax: `python -c "import yaml; yaml.safe_load(open('config.yaml'))"`
3. Verify .env file exists and has correct format
4. Check file permissions (must be readable)

### Port Already in Use

**Problem:** `Address already in use` error

**Solution:**
```bash
# Change port in .env
WEB_PORT=5001

# Or kill existing process
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### API Key Not Working

**Problem:** API returns 401 Unauthorized

**Solution:**
1. Verify authentication enabled:
   ```bash
   API_ENABLE_AUTHENTICATION=true
   ```
2. Check API key in header:
   ```bash
   curl -H "Authorization: Bearer YOUR_KEY" http://localhost:5000/api/status
   ```
3. Regenerate key if needed:
   ```bash
   openssl rand -hex 32
   ```

### High Memory Usage

**Problem:** Emulator using too much RAM

**Solution:**
1. Reduce concurrent devices:
   ```bash
   ADVANCED_MAX_CONCURRENT_EMULATORS=20
   ```
2. Disable advanced features:
   ```yaml
   simulation:
     enable_traffic_simulation: false
     enable_weather_effects: false
   ```
3. Lower metrics retention:
   ```yaml
   monitoring:
     metrics_retention_hours: 24
   ```

### Traccar Not Receiving Data

**Problem:** Devices not appearing in Traccar

**Solution:**
1. Verify Traccar is running:
   ```bash
   curl http://localhost:8082
   ```
2. Check port numbers match:
   - TK103: Emulator port 5002 = Traccar port 5002
3. Verify Traccar credentials:
   ```bash
   TRACCAR_USERNAME=admin
   TRACCAR_PASSWORD=admin
   ```
4. Check device created in Traccar with correct unique ID

---

## Need Help?

- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for more issues
- Check [FAQ.md](FAQ.md) for common questions
- Review [INSTALLATION.md](INSTALLATION.md) for setup help
- Contact: singaotillos@gmail.com

---

*Configuration guide updated: October 2025*
