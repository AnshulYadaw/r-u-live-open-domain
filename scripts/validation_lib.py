#!/usr/bin/env python3
"""
Enhanced Validation Library for r-u.live
Inspired by open-domains/register validation patterns
"""

import re
import socket
import ipaddress
import yaml
import json
import requests
from typing import Dict, List, Tuple, Optional, Any
from urllib.parse import urlparse
import dns.resolver
import whois
from datetime import datetime, timedelta

class SubdomainValidator:
    """
    Comprehensive subdomain validation inspired by open-domains patterns
    """
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        
        # Reserved subdomains (comprehensive list from open-domains)
        self.reserved_subdomains = {
            # Administrative
            'www', 'mail', 'ftp', 'admin', 'api', 'app', 'dashboard', 'panel',
            'control', 'cp', 'root', 'system', 'network', 'monitoring',
            
            # Development
            'test', 'dev', 'staging', 'prod', 'production', 'beta', 'alpha',
            'preview', 'demo', 'sandbox', 'lab', 'experimental',
            
            # Content/Media
            'blog', 'shop', 'store', 'cdn', 'static', 'assets', 'img', 'images',
            'css', 'js', 'fonts', 'media', 'uploads', 'files', 'download',
            
            # Support/Community
            'help', 'support', 'docs', 'documentation', 'wiki', 'forum',
            'community', 'news', 'about', 'contact', 'legal', 'privacy', 'terms',
            
            # Authentication
            'login', 'register', 'signup', 'signin', 'auth', 'oauth', 'sso',
            'account', 'profile', 'user', 'users', 'member', 'members',
            
            # Infrastructure
            'vpn', 'proxy', 'gateway', 'router', 'switch', 'firewall',
            'dns', 'ntp', 'ldap', 'smtp', 'pop', 'imap', 'webmail',
            
            # Monitoring/Analytics
            'logs', 'metrics', 'health', 'status', 'ping', 'uptime',
            'analytics', 'stats', 'graph', 'charts', 'reports',
            
            # Storage/Database
            'backup', 'sync', 'mirror', 'replica', 'cache', 'redis',
            'db', 'database', 'mysql', 'postgres', 'mongo', 'elastic',
            
            # Security
            'secure', 'ssl', 'tls', 'cert', 'certificate', 'key', 'crypto',
            'vault', 'secrets', 'security', 'firewall', 'intrusion',
            
            # Abuse/Malicious
            'abuse', 'security', 'vulnerability', 'exploit', 'hack', 'malware',
            'illegal', 'spam', 'phishing', 'scam', 'fraud', 'fake', 'virus',
            'trojan', 'worm', 'bot', 'botnet', 'ddos', 'attack',
            
            # Inappropriate
            'nazi', 'hitler', 'isis', 'terrorist', 'extremist', 'hate',
            'porn', 'sex', 'xxx', 'adult', 'nsfw', 'explicit'
        }
        
        # Temporary email domains
        self.temp_email_domains = {
            '10minutemail.com', 'guerrillamail.com', 'tempmail.org',
            'throwaway.email', 'mailinator.com', 'temp-mail.org',
            'maildrop.cc', 'sharklasers.com', 'guerrillamailblock.com',
            'pokemail.net', 'spam4.me', 'bccto.me', 'chacuo.net',
            'emailsensei.com', 'emailtemporanea.net', 'incognitomail.org',
            'mytrashmail.com', 'no-spam.ws', 'nospamfor.us',
            'objectmail.com', 'proxymail.eu', 'rcpt.at', 'trash2009.com'
        }
        
        # Malicious content patterns
        self.malicious_patterns = [
            # XSS
            r'<script.*?>.*?</script>',
            r'javascript:',
            r'data:text/html',
            r'vbscript:',
            r'on\w+\s*=',
            
            # Template injection
            r'\$\{.*?\}',
            r'<%.*?%>',
            r'{{.*?}}',
            r'{%.*?%}',
            
            # SQL injection patterns
            r'union\s+select',
            r'drop\s+table',
            r'insert\s+into',
            r'delete\s+from',
            
            # Command injection
            r';\s*rm\s+-rf',
            r';\s*cat\s+/etc/passwd',
            r'`.*`',
            r'\$\(.*\)',
        ]
        
        # Inappropriate content patterns
        self.inappropriate_patterns = [
            r'\b(spam|hack|phish|scam|fake|virus|malware|trojan|worm|bot)\b',
            r'\b(illegal|drugs|weapon|bomb|terror|kill|murder|rape)\b',
            r'\b(nazi|hitler|isis|terrorist|extremist)\b',
            r'\b(porn|sex|xxx|adult|nsfw|explicit)\b',
            r'\b(hate|racist|sexist|homophobic|transphobic)\b'
        ]

    def reset(self):
        """Reset errors and warnings for new validation"""
        self.errors = []
        self.warnings = []

    def validate_subdomain_format(self, subdomain: str) -> bool:
        """Validate subdomain format according to RFC standards"""
        if not subdomain:
            self.errors.append("Subdomain cannot be empty")
            return False
        
        # Length check
        if len(subdomain) < 1:
            self.errors.append("Subdomain too short (minimum 1 character)")
            return False
        elif len(subdomain) > 63:
            self.errors.append(f"Subdomain too long: {len(subdomain)} characters (maximum 63)")
            return False
        
        # Format validation
        if not re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$', subdomain):
            self.errors.append(f"Invalid subdomain format: '{subdomain}' (must be alphanumeric + hyphens)")
            return False
        
        # Cannot start or end with hyphen
        if subdomain.startswith('-') or subdomain.endswith('-'):
            self.errors.append(f"Subdomain cannot start or end with hyphen: '{subdomain}'")
            return False
        
        # Check for consecutive hyphens
        if '--' in subdomain:
            self.warnings.append(f"Subdomain contains consecutive hyphens: '{subdomain}'")
        
        return True

    def validate_subdomain_availability(self, subdomain: str, existing_files: List[str]) -> bool:
        """Check if subdomain is available"""
        subdomain_lower = subdomain.lower()
        
        # Check reserved names
        if subdomain_lower in self.reserved_subdomains:
            self.errors.append(f"Subdomain '{subdomain}' is reserved")
            return False
        
        # Check existing subdomains
        existing_subdomains = set()
        for file_path in existing_files:
            try:
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                if data and 'subdomain' in data:
                    existing_subdomains.add(data['subdomain'].lower())
            except Exception:
                continue
        
        if subdomain_lower in existing_subdomains:
            self.errors.append(f"Subdomain '{subdomain}' already exists")
            return False
        
        return True

    def validate_subdomain_content(self, subdomain: str) -> bool:
        """Check subdomain for inappropriate content"""
        for pattern in self.inappropriate_patterns:
            if re.search(pattern, subdomain, re.IGNORECASE):
                self.errors.append(f"Subdomain '{subdomain}' contains inappropriate content")
                return False
        return True

    def validate_ip_address(self, ip_str: str, record_type: str) -> bool:
        """Validate IP address for A or AAAA records"""
        try:
            if record_type == 'A':
                ip = ipaddress.IPv4Address(ip_str)
                
                # Check for private/reserved IPs
                if ip.is_private:
                    self.warnings.append(f"Private IP address detected: {ip_str}")
                elif ip.is_loopback:
                    self.errors.append(f"Loopback IP not allowed: {ip_str}")
                    return False
                elif ip.is_reserved:
                    self.errors.append(f"Reserved IP address: {ip_str}")
                    return False
                elif ip.is_multicast:
                    self.errors.append(f"Multicast IP not allowed: {ip_str}")
                    return False
                
                # Check specific reserved ranges
                ip_str_parts = str(ip).split('.')
                first_octet = int(ip_str_parts[0])
                
                if first_octet in [0, 127, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]:
                    self.errors.append(f"Invalid IP address range: {ip_str}")
                    return False
                
            elif record_type == 'AAAA':
                ip = ipaddress.IPv6Address(ip_str)
                
                if ip.is_private or ip.is_loopback or ip.is_reserved or ip.is_multicast:
                    self.errors.append(f"Invalid IPv6 address: {ip_str} (private/loopback/reserved/multicast)")
                    return False
                
                # Check documentation ranges
                if str(ip).lower().startswith(('fc', 'fd', 'fe80', '::1', '2001:db8')):
                    self.errors.append(f"Invalid IPv6 address: {ip_str} (documentation/private range)")
                    return False
            
            return True
            
        except ipaddress.AddressValueError:
            self.errors.append(f"Invalid {record_type} address format: {ip_str}")
            return False

    def validate_domain(self, domain: str) -> bool:
        """Validate domain format for CNAME records"""
        if len(domain) > 253:
            self.errors.append(f"Domain too long: {domain} (max 253 characters)")
            return False
        
        # Basic domain format validation
        if not re.match(r'^(?=.{1,253}$)(?:(?:[_a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)\.)+[a-zA-Z]{2,63}$', domain):
            self.errors.append(f"Invalid domain format: {domain}")
            return False
        
        # Cannot point to self
        if domain.endswith('.r-u.live') or domain.endswith('.r-u.live.'):
            self.errors.append("Cannot point to another r-u.live subdomain")
            return False
        
        # Must have at least one dot
        if domain.count('.') < 1:
            self.errors.append(f"Invalid domain: {domain} (must have at least one dot)")
            return False
        
        return True

    def validate_domain_resolution(self, domain: str) -> bool:
        """Check if domain resolves"""
        try:
            socket.gethostbyname(domain)
            return True
        except socket.gaierror:
            self.warnings.append(f"Domain {domain} may not exist or is unreachable")
            return True  # Warning, not error

    def validate_email(self, email: str) -> bool:
        """Validate email address"""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            self.errors.append(f"Invalid email format: {email}")
            return False
        
        # Check for temporary email domains
        try:
            domain = email.split('@')[1].lower()
            if domain in self.temp_email_domains:
                self.warnings.append(f"Temporary email domain detected: {domain}")
        except IndexError:
            pass
        
        return True

    def validate_repository_url(self, repo_url: str) -> bool:
        """Validate repository URL"""
        if not repo_url:
            return True  # Optional field
        
        # Ensure it starts with http/https
        if not repo_url.startswith(('http://', 'https://')):
            repo_url = 'https://' + repo_url
        
        # Check if it's from a known Git hosting service
        known_hosts = ['github.com', 'gitlab.com', 'bitbucket.org', 'codeberg.org', 'sourceforge.net']
        parsed = urlparse(repo_url)
        
        if not any(host in parsed.netloc for host in known_hosts):
            self.warnings.append(f"Repository URL should be from a known Git hosting service: {repo_url}")
        
        return True

    def validate_security(self, content: str) -> bool:
        """Check for security issues in content"""
        # Check for malicious patterns
        for pattern in self.malicious_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.errors.append("Suspicious content detected in submission")
                return False
        
        return True

    def validate_yaml_structure(self, data: Dict[str, Any]) -> bool:
        """Validate YAML structure"""
        required_fields = ['subdomain', 'owner', 'record']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            self.errors.append(f"Missing required fields: {', '.join(missing_fields)}")
            return False
        
        # Validate owner structure
        if 'owner' in data:
            owner = data['owner']
            if not isinstance(owner, dict):
                self.errors.append("Owner field must be an object")
                return False
            
            if 'name' not in owner or 'email' not in owner:
                self.errors.append("Owner must have name and email fields")
                return False
        
        # Validate record structure
        if 'record' in data:
            record = data['record']
            if not isinstance(record, dict):
                self.errors.append("Record field must be an object")
                return False
            
            valid_record_types = ['A', 'AAAA', 'CNAME']
            has_valid_record = any(rt in record for rt in valid_record_types)
            
            if not has_valid_record:
                self.errors.append(f"Must have at least one valid DNS record type: {', '.join(valid_record_types)}")
                return False
        
        return True

    def validate_complete_submission(self, data: Dict[str, Any], existing_files: List[str] = None) -> Tuple[List[str], List[str]]:
        """Complete validation of a subdomain submission"""
        self.reset()
        existing_files = existing_files or []
        
        # Convert data to string for security scanning
        content_str = yaml.dump(data) if isinstance(data, dict) else str(data)
        
        # Security validation first
        if not self.validate_security(content_str):
            return self.errors, self.warnings
        
        # Structure validation
        if not self.validate_yaml_structure(data):
            return self.errors, self.warnings
        
        # Subdomain validation
        subdomain = data.get('subdomain', '')
        if subdomain:
            self.validate_subdomain_format(subdomain)
            self.validate_subdomain_content(subdomain)
            self.validate_subdomain_availability(subdomain, existing_files)
        
        # Owner validation
        owner = data.get('owner', {})
        if 'email' in owner:
            self.validate_email(owner['email'])
        
        if 'repo' in owner:
            self.validate_repository_url(owner['repo'])
        
        # DNS record validation
        record = data.get('record', {})
        for record_type, target in record.items():
            if record_type in ['A', 'AAAA']:
                if isinstance(target, list):
                    for ip in target:
                        self.validate_ip_address(str(ip), record_type)
                else:
                    self.validate_ip_address(str(target), record_type)
            elif record_type == 'CNAME':
                if self.validate_domain(str(target)):
                    self.validate_domain_resolution(str(target))
        
        return self.errors, self.warnings


def validate_file(file_path: str, existing_files: List[str] = None) -> Tuple[List[str], List[str]]:
    """Validate a single subdomain file"""
    validator = SubdomainValidator()
    
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return [f"Failed to parse YAML file: {e}"], []
    
    return validator.validate_complete_submission(data, existing_files)


if __name__ == "__main__":
    import sys
    import glob
    
    if len(sys.argv) < 2:
        print("Usage: python validation_lib.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    existing_files = glob.glob("subdomains/*.yaml")
    
    errors, warnings = validate_file(file_path, existing_files)
    
    if errors:
        print(f"❌ Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    
    if warnings:
        print(f"⚠️ Validation passed with {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  - {warning}")
    else:
        print("✅ Validation passed!")
    
    sys.exit(0)
