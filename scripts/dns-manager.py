#!/usr/bin/env python3
"""
🌐 r-u.live DNS Management Script
Manage DNS records for r-u.live subdomains via Cloudflare API
"""

import os
import sys
import yaml
import requests
import json
import argparse
from datetime import datetime
from pathlib import Path

class CloudflareManager:
    def __init__(self, api_token, zone_id):
        self.api_token = api_token
        self.zone_id = zone_id
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        self.base_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    def get_records(self, name=None):
        """Get DNS records"""
        params = {}
        if name:
            params["name"] = name
            
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json().get('result', [])
        else:
            print(f"❌ Error fetching records: {response.status_code}")
            return []

    def create_record(self, name, record_type, content, ttl=3600):
        """Create a new DNS record"""
        payload = {
            "type": record_type,
            "name": name,
            "content": content,
            "ttl": ttl,
            "proxied": False
        }
        
        response = requests.post(self.base_url, json=payload, headers=self.headers)
        return response

    def update_record(self, record_id, name, record_type, content, ttl=3600):
        """Update an existing DNS record"""
        payload = {
            "type": record_type,
            "name": name,
            "content": content,
            "ttl": ttl,
            "proxied": False
        }
        
        response = requests.put(f"{self.base_url}/{record_id}", json=payload, headers=self.headers)
        return response

    def delete_record(self, record_id):
        """Delete a DNS record"""
        response = requests.delete(f"{self.base_url}/{record_id}", headers=self.headers)
        return response

def load_subdomain_files():
    """Load all subdomain YAML files"""
    subdomains_dir = Path("subdomains")
    if not subdomains_dir.exists():
        print("❌ subdomains/ directory not found")
        return []
    
    subdomains = []
    for yaml_file in subdomains_dir.glob("*.yaml"):
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)
                data['_file'] = str(yaml_file)
                subdomains.append(data)
        except Exception as e:
            print(f"❌ Error loading {yaml_file}: {e}")
    
    return subdomains

def deploy_all(cf_manager):
    """Deploy all subdomain files to Cloudflare"""
    subdomains = load_subdomain_files()
    
    if not subdomains:
        print("❌ No subdomain files found")
        return
    
    print(f"🚀 Deploying {len(subdomains)} subdomains...")
    
    success_count = 0
    error_count = 0
    
    for data in subdomains:
        try:
            subdomain = data["subdomain"]
            record_type = list(data["record"].keys())[0]
            record_value = data["record"][record_type]
            full_name = f"{subdomain}.r-u.live"
            
            # Check if record exists
            existing_records = cf_manager.get_records(full_name)
            
            if existing_records:
                # Update existing record
                record_id = existing_records[0]['id']
                response = cf_manager.update_record(record_id, full_name, record_type, record_value)
                action = "UPDATED"
            else:
                # Create new record
                response = cf_manager.create_record(full_name, record_type, record_value)
                action = "CREATED"
            
            if response.status_code in [200, 201]:
                result = response.json()
                if result.get('success'):
                    print(f"✅ {action}: {full_name} → {record_value} ({record_type})")
                    success_count += 1
                else:
                    errors = result.get('errors', [])
                    print(f"❌ FAILED: {full_name} - {errors}")
                    error_count += 1
            else:
                print(f"❌ HTTP {response.status_code}: {full_name} - {response.text}")
                error_count += 1
                
        except Exception as e:
            print(f"❌ Error processing {data.get('_file', 'unknown')}: {e}")
            error_count += 1
    
    print(f"\n📊 DEPLOYMENT SUMMARY:")
    print(f"   ✅ Success: {success_count}")
    print(f"   ❌ Errors: {error_count}")
    print(f"   📁 Total: {len(subdomains)}")

def list_records(cf_manager):
    """List all r-u.live DNS records"""
    records = cf_manager.get_records()
    
    if not records:
        print("📭 No DNS records found")
        return
    
    print(f"📋 Found {len(records)} DNS records:\n")
    print(f"{'Name':<40} {'Type':<8} {'Content':<40} {'TTL':<8}")
    print("-" * 100)
    
    for record in records:
        name = record['name']
        record_type = record['type']
        content = record['content']
        ttl = record['ttl']
        
        print(f"{name:<40} {record_type:<8} {content:<40} {ttl:<8}")

def validate_files():
    """Validate all subdomain YAML files"""
    subdomains = load_subdomain_files()
    
    if not subdomains:
        print("❌ No subdomain files found")
        return False
    
    print(f"🔍 Validating {len(subdomains)} subdomain files...")
    
    errors = []
    success = []
    
    for data in subdomains:
        file_path = data.get('_file', 'unknown')
        
        try:
            # Check required fields
            required_fields = ['subdomain', 'owner', 'record']
            for field in required_fields:
                if field not in data:
                    errors.append(f"❌ {file_path}: Missing field '{field}'")
                    continue
            
            subdomain = data["subdomain"]
            
            # Validate subdomain format
            if not subdomain.replace('-', '').replace('_', '').isalnum():
                errors.append(f"❌ {file_path}: Invalid subdomain format '{subdomain}'")
            
            if len(subdomain) < 3 or len(subdomain) > 63:
                errors.append(f"❌ {file_path}: Subdomain length must be 3-63 characters")
            
            # Check record
            if 'record' in data:
                record = data['record']
                if not record or len(record) != 1:
                    errors.append(f"❌ {file_path}: Must have exactly one record type")
                else:
                    record_type = list(record.keys())[0]
                    if record_type not in ['A', 'CNAME']:
                        errors.append(f"❌ {file_path}: Unsupported record type '{record_type}'")
            
            if not errors:
                record_type = list(data["record"].keys())[0]
                record_value = data["record"][record_type]
                success.append(f"✅ {file_path}: {subdomain}.r-u.live → {record_value} ({record_type})")
                
        except Exception as e:
            errors.append(f"❌ {file_path}: Validation error - {e}")
    
    # Print results
    if success:
        print("\n✅ VALID FILES:")
        for msg in success:
            print(f"   {msg}")
    
    if errors:
        print("\n❌ VALIDATION ERRORS:")
        for error in errors:
            print(f"   {error}")
        return False
    else:
        print(f"\n🎉 All {len(subdomains)} files are valid!")
        return True

def main():
    parser = argparse.ArgumentParser(description="🌐 r-u.live DNS Management")
    parser.add_argument('action', choices=['deploy', 'list', 'validate'], 
                       help='Action to perform')
    parser.add_argument('--api-token', 
                       default=os.getenv('CLOUDFLARE_API_TOKEN'),
                       help='Cloudflare API token')
    parser.add_argument('--zone-id', 
                       default=os.getenv('CLOUDFLARE_ZONE_ID'),
                       help='Cloudflare Zone ID')
    
    args = parser.parse_args()
    
    if args.action == 'validate':
        success = validate_files()
        sys.exit(0 if success else 1)
    
    if not args.api_token or not args.zone_id:
        print("❌ Missing Cloudflare credentials!")
        print("Set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ZONE_ID environment variables")
        print("or use --api-token and --zone-id arguments")
        sys.exit(1)
    
    cf_manager = CloudflareManager(args.api_token, args.zone_id)
    
    if args.action == 'deploy':
        deploy_all(cf_manager)
    elif args.action == 'list':
        list_records(cf_manager)

if __name__ == "__main__":
    main()
