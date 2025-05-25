# 🌐 r-u-live Open Domain

Get your **free subdomain** under **r-u.live** — completely automated through GitHub and Cloudflare!

[![GitHub issues](https://img.shields.io/github/issues/anshulyadaw/r-u-live-open-domain)](https://github.com/anshulyadaw/r-u-live-open-domain/issues)
[![GitHub stars](https://img.shields.io/github/stars/anshulyadaw/r-u-live-open-domain)](https://github.com/anshulyadaw/r-u-live-open-domain/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/anshulyadaw/r-u-live-open-domain)](https://github.com/anshulyadaw/r-u-live-open-domain/network)
[![License](https://img.shields.io/github/license/anshulyadaw/r-u-live-open-domain)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Community-7289da)](https://discord.gg/your-discord-link)
[![Website](https://img.shields.io/badge/Website-r--u.live-blue)](https://r-u.live)

## 🎯 What is this?

This project provides **free subdomains** under the `r-u.live` domain with **fully automated DNS management** via Cloudflare API. Perfect for:

- 🚀 **Personal projects** and portfolios
- 💻 **GitHub Pages** websites  
- 🔧 **Development** and testing environments
- 📱 **Small applications** and demos
- 🎓 **Student projects** and learning
- 🌟 **Open source** project websites

**🎉 Join 100+ developers already using r-u.live subdomains!**

## 📋 Table of Contents

- [⚡ Automation Features](#-automation-features)
- [🚀 How to Request Your Subdomain](#-how-to-request-your-subdomain)
- [📖 Examples](#-examples)
- [⏱️ Processing Timeline](#️-processing-timeline)
- [🛡️ Security & Guidelines](#️-security--guidelines)
- [🤖 API Integration](#-api-integration)
- [🏗️ For Administrators](#️-for-administrators)
- [🤝 Contributing](#-contributing)
- [📞 Support](#-support)
- [📄 License](#-license)

## ⚡ Enhanced Automation Features

**🎯 Inspired by open-domains/register project:**

- 🔍 **Intelligent auto-parsing** with multiple pattern recognition
- 🛡️ **Multi-stage security validation** (malware, phishing, spam detection)
- 🌐 **Comprehensive DNS validation** (A, AAAA, CNAME records)
- 📧 **Smart error reporting** with detailed guidance and examples
- 🤖 **Auto-conversion** from issues to pull requests
- 🔒 **Security scanning** for malicious content and suspicious patterns
- 📊 **Community health monitoring** with abuse report handling
- 🎯 **Advanced validation pipeline** with connectivity testing
- 🏷️ **Intelligent labeling** and workflow automation
- 📈 **Analytics and tracking** for all requests
- 🚨 **Real-time abuse detection** and response system

**📚 [View Complete Feature Documentation](./docs/ENHANCED_FEATURES.md)**

## 🚀 How to Request Your Subdomain

### Method 1: Create an Issue (Recommended for beginners)

1. **[Create a new issue](https://github.com/anshulyadaw/r-u-live-open-domain/issues/new?template=subdomain-request.md)** using our template
2. Fill in the required details:
   - Your desired subdomain name
   - Record type (A or CNAME)
   - Target IP address or domain
   - Your contact information
3. Wait for approval and automatic setup!

### Method 2: Direct Pull Request (For developers)

1. **Fork this repository**
   ```bash
   # Click the "Fork" button on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/r-u-live-open-domain.git
   cd r-u-live-open-domain
   ```

2. **Create your subdomain file**
   ```bash
   # Create a new YAML file in the subdomains directory
   touch subdomains/yourname.yaml
   ```

3. **Add your configuration** (see examples below)

4. **Submit a Pull Request**
   ```bash
   git add subdomains/yourname.yaml
   git commit -m "Add subdomain: yourname.r-u.live"
   git push origin main
   # Then create a PR on GitHub
   ```

## 📝 Subdomain Configuration Examples

### Example 1: Point to an IP Address (A Record)
```yaml
subdomain: "myproject"
owner:
  name: "John Doe"
  email: "john@example.com"
record:
  A: "192.168.1.100"
```
**Result:** `myproject.r-u.live` → `192.168.1.100`

### Example 2: Point to GitHub Pages (CNAME Record)
```yaml
subdomain: "portfolio"
owner:
  name: "Jane Smith"
  email: "jane@example.com"
record:
  CNAME: "janesmith.github.io"
```
**Result:** `portfolio.r-u.live` → `janesmith.github.io`

### Example 3: Point to Netlify/Vercel (CNAME Record)
```yaml
subdomain: "webapp"
owner:
  name: "Dev Team"
  email: "team@startup.com"
record:
  CNAME: "amazing-app-123.netlify.app"
```
**Result:** `webapp.r-u.live` → `amazing-app-123.netlify.app`

### Example 4: Point to Heroku App (CNAME Record)
```yaml
subdomain: "api"
owner:
  name: "Backend Developer"
  email: "dev@company.com"
record:
  CNAME: "my-api-app.herokuapp.com"
```
**Result:** `api.r-u.live` → `my-api-app.herokuapp.com`

## 📋 Requirements

### Subdomain Name Rules
- ✅ Must be 3-63 characters long
- ✅ Can contain letters (a-z), numbers (0-9), and hyphens (-)
- ✅ Must start and end with a letter or number
- ❌ Cannot contain special characters or spaces
- ❌ Cannot be offensive or inappropriate

### Valid Examples:
- `mysite`, `portfolio`, `blog`, `api-v2`, `test123`

### Invalid Examples:
- `my site` (contains space)
- `-api` (starts with hyphen)
- `@#$%` (special characters)

## ⏱️ Processing Timeline

Our automated system ensures fast processing times:

| Stage | Time | What Happens |
|-------|------|--------------|
| **🔍 Initial Validation** | Instant | Automated checks run on PR creation |
| **👥 Manual Review** | 1-3 days | Maintainer reviews for compliance |
| **🔄 Feedback Loop** | 1-2 days | Address any requested changes |
| **✅ Final Approval** | 1-2 days | Maintainer approves and merges |
| **🚀 DNS Deployment** | Instant | Cloudflare API automatically creates records |
| **🌐 Propagation** | 5-60 min | DNS propagates globally |

**Total time: Usually 2-5 days for compliant requests**

## 🛡️ Security & Guidelines

### ✅ Allowed Use Cases
- Personal portfolios and blogs
- Open source project websites
- Educational and student projects
- Development demos and prototypes
- GitHub Pages hosting
- Non-commercial applications

### ❌ Prohibited Use Cases
- Commercial/business websites
- Malicious content (malware, phishing)
- Adult or inappropriate content
- Resource-intensive applications
- Multiple subdomains without justification

**📖 Read our [Community Guidelines](COMMUNITY_GUIDELINES.md) for detailed rules**

## 🤖 API Integration

### Programmatic Access
While we don't offer a public API yet, you can integrate with our system through:

- **GitHub API**: Automate issue/PR creation
- **Webhooks**: Monitor your subdomain status
- **Actions Integration**: Build deployment pipelines

### Coming Soon 🚧
- REST API for subdomain management
- Webhook notifications for DNS changes
- Bulk operations endpoint
- Status dashboard API

## ⚡ Automatic Processing

Our **fully automated system** handles everything for you:

### 🔍 **Pull Request Validation**
- Real-time YAML syntax checking
- Subdomain availability verification  
- IP address and domain validation
- Duplicate detection across all files
- Security screening for malicious content
- Automatic PR comments with results

### 🚀 **DNS Deployment** (After Merge)
- Instant Cloudflare API integration
- Automatic DNS record creation/updates
- Error handling and retry logic
- Success confirmation notifications
- Complete deployment logging

### 📊 **Monitoring & Management**
- Real-time status updates
- Automated health checks  
- Manual override capabilities
- Bulk operations support
- Performance analytics

## 🛠️ For GitHub Pages Users

If you're hosting on GitHub Pages, add this to your repository settings:

1. Go to your repo **Settings** → **Pages**
2. Add **Custom domain**: `yourname.r-u.live`
3. Enable **Enforce HTTPS**

## 📞 Support & Help

- 🐛 **Found a bug?** [Create an issue](https://github.com/anshulyadaw/r-u-live-open-domain/issues)
- ❓ **Need help?** Check our [Wiki](https://github.com/anshulyadaw/r-u-live-open-domain/wiki) or comment on your PR
- 💬 **Questions?** Mention `@anshulyadaw` in your issue

## 🚫 Abuse Policy

Subdomains used for spam, malware, or illegal content will be **immediately removed**. This service is for legitimate projects only.

## 📊 Statistics

- 🎯 **Active Subdomains**: Check the [subdomains directory](./subdomains/)
- ⚡ **Average Setup Time**: 5-10 minutes after approval
- 🔄 **Uptime**: 99.9% (powered by Cloudflare)

## 🤝 Contributing

Want to help improve this project?

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 🗺️ Roadmap

### 🚀 Version 2.0 (Coming Soon)
- [ ] **REST API**: Programmatic subdomain management
- [ ] **Dashboard**: Web interface for subdomain management
- [ ] **Analytics**: Usage statistics and monitoring
- [ ] **Custom TTL**: Configure DNS record TTL values
- [ ] **Subdomain Transfer**: Transfer ownership between users

### 🔮 Future Plans
- [ ] **Multiple Domains**: Support for additional free domains
- [ ] **Premium Features**: Priority support and advanced features
- [ ] **Mobile App**: Native mobile application
- [ ] **Integration Plugins**: WordPress, Shopify, etc.
- [ ] **Enterprise Support**: For educational institutions

**💡 Have ideas? [Share them in Discussions](https://github.com/anshulyadaw/r-u-live-open-domain/discussions)**

## 📊 Project Stats

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/anshulyadaw/r-u-live-open-domain)
![GitHub language count](https://img.shields.io/github/languages/count/anshulyadaw/r-u-live-open-domain)
![GitHub top language](https://img.shields.io/github/languages/top/anshulyadaw/r-u-live-open-domain)
![GitHub last commit](https://img.shields.io/github/last-commit/anshulyadaw/r-u-live-open-domain)

</div>

## 🌟 Acknowledgments

Special thanks to:
- **Cloudflare** for providing reliable DNS infrastructure
- **GitHub Actions** for automation capabilities
- **Open source community** for inspiration and feedback
- **All contributors** who help maintain this service

Inspired by similar projects:
- [is-a-dev](https://github.com/is-a-dev/register) - Free .is-a.dev subdomains
- [js.org](https://github.com/js-org/js.org) - Free .js.org subdomains
- [thedev.id](https://github.com/fransallen/thedev.id) - Free .thedev.id subdomains

---

<div align="center">

**⭐ Star this repo if you found it useful!**

**💝 [Sponsor this project](https://github.com/sponsors/anshulyadaw) to keep it running!**

**🔄 [Fork it](https://github.com/anshulyadaw/r-u-live-open-domain/fork) to contribute!**

</div>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Maintainer

**Anshul Yadav**  
- GitHub: [@anshulyadaw](https://github.com/anshulyadaw)
- Domain: [r-u.live](https://r-u.live)

---

⭐ **Star this repo** if you found it useful!

💝 **Support**: If this service helped you, consider [sponsoring the project](https://github.com/sponsors/anshulyadaw) to keep it running!

## 🏗️ For Administrators

### Quick Setup Commands
```bash
# Clone and navigate to the project
git clone https://github.com/anshulyadaw/r-u-live-open-domain.git
cd r-u-live-open-domain

# Install Python dependencies
pip3 install -r requirements.txt

# Set up environment variables
export CLOUDFLARE_API_TOKEN="your_token_here"
export CLOUDFLARE_ZONE_ID="your_zone_id_here"

# Test the DNS manager
python3 scripts/dns-manager.py validate
```

### GitHub Secrets Required
Set these in your repository settings:
- `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token
- `CLOUDFLARE_ZONE_ID`: Zone ID for r-u.live domain

### Management Operations
```bash
# Validate all subdomain files
python3 scripts/dns-manager.py validate

# Deploy all DNS records to Cloudflare
python3 scripts/dns-manager.py deploy

# List current DNS records
python3 scripts/dns-manager.py list

# Update specific subdomain
python3 scripts/dns-manager.py update example.yaml
```

📖 **[Complete Setup Guide](docs/SETUP.md)** for detailed administrator instructions

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Report Issues
- Found a bug? [Create an issue](https://github.com/anshulyadaw/r-u-live-open-domain/issues/new)
- Include detailed steps to reproduce
- Add relevant screenshots or logs

### 💡 Suggest Features
- Have an idea? [Start a discussion](https://github.com/anshulyadaw/r-u-live-open-domain/discussions)
- Explain the use case and benefits
- Consider implementation complexity

### 🔧 Code Contributions
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### 📖 Documentation
- Improve README or documentation
- Add examples and tutorials
- Translate to other languages

**📋 See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines**

## 📞 Support

### 🆘 Getting Help
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Community questions and ideas
- **Email**: `anshul@r-u.live` (security issues only)

### 🔍 Troubleshooting

**"My subdomain isn't working"**
- Wait 5-60 minutes for DNS propagation
- Check your DNS settings with `dig yourname.r-u.live`
- Verify your target IP/domain is accessible

**"My request was rejected"**
- Review the feedback comments
- Check our [Community Guidelines](COMMUNITY_GUIDELINES.md)
- Make necessary changes and update your PR

**"Can I get multiple subdomains?"**
- Generally one per person/project
- Explain your use case in the request
- Must be for different legitimate projects

### 📊 Service Status
- **Uptime**: 99.9% (powered by Cloudflare)
- **Current Issues**: Check [GitHub Issues](https://github.com/anshulyadaw/r-u-live-open-domain/issues)
- **Maintenance**: Announced in [Discussions](https://github.com/anshulyadaw/r-u-live-open-domain/discussions)
