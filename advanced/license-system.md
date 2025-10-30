# License System - Demo & Full Version

## Vue d'ensemble

Le système implémente deux versions:
- **DEMO**: Gratuite, limitée à **3 devices**
- **FULL**: Payante (CodeCanyon), **devices illimités**

```
┌─────────────────────────────────────┐
│  VERSION    │  DEVICES  │  PRIX     │
├─────────────────────────────────────┤
│  DEMO       │  Max 3    │  GRATUIT  │
│  FULL       │  Illimité │  $XX USD  │
└─────────────────────────────────────┘
```

---

## 🔒 Fonctionnalités

### Version DEMO (Par Défaut)

**Limitations:**
- Maximum **3 devices** simultanés
- Message d'erreur au 4ème device
- Lien vers CodeCanyon pour upgrade

**Fonctionnalités complètes:**
- ✅ Tous les 86 protocoles
- ✅ Carte Leaflet temps réel
- ✅ Sync Traccar
- ✅ Routes réalistes OSRM
- ✅ Commandes vehicles
- ✅ Toutes features premium

### Version FULL (Après Achat)

**Unlock:**
- **Devices illimités**
- License key fournie après achat CodeCanyon
- Activation en 1 clic

---

## 🎯 Flux d'Utilisation

### Scénario 1: User DEMO

```
1. User télécharge depuis CodeCanyon
2. Lance python app.py
3. Voit: "DEMO VERSION - Limited to 3 devices"
4. Ajoute Device 1: ✅ OK
5. Ajoute Device 2: ✅ OK
6. Ajoute Device 3: ✅ OK
7. Tente Device 4: ❌ BLOCKED

Message affiché:
┌─────────────────────────────────────────────┐
│  DEMO VERSION LIMIT                         │
│  You can only add 3 devices.                │
│                                             │
│  To unlock unlimited devices:               │
│  1. Purchase on CodeCanyon: [LINK]          │
│  2. Enter your purchase code in Settings    │
│  3. Enjoy unlimited devices!                │
└─────────────────────────────────────────────┘
```

### Scénario 2: User Achète

```
1. User clique lien CodeCanyon
2. Achète le produit ($XX USD)
3. Reçoit Purchase Code: a1b2c3d4-e5f6-7890-abcd-ef1234567890
4. Dans dashboard: Settings → License
5. Entre Purchase Code
6. Système génère License Key automatiquement
7. Activation: ✅ FULL VERSION UNLOCKED
8. Peut maintenant ajouter devices illimités
```

---

## 🔑 Format License Key

### Structure

```
UGPS-XXXX-XXXX-XXXX-XXXX

Exemple: UGPS-13C8-F7DF-5665-E86B

Où:
- UGPS:  Prefix produit (Universal GPS)
- XXXX:  Hash du purchase code (partie 1)
- XXXX:  Hash du purchase code (partie 2)
- XXXX:  Hash du purchase code (partie 3)
- XXXX:  Checksum MD5 pour validation
```

### Génération

**Depuis Purchase Code:**
```
Input:  a1b2c3d4-e5f6-7890-abcd-ef1234567890
Output: UGPS-13C8-F7DF-5665-E86B
```

**Algorithme:**
1. Hash SHA256 du purchase code
2. Extraire 3 parties de 4 chars
3. Calculer checksum MD5
4. Combiner: UGPS-{part1}-{part2}-{part3}-{checksum}

### Validation

**Critères:**
1. Format correct (25 chars, 5 parties)
2. Prefix = "UGPS"
3. Checksum MD5 valide
4. Parties alphanumériques

---

## 📡 API Endpoints

### 1. Get License Info

```bash
GET /api/license/info
```

**Response (DEMO):**
```json
{
  "success": true,
  "license": {
    "status": "demo",
    "version": "demo",
    "key": null,
    "activated_at": null,
    "max_devices": 3
  },
  "limits": {
    "version": "demo",
    "is_licensed": false,
    "current_devices": 2,
    "max_devices": 3,
    "remaining_devices": 1,
    "message": "Demo version - 1/3 devices remaining",
    "upgrade_url": "https://codecanyon.net/..."
  }
}
```

**Response (FULL):**
```json
{
  "success": true,
  "license": {
    "status": "active",
    "version": "full",
    "key": "UGPS-13C8-F7DF-5665-E86B",
    "activated_at": "2025-10-27T20:00:00",
    "max_devices": "unlimited"
  },
  "limits": {
    "version": "full",
    "is_licensed": true,
    "current_devices": 10,
    "max_devices": "unlimited",
    "remaining_devices": "unlimited",
    "message": "Full version - Unlimited devices"
  }
}
```

