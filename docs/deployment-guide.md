# Deployment Guide

This guide explains how to deploy your subdomain to our hosting infrastructure.

## Prerequisites

- Your subdomain must be approved and registered in the system
- You need developer access to the repository
- Familiarity with Git and GitHub workflows

## Deployment Steps

1. **Prepare your files**
   - Ensure all content is in your subdomain's `/public` directory
   - Test locally using `npm run dev:subdomain your-subdomain`

2. **Configure deployment settings**
   - Update your subdomain's `config.json` with deployment preferences
   - Set appropriate environment variables in `.env.subdomain` file

3. **Deploy to staging**
   - Run `npm run deploy:staging your-subdomain`
   - Test at `your-subdomain-staging.example.com`

4. **Production deployment**
   - Submit a pull request to the main branch
   - Once approved, CI/CD will deploy to production
   - Verify at `your-subdomain.example.com`

## Monitoring and Logs

- View deployment logs in GitHub Actions
- Runtime logs are available in the admin dashboard
- Set up alerts in your subdomain's `monitoring.json` file

## Troubleshooting

Common issues and solutions:

- **404 errors**: Check that your index.html exists and paths are correct
- **Build failures**: Review build logs in GitHub Actions
- **SSL issues**: Ensure HTTPS is enabled in your config.json
