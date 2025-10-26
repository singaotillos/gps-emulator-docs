# Installation

Learn how to install the Universal GPS Tracker Emulator on your system.

---

## Prerequisites

Before installing, ensure you have:

* Python 3.8 or higher
* pip (Python package manager)
* 500 MB free disk space
* Administrative/sudo privileges (for some installations)

---

## Installation Methods

{% tabs %}
{% tab title="Windows" %}
### Windows Installation

#### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **✅ CHECK:** "Add Python to PATH"
4. Click "Install Now"

#### Step 2: Verify Installation

```powershell
python --version
# Should show: Python 3.8.x or higher

pip --version
# Should show: pip 21.x or higher
```

#### Step 3: Extract the Package

1. Extract `Universal-GPS-Tracker-Emulator-v2.0.zip`
2. Navigate to the `src` folder

#### Step 4: Install Dependencies

```powershell
cd path\to\Universal-GPS-Tracker-Emulator-v2.0\src
pip install -r requirements.txt
```

#### Step 5: Run the Emulator

```powershell
python app.py
```

#### Step 6: Access Dashboard

Open browser: **http://localhost:5000**

{% hint style="success" %}
**Success!** You should see the GPS Emulator dashboard.
{% endhint %}

### Common Windows Issues

**Issue: Python not found**
```powershell
# Add Python to PATH manually
# Control Panel > System > Advanced > Environment Variables
# Add: C:\Python3x\ and C:\Python3x\Scripts\
```

**Issue: pip install fails**
```powershell
# Run as Administrator
# Right-click Command Prompt > Run as administrator
pip install -r requirements.txt
```
{% endtab %}

{% tab title="Linux" %}
### Linux Installation

#### Step 1: Install Python

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip
```

#### Step 2: Verify Installation

```bash
python3 --version
# Should show: Python 3.8.x or higher

pip3 --version
# Should show: pip 21.x or higher
```

#### Step 3: Extract the Package

```bash
cd ~/Downloads
unzip Universal-GPS-Tracker-Emulator-v2.0.zip
cd Universal-GPS-Tracker-Emulator-v2.0/src
```

#### Step 4: Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 6: Run the Emulator

```bash
python app.py
```

#### Step 7: Access Dashboard

Open browser: **http://localhost:5000**

{% hint style="info" %}
**Firewall:** You may need to allow port 5000 through firewall.
```bash
sudo ufw allow 5000/tcp
```
{% endhint %}

### Running as System Service

Create a systemd service:

```bash
sudo nano /etc/systemd/system/gps-emulator.service
```

Add this content:
```ini
[Unit]
Description=GPS Tracker Emulator
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/src
ExecStart=/usr/bin/python3 /path/to/src/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable gps-emulator
sudo systemctl start gps-emulator
sudo systemctl status gps-emulator
```
{% endtab %}

{% tab title="macOS" %}
### macOS Installation

#### Step 1: Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Python

```bash
brew install python@3.10
```

#### Step 3: Verify Installation

```bash
python3 --version
# Should show: Python 3.8.x or higher

pip3 --version
```

#### Step 4: Extract and Navigate

```bash
cd ~/Downloads
unzip Universal-GPS-Tracker-Emulator-v2.0.zip
cd Universal-GPS-Tracker-Emulator-v2.0/src
```

#### Step 5: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 7: Run the Emulator

```bash
python app.py
```

#### Step 8: Access Dashboard

Open browser: **http://localhost:5000**

{% hint style="warning" %}
**macOS Security:** You may see a security warning. Go to System Preferences > Security & Privacy and click "Allow".
{% endhint %}
{% endtab %}

{% tab title="Docker" %}
### Docker Installation

#### Step 1: Install Docker

Download from [docker.com](https://www.docker.com/get-started)

#### Step 2: Create Dockerfile

In the project root, create `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

#### Step 3: Build Image

```bash
docker build -t gps-emulator:latest .
```

#### Step 4: Run Container

```bash
docker run -d \
  --name gps-emulator \
  -p 5000:5000 \
  -p 5002:5002 \
  -p 5023:5023 \
  -p 5027:5027 \
  -v $(pwd)/config.yaml:/app/config.yaml \
  gps-emulator:latest
```

#### Step 5: Access Dashboard

Open browser: **http://localhost:5000**

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  gps-emulator:
    build: .
    ports:
      - "5000:5000"
      - "5002:5002"   # TK103
      - "5023:5023"   # GT06
      - "5027:5027"   # Teltonika
      - "5055:5055"   # OsmAnd
    volumes:
      - ./config.yaml:/app/config.yaml
      - ./data:/app/data
    restart: unless-stopped
    environment:
      - WEB_HOST=0.0.0.0
      - WEB_PORT=5000
```

Run with:
```bash
docker-compose up -d
```

{% hint style="success" %}
**Pro Tip:** Use Docker for easy deployment and isolation!
{% endhint %}
{% endtab %}
{% endtabs %}

---

## Post-Installation

### Verify Installation

1. **Check Web Interface**
   - Open http://localhost:5000
   - You should see the dashboard

2. **Check API**
   ```bash
   curl http://localhost:5000/api/status
   ```

3. **Check Protocols**
   ```bash
   curl http://localhost:5000/api/protocols
   ```

### Configuration

After installation, configure the emulator:

{% content-ref url="../user-guide/configuration.md" %}
[configuration.md](../user-guide/configuration.md)
{% endcontent-ref %}

---

## Updating

### Update to Latest Version

1. Download the new version
2. Extract to new directory
3. Copy your `config.yaml` from old installation
4. Copy your `.env` file (if customized)
5. Run `pip install -r requirements.txt` (in case dependencies changed)

{% hint style="info" %}
**Backup:** Always backup your configuration before updating!
{% endhint %}

---

## Uninstallation

### Remove the Emulator

**Windows/macOS/Linux:**
```bash
# Stop the emulator (Ctrl+C)

# Remove virtual environment (if used)
rm -rf venv

# Remove application files
cd ..
rm -rf Universal-GPS-Tracker-Emulator-v2.0
```

**Docker:**
```bash
docker stop gps-emulator
docker rm gps-emulator
docker rmi gps-emulator:latest
```

---

## Next Steps

{% content-ref url="quick-start.md" %}
[quick-start.md](quick-start.md)
{% endcontent-ref %}

{% content-ref url="../user-guide/configuration.md" %}
[configuration.md](../user-guide/configuration.md)
{% endcontent-ref %}
