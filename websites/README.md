# Website Directory

This directory contains the source code for all websites hosted on various subdomains.

## Structure

Each subdomain has its own directory with the following structure:

```
/[subdomain-name]/
  ├── public/           # Static assets and built files
  ├── src/              # Source code
  ├── config.json       # Subdomain-specific configuration
  ├── README.md         # Documentation for this subdomain website
  └── package.json      # Dependencies and scripts
```

## Getting Started

To add a new website:

1. Create a new directory with your subdomain name
2. Copy the appropriate template from `/templates/websites/`
3. Update configuration files
4. Deploy using the deployment guide

## Available Templates

- Basic HTML/CSS/JS
- React
- Vue
- Next.js
- Static site generator
