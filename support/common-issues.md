# Common Issues

Quick solutions to common problems.

---

## Installation Issues

### Python Not Found
**Solution:** Install Python 3.8+ and add to PATH

### Pip Install Fails
**Solution:** 
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Runtime Issues

### Port Already in Use
**Solution:** Change port in `.env`
```bash
WEB_PORT=5001
```

### Device Not Sending Data
**Check:**
- Device is running (status = "running")
- Correct protocol port
- Traccar is running

---

## Traccar Issues

### Can't Connect to Traccar
**Check:**
- Traccar URL and port correct
- Traccar credentials valid
- Network connectivity

---

See {% content-ref url="troubleshooting.md" %}[troubleshooting.md](troubleshooting.md){% endcontent-ref %} for detailed solutions.

---

*Last updated: October 2025*
