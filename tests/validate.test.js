const fs = require('fs');
const path = require('path');

// Mock fs and path modules
jest.mock('fs');
jest.mock('path');

describe('Domain Configuration Validation', () => {
  let validateModule;
  let mockExit;
  
  beforeEach(() => {
    // Set up test environment
    mockExit = jest.spyOn(process, 'exit').mockImplementation(() => {});
    
    // Mock path.join to return predictable paths
    path.join.mockImplementation((...args) => args.join('/'));
    
    // Reset validation module before each test
    jest.resetModules();
  });
  
  afterEach(() => {
    mockExit.mockRestore();
    jest.clearAllMocks();
  });
  
  test('validates a valid domain configuration', () => {
    // Mock valid domain file
    const validDomain = {
      description: 'Valid test domain',
      domain: 'r-u.live',
      subdomain: 'test',
      owner: {
        repo: 'https://github.com/username/repo',
        email: 'test@example.com'
      },
      record: {
        A: ['192.0.2.1']
      },
      proxied: true
    };
    
    fs.readdirSync.mockReturnValue(['test.json']);
    fs.readFileSync.mockReturnValue(JSON.stringify(validDomain));
    
    // Run validation
    require('../tests/validate');
    
    // Expect successful validation (exit not called with error)
    expect(mockExit).not.toHaveBeenCalled();
  });
  
  test('detects invalid domain configuration', () => {
    // Mock invalid domain file with missing required fields
    const invalidDomain = {
      domain: 'r-u.live',
      subdomain: 'test',
      // Missing 'description' and 'owner'
      record: {
        A: ['192.0.2.1']
      },
      proxied: true
    };
    
    fs.readdirSync.mockReturnValue(['invalid.json']);
    fs.readFileSync.mockReturnValue(JSON.stringify(invalidDomain));
    
    // Redirect console.error to prevent test output clutter
    jest.spyOn(console, 'error').mockImplementation(() => {});
    
    // Run validation
    require('../tests/validate');
    
    // Expect failed validation
    expect(mockExit).toHaveBeenCalledWith(1);
  });
  
  test('detects duplicate subdomains', () => {
    // Mock two files with the same subdomain
    const validDomain = {
      description: 'Valid test domain',
      domain: 'r-u.live',
      subdomain: 'test',
      owner: {
        repo: 'https://github.com/username/repo',
        email: 'test@example.com'
      },
      record: {
        A: ['192.0.2.1']
      },
      proxied: true
    };
    
    fs.readdirSync.mockReturnValue(['test1.json', 'test2.json']);
    fs.readFileSync.mockReturnValue(JSON.stringify(validDomain));
    
    // Redirect console.error to prevent test output clutter
    jest.spyOn(console, 'error').mockImplementation(() => {});
    
    // Run validation
    require('../tests/validate');
    
    // Expect failed validation due to duplicate subdomains
    expect(mockExit).toHaveBeenCalledWith(1);
  });
});
