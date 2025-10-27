# GitBook Assets Guide

Instructions for adding images and videos to the GitBook documentation.

---

## Video Tutorial

### Current Status

✅ **Video created:** `C:\Users\PRO\Downloads\Codecanyon\Universal GPS Tracker Emulator.webm`

⏳ **Needs upload:** Video must be uploaded to YouTube or Vimeo

### Steps to Add Video

**1. Upload to YouTube:**

1. Go to [YouTube Studio](https://studio.youtube.com)
2. Click "Create" → "Upload videos"
3. Upload `Universal GPS Tracker Emulator.webm`
4. **Title:** "GPS Tracker Emulator - Creating Your First Device"
5. **Description:**
   ```
   Learn how to create your first GPS device in the Universal GPS Tracker Emulator.

   In this 2-minute tutorial:
   - Open the web dashboard
   - Select a protocol (TK103)
   - Fill device information
   - Start the simulation
   - View device in Traccar

   Documentation: https://YOUR-GITBOOK-URL.gitbook.io/gps-emulator/
   ```
6. **Visibility:** Public or Unlisted
7. Copy the video ID from URL (e.g., `https://youtube.com/watch?v=ABC123XYZ`)

**2. Update GitBook:**

Edit `user-guide/creating-devices.md`:

```markdown
{% embed url="https://www.youtube.com/watch?v=ABC123XYZ" %}
Complete walkthrough of creating your first GPS device
{% endembed %}
```

**3. Alternative: Vimeo**

If you prefer Vimeo:
1. Upload to [Vimeo](https://vimeo.com/upload)
2. Copy video URL
3. Use same embed syntax with Vimeo URL

---

## Screenshots

### Current Status

✅ **12 screenshots created:** `C:\Users\PRO\Downloads\Codecanyon\screenshots\`

⏳ **Needs integration:** Copy to GitBook assets folder

### Screenshots List

| File | Description | Recommended Page |
|------|-------------|------------------|
| `image1.png` | Dashboard principal | README.md, quick-start.md |
| `image2.png` | Device details | creating-devices.md |
| `image3.png` | Traccar Map | traccar-integration.md |
| `image4.png` | Traccar Configuration | traccar-integration.md |
| `image5.png` | Device Configuration | configuration.md |
| `image6.png` | Protocol Selection | creating-devices.md |
| `image7.png` | By Device Tab | creating-devices.md |
| `image8.png` | Dashboard Header | README.md |
| `image9.png` | GPS103 Commands | protocols/gps103.md |
| `image10.png` | TK103 Vehicle Data | protocols/tk103.md |
| `image11.png` | 86 Protocols Showcase | protocols/overview.md |
| `image12.png` | Multi-Device Grid | creating-devices.md |
| `preview.png` | Preview image (590×300) | README.md |
| `thumbnail.png` | Thumbnail (80×80) | README.md |

### Steps to Add Screenshots

**Method 1: GitBook UI (Recommended)**

1. Go to GitBook editor
2. Navigate to page where you want to add image
3. Click "+" → "Image"
4. Upload image from `C:\Users\PRO\Downloads\Codecanyon\screenshots\`
5. Add caption and alt text
6. GitBook automatically optimizes and hosts the image

**Method 2: Git Repository**

1. Create assets folder:
   ```bash
   cd "C:\Users\PRO\Downloads\Universal GPS Tracker Emulator\gitbook"
   mkdir .gitbook\assets
   ```

2. Copy screenshots:
   ```bash
   copy "C:\Users\PRO\Downloads\Codecanyon\screenshots\*" ".gitbook\assets\"
   ```

3. Rename for clarity:
   ```bash
   ren .gitbook\assets\image1.png dashboard-main.png
   ren .gitbook\assets\image2.png device-details.png
   ren .gitbook\assets\image3.png traccar-map.png
   # ... etc
   ```

4. Reference in markdown:
   ```markdown
   ![Dashboard](/.gitbook/assets/dashboard-main.png)
   ```

5. Commit and push:
   ```bash
   git add .gitbook/assets/
   git commit -m "Add screenshots to GitBook documentation"
   git push origin main
   ```

**Method 3: External Hosting**

Upload to image hosting service (Imgur, Cloudinary, etc.) and use URLs:

```markdown
![Dashboard](https://i.imgur.com/ABC123.png)
```

---

## Recommended Image Placement

### README.md (Home Page)

```markdown
# Universal GPS Tracker Emulator

![GPS Emulator Dashboard](/.gitbook/assets/dashboard-main.png)

## 86 GPS Protocols Supported

![86 Protocols](/.gitbook/assets/protocols-showcase.png)

## Multi-Device Simulation

![Multi-Device Grid](/.gitbook/assets/multi-device-grid.png)
```

### getting-started/quick-start.md

```markdown
## Step 3: Create Your First Device

![Protocol Selection](/.gitbook/assets/protocol-selection.png)

Fill in the device information...

![Device Details](/.gitbook/assets/device-details.png)
```

### user-guide/creating-devices.md

```markdown
## Method 1: Web Interface

### Step 2: Click "Create New Device"

![Create Device Button](/.gitbook/assets/dashboard-header.png)

### Step 3: Fill Device Information

![Device Configuration Form](/.gitbook/assets/device-configuration.png)
```

### user-guide/traccar-integration.md

```markdown
## Viewing in Traccar

Once your device is running, open Traccar:

![Traccar Map View](/.gitbook/assets/traccar-map.png)

## Configuring Traccar

![Traccar Configuration](/.gitbook/assets/traccar-configuration.png)
```

### protocols/overview.md

```markdown
# GPS Protocols Overview

We support 86 different GPS protocols:

![All Protocols](/.gitbook/assets/protocols-showcase.png)
```

---

## Image Optimization

Before uploading, consider optimizing images:

**Tools:**
- [TinyPNG](https://tinypng.com) - Compress PNG/JPG
- [Squoosh](https://squoosh.app) - Google's image optimizer
- ImageMagick - Command line tool

**Recommended sizes:**
- Screenshots: Max 1920px width
- Icons: 80×80px or 120×120px
- Preview images: 590×300px
- Full-width images: 1200-1600px width

**Formats:**
- PNG: Screenshots with text
- JPG: Photos, complex images
- WebP: Modern format (best compression)

---

## Next Steps

**Priority 1: Add Video**
1. ✅ Video file exists
2. ⏳ Upload to YouTube
3. ⏳ Update `creating-devices.md` with video ID

**Priority 2: Add Key Screenshots**
1. ⏳ Add dashboard screenshot to README.md
2. ⏳ Add protocol showcase to protocols/overview.md
3. ⏳ Add Traccar screenshots to traccar-integration.md

**Priority 3: Complete Documentation**
1. ⏳ Create missing protocol pages
2. ⏳ Add all screenshots to relevant pages
3. ⏳ Verify all links work

---

## Questions?

- **GitBook image upload issues?** Check file size (<5MB) and format (PNG/JPG/GIF)
- **Video embed not working?** Ensure URL is public and from supported platform (YouTube, Vimeo, Loom)
- **Images not showing?** Check file paths are correct (relative to page location)

---

*Last updated: October 2025*
