#!/bin/bash

# 🚀 GitHub Repository Setup for r-u.live
# This script helps initialize the GitHub repository and configure settings

set -e

echo "🚀 GitHub Repository Setup for r-u.live"
echo "======================================="
echo ""

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️ $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️ $1${NC}"; }

# Get repository information
get_repo_info() {
    print_info "Repository Setup Information"
    echo ""
    echo "Repository Name: r-u-live-open-domain"
    echo "Description: Free subdomains under r-u.live with automated DNS management"
    echo "Website: https://r-u.live"
    echo "Topics: dns, subdomains, cloudflare, github-actions, open-source"
    echo ""
}

# Initialize git repository
init_git() {
    print_info "Initializing Git repository..."
    
    if [ ! -d ".git" ]; then
        git init
        print_success "Git repository initialized"
    else
        print_warning "Git repository already exists"
    fi
    
    # Set up gitignore if not exists
    if [ ! -f ".gitignore" ]; then
        print_warning ".gitignore not found"
    else
        print_success ".gitignore is present"
    fi
}

# Commit initial files
commit_files() {
    print_info "Committing initial files..."
    
    git add .
    
    if git diff --staged --quiet; then
        print_warning "No changes to commit"
    else
        git commit -m "🎉 Initial commit: r-u.live open domain service

✨ Features:
- Automated subdomain registration via GitHub
- Cloudflare DNS integration
- GitHub Actions workflows for validation and deployment
- Community-driven subdomain management
- Comprehensive documentation and examples

🚀 Ready for production use!"
        print_success "Initial commit created"
    fi
}

# Setup GitHub repository
setup_github_repo() {
    print_info "GitHub Repository Setup Instructions"
    echo ""
    echo "1. Create a new repository on GitHub:"
    echo "   - Name: r-u-live-open-domain"
    echo "   - Description: Free subdomains under r-u.live with automated DNS management"
    echo "   - Public repository"
    echo "   - Initialize with README: No (we have our own)"
    echo ""
    echo "2. Add the repository URL as remote:"
    echo "   git remote add origin https://github.com/yourusername/r-u-live-open-domain.git"
    echo ""
    echo "3. Push the code:"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
}

# Configure repository settings
configure_repo_settings() {
    print_info "Repository Configuration Checklist"
    echo ""
    echo "After creating the GitHub repository, configure these settings:"
    echo ""
    echo "📋 General Settings:"
    echo "   ✅ Enable Issues"
    echo "   ✅ Enable Discussions"
    echo "   ✅ Enable Projects (optional)"
    echo "   ✅ Enable Wiki (optional)"
    echo ""
    echo "🔒 Security Settings:"
    echo "   ✅ Enable vulnerability alerts"
    echo "   ✅ Enable automated security updates"
    echo ""
    echo "🔑 Secrets (Settings → Secrets and variables → Actions):"
    echo "   ✅ CLOUDFLARE_API_TOKEN (required)"
    echo "   ✅ CLOUDFLARE_ZONE_ID (required)"
    echo ""
    echo "🏷️ Topics/Tags:"
    echo "   dns, subdomains, cloudflare, github-actions, open-source,"
    echo "   automation, free-service, community"
    echo ""
    echo "📄 Repository Description:"
    echo "   'Free subdomains under r-u.live with automated DNS management'"
    echo ""
    echo "🌐 Website URL:"
    echo "   https://r-u.live"
    echo ""
}

# Setup branch protection
setup_branch_protection() {
    print_info "Branch Protection Setup"
    echo ""
    echo "Recommended branch protection rules for 'main' branch:"
    echo ""
    echo "✅ Require pull request reviews before merging"
    echo "   - Required approving reviews: 1"
    echo "   - Dismiss stale reviews when new commits are pushed"
    echo ""
    echo "✅ Require status checks to pass before merging"
    echo "   - Require branches to be up to date before merging"
    echo "   - Status checks: validate (from validate-subdomain workflow)"
    echo ""
    echo "✅ Require conversation resolution before merging"
    echo ""
    echo "✅ Restrict pushes that create files"
    echo "   - Restrict to subdomains directory only"
    echo ""
}

# Generate README for next steps
generate_next_steps() {
    cat > NEXT_STEPS.md << 'EOF'
# 🚀 Next Steps for r-u.live Setup

## ✅ Completed
- [x] Project structure created
- [x] Documentation written
- [x] GitHub Actions workflows configured
- [x] Community guidelines established
- [x] Scripts and automation ready

## 🔄 Pending Actions

### 1. GitHub Repository Setup
- [ ] Create GitHub repository
- [ ] Push initial code
- [ ] Configure repository settings
- [ ] Set up branch protection rules

### 2. Cloudflare Configuration
- [ ] Obtain Cloudflare API token
- [ ] Get zone ID for r-u.live domain
- [ ] Add secrets to GitHub repository

### 3. Testing & Validation
- [ ] Test DNS manager script locally
- [ ] Create test subdomain request
- [ ] Verify GitHub Actions workflows
- [ ] Test end-to-end automation

### 4. Community Setup
- [ ] Enable GitHub Discussions
- [ ] Configure issue templates
- [ ] Set up project labels
- [ ] Create initial documentation wiki

### 5. Production Launch
- [ ] Announce service availability
- [ ] Create initial blog post/documentation
- [ ] Share on social media/communities
- [ ] Monitor for initial requests

## 📚 Important Links
- [Setup Documentation](docs/SETUP.md)
- [Community Guidelines](COMMUNITY_GUIDELINES.md)
- [Contributing Guide](CONTRIBUTING.md)
- [DNS Manager Script](scripts/dns-manager.py)

## 🆘 Need Help?
- Check the README.md for detailed instructions
- Review the setup.sh script output
- Contact: anshul@r-u.live
EOF
    
    print_success "Generated NEXT_STEPS.md with detailed action items"
}

# Main function
main() {
    get_repo_info
    echo ""
    
    init_git
    echo ""
    
    commit_files
    echo ""
    
    setup_github_repo
    echo ""
    
    configure_repo_settings
    echo ""
    
    setup_branch_protection
    echo ""
    
    generate_next_steps
    echo ""
    
    print_success "GitHub setup guide completed!"
    print_info "Check NEXT_STEPS.md for detailed action items"
}

# Run main function
main
