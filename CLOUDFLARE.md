# Cloudflare Setup Guide for r-u.live

This guide explains how to set up Cloudflare for the r-u.live domain registry. This is primarily for administrators of the r-u.live service.

## Prerequisites

1. A Cloudflare account
2. The domain r-u.live added to your Cloudflare account
3. API token with DNS edit permissions

## Step 1: Add Your Domain to Cloudflare

1. Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/)
2. Click "Add a Site" and enter your domain name (r-u.live)
3. Select a plan (Free is sufficient for most uses)
4. Follow the instructions to update your domain's nameservers

## Step 2: Create an API Token

1. Go to "My Profile" in your Cloudflare dashboard
2. Select the "API Tokens" tab
3. Click "Create Token"
4. Use the "Edit zone DNS" template
5. Under "Zone Resources", select "Include" > "Specific zone" > "r-u.live"
6. Create the token and save it securely

## Step 3: Add the API Token to GitHub

1. Go to your GitHub repository
2. Navigate to Settings > Secrets > Actions
3. Click "New repository secret"
4. Name: `CLOUDFLARE_API_TOKEN`
5. Value: Paste the API token from Step 2
6. Click "Add secret"

## Step 4: Configure DNSControl

The `dnsconfig.js` file already contains the necessary configuration. Make sure it includes:

```javascript
var providerCf = DnsProvider(NewDnsProvider("cloudflare"));
```

## Step 5: Test the Configuration

Run a test deployment using GitHub Actions:

1. Go to the Actions tab in your repository
2. Select the "Deploy DNS" workflow
3. Click "Run workflow" and select the main branch
4. Verify that the workflow completes successfully

## Cloudflare Settings Recommendations

For optimal security and performance, we recommend the following settings:

### SSL/TLS Settings

- SSL/TLS Mode: Full (Strict)
- Always Use HTTPS: On
- Minimum TLS Version: 1.2
- TLS 1.3: On

### Security Settings

- Security Level: Medium
- Bot Fight Mode: On
- Browser Integrity Check: On
- Challenge Passage: 30 Minutes
- Privacy Pass Support: On

### Performance Settings

- Auto Minify: HTML, CSS, JavaScript
- Brotli: On
- Early Hints: On
- Rocket Loader: Off (can cause issues with some sites)
- HTTP/2: On
- HTTP/3: On

## Troubleshooting

### DNS Changes Not Propagating

1. Check the GitHub Actions logs for errors
2. Verify that the API token has the correct permissions
3. Make sure the domain is active in Cloudflare

### Error: "API Token Does Not Have Required Permissions"

1. Go back to your Cloudflare dashboard
2. Edit the API token to ensure it has "Edit" permissions for DNS
3. Verify that it's scoped to the correct zone (r-u.live)

## Maintenance

- Periodically rotate your API token for security
- Monitor GitHub Actions for deployment failures
- Regularly check Cloudflare analytics for any unusual traffic patterns
