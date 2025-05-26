# Subdomains Management

This directory contains all subdomains managed under the open domain system.

## Structure
- Each subdomain has its own directory
- Configuration files are stored in `/config` directory
- Templates for new subdomains are in `/templates`

## Available Subdomains

| Subdomain | Purpose | Status |
|-----------|---------|--------|
| www       | Main website | Active |
| mail      | Email services | Active |
| api       | API endpoints | Active |
| docs      | Documentation | Active |
| blog      | Blog content | Active |

## Adding a New Subdomain

1. Copy the template from `/templates/basic-subdomain`
2. Create a new directory with the subdomain name
3. Update the DNS configuration in `/config/dns-config.json`
4. Deploy following the instructions in `/docs/deployment-guide.md`
