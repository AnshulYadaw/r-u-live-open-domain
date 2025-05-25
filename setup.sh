#!/bin/bash

# 🌐 r-u.live Setup Script
# Automated setup for r-u.live open domain service
# Usage: ./setup.sh

set -e

echo "🌐 r-u.live Open Domain Setup"
echo "==============================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️ $1${NC}"
}

# Check prerequisites
check_prerequisites() {
    print_info "Checking prerequisites..."
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
    print_success "Git is installed"
    
    # Check if Python 3 is installed
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.8+ first."
        exit 1
    fi
    print_success "Python 3 is installed"
    
    # Check Python version
    python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    required_version="3.8"
    if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
        print_success "Python version $python_version is compatible"
    else
        print_error "Python version $python_version is too old. Requires Python 3.8+"
        exit 1
    fi
    
    # Check if pip is installed
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 is not installed. Please install pip3 first."
        exit 1
    fi
    print_success "pip3 is installed"
}

# Install Python dependencies
install_dependencies() {
    print_info "Installing Python dependencies..."
    
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
        print_success "Dependencies installed from requirements.txt"
    else
        print_warning "requirements.txt not found, installing basic dependencies..."
        pip3 install PyYAML requests jsonschema
        print_success "Basic dependencies installed"
    fi
}

# Setup environment variables
setup_environment() {
    print_info "Setting up environment variables..."
    
    if [ ! -f ".env" ]; then
        cat > .env << EOF
# Cloudflare Configuration
CLOUDFLARE_API_TOKEN=your_token_here
CLOUDFLARE_ZONE_ID=your_zone_id_here

# Optional: Email notifications
ADMIN_EMAIL=admin@r-u.live

# Optional: GitHub token for enhanced API access
GITHUB_TOKEN=your_github_token_here
EOF
        print_success "Created .env template file"
        print_warning "Please edit .env file with your actual Cloudflare credentials"
    else
        print_warning ".env file already exists"
    fi
}

# Validate DNS manager script
validate_dns_manager() {
    print_info "Validating DNS manager script..."
    
    if [ -f "scripts/dns-manager.py" ]; then
        python3 scripts/dns-manager.py --help > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            print_success "DNS manager script is working"
        else
            print_warning "DNS manager script has issues (may need API credentials)"
        fi
    else
        print_error "DNS manager script not found"
        exit 1
    fi
}

# Setup GitHub repository (if not already done)
setup_github() {
    print_info "Checking GitHub repository setup..."
    
    if git remote -v | grep -q "origin"; then
        print_success "Git remote origin is configured"
    else
        print_warning "No git remote origin found"
        print_info "To connect to GitHub:"
        echo "  git remote add origin https://github.com/yourusername/r-u-live-open-domain.git"
    fi
    
    # Check if we're in a git repository
    if git rev-parse --git-dir > /dev/null 2>&1; then
        print_success "Inside a Git repository"
    else
        print_warning "Not inside a Git repository"
        print_info "Initialize with: git init"
    fi
}

# Create necessary directories
create_directories() {
    print_info "Creating necessary directories..."
    
    mkdir -p subdomains
    mkdir -p docs
    mkdir -p scripts
    mkdir -p .github/workflows
    mkdir -p .github/ISSUE_TEMPLATE
    mkdir -p reports
    
    print_success "Directories created"
}

# Test basic functionality
test_functionality() {
    print_info "Testing basic functionality..."
    
    # Test YAML parsing
    if [ -f "subdomains/example.yaml" ]; then
        python3 -c "import yaml; yaml.safe_load(open('subdomains/example.yaml'))" 2>/dev/null
        if [ $? -eq 0 ]; then
            print_success "YAML parsing works"
        else
            print_error "YAML parsing failed"
        fi
    else
        print_warning "No example.yaml found to test"
    fi
    
    # Test API imports
    python3 -c "import requests, yaml, jsonschema" 2>/dev/null
    if [ $? -eq 0 ]; then
        print_success "Required Python modules are available"
    else
        print_error "Some Python modules are missing"
    fi
}

# Generate setup report
generate_report() {
    print_info "Generating setup report..."
    
    cat > setup-report.txt << EOF
r-u.live Setup Report
Generated: $(date)

System Information:
- OS: $(uname -s)
- Python Version: $(python3 --version)
- Git Version: $(git --version)

Project Status:
- Dependencies: $(pip3 list | grep -E "PyYAML|requests|jsonschema" | wc -l)/3 installed
- Configuration: $([[ -f ".env" ]] && echo "Present" || echo "Missing")
- Scripts: $([[ -f "scripts/dns-manager.py" ]] && echo "Present" || echo "Missing")

Next Steps:
1. Edit .env file with your Cloudflare credentials
2. Set up GitHub repository secrets:
   - CLOUDFLARE_API_TOKEN
   - CLOUDFLARE_ZONE_ID
3. Test DNS manager: python3 scripts/dns-manager.py validate
4. Create your first subdomain request

For help: https://github.com/anshulyadaw/r-u-live-open-domain
EOF
    
    print_success "Setup report saved to setup-report.txt"
}

# Main setup process
main() {
    echo "Starting setup process..."
    echo ""
    
    check_prerequisites
    echo ""
    
    create_directories
    echo ""
    
    install_dependencies
    echo ""
    
    setup_environment
    echo ""
    
    validate_dns_manager
    echo ""
    
    setup_github
    echo ""
    
    test_functionality
    echo ""
    
    generate_report
    echo ""
    
    print_success "Setup completed successfully!"
    echo ""
    print_info "Next steps:"
    echo "1. Edit .env file with your credentials"
    echo "2. Run: python3 scripts/dns-manager.py validate"
    echo "3. Check setup-report.txt for details"
    echo ""
    print_info "For help, visit: https://github.com/anshulyadaw/r-u-live-open-domain"
}

# Run main function
main
