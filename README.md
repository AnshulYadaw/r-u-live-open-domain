# r-u-live-open-domain

Request a free subdomain under **r-u.live** — powered by GitHub and Cloudflare.

## How to Request a Subdomain

1. **Fork** this repo.
2. Add your subdomain file in `subdomains/yourname.yaml`.
3. Submit a **pull request**.
4. After approval, your subdomain will be live.

## Example Subdomain File

```yaml
subdomain: "yourname"
owner:
  name: "Your Name"
  email: "you@example.com"
record:
  A: "1.2.3.4"
```

Or use CNAME:

```yaml
record:
  CNAME: "yourname.github.io"
```

## Maintainer

Anshul Yadav
