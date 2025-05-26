# Subdomain Template

This is a starter template for creating a new subdomain.

## Setup Instructions

1. Copy this directory to `/subdomains/your-subdomain-name`
2. Update the `config.json` file with your specific settings
3. Deploy your website contents to the `/public` directory
4. Add DNS entry in `/config/dns-config.json`
5. Register your subdomain in `/config/registry.json`

## Configuration

Edit the `config.json` file to match your needs:

```json
{
  "name": "your-subdomain",
  "owner": "your-username",
  "technology": "html/js/css",
  "description": "Description of your subdomain"
}
```

## Support

If you need assistance, refer to the documentation at `/docs/subdomain-management.md` or open an issue on GitHub.
