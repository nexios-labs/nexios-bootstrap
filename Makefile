.PHONY: help install dev docker-build docker-up docker-down migrate upgrade clean test lint format

# Default target
help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  dev         - Run development server"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-up   - Start services with Docker Compose"
	@echo "  docker-down - Stop Docker Compose services"
	@echo "  migrate     - Create initial migration"
	@echo "  upgrade     - Apply migrations"
	@echo "  clean       - Clean up generated files"
	@echo "  test        - Run tests"
	@echo "  lint        - Run linting"
	@echo "  format      - Format code"

# Install dependencies
install:
	pip install -r requirements.txt

# Development server
dev:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Docker commands
docker-build:
	docker build -t nexios-bootstrap .

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f app

# Migration commands with Aerich
init-migrate:
	@echo "Initializing Aerich..."
	aerich init-db

migrate:
	@echo "Creating new migration..."
	@read -p "Enter migration name: " name && aerich migrate --name $$name

upgrade:
	@echo "Applying migrations..."
	aerich upgrade

downgrade:
	@echo "Downgrading migrations..."
	aerich downgrade

history:
	@echo "Migration history:"
	aerich history

# Custom migration script
create-migration:
	@echo "Creating migration: $(NAME)"
	aerich migrate --name $(NAME)

apply-migration:
	@echo "Applying migration: $(VERSION)"
	aerich upgrade $(VERSION)

# Database reset
reset-db:
	@echo "Resetting database..."
	@echo "Dropping tables..."
	rm -f db.sqlite3
	@echo "Creating new migration..."
	aerich migrate --name init
	@echo "Applying migration..."
	aerich upgrade

# Development tools
test:
	pytest -v

lint:
	ruff check src/

format:
	ruff format src/
	black src/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf dist
	rm -rf build

# Full setup
setup: install init-migrate
	@echo "Setup complete!"

# Production deployment
deploy-prod:
	@echo "Deploying to production..."
	docker-compose -f docker-compose.prod.yml up -d --build

# Development environment
dev-env:
	@echo "Setting up development environment..."
	cp .env.example .env
	@echo "Please edit .env file with your settings"
