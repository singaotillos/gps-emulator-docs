# Example Page with Images - GitBook

Ce fichier montre comment intégrer des images dans GitBook.

---

## 📸 1. Image Simple

Pour ajouter une image simple :

```markdown
![Description de l'image](/.gitbook/assets/screenshots/dashboard.png)
```

**Résultat :**

![Application Preview](/.gitbook/assets/screenshots/preview.png)

---

## 📸 2. Image avec Légende

Pour ajouter une image avec légende et contexte :

```markdown
{% hint style="info" %}
**Dashboard Overview** - Vue complète avec 5 appareils actifs
{% endhint %}

![Dashboard](/.gitbook/assets/screenshots/screen1.jpg)
```

**Résultat :**

{% hint style="info" %}
**Dashboard Overview** - Vue complète du tableau de bord avec plusieurs appareils simulés
{% endhint %}

![Dashboard](/.gitbook/assets/screenshots/screen1.jpg)

---

## 📸 3. Galerie d'Images (Cards)

Pour créer une galerie d'images en mode carte :

```markdown
<table data-view="cards">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Dashboard</strong></td>
      <td>Vue principale de l'application</td>
      <td>
        <img src="/.gitbook/assets/screenshots/screen1.jpg" alt="Dashboard">
      </td>
    </tr>
    <tr>
      <td><strong>Device List</strong></td>
      <td>Liste des appareils GPS simulés</td>
      <td>
        <img src="/.gitbook/assets/screenshots/screen2.jpg" alt="Devices">
      </td>
    </tr>
    <tr>
      <td><strong>Map View</strong></td>
      <td>Visualisation carte en temps réel</td>
      <td>
        <img src="/.gitbook/assets/screenshots/screen3.jpg" alt="Map">
      </td>
    </tr>
  </tbody>
</table>
```

---

## 📸 4. Image avec Avertissement

Pour attirer l'attention sur une image importante :

```markdown
{% hint style="warning" %}
**Important:** Assurez-vous de configurer les ports correctement
{% endhint %}

![Configuration](/.gitbook/assets/screenshots/screen4.jpg)
```

**Résultat :**

{% hint style="warning" %}
**Important:** Assurez-vous de configurer les ports correctement avant de démarrer
{% endhint %}

![Configuration](/.gitbook/assets/screenshots/screen4.jpg)

---

## 📸 5. Images Côte à Côte

Pour comparer deux images :

```markdown
| Avant | Après |
|-------|-------|
| ![Before](/.gitbook/assets/screenshots/image5.png) | ![After](/.gitbook/assets/screenshots/image6.png) |
```

**Résultat :**

| Avant | Après |
|-------|-------|
| ![Before](/.gitbook/assets/screenshots/image5.png) | ![After](/.gitbook/assets/screenshots/image6.png) |

---

## 📸 6. Image Cliquable (Zoom)

Les images dans GitBook sont automatiquement cliquables pour zoomer.

```markdown
Cliquez sur l'image pour l'agrandir :

![Large Screenshot](/.gitbook/assets/screenshots/image11.png)
```

**Résultat :**

Cliquez sur l'image pour l'agrandir :

![Large Screenshot](/.gitbook/assets/screenshots/image11.png)

---

## 🎬 7. GIF Animé (Future)

Pour ajouter un GIF animé :

```markdown
### Quick Start Demo

Voici comment créer votre premier appareil GPS :

![Quick Start](/.gitbook/assets/gifs/quick-start.gif)
```

---

## 📊 8. Diagramme (Future)

Pour ajouter un diagramme d'architecture :

```markdown
### Architecture Overview

![System Architecture](/.gitbook/assets/diagrams/architecture.svg)
```

---

## 🎨 9. Icône Inline

Pour ajouter une petite icône dans le texte :

```markdown
Fonctionnalités principales :
- ✅ Multi-device simulation
- 🗺️ Real-time map
- 🔌 REST API
- 📊 Monitoring
```

**Résultat :**

Fonctionnalités principales :
- ✅ Multi-device simulation
- 🗺️ Real-time map
- 🔌 REST API
- 📊 Monitoring

---

## 💡 Conseils

### Chemins d'Images

**Toujours utiliser le chemin absolu depuis la racine :**
```markdown
✅ CORRECT : ![Image](/.gitbook/assets/screenshots/image.png)
❌ INCORRECT : ![Image](../assets/screenshots/image.png)
❌ INCORRECT : ![Image](assets/screenshots/image.png)
```

### Taille des Images

**Optimiser les images :**
- PNG : < 500KB
- JPG : < 300KB
- GIF : < 2MB

**Si trop lourdes :**
- Utiliser https://tinypng.com/
- Ou https://squoosh.app/

### Alt Text

**Toujours ajouter un texte alternatif :**
```markdown
![Dashboard showing 5 active GPS devices](/.gitbook/assets/screenshots/dashboard.png)
```

---

## 🔗 Liens Utiles

- [GitBook Image Documentation](https://docs.gitbook.com/content-editor/blocks/insert-images)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Image Optimization](https://tinypng.com/)

---

**Fichier de démonstration créé le :** 30 octobre 2025
**Statut :** ✅ Prêt à être dupliqué dans d'autres pages
