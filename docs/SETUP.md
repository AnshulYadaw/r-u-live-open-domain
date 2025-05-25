# 🛠️ Cloudflare DNS Automation Setup Guide

This guide will help you set up automated DNS management for your r-u.live subdomain service using Cloudflare.

## 📋 Prerequisites

1. **Cloudflare Account** with r-u.live domain
2. **GitHub Repository** with appropriate permissions
3. **Python 3.8+** (for local testing)

## 🔑 Step 1: Get Cloudflare Credentials

### Get API Token

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/profile/api-tokens)
2. Click "Create Token"
3. Use "Custom token" template
4. Configure permissions:
   - **Zone** - `Zone:Read`, `DNS:Edit`
   - **Zone Resources** - `Include: Specific zone: r-u.live`
5. Copy the generated token ⚠️ **Save it securely!**

### Get Zone ID

1. Go to your domain overview in Cloudflare
2. In the right sidebar, copy the **Zone ID**

## 🔐 Step 2: Configure GitHub Secrets

1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Add these repository secrets:

```
CLOUDFLARE_API_TOKEN = your_api_token_here
CLOUDFLARE_ZONE_ID = your_zone_id_here
```

## 🚀 Step 3: Test the Automation

### Method 1: GitHub Actions (Automatic)

1. Create a test subdomain file:
   ```bash
   # Create test file
   cat > subdomains/test.yaml << EOF
   subdomain: "test"
   owner:
     name: "Test User"
     email: "test@example.com"
   record:
     A: "1.2.3.4"
   EOF
   ```

2. Create a Pull Request
3. The validation workflow will run automatically
4. After merging, the DNS deployment workflow will execute

### Method 2: Manual Deployment (Local Testing)

```bash
# Install dependencies
pip install pyyaml requests jsonschema

# Set environment variables
export CLOUDFLARE_API_TOKEN="your_token_here"
export CLOUDFLARE_ZONE_ID="your_zone_id_here"

# Test validation
python scripts/dns-manager.py validate

# Test deployment
python scripts/dns-manager.py deploy

# List current records
python scripts/dns-manager.py list
```

## 📊 Step 4: Monitor & Verify

### Check DNS Records

```bash
# Test DNS resolution
nslookup test.r-u.live

# Check with dig
dig test.r-u.live

# Verify in Cloudflare Dashboard
```

### GitHub Actions Logs

1. Go to **Actions** tab in your repository
2. Check workflow runs for any errors
3. Review deployment summaries

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `401 Unauthorized` | Check API token permissions |
| `403 Forbidden` | Verify Zone ID is correct |
| `Invalid IP address` | Validate IP format in YAML |
| `YAML parsing error` | Check indentation and syntax |

### Debug Commands

```bash
# Validate specific file
python -c "
import yaml
with open('subdomains/yourfile.yaml') as f:
    data = yaml.safe_load(f)
    print(data)
"

# Test Cloudflare API
curl -X GET "https://api.cloudflare.com/client/v4/zones/YOUR_ZONE_ID/dns_records" \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json"
```

## ⚡ Advanced Configuration

### Custom Workflow Triggers

Edit `.github/workflows/cloudflare-dns.yml` to add:

```yaml
on:
  # Manual trigger
  workflow_dispatch:
    inputs:
      force_update:
        description: 'Force update all records'
        required: false
        default: false
        type: boolean
  
  # Schedule (daily at 2 AM UTC)
  schedule:
    - cron: '0 2 * * *'
```

### Bulk Operations

```bash
# Deploy all subdomains
python scripts/dns-manager.py deploy

# Validate all files
python scripts/dns-manager.py validate

# List all DNS records
python scripts/dns-manager.py list
```

## 📈 Performance & Limits

### Cloudflare Limits

- **API Rate Limit**: 1,200 requests per 5 minutes
- **DNS Records**: 1,000 per zone (free plan)
- **TTL Minimum**: 120 seconds (free plan)

### Optimization Tips

1. Use reasonable TTL values (3600 seconds default)
2. Batch operations when possible
3. Monitor API usage in Cloudflare dashboard

## 🔒 Security Best Practices

### API Token Security

- ✅ Use minimal required permissions
- ✅ Set token expiration dates
- ✅ Regularly rotate tokens
- ✅ Monitor token usage

### Repository Security

- ✅ Use repository secrets (never commit tokens)
- ✅ Enable branch protection rules
- ✅ Require PR reviews for main branch
- ✅ Enable security alerts

## 📞 Support

### Getting Help

1. **Check logs** in GitHub Actions
2. **Validate YAML** syntax online
3. **Test locally** with debug commands
4. **Create an issue** with error details

### Useful Resources

- [Cloudflare API Documentation](https://developers.cloudflare.com/api/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)

---

🎉 **Your automated DNS system is now ready!**

Users can now request subdomains via Pull Requests, and the system will automatically validate and deploy DNS records to Cloudflare.
