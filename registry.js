#!/usr/bin/env node

/**
 * Domain Registration Helper Tool
 * 
 * This script helps maintain and validate the r-u.live domain registry
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration
const DOMAINS_DIR = path.join(__dirname, 'domains');
const VALID_DOMAINS = ['r-u.live'];

// Command line arguments
const args = process.argv.slice(2);
const command = args[0];

// Function to list all subdomains
function listSubdomains() {
  const files = fs.readdirSync(DOMAINS_DIR).filter(file => file.endsWith('.json'));
  
  console.log('\n🌐 r-u.live Subdomain Registry');
  console.log('==============================');
  
  let count = 0;
  
  files.forEach(file => {
    try {
      const data = JSON.parse(fs.readFileSync(path.join(DOMAINS_DIR, file)));
      console.log(`${++count}. ${data.subdomain}.${data.domain} - ${data.description}`);
      console.log(`   Owner: ${data.owner.email}`);
      console.log(`   Proxied: ${data.proxied ? 'Yes' : 'No'}`);
      console.log('   Records:');
      
      // List records
      Object.keys(data.record).forEach(recordType => {
        if (Array.isArray(data.record[recordType])) {
          data.record[recordType].forEach(value => {
            console.log(`     - ${recordType}: ${value}`);
          });
        } else {
          console.log(`     - ${recordType}: ${data.record[recordType]}`);
        }
      });
      
      console.log(''); // Empty line between entries
    } catch (error) {
      console.error(`Error processing ${file}: ${error.message}`);
    }
  });
  
  console.log(`\nTotal subdomains: ${count}`);
}

// Function to validate all domain files
function validateDomains() {
  const files = fs.readdirSync(DOMAINS_DIR).filter(file => file.endsWith('.json'));
  
  console.log('\n🔍 Validating domain configurations');
  console.log('=================================');
  
  let validCount = 0;
  let errorCount = 0;
  const subdomains = {};
  
  files.forEach(file => {
    try {
      const data = JSON.parse(fs.readFileSync(path.join(DOMAINS_DIR, file)));
      let isValid = true;
      
      // Check required fields
      if (!data.description || !data.domain || !data.subdomain || !data.owner || !data.record) {
        console.error(`❌ ${file}: Missing required fields`);
        isValid = false;
      }
      
      // Check owner fields
      if (data.owner && (!data.owner.repo || !data.owner.email)) {
        console.error(`❌ ${file}: Missing owner information`);
        isValid = false;
      }
      
      // Check domain is valid
      if (!VALID_DOMAINS.includes(data.domain)) {
        console.error(`❌ ${file}: Invalid domain "${data.domain}"`);
        isValid = false;
      }
      
      // Check subdomain format
      if (!/^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$/.test(data.subdomain)) {
        console.error(`❌ ${file}: Invalid subdomain name "${data.subdomain}"`);
        isValid = false;
      }
      
      // Check for duplicate subdomains
      const key = `${data.subdomain}.${data.domain}`;
      if (subdomains[key]) {
        console.error(`❌ ${file}: Duplicate subdomain "${key}" (also in ${subdomains[key]})`);
        isValid = false;
      } else {
        subdomains[key] = file;
      }
      
      // Check that at least one record exists
      if (data.record && Object.keys(data.record).length === 0) {
        console.error(`❌ ${file}: No DNS records specified`);
        isValid = false;
      }
      
      if (isValid) {
        console.log(`✅ ${file}: Valid`);
        validCount++;
      } else {
        errorCount++;
      }
    } catch (error) {
      console.error(`❌ ${file}: ${error.message}`);
      errorCount++;
    }
  });
  
  console.log('\nValidation Summary:');
  console.log(`Total files: ${files.length}`);
  console.log(`Valid: ${validCount}`);
  console.log(`Errors: ${errorCount}`);
  
  return errorCount === 0;
}

// Function to generate a report
function generateReport() {
  const files = fs.readdirSync(DOMAINS_DIR).filter(file => file.endsWith('.json'));
  const recordTypes = {};
  const proxiedCount = { true: 0, false: 0 };
  
  files.forEach(file => {
    try {
      const data = JSON.parse(fs.readFileSync(path.join(DOMAINS_DIR, file)));
      
      // Count record types
      Object.keys(data.record).forEach(type => {
        recordTypes[type] = (recordTypes[type] || 0) + 1;
      });
      
      // Count proxied status
      if (data.proxied === true) {
        proxiedCount.true++;
      } else {
        proxiedCount.false++;
      }
    } catch (error) {
      console.error(`Error processing ${file}: ${error.message}`);
    }
  });
  
  console.log('\n📊 r-u.live Domain Registry Report');
  console.log('================================');
  console.log(`Total subdomains: ${files.length}`);
  console.log('\nRecord Types:');
  Object.keys(recordTypes).forEach(type => {
    console.log(`  - ${type}: ${recordTypes[type]}`);
  });
  
  console.log('\nProxied Status:');
  console.log(`  - Proxied: ${proxiedCount.true}`);
  console.log(`  - Not Proxied: ${proxiedCount.false}`);
}

// Main command dispatcher
switch (command) {
  case 'list':
    listSubdomains();
    break;
    
  case 'validate':
    validateDomains();
    break;
    
  case 'report':
    generateReport();
    break;
    
  default:
    console.log('\n🔧 r-u.live Domain Registry Helper');
    console.log('================================');
    console.log('Usage: node registry.js <command>');
    console.log('\nCommands:');
    console.log('  list      List all registered subdomains');
    console.log('  validate  Validate all domain files');
    console.log('  report    Generate registry statistics');
}
