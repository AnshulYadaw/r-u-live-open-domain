#!/bin/bash

# r-u.live DNS Management Script
# This script helps with common DNS management tasks

# Colors for terminal output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Display script header
echo -e "${BLUE}===============================${NC}"
echo -e "${BLUE}  r-u.live DNS Management Tool ${NC}"
echo -e "${BLUE}===============================${NC}"
echo ""

# Function to validate a domain file
validate_domain_file() {
    local file=$1
    echo -e "${YELLOW}Validating ${file}...${NC}"
    
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo -e "${RED}Error: File does not exist${NC}"
        return 1
    fi
    
    # Check if file is valid JSON
    if ! jq . "$file" > /dev/null 2>&1; then
        echo -e "${RED}Error: Invalid JSON format${NC}"
        return 1
    fi
    
    # Check required fields
    if ! jq -e '.domain' "$file" > /dev/null 2>&1 || \
       ! jq -e '.subdomain' "$file" > /dev/null 2>&1 || \
       ! jq -e '.record' "$file" > /dev/null 2>&1 || \
       ! jq -e '.owner' "$file" > /dev/null 2>&1; then
        echo -e "${RED}Error: Missing required fields${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✓ File is valid${NC}"
    return 0
}

# Function to create a new domain file from template
create_domain_file() {
    echo -e "${YELLOW}Creating new domain file...${NC}"
    
    # Ask for subdomain name
    read -p "Enter subdomain name (e.g., 'mysite' for mysite.r-u.live): " subdomain
    
    # Validate subdomain format
    if [[ ! $subdomain =~ ^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$ ]]; then
        echo -e "${RED}Error: Invalid subdomain format. Use only lowercase letters, numbers, and hyphens.${NC}"
        return 1
    fi
    
    # Check if subdomain already exists
    if [ -f "domains/${subdomain}.json" ]; then
        echo -e "${RED}Error: Subdomain already exists${NC}"
        return 1
    fi
    
    # Ask for description
    read -p "Enter a brief description: " description
    
    # Ask for owner details
    read -p "Enter your GitHub repo URL: " repo
    read -p "Enter your email address: " email
    
    # Ask for record type
    echo "Select record type:"
    echo "1) A record (IP address)"
    echo "2) CNAME record (another domain)"
    read -p "Enter your choice (1 or 2): " record_choice
    
    if [ "$record_choice" == "1" ]; then
        read -p "Enter IP address: " ip_address
        record_section="\"A\": [\"${ip_address}\"]"
    elif [ "$record_choice" == "2" ]; then
        read -p "Enter domain (without http/https): " cname_domain
        record_section="\"CNAME\": \"${cname_domain}\""
    else
        echo -e "${RED}Error: Invalid choice${NC}"
        return 1
    fi
    
    # Ask for Cloudflare proxy
    read -p "Enable Cloudflare proxy? (y/n): " proxy_choice
    if [ "$proxy_choice" == "y" ] || [ "$proxy_choice" == "Y" ]; then
        proxied="true"
    else
        proxied="false"
    fi
    
    # Create the file
    cat > "domains/${subdomain}.json" << EOF
{
  "description": "${description}",
  "domain": "r-u.live",
  "subdomain": "${subdomain}",
  
  "owner": {
    "repo": "${repo}",
    "email": "${email}"
  },
  
  "record": {
    ${record_section}
  },
  
  "proxied": ${proxied}
}
EOF
    
    echo -e "${GREEN}✓ Created domains/${subdomain}.json${NC}"
    
    # Validate the created file
    validate_domain_file "domains/${subdomain}.json"
}

# Function to list all registered domains
list_domains() {
    echo -e "${YELLOW}Listing all registered domains...${NC}"
    node registry.js list
}

# Main menu
show_menu() {
    echo ""
    echo "What would you like to do?"
    echo "1) Create a new subdomain"
    echo "2) Validate domain files"
    echo "3) List all domains"
    echo "4) Generate report"
    echo "5) Exit"
    read -p "Enter your choice: " choice
    
    case $choice in
        1)
            create_domain_file
            ;;
        2)
            echo -e "${YELLOW}Validating all domain files...${NC}"
            npm run validate
            ;;
        3)
            list_domains
            ;;
        4)
            echo -e "${YELLOW}Generating report...${NC}"
            node registry.js report
            ;;
        5)
            echo -e "${GREEN}Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid choice${NC}"
            ;;
    esac
    
    show_menu
}

# Check if we're in the right directory
if [ ! -d "domains" ] || [ ! -f "dnsconfig.js" ]; then
    echo -e "${RED}Error: Please run this script from the project root directory${NC}"
    exit 1
fi

# Start the menu
show_menu
