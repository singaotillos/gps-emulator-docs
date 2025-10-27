# CI/CD Integration

Integrate emulator in CI/CD pipelines.

---

## GitHub Actions

```yaml
name: GPS Emulator Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Start emulator
        run: python app.py &
      
      - name: Run tests
        run: pytest tests/
```

---

## GitLab CI

```yaml
test:
  image: python:3.10
  script:
    - pip install -r requirements.txt
    - python app.py &
    - pytest tests/
```

---

*Last updated: October 2025*
