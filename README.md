# CareCloud Voice Agent Infrastructure

## Overview
AI-powered healthcare voice agent backend infrastructure for Lakewood Family Medicine.
Built for the CareCloud DevOps/Infrastructure Engineer technical assessment.

## Architecture
- **Voice Platform:** Vapi.ai (inbound calls, LLM-powered)
- **Phone Number:** +1 (727) 633 0087
- **LLM:** OpenAI GPT-4.1
- **Backend:** FastAPI (Python)
- **Containerization:** Docker + Docker Compose
- **Logging:** Loguru (structured JSON logs, 7-day retention)

## What Was Built
1. Vapi voice agent (Sarah) answering inbound patient calls
2. FastAPI backend receiving webhooks from Vapi
3. Structured logging for all call events
4. Docker containerization for reproducible deployment
5. Health check endpoint at /health

## How to Run
```bash
cp .env.example .env
# Add your API keys to .env
docker-compose up --build
```

## API Endpoints
- GET /health — Health check
- POST /webhook — Vapi webhook receiver
- POST /call-started — Call start events
- POST /call-ended — Call end events

## Security & HIPAA Awareness
- API keys stored in environment variables, never committed to git
- In production: AWS Secrets Manager for all credentials
- HIPAA compliance would require: BAAs with all vendors, encryption at rest, audit logging, network isolation, access controls

## What I Would Do With More Time
- Deploy to AWS EC2 with Terraform
- Add PostgreSQL for call record persistence
- Set up CloudWatch metrics and alerts
- Add S3 backup for call logs
- Implement CI/CD with GitHub Actions
- Add Grafana dashboard for call volume monitoring
- HIPAA-compliant audit logging

## Known Risks
- Backend not yet deployed to cloud (time constraint)
- No database persistence in current implementation
- No alerting configured yet
- Voice number may have activation delay

## Trade-offs Made
Given 3-hour constraint, prioritized:
1. Working voice agent (Part 1 complete)
2. Clean, documented backend code
3. Docker containerization for reproducibility
4. Clear documentation over partial implementations