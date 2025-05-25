# 🌐 r-u-live-open-domain

Get your **FREE** subdomain under **r-u.live** — powered by GitHub and Cloudflare automation!

[![GitHub Stars](https://img.shields.io/github/stars/anshulyadaw/r-u-live-open-domain?style=flat-square)](https://github.com/anshulyadaw/r-u-live-open-domain/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/anshulyadaw/r-u-live-open-domain?style=flat-square)](https://github.com/anshulyadaw/r-u-live-open-domain/network)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 🚀 How to Request Your FREE Subdomain

### Method 1: Via GitHub Issues (Recommended)
1. **[Click here to create a subdomain request](https://github.com/anshulyadaw/r-u-live-open-domain/issues/new?assignees=anshulyadaw&labels=subdomain+request&template=subdomain-request.md&title=Request%3A+%5Byour-subdomain%5D.r-u.live)**
2. Fill out the issue template with your details
3. Wait for approval (usually within 24-48 hours)
4. Your subdomain will be automatically configured!

### Method 2: Via Pull Request (Advanced Users)
1. **Fork this repository** by clicking the "Fork" button above
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/r-u-live-open-domain.git
   cd r-u-live-open-domain
   ```
3. **Create your subdomain file** in the `subdomains/` directory:
   ```bash
   # Replace 'yourname' with your desired subdomain
   cp subdomains/example.yaml subdomains/yourname.yaml
   ```
4. **Edit your subdomain file** (see examples below)
5. **Commit and push** your changes:
   ```bash
   git add subdomains/yourname.yaml
   git commit -m "Add subdomain: yourname.r-u.live"
   git push origin main
   ```
6. **Create a Pull Request** from your fork to this repository
7. **Wait for approval** - once merged, your subdomain goes live automatically!

## 📝 Subdomain Configuration Examples

### For Static Websites (GitHub Pages)
```yaml
subdomain: "myportfolio"
owner:
  name: "Your Full Name"
  email: "your.email@example.com"
record:
  CNAME: "yourusername.github.io"
```
**Result:** `myportfolio.r-u.live` → `yourusername.github.io`

### For Custom Servers (VPS/Cloud)
```yaml
subdomain: "myapi"
owner:
  name: "Your Full Name"
  email: "your.email@example.com"
record:
  A: "123.456.789.123"
```
**Result:** `myapi.r-u.live` → `123.456.789.123`

### For Netlify/Vercel Sites
```yaml
subdomain: "myapp"
owner:
  name: "Your Full Name"
  email: "your.email@example.com"
record:
  CNAME: "your-app-name.netlify.app"
```
**Result:** `myapp.r-u.live` → `your-app-name.netlify.app`

### For Discord Bots/Services
```yaml
subdomain: "mybot"
owner:
  name: "Your Full Name"
  email: "your.email@example.com"
record:
  A: "198.51.100.42"
```
**Result:** `mybot.r-u.live` → `198.51.100.42`

## ✅ Requirements & Rules

### ✅ Allowed:
- Personal websites and portfolios
- Open source projects
- Educational content
- API endpoints
- Discord bots and services
- Static sites (GitHub Pages, Netlify, Vercel)
- Development/staging environments

### ❌ Not Allowed:
- Illegal content or activities
- Adult/NSFW content
- Spam or phishing sites
- Commercial use without permission
- Trademark violations
- Malware or harmful content

## 🔧 Technical Details

- **DNS TTL:** 1 hour (3600 seconds)
- **Supported Records:** A, CNAME
- **Cloudflare Proxy:** Disabled (direct DNS)
- **SSL/TLS:** Automatic via Cloudflare
- **Processing Time:** 24-48 hours for approval
- **Automation:** GitHub Actions + Cloudflare API

## 📋 Subdomain Naming Guidelines

- Use lowercase letters, numbers, and hyphens only
- Must be between 1-63 characters
- Cannot start or end with a hyphen
- Must be unique (first come, first served)
- Descriptive names preferred (e.g., `portfolio`, `api`, `blog`)

### Good Examples:
- ✅ `portfolio.r-u.live`
- ✅ `my-blog.r-u.live`
- ✅ `api-v2.r-u.live`
- ✅ `discord-bot.r-u.live`

### Bad Examples:
- ❌ `test123.r-u.live` (not descriptive)
- ❌ `-mysite.r-u.live` (starts with hyphen)
- ❌ `MyPortfolio.r-u.live` (uppercase letters)

## 🆘 Need Help?

- **Issues with your subdomain?** [Open an issue](https://github.com/anshulyadaw/r-u-live-open-domain/issues)
- **Questions?** Check existing [discussions](https://github.com/anshulyadaw/r-u-live-open-domain/discussions)
- **Email:** Contact the maintainer at the email in your subdomain file

## 🤝 Contributing

We welcome contributions! Feel free to:
- Improve documentation
- Report bugs
- Suggest new features
- Help review subdomain requests

## 📊 Stats

- **Total Subdomains:** Check the [`subdomains/`](./subdomains/) directory
- **Active Since:** 2025
- **Powered By:** GitHub Actions + Cloudflare

## 🔗 Useful Links

- [Cloudflare DNS Documentation](https://developers.cloudflare.com/dns/)
- [GitHub Pages Guide](https://pages.github.com/)
- [How to set up custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

---

## 👨‍💻 Maintainer

Anshul Yadav