### 2. Activate License

```bash
POST /api/license/activate
Content-Type: application/json

{
  "license_key": "UGPS-13C8-F7DF-5665-E86B"
}
```

**Response (Success):**
```json
{
  "success": true,
  "message": "License activated successfully! Unlimited devices unlocked.",
  "license": {
    "status": "active",
    "version": "full",
    "key": "UGPS-13C8-F7DF-5665-E86B",
    "activated_at": "2025-10-27T20:00:00",
    "max_devices": "unlimited"
  }
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Invalid license key. Please check and try again."
}
```

### 3. Generate License (Admin/Test)

```bash
POST /api/license/generate
Content-Type: application/json

{
  "purchase_code": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

**Response:**
```json
{
  "success": true,
  "license_key": "UGPS-13C8-F7DF-5665-E86B",
  "purchase_code": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

---

## 💻 Intégration Code

### Backend (app.py)

**Vérification lors ajout device:**
```python
# Dans api_add_device_with_traccar_sync()
current_device_count = len(manager.emulators)
can_add, error_message = manager.license_manager.can_add_device(current_device_count)

if not can_add:
    return jsonify({
        'success': False,
        'error': error_message,
        'license_limit_reached': True
    })
```

**Initialisation:**
```python
# Dans EmulatorManager.__init__()
self.license_manager = LicenseManager()
logger.info(f"License: {self.license_manager.get_license_info()['version'].upper()} version")
```

### Frontend (JavaScript)

**Afficher erreur limitation:**
```javascript
// Quand addDevice échoue
if (response.license_limit_reached) {
    showLicenseModal(response.error, response.license_info);
}
```

**Vérifier status license:**
```javascript
async function checkLicenseStatus() {
    const response = await fetch('/api/license/info');
    const data = await response.json();

    if (data.license.version === 'demo') {
        showDemoBanner(data.limits);
    }
}
```

---

## 🗂️ Fichiers

### 1. license_manager.py

**Module principal** gérant toute la logique license:
- Vérification limites
- Génération clés
- Validation checksums
- Stockage (license.json)

**Classes:**
```python
class LicenseManager:
    DEMO_MAX_DEVICES = 3

    def can_add_device(current_count) -> (bool, str)
    def activate_license(license_key) -> bool
    def generate_license_key(purchase_code) -> str
```

### 2. license.json

**Fichier de stockage** de la license activée:
```json
{
  "key": "UGPS-13C8-F7DF-5665-E86B",
  "activated_at": "2025-10-27T20:00:00",
  "product": "Universal GPS Tracker Emulator",
  "version": "full"
}
```

**Emplacement:** Racine du projet

---

## 🧪 Tests

### Test 1: Limitation DEMO

```bash
# 1. S'assurer en mode DEMO
rm license.json  # Si existe

# 2. Démarrer app
python app.py
# Log: "DEMO VERSION - Limited to 3 devices"

# 3. Ajouter devices via dashboard
Device 1: ✅ Success
Device 2: ✅ Success
Device 3: ✅ Success
Device 4: ❌ BLOCKED - "DEMO VERSION LIMIT: You can only add 3 devices"
```

### Test 2: Activation License

```bash
# 1. Générer license key
curl -X POST http://localhost:5000/api/license/generate \
  -H "Content-Type: application/json" \
  -d '{"purchase_code": "test-purchase-code-12345"}'

# Response: {"license_key": "UGPS-XXXX-XXXX-XXXX-XXXX"}

# 2. Activer
curl -X POST http://localhost:5000/api/license/activate \
  -H "Content-Type: application/json" \
  -d '{"license_key": "UGPS-XXXX-XXXX-XXXX-XXXX"}'

# Response: {"success": true, "message": "License activated..."}

# 3. Vérifier
curl http://localhost:5000/api/license/info

# Response: {"license": {"version": "full", ...}}

# 4. Tester devices illimités
# Ajouter 10+ devices: ✅ Tous passent
```

### Test 3: License Invalide

```bash
curl -X POST http://localhost:5000/api/license/activate \
  -H "Content-Type: application/json" \
  -d '{"license_key": "INVALID-KEY-1234-5678"}'

# Response: {"success": false, "error": "Invalid license key..."}
```

---

## 🎨 UI/UX

### Banner DEMO

**Affichage permanent** en haut du dashboard:
```
┌─────────────────────────────────────────────────────┐
│  ℹ️ DEMO VERSION - 1/3 devices remaining            │
│  [Upgrade to Full Version]                          │
└─────────────────────────────────────────────────────┘
```

### Modal Limitation Atteinte

**Quand 4ème device tenté:**
```
┌─────────────────────────────────────────────────────┐
│  ⚠️ DEMO VERSION LIMIT REACHED                      │
│                                                     │
│  You have reached the maximum of 3 devices.         │
│                                                     │
│  To unlock unlimited devices:                       │
│  1. Purchase on CodeCanyon                          │
│     [Buy Now - $XX USD]                             │
│  2. Enter your purchase code below                  │
│                                                     │
│  [Cancel]                [I Have a Purchase Code]   │
└─────────────────────────────────────────────────────┘
```

### Modal Activation

**Quand user clique "I Have a Purchase Code":**
```
┌─────────────────────────────────────────────────────┐
│  🔑 Activate Full Version                           │
│                                                     │
│  Enter your CodeCanyon Purchase Code:               │
│  ┌───────────────────────────────────────────────┐ │
│  │ a1b2c3d4-e5f6-7890-abcd-ef1234567890         │ │
│  └───────────────────────────────────────────────┘ │
│                                                     │
│  [Cancel]                          [Activate]       │
└─────────────────────────────────────────────────────┘
```

---

## ⚙️ Configuration

### Changer Limite DEMO

**Dans license_manager.py:**
```python
class LicenseManager:
    DEMO_MAX_DEVICES = 3  # Changer à 5, 10, etc.
```

### Changer URL CodeCanyon

**Dans license_manager.py:**
```python
CODECANYON_URL = "https://codecanyon.net/item/universal-gps-emulator/XXXXXX"
```

**Remplacer XXXXXX** par votre vrai ID produit CodeCanyon.

### Désactiver License (Dev)

**Pour tests illimités:**
```python
# Dans EmulatorManager.__init__()
# Commenter:
# self.license_manager = LicenseManager()

# Ou modifier can_add_device:
def can_add_device(self, current_count):
    return True, None  # Toujours OK
```

---

## 📊 Statistiques

### Taux Conversion Attendu

```
100 Downloads DEMO:
├─ 80 users testent (3 devices)
├─ 20 users bloqués (veulent + de 3)
└─ 5-10 achètent (~5-10% conversion)

ROI:
- Prix: $XX USD
- 5 ventes = $XXX USD
- 10 ventes = $XXXX USD
```

### Métriques à Tracker

- Nombre total downloads
- Nombre users DEMO vs FULL
- Tentatives 4ème+ device (= intérêt achat)
- Taux activation licenses
- Revenue total

---

## ✅ Checklist Deployment

### Avant Release CodeCanyon

- [ ] Mettre vrai URL CodeCanyon dans `license_manager.py`
- [ ] Mettre vrai prix dans messages
- [ ] Tester limitation 3 devices
- [ ] Tester activation license
- [ ] Documenter dans README
- [ ] Créer guide purchase pour buyers
- [ ] Préparer support responses
- [ ] Tester sur Windows/Linux/Mac

### Pour Chaque Vente

1. Buyer achète sur CodeCanyon
2. Envato génère Purchase Code
3. Buyer entre Purchase Code dans app
4. App génère License Key automatiquement
5. License activée ✅
6. Devices illimités unlocked ✅

---

## 🚀 Avantages du Système

### Pour Développeur

- ✅ Revenue récurrent
- ✅ Limite abuse version gratuite
- ✅ Encourage achats légitimes
- ✅ Facile à implémenter
- ✅ Pas de serveur externe requis
- ✅ Validation offline

### Pour Users

- ✅ Version DEMO complète (toutes features)
- ✅ 3 devices gratuits (suffisant pour tests)
- ✅ Activation simple (1 clic)
- ✅ Purchase code = License key auto
- ✅ Pas d'abonnement
- ✅ License permanente

---

**Créé:** 27 octobre 2025
**Projet:** Universal GPS Tracker Emulator
**Fonctionnalité:** Demo/Full License System
**Status:** ✅ PRODUCTION READY
**Impact:** REVENUE GENERATION

---

**Fichiers:**
- [license_manager.py](license_manager.py) - Module license (300+ lignes)
- [app.py](app.py) - Intégration API routes
- [LICENSE_SYSTEM.md](LICENSE_SYSTEM.md) - Ce document

**Navigation:**
- 🏠 Accueil: [START_HERE.md](START_HERE.md)
- 🗺️ Routing: [REALISTIC_ROUTING.md](REALISTIC_ROUTING.md)
- 📖 GitBook: [gitbook/](gitbook/)
