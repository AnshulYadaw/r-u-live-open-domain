# Subdomain Management Guide

This document explains how to manage subdomains in our open domain system.

## Adding a New Subdomain

1. Choose a unique subdomain name that follows our naming conventions
2. Copy the template from `/templates/basic-subdomain` to `/subdomains/your-subdomain-name`
3. Edit the configuration files with your information
4. Submit a pull request for review

## Naming Conventions

- Use lowercase letters, numbers and hyphens only
- No special characters or spaces
- Avoid reserved names (check `/config/registry.json` for existing names)
- Names should be descriptive and related to the content

## DNS Configuration

DNS records are maintained in `/config/dns-config.json`. Each subdomain requires:

- Name (subdomain prefix)
- Record type (A, CNAME, MX, TXT, etc.)
- Value (IP address or domain)
- TTL (Time to Live in seconds)

## Deployment

After your subdomain is approved:

1. Place your website files in `/subdomains/your-subdomain-name/public/`
2. Configure any necessary build scripts in `/subdomains/your-subdomain-name/scripts/`
3. Follow the deployment guide at `/docs/deployment-guide.md`

## Management and Updates

To update your subdomain:

1. Make changes to your files in the subdomain directory
2. Test locally using the local development server
3. Submit changes via pull request
4. Once approved, changes will be deployed automatically
