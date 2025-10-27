# Production Deployment

Deploy emulator to production.

---

## Checklist

- [ ] Enable API authentication
- [ ] Disable debug mode
- [ ] Use HTTPS (reverse proxy)
- [ ] Set strong passwords
- [ ] Enable rate limiting
- [ ] Configure monitoring
- [ ] Setup backups
- [ ] Document deployment

---

## Reverse Proxy (Nginx)

```nginx
server {
    listen 443 ssl;
    server_name gps.example.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## Systemd Service

```ini
[Unit]
Description=GPS Emulator
After=network.target

[Service]
Type=simple
User=gpsuser
WorkingDirectory=/opt/gps-emulator
ExecStart=/usr/bin/python3 /opt/gps-emulator/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

**Enable:**
```bash
sudo systemctl enable gps-emulator
sudo systemctl start gps-emulator
```

---

*Last updated: October 2025*
