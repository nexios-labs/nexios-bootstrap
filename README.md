<div align="center">

![Nexios Logo](https://nexioslabs.com/logo.png)

# 🚀 Nexios Bootstrap

A modern, high-performance ASGI web framework starter template built with **Nexios** - the next-generation Python web framework designed for speed, flexibility, and simplicity with Rust-powered performance.
</div>

## ✨ Nexios Features

- 🏗️ **ASGI Architecture** - Built for async/await from the ground up
- 🔄 **Dependency Injection** - Modern DI system for clean, testable code
- 📚 **Auto Documentation** - Automatic OpenAPI/Swagger generation
- 🛡️ **Security Built-in** - JWT, API Key authentication, CORS, CSRF protection
- 🌐 **WebSocket Support** - Real-time communication out of the box
- 🎯 **Pydantic Integration** - Type-safe data validation and serialization
- 🛣️ **Flexible Routing** - Express.js-like routing with modern Python features
- 🧪 **Testing Utilities** - Comprehensive testing framework integration
- 📊 **Pagination** - Built-in pagination support
- ⚡ **HTTP/2 Support** - Latest web protocol support
- 🔄 **Session Management** - Secure session handling
- 🎨 **Custom Decorators** - Extensible middleware and decorators

## 🏁 Quick Start

### Prerequisites

- Python 3.10+
- pip or uv package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/nexios-labs/nexios-bootstrap.git
cd nexios-bootstrap

# Install dependencies
pip install -r requirements.txt

# Or using uv (recommended)
uv pip install -r requirements.txt

# Run development server
make dev
```

### Docker Setup

```bash
# Build and run with Docker
make docker-up

# Or manually
docker-compose up -d
```

## 📁 Project Structure

```
nexios-bootstrap/
├── src/                          # Source code
│   ├── api/                   # API routes
│   │   └── health/           # Health check endpoints
│   ├── core/                  # Core application logic
│   │   ├── middleware/         # Custom middleware
│   │   └── database.py         # Database configuration
│   ├── models/                 # Database models
│   ├── utils/                  # Utility functions
│   └── main.py               # Application entry point
├── tests/                         # Test suite
├── scripts/                        # Utility scripts
├── docker-compose.yml               # Development environment
├── docker-compose.prod.yml         # Production environment
├── Dockerfile                     # Container configuration
├── Makefile                       # Build automation
├── requirements.txt                # Dependencies
├── pyproject.toml                 # Project configuration
└── README.md                      # This file
```

## 🛣️ API Endpoints

### Health Check

#### GET `/health/`
Basic health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "service": "nexios-starter",
  "timestamp": "2024-02-20T12:00:00Z",
  "version": "0.1.0"
}
```

#### POST `/health/`
Advanced health check with async counting functionality.

**Request:**
```json
{
  "service_name": "my-service",
  "include_details": true,
  "start_number": 1,
  "end_number": 10,
  "step": 2
}
```

**Response:**
```json
{
  "status": "ok",
  "service": "my-service",
  "timestamp": "2024-02-20T12:00:00Z",
  "version": "0.1.0",
  "check_type": "basic",
  "counting_result": {
    "start": 1,
    "end": 10,
    "step": 2,
    "numbers": [1, 3, 5, 7, 9],
    "total_count": 5
  },
  "details": {
    "database": "connected",
    "cache": "available",
    "external_apis": "responsive"
  }
}
```

## 🗃️ Database Integration

### Supported Databases

- **PostgreSQL** - Production-ready with connection pooling
- **SQLite** - Development and testing (default fallback)

### Environment Variables

```bash
# PostgreSQL (recommended)
DATABASE_URL=postgres://user:password@localhost:5432/nexios

# Or individual settings
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=nexios

# Application
APP_ENV=development
DEBUG=true
```

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Verbose output
pytest tests/ -v
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker
docker-compose up -d

# Stop services
docker-compose down
```

## 🔧 Development Workflow

### Code Quality

```bash
# Format code
ruff format src/ tests/

# Lint code
ruff check src/ tests/

# Install dependencies
pip install -r requirements.txt
```

## 📚 Documentation

### Official Documentation
- **Nexios Docs**: [https://nexios-labs.github.io/nexios/](https://nexios-labs.github.io/nexios/)
- **API Reference**: [https://nexios-labs.github.io/nexios/api-reference/](https://nexios-labs.github.io/nexios/api-reference/)
- **Examples**: [https://nexios-labs.github.io/nexios/examples/](https://nexios-labs.github.io/nexios/examples/)

### Repository
- **Main Repository**: [https://github.com/nexios-labs/nexios](https://github.com/nexios-labs/nexios)
- **Bootstrap Template**: [https://github.com/nexios-labs/nexios-bootstrap](https://github.com/nexios-labs/nexios-bootstrap)

## � Middleware

The application includes:
- **CORS Middleware** - Cross-origin request handling
- **Logging Middleware** - Request/response logging

## 📊 Logging

Automatic request/response logging with:
- HTTP method and URL
- Origin tracking
- Response status codes

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md).

### Development Setup

```bash
# Fork and clone
git clone https://github.com/your-username/nexios-bootstrap.git
cd nexios-bootstrap

# Install dependencies
pip install -r requirements.txt

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and test
pytest tests/
ruff check src/ tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏‍♂️ Acknowledgments

- Built with [Nexios](https://github.com/nexios-labs/nexios) framework
- Inspired by modern web framework best practices

## 📞 Support

- 📖 [Documentation](https://nexioslabs.com)
- 🐛 [Issues](https://github.com/nexios-labs/nexios/issues)
- 💬 [Discussions](https://github.com/nexios-labs/nexios/discussions)

---

<div align="center">

**[⭐ Star this repository](https://github.com/nexios-labs/nexios-bootstrap)** if it helped you!

Built with ❤️ using [Nexios](https://github.com/nexios-labs/nexios)

