# How to Deploy to GitBook

Complete guide to publish your documentation on GitBook.com

---

## Prerequisites

- GitHub account
- GitBook account (free tier available)
- Git installed on your computer

---

## Step 1: Create GitHub Repository

### 1.1 Create New Repository

1. Go to https://github.com/new
2. Repository name: `gps-emulator-docs`
3. Description: `Documentation for Universal GPS Tracker Emulator`
4. Select: **Public** (for free GitBook hosting)
5. ✅ Check "Add a README file"
6. Click "Create repository"

### 1.2 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/gps-emulator-docs.git
cd gps-emulator-docs
```

---

## Step 2: Prepare Documentation Files

### 2.1 Copy GitBook Files

Copy all files from the `gitbook/` folder to your repository:

```bash
# From your emulator directory
cp -r gitbook/* /path/to/gps-emulator-docs/
```

### 2.2 Verify Structure

Your repository should look like this:

```
gps-emulator-docs/
├── .gitbook.yaml
├── README.md
├── SUMMARY.md
├── getting-started/
│   ├── installation.md
│   ├── quick-start.md
│   └── ...
├── user-guide/
│   └── ...
├── protocols/
│   └── ...
├── api-reference/
│   └── ...
└── support/
    └── ...
```

---

## Step 3: Push to GitHub

```bash
# Add all files
git add .

# Commit
git commit -m "Initial documentation"

# Push to GitHub
git push origin main
```

---

## Step 4: Create GitBook Account

### 4.1 Sign Up

1. Go to https://www.gitbook.com/
2. Click "Sign up"
3. Choose "Sign up with GitHub" (recommended)
4. Authorize GitBook to access your GitHub

### 4.2 Choose Plan

- **Free Plan**: Perfect for open-source documentation
- **Plus Plan** ($8/month): For private docs with custom domain
- **Pro Plan** ($32/month): For teams

For this project, **Free Plan** is sufficient.

---

## Step 5: Connect GitHub Repository

### 5.1 Create New Space

1. In GitBook dashboard, click "+ New space"
2. Choose "Import from Git"
3. Select "GitHub"
4. Authorize GitBook to access repositories

### 5.2 Select Repository

1. Find `gps-emulator-docs` in the list
2. Click "Import"
3. GitBook will detect `.gitbook.yaml` automatically

### 5.3 Configure Integration

1. **Branch**: `main`
2. **Auto-sync**: ✅ Enable (syncs automatically when you push to GitHub)
3. Click "Import"

---

## Step 6: Configure GitBook Space

### 6.1 Space Settings

1. Click on space name to edit:
   - **Title**: `Universal GPS Tracker Emulator`
   - **Description**: `Professional GPS Protocol Simulation`

2. **Visibility**:
   - Public (free)
   - Or Private (requires paid plan)

3. **URL**: Choose your subdomain
   - Example: `gps-emulator.gitbook.io`

### 6.2 Customize Appearance

1. **Theme**: Choose Light or Dark
2. **Logo**: Upload your logo (optional)
3. **Favicon**: Upload favicon (optional)
4. **Primary Color**: Set brand color

### 6.3 Enable Features

- ✅ Search
- ✅ Table of Contents
- ✅ Page Navigation
- ✅ PDF Export (paid plan only)

---

## Step 7: Test Your Documentation

### 7.1 Preview

Click "View published site" to see your live documentation:

```
https://YOUR_SPACE.gitbook.io/gps-emulator/
```

### 7.2 Verify

Check that:
- [ ] All pages load correctly
- [ ] Navigation works
- [ ] Search works
- [ ] Images display (if any)
- [ ] Links work
- [ ] Code blocks format correctly

---

## Step 8: Custom Domain (Optional)

### For Paid Plans

1. Go to Space Settings > Domain
2. Add your custom domain: `docs.yourdomain.com`
3. Add CNAME record in your DNS:
   ```
   CNAME docs.yourdomain.com → hosting.gitbook.io
   ```
4. Click "Verify domain"

---

## Step 9: Automatic Updates

### How It Works

Every time you push to GitHub, GitBook automatically updates:

```bash
# Make changes to documentation
nano getting-started/installation.md

# Commit and push
git add .
git commit -m "Update installation guide"
git push origin main

# GitBook syncs automatically within 1-2 minutes
```

---

## Step 10: Collaboration (Optional)

### Invite Team Members

1. Go to Space Settings > Members
2. Click "Invite members"
3. Enter email addresses
4. Choose role:
   - **Editor**: Can edit content
   - **Reviewer**: Can review and comment
   - **Reader**: Read-only access

---

## Alternative: GitBook CLI

### Install GitBook CLI

```bash
npm install -g gitbook-cli
```

### Initialize GitBook Locally

```bash
cd gps-emulator-docs
gitbook init
```

### Serve Locally

```bash
gitbook serve
# Open http://localhost:4000
```

### Build Static Site

```bash
gitbook build
# Output in _book/ directory
```

---

## Publishing to Other Platforms

### GitHub Pages

```bash
# Build static site
gitbook build

# Create gh-pages branch
git checkout -b gh-pages
git add _book/*
git commit -m "Deploy documentation"
git push origin gh-pages

# Enable GitHub Pages in repository settings
# Source: gh-pages branch
```

### ReadTheDocs

1. Go to https://readthedocs.org/
2. Import repository
3. Configure to use GitBook format

### Custom Hosting

Upload `_book/` folder to any web server:
- AWS S3 + CloudFront
- Netlify
- Vercel
- Your own server

---

## Maintenance

### Regular Updates

1. **Keep docs in sync** with code changes
2. **Update screenshots** when UI changes
3. **Add new protocols** as they're added
4. **Fix broken links** regularly

### Versioning

Create versions for major releases:

```bash
# Tag a version
git tag v2.0
git push origin v2.0

# In GitBook, create variant:
# Settings > Variants > New variant > v2.0
```

---

## SEO Optimization

### Meta Tags

Edit `.gitbook.yaml`:

```yaml
root: ./

meta:
  title: Universal GPS Tracker Emulator Documentation
  description: Professional GPS protocol simulation without hardware. 86 protocols supported.
  keywords: gps, tracker, emulator, simulation, tk103, gt06, teltonika

structure:
  readme: README.md
  summary: SUMMARY.md
```

### Sitemap

GitBook generates sitemap automatically at:
```
https://YOUR_SPACE.gitbook.io/sitemap.xml
```

### Robots.txt

GitBook handles this automatically.

---

## Analytics (Optional)

### Google Analytics

1. Get GA tracking ID
2. In GitBook: Settings > Integrations
3. Add Google Analytics
4. Enter tracking ID

### Custom Analytics

Add to `.gitbook.yaml`:

```yaml
plugins:
  - ga
  - matomo

ga:
  token: UA-XXXXXXXX-X

matomo:
  url: https://analytics.yourdomain.com
  siteId: 1
```

---

## Troubleshooting

### Documentation Not Updating

1. Check GitHub integration status
2. Force sync: Settings > Git Sync > Sync Now
3. Check `.gitbook.yaml` is in root

### Pages Not Showing

1. Verify `SUMMARY.md` structure
2. Check file paths are correct
3. Ensure files are committed to GitHub

### Broken Images

1. Use relative paths: `./images/screenshot.png`
2. Or use absolute GitHub URLs
3. Check image files are committed

---

## Cost Breakdown

| Plan | Price | Features |
|------|-------|----------|
| **Free** | $0 | Public docs, GitHub sync, Basic analytics |
| **Plus** | $8/mo | Custom domain, Private docs, PDF export |
| **Pro** | $32/mo | Teams, Advanced customization, SSO |

**Recommendation**: Start with **Free**, upgrade if you need private docs or custom domain.

---

## Your Documentation URL

After setup, your documentation will be available at:

```
https://gps-emulator.gitbook.io/universal-gps-tracker-emulator/
```

Or with custom domain:

```
https://docs.yourdomain.com/
```

---

## Next Steps

1. ✅ Push gitbook files to GitHub
2. ✅ Create GitBook account
3. ✅ Import repository
4. ✅ Configure space
5. ✅ Test live site
6. ✅ Share URL with users!

---

## Example URLs

Here are some well-known projects using GitBook:

- **GitBook itself**: https://docs.gitbook.com/
- **Stripe**: https://stripe.com/docs
- **Kong**: https://docs.konghq.com/
- **OpenZeppelin**: https://docs.openzeppelin.com/

Your documentation can look just as professional!

---

## Support

**GitBook Support**: https://www.gitbook.com/support
**Community**: https://community.gitbook.com/

---

*Ready to publish world-class documentation!* 🚀
