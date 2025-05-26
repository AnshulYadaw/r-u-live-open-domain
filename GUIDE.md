# Step-by-Step Guide to Register Your r-u.live Subdomain

This guide will walk you through the process of registering a subdomain on r-u.live.

## Prerequisites

- A GitHub account
- Basic knowledge of Git and GitHub
- A destination for your subdomain (either an IP address, another domain, or GitHub Pages)

## Step 1: Fork the Repository

1. Visit our [GitHub repository](https://github.com/yourusername/r-u-live)
2. Click the "Fork" button in the upper right corner
3. Wait for the repository to be forked to your account

## Step 2: Clone Your Fork

Open your terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/r-u-live.git
cd r-u-live
```

## Step 3: Create Your Domain Configuration File

1. Create a new JSON file in the `/domains` directory
2. Name your file according to your desired subdomain (e.g., `mysite.json` for `mysite.r-u.live`)
3. Use this template for your file content:

```json
{
  "description": "Brief description of your site or project",
  "domain": "r-u.live",
  "subdomain": "mysite",
  
  "owner": {
    "repo": "https://github.com/your-username/your-repo",
    "email": "your.email@example.com"
  },
  
  "record": {
    "A": ["192.0.2.1"],
    "CNAME": "example.com"
  },
  
  "proxied": true
}
```

4. Customize the file with your information:
   - Replace `"mysite"` with your desired subdomain name
   - Update the owner section with your GitHub repository and email
   - Set up the appropriate DNS records (choose one):

### For GitHub Pages:
```json
"record": {
  "CNAME": "username.github.io"
},
```

### For a Custom Domain:
```json
"record": {
  "CNAME": "your-domain.com"
},
```

### For a Server IP:
```json
"record": {
  "A": ["203.0.113.1"]
},
```

### For IPv6 Address:
```json
"record": {
  "AAAA": ["2001:db8::1"]
},
```

## Step 4: Commit and Push Your Changes

```bash
git add domains/mysite.json
git commit -m "Add mysite.r-u.live subdomain"
git push origin main
```

## Step 5: Create a Pull Request

1. Go to your forked repository on GitHub
2. Click "Pull request" (or "New pull request")
3. Ensure the base repository is set to the original repository
4. Click "Create pull request"
5. Add a description explaining your request
6. Submit the pull request

## Step 6: Wait for Approval

Your pull request will be reviewed. If approved, it will be merged into the main repository.

## Step 7: DNS Propagation

After your pull request is merged, DNS changes will begin propagating. This usually takes 5-15 minutes but can take up to 24 hours.

## Updating Your Subdomain

To update your subdomain's DNS records later:

1. Fork the repository again (if you don't still have your fork)
2. Update your JSON file with the new information
3. Create a new pull request

## Common Issues and Solutions

### My pull request was rejected
- Check that your JSON file is properly formatted
- Ensure there are no duplicate subdomain names
- Make sure you provided a clear description

### My subdomain isn't working after approval
- DNS changes can take up to 24 hours to propagate
- Check that your destination (IP, CNAME, etc.) is correctly set up
- Verify that your JSON file was correctly merged

## Need Help?

If you encounter any issues or have questions, please [open an issue](https://github.com/yourusername/r-u-live/issues) in our GitHub repository.
