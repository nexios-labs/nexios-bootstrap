# Contributing to Nexios Bootstrap

Thank you for your interest in contributing to Nexios Bootstrap! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

- Use the [GitHub Issues](https://github.com/nexios-labs/nexios-bootstrap/issues) page
- Search existing issues before creating a new one
- Provide clear, descriptive titles and detailed descriptions
- Include steps to reproduce, expected behavior, and actual behavior
- Add relevant code examples or screenshots

### Suggesting Features

- Open an issue with the "enhancement" label
- Describe the feature and why it would be useful
- Consider whether it fits the project's scope
- Provide examples of how it would work

### Submitting Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/nexios-bootstrap.git
   cd nexios-bootstrap
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Run Tests**
   ```bash
   pytest tests/
   ```

5. **Check Code Quality**
   ```bash
   ruff check src/ tests/
   ruff format src/ tests/
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

7. **Push and Create Pull Request**
   ```bash
   git push origin feature/amazing-feature
   ```

## 📝 Code Style

### Python Code

We use the following tools for code formatting and linting:

- **Ruff** for linting and formatting
- **Black** (via Ruff) for code formatting

#### Installation
```bash
pip install ruff
```

#### Usage
```bash
# Check code style
ruff check src/ tests/

# Format code
ruff format src/ tests/
```

### Code Guidelines

- Use snake_case for variables and functions
- Use PascalCase for classes
- Add type hints for function signatures
- Write descriptive docstrings for functions and classes
- Keep functions small and focused
- Follow PEP 8 style guidelines

### Example

```python
from typing import Optional
from nexios import Request, Response


async def get_user(request: Request, user_id: int) -> dict:
    """
    Get user by ID.
    
    Args:
        request: The HTTP request object
        user_id: The user ID to retrieve
        
    Returns:
        User data dictionary
        
    Raises:
        HTTPException: If user not found
    """
    # Implementation here
    pass
```

## 🧪 Testing

### Test Structure

- Place tests in the `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies

### Example Test

```python
import pytest
from nexios.testclient import TestClient
from src.main import app


def test_health_check():
    """Test health check endpoint."""
    client = TestClient(app)
    response = client.get("/health/")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_health.py

# Verbose output
pytest tests/ -v
```

## 📁 Project Structure

```
nexios-bootstrap/
├── src/                    # Source code
│   ├── api/               # API routes
│   ├── core/              # Core functionality
│   ├── models/            # Database models
│   ├── utils/             # Utility functions
│   └── main.py           # Application entry point
├── tests/                 # Test suite
├── docs/                  # Documentation
├── scripts/               # Utility scripts
├── requirements.txt        # Dependencies
├── README.md             # Project documentation
└── CONTRIBUTING.md       # This file
```

## 🔧 Development Setup

### Prerequisites

- Python 3.10+
- pip or uv package manager
- Git

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nexios-labs/nexios-bootstrap.git
   cd nexios-bootstrap
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run Development Server**
   ```bash
   python -m src.main
   ```

## 📋 Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(health): add async counting functionality
fix(auth): resolve token validation issue
docs(readme): update installation instructions
test(health): add edge case tests
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment Information**
   - Python version
   - Operating system
   - Nexios version
   - Dependencies version

2. **Steps to Reproduce**
   - Clear, numbered steps
   - Minimal example code
   - Expected vs actual behavior

3. **Additional Context**
   - Error messages
   - Screenshots
   - Related issues

## 🚀 Release Process

1. Update version in `src/main.py`
2. Update `CHANGELOG.md`
3. Create release notes
4. Tag the release
5. Create GitHub release

## 📞 Getting Help

- **Documentation**: [Nexios Docs](https://nexios-labs.github.io/nexios/)
- **Issues**: [GitHub Issues](https://github.com/nexios-labs/nexios-bootstrap/issues)
- **Discussions**: [GitHub Discussions](https://github.com/nexios-labs/nexios-bootstrap/discussions)

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- Be respectful and considerate
- Use inclusive language
- Focus on constructive feedback
- Help others learn and grow

## 🙏‍♂️ Recognition

Contributors are recognized in:

- README.md contributors section
- Release notes
- GitHub contributor statistics

Thank you for contributing to Nexios Bootstrap! 🎉
