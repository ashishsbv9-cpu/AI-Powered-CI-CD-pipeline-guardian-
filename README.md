# Agentic AI-Powered Self-Healing CI/CD Backend

This project implements an autonomous DevOps backend that detects CI/CD pipeline failures, analyzes them using Gemini AI, and generates/validates fixes using a multi-agent system built with Google ADK.

## Features
- **Auto-Failure Detection**: Receives failure logs from GitHub Actions.
- **AI-Powered Root Cause Analysis**: Uses Gemini 1.5 Flash to identify issues.
- **Multi-Agent Orchestration**: Specialized agents for Monitoring, Analysis, Fix Generation, and Validation.
- **Auto-Fix Engine**: Automatically repairs common issues like missing dependencies.
- **Validation Engine**: Runs Pytest, Flake8, and Trivy scans to ensure fix quality.

## Tech Stack
- **Python 3.12**
- **FastAPI**
- **PostgreSQL** (SQLAlchemy + Asyncpg)
- **Google ADK** (Agent Development Kit)
- **Google Gemini API**
- **Docker & Docker Compose**

## Setup Instructions

### 1. Prerequisites
- Docker & Docker Compose
- Google Gemini API Key

### 2. Configuration
Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
Update `GOOGLE_API_KEY` and other variables in `.env`.

### 3. Run with Docker
```bash
docker-compose up --build
```

### 4. API Documentation
Once running, access the interactive API docs at:
- Swagger UI: `http://localhost:8006/docs`
- Redoc: `http://localhost:8006/redoc`

## Project Structure
```
backend/
├── app/
│   ├── api/            # API v1 routes
│   ├── agents/         # Google ADK agent logic
│   ├── services/       # Gemini and Fix engine services
│   ├── models/         # SQLAlchemy models
│   ├── database/       # DB session and setup
│   ├── validators/     # Test and scan runners
│   └── core/           # Config and security
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## How it Works
1. **GitHub Action** fails and sends a POST request to `/api/v1/pipeline/failure`.
2. **Monitor Agent** registers the failure.
3. **Analyzer Agent** calls Gemini with the logs.
4. **Fix Generator Agent** suggests code changes.
5. **Validator Agent** runs tests/scans in the container.
6. **Decision Agent** approves or rejects the fix based on validation results.
