# 🌟 Community Guidelines for r-u.live

Welcome to the **r-u.live** open domain community! This project provides free subdomains to help developers, students, and hobbyists showcase their work. To keep this service sustainable and safe for everyone, please follow these guidelines.

## 📋 Subdomain Request Guidelines

### ✅ Allowed Use Cases
- **Personal portfolios** and resume websites
- **Open source projects** and documentation
- **Educational projects** and student work
- **Development demos** and prototypes
- **Non-commercial blogs** and personal sites
- **GitHub Pages** hosting
- **Testing environments** for legitimate projects

### ❌ Prohibited Use Cases
- **Commercial services** or business websites
- **Malicious content** (malware, phishing, spam)
- **Adult content** or inappropriate material
- **Illegal activities** or copyright infringement
- **Resource-intensive applications** that may affect service
- **Temporary/throw-away** projects (use for serious projects only)
- **Multiple subdomains** for the same project/person without justification

## 🛡️ Security & Safety Requirements

### DNS Record Security
- **No private IP addresses** (192.168.x.x, 10.x.x.x, 172.16-31.x.x)
- **No localhost/loopback** addresses (127.x.x.x)
- **Valid public IP addresses** only for A records
- **Legitimate domains** only for CNAME records
- **No URL shorteners** or redirect services

### Content Requirements
- Must comply with **GitHub Terms of Service**
- Must comply with **Cloudflare Terms of Service**
- No content that violates **applicable laws**
- No impersonation of organizations or individuals
- No misleading or deceptive content

## 📝 Request Format Standards

### Required Information
```yaml
subdomain: your-project-name
owner:
  name: Your Full Name
  email: your.email@example.com
record:
  A: "1.2.3.4"  # OR
  CNAME: "yourdomain.com"
description: Brief description of your project (optional but recommended)
```

### Naming Conventions
- **Alphanumeric characters** and hyphens only
- **3-63 characters** in length
- **No consecutive hyphens** (--) 
- **Cannot start or end** with a hyphen
- **Must be unique** across all existing subdomains
- **Descriptive names** preferred (avoid random strings)

## 🤝 Community Standards

### Be Respectful
- Use **professional language** in issues and PRs
- Be **patient** with review times (this is a volunteer service)
- **Help others** by reviewing their requests constructively
- **Follow up** on your requests if changes are needed

### Quality Over Quantity
- **One subdomain per person/project** (unless you have a valid reason for more)
- **Maintain your subdomain** - keep content updated
- **Notify us** if you no longer need your subdomain
- **Use meaningful descriptions** to help reviewers understand your project

## 🔄 Request Process

### 1. Before Requesting
- [ ] Check existing subdomains to avoid conflicts
- [ ] Ensure your project meets our guidelines
- [ ] Prepare your target IP/domain
- [ ] Have a valid email for contact

### 2. Submission Methods
- **GitHub Issue** (recommended for beginners)
- **Direct Pull Request** (for experienced developers)
- **Following our templates** ensures faster processing

### 3. Review Process
- **Automated validation** checks format and security
- **Manual review** by maintainers for content and compliance
- **Feedback provided** if changes are needed
- **Approval and deployment** via Cloudflare automation

## ⚡ Response Times & Expectations

### Typical Processing Times
- **Automated validation**: Immediate
- **Initial review**: 1-3 business days
- **Feedback response**: 1-2 business days
- **Final approval**: 1-2 business days after requirements met
- **DNS deployment**: Immediate after merge

### What Affects Processing Time
- **Request volume** during busy periods
- **Completeness** of your submission
- **Complexity** of your use case
- **Holiday periods** and maintainer availability

## 🚫 Violations & Enforcement

### Warning System
1. **First violation**: Warning and opportunity to correct
2. **Second violation**: Temporary subdomain suspension
3. **Severe violations**: Immediate removal and potential ban

### Reporting Issues
- Report violations via **GitHub Issues** with `violation-report` label
- Include **evidence** and **specific subdomain** in question
- **False reports** will be investigated and may result in restrictions

### Appeals Process
- Submit appeals via **GitHub Issues** with detailed explanation
- Include **corrective actions** taken
- Final decisions made by project maintainers

## 🏆 Recognition & Contributions

### Ways to Contribute
- **Review subdomain requests** from other users
- **Improve documentation** and guidelines
- **Report bugs** in automation systems
- **Suggest enhancements** to the service
- **Help with support** in issues and discussions

### Recognition Program
- Active contributors may receive **special mentions**
- **Priority review** for future subdomain requests
- **Collaborator status** for trusted long-term contributors

## 📞 Support & Contact

### Getting Help
- **GitHub Issues**: Technical problems and general questions
- **GitHub Discussions**: Community chat and ideas
- **Email**: Critical security issues only

### Common Questions
- **"My subdomain isn't working"**: Check DNS propagation (24-48 hours)
- **"Can I change my target IP?"**: Submit a new PR with updated YAML
- **"Can I get a second subdomain?"**: Explain your use case in the request
- **"My request was rejected"**: Check the feedback and guidelines

## 📜 Legal & Disclaimer

### Service Terms
- This is a **free service** provided as-is
- **No guaranteed uptime** or SLA
- **Service may be discontinued** with reasonable notice
- **We reserve the right** to remove any subdomain for any reason

### Data Privacy
- Your **email and name** are stored for contact purposes
- **No personal data** is shared with third parties
- **Public GitHub activity** is visible as part of the open source process

### Liability
- **You are responsible** for your subdomain content
- **We are not liable** for any damages from service use
- **Follow all applicable laws** in your jurisdiction

---

## 🎯 TL;DR - Quick Checklist

Before submitting your subdomain request:

- [ ] ✅ My project is legitimate and follows the guidelines
- [ ] 🛡️ My DNS target is secure and publicly accessible
- [ ] 📝 I've filled out all required information accurately
- [ ] 🔍 I've checked for naming conflicts with existing subdomains
- [ ] 📚 I understand this is a volunteer-run service
- [ ] 🤝 I'll be respectful and patient during the review process

**Ready to get your free subdomain? [Create a request!](https://github.com/anshulyadaw/r-u-live-open-domain/issues/new?template=subdomain-request.md)**

---

*These guidelines are subject to change. Check back regularly for updates. Last updated: December 2024*
