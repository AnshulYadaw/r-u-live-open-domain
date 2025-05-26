# Contributing to r-u.live

Thank you for considering contributing to r-u.live! This document provides guidelines and instructions for contributing to this project.

## Ways to Contribute

1. **Register a Subdomain**: Follow the [guide](GUIDE.md) to register your own subdomain
2. **Report Issues**: Report bugs or suggest improvements by opening an issue
3. **Submit Improvements**: Enhance the codebase by submitting pull requests
4. **Documentation**: Help improve or translate documentation
5. **Spread the Word**: Share the project with others who might benefit from it

## Development Setup

### Prerequisites

- Node.js 14 or higher
- Git
- A GitHub account
- Basic knowledge of DNS, JavaScript, and GitHub Actions

### Local Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/r-u-live.git
   cd r-u-live
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Run validation tests:
   ```bash
   npm run validate
   ```

## Making Changes

### For Code Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Run tests:
   ```bash
   npm test
   ```
4. Commit your changes:
   ```bash
   git commit -am "Add new feature: description"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Submit a pull request

### For Documentation Changes

1. Edit the relevant Markdown files
2. Commit and push your changes
3. Submit a pull request

## Pull Request Guidelines

1. Update documentation if needed
2. Add tests for new features
3. Follow existing code style
4. Keep pull requests focused on a single topic
5. Write a descriptive title and detailed description

## Code Style

- Use consistent indentation (2 spaces)
- Follow JavaScript Standard Style
- Comment complex sections of code
- Write meaningful commit messages

## Subdomain Request Guidelines

When submitting a new subdomain:

1. Use a descriptive name that represents your project
2. Ensure JSON is properly formatted
3. Include all required fields
4. Provide a clear description of how the subdomain will be used

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

## Questions?

If you have questions or need help with the contribution process, please open an issue for assistance.
