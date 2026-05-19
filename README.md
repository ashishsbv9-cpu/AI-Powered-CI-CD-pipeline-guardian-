Agentic AI-Powered Self-Healing CI/CD Platform

An intelligent autonomous CI/CD platform that detects pipeline failures, analyzes logs using AI, generates automated fixes, validates them securely, and re-runs pipelines with minimal human intervention.

⸻

Overview

Traditional CI/CD systems can detect failures but cannot understand the root cause or automatically recover from them.

This project introduces an Agentic AI-powered backend system capable of:

* Detecting CI/CD failures
* Collecting pipeline logs
* Performing AI-based root cause analysis
* Generating automated fixes
* Running validation and security checks
* Re-triggering pipelines automatically
* Maintaining build stability and release quality

The system acts like an autonomous DevOps engineer.

⸻

Features

CI/CD Failure Detection

* Receives failure events from GitHub Actions
* Collects logs and metadata
* Tracks pipeline history

AI Root Cause Analysis

* Uses Gemini API for intelligent log analysis
* Identifies dependency issues
* Detects Docker, YAML, and script errors
* Generates structured AI responses

Multi-Agent Architecture

Built using Google ADK with multiple intelligent agents:

* Monitor Agent
* Analyzer Agent
* Fix Generator Agent
* Validator Agent
* Decision Agent

Automated Fix Generation

Supports:

* Dependency fixes
* YAML corrections
* Dockerfile repairs
* Environment variable fixes
* Script repair suggestions

Validation & Security

Runs:

* Pytest
* Flake8
* Trivy security scans
* Static validations

PostgreSQL Storage

Stores:

* Pipeline history
* Failure logs
* AI analysis
* Fix records
* Validation reports

Dockerized Deployment

Fully containerized backend using Docker and Docker Compose.

⸻

Tech Stack

Layer	Technology
Frontend	Next.js
Styling	Tailwind CSS v3
Backend	FastAPI
Language	Python 3.12
Database	PostgreSQL
ORM	SQLAlchemy
AI Model	Gemini API
Agent Framework	Google ADK
Version Control	Git + GitHub
CI/CD	GitHub Actions
Containerization	Docker
Security Scanning	Trivy
Linting	Flake8
Testing	Pytest
Monitoring	ELK Stack
Deployment	Kubernetes

⸻

Frontend Overview

The frontend dashboard is built using Next.js and Tailwind CSS v3.

The frontend provides:

* Pipeline monitoring dashboard
* AI analysis visualization
* Failure tracking
* Validation reports
* Agent activity monitoring
* Security scan reports
* Deployment status tracking

⸻

Frontend Features

Dashboard

Displays:

* Running pipelines
* Failed builds
* Successful deployments
* AI-generated fixes

Failure Logs Viewer

* View pipeline logs
* Inspect AI root cause analysis
* Review fix history

Agent Monitoring

Track activities of:

* Monitor Agent
* Analyzer Agent
* Fix Generator Agent
* Validator Agent
* Decision Agent

Security Reports

Displays:

* Vulnerability scan results
* Validation status
* Code quality metrics

⸻

Frontend Structure

frontend/
│
├── app/
│   ├── dashboard/
│   ├── failures/
│   ├── logs/
│   ├── agents/
│   ├── security/
│   └── settings/
│
├── components/
├── services/
├── hooks/
├── store/
├── styles/
└── utils/

⸻

Git & GitHub Workflow

This project uses Git and GitHub for version control and collaboration.

Initialize Git

git init

⸻

Connect GitHub Repository

git remote add origin https://github.com/your-username/self-healing-ci.git

⸻

Push Code

git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

⸻

Recommended Git Workflow

Create Feature Branch

git checkout -b feature/ai-analyzer

Commit Changes

git add .
git commit -m "Added Gemini AI analyzer"

Push Branch

git push origin feature/ai-analyzer

Create Pull Request

Open a Pull Request on GitHub for code review and merging.

⸻

⸻

Architecture

Developer Pushes Code
          ↓
GitHub Actions Pipeline Runs
          ↓
Pipeline Failure Detected
          ↓
FastAPI Backend Receives Logs
          ↓
Google ADK Agent Workflow
    ├── Monitor Agent
    ├── Analyzer Agent
    ├── Fix Generator Agent
    ├── Validator Agent
    └── Decision Agent
          ↓
AI Root Cause Analysis
          ↓
Automated Fix Generation
          ↓
Validation & Security Checks
          ↓
Pipeline Re-run
          ↓
Deployment Success

⸻

Project Structure

backend/
│
├── app/
│   ├── api/
│   ├── agents/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── validators/
│   ├── logs/
│   ├── utils/
│   ├── core/
│   └── config/
│
├── tests/
├── docker/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── main.py

⸻

Installation

1. Clone Repository

git clone https://github.com/your-username/self-healing-ci.git
cd self-healing-ci/backend

⸻

2. Create Virtual Environment

python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

⸻

3. Install Dependencies

pip install -r requirements.txt

⸻

4. Configure Environment Variables

Create .env

DATABASE_URL=postgresql://postgres:password@localhost:5432/selfhealingci
GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_secret_key

⸻

5. Run PostgreSQL

Using Docker:

docker-compose up -d postgres

⸻

6. Start FastAPI Server

uvicorn main:app --reload

Server:

http://localhost:8000

Swagger Docs:

http://localhost:8000/docs

⸻

Docker Setup

Build Containers

docker-compose build

Start Services

docker-compose up

⸻

API Endpoints

Health Check

GET /health

⸻

Receive Pipeline Failure

POST /api/v1/pipeline/failure

Example Payload:

{
  "pipeline_id": "123",
  "repository": "sample-repo",
  "branch": "main",
  "error_log": "ModuleNotFoundError: requests"
}

⸻

Get Failure History

GET /api/v1/failures

⸻

Get Validation Results

GET /api/v1/validations

⸻

Example Workflow

Pipeline Failure

ModuleNotFoundError: No module named 'requests'

⸻

AI Analysis

{
  "issue": "Missing dependency",
  "root_cause": "requests package missing",
  "suggested_fix": "Install requests package"
}

⸻

Auto Fix Applied

pip install requests

⸻

Validation

pytest
flake8 .
trivy image app

⸻

Pipeline Re-run

Build Successful

⸻

Google ADK Agents

Monitor Agent

Detects pipeline failures and collects logs.

Analyzer Agent

Uses Gemini AI to analyze logs and determine root causes.

Fix Generator Agent

Creates automated fixes and patches.

Validator Agent

Runs tests, linting, and security scans.

Decision Agent

Determines whether deployment is safe.

⸻

Security Features

* JWT Authentication
* Environment Variable Protection
* Input Validation
* Rate Limiting
* Security Scanning with Trivy
* Static Analysis with Flake8

⸻

Future Enhancements

* Kubernetes self-healing
* Predictive failure detection
* Reinforcement learning for automated fixes
* Slack/Discord notifications
* Multi-cloud deployment support
* Real-time monitoring dashboard
* AI memory for historical failures

⸻

MVP Goals

The initial MVP includes:

* FastAPI backend
* Pipeline failure receiver
* AI log analysis
* Automated fix suggestions
* Validation engine
* PostgreSQL storage
* Docker deployment

⸻

Deployment

Recommended deployment stack:

Component	Platform
Backend	Render / Railway
Database	Supabase / Neon
Containers	Docker Hub
CI/CD	GitHub Actions
Future Kubernetes	Google Kubernetes Engine

⸻

Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

⸻

License

This project is licensed under the MIT License.

⸻

Author

Ashish M Rao

Engineering Student | AI + DevOps Enthusiast
