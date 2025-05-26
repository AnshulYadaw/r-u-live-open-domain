const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');
const ajv = new Ajv();

// Define schema for domain JSON files
const schema = {
  type: 'object',
  required: ['description', 'domain', 'subdomain', 'owner', 'record'],
  properties: {
    description: { type: 'string', minLength: 3 },
    domain: { 
      type: 'string',
      enum: ['r-u.live'] 
    },
    subdomain: { 
      type: 'string', 
      pattern: '^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$'
    },
    owner: {
      type: 'object',
      required: ['repo', 'email'],
      properties: {
        repo: { type: 'string', format: 'uri' },
        email: { type: 'string', format: 'email' }
      },
      additionalProperties: false
    },
    record: {
      type: 'object',
      properties: {
        A: { 
          type: 'array',
          items: { 
            type: 'string',
            pattern: '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
          }
        },
        AAAA: { 
          type: 'array',
          items: { type: 'string' }
        },
        CNAME: { type: 'string' },
        MX: { 
          type: 'array', 
          items: { type: 'string' }
        },
        TXT: { 
          type: 'array', 
          items: { type: 'string' }
        },
        NS: { 
          type: 'array', 
          items: { type: 'string' }
        },
        CAA: {
          type: 'array',
          items: {
            type: 'object',
            required: ['flags', 'tag', 'value'],
            properties: {
              flags: { type: 'integer', minimum: 0 },
              tag: { type: 'string' },
              value: { type: 'string' }
            }
          }
        },
        SRV: {
          type: 'array',
          items: {
            type: 'object',
            required: ['priority', 'weight', 'port', 'target'],
            properties: {
              priority: { type: 'integer', minimum: 0 },
              weight: { type: 'integer', minimum: 0 },
              port: { type: 'integer', minimum: 1, maximum: 65535 },
              target: { type: 'string' }
            }
          }
        }
      },
      minProperties: 1,
      additionalProperties: false
    },
    proxied: { type: 'boolean' }
  },
  additionalProperties: false
};

const validate = ajv.compile(schema);

// Get all JSON files in the domains directory
const domainsDir = path.join(__dirname, '..', 'domains');
const domainFiles = fs.readdirSync(domainsDir).filter(file => file.endsWith('.json'));

let hasErrors = false;
const usedSubdomains = new Map();

// Validate each domain file
domainFiles.forEach(file => {
  const filePath = path.join(domainsDir, file);
  try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const valid = validate(data);
    
    if (!valid) {
      console.error(`❌ ${file} - Invalid JSON schema:`, validate.errors);
      hasErrors = true;
      return;
    }
    
    // Check for duplicate subdomains
    const key = `${data.subdomain}.${data.domain}`;
    if (usedSubdomains.has(key)) {
      console.error(`❌ ${file} - Duplicate subdomain: ${key} already defined in ${usedSubdomains.get(key)}`);
      hasErrors = true;
      return;
    }
    usedSubdomains.set(key, file);
    
    // Additional validation can be added here
    
    console.log(`✅ ${file} - OK`);
  } catch (error) {
    console.error(`❌ ${file} - Error:`, error.message);
    hasErrors = true;
  }
});

if (hasErrors) {
  console.error('Validation failed!');
  process.exit(1);
} else {
  console.log('All domain configurations are valid!');
}
