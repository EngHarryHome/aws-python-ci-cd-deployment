# AWS Python CI/CD Deployment

A Python Flask service with a fully automated CI/CD pipeline using GitHub Actions and Docker, designed for deployment on AWS EC2.

---

## What this project demonstrates

- Containerised Python application using Docker
- Automated CI/CD pipeline with GitHub Actions
- Automated testing with pytest on every push
- Docker image build validation on every push
- AWS EC2 deployment-ready architecture

---

## Tech stack

| Layer     | Technology               |
| --------- | ------------------------ |
| Language  | Python 3.11              |
| Framework | Flask                    |
| Container | Docker                   |
| CI/CD     | GitHub Actions           |
| Testing   | pytest                   |
| Cloud     | AWS EC2 (ap-southeast-2) |

---

## Project structure

- app/main.py — Flask application
- app/requirements.txt — Python dependencies
- app/tests/ — pytest test files
- .github/workflows/ci.yml — GitHub Actions pipeline
- .env.example — Environment variable template
- Dockerfile — Container definition
- README.md — This file

---

## How to run locally

```bash
git clone https://github.com/EngHarryHome/aws-python-ci-cd-deployment.git
cd aws-python-ci-cd-deployment
pip install -r app/requirements.txt
python app/main.py
```

Visit `http://localhost:8000`

---

## How to run with Docker

```bash
docker build -t aws-python-app .
docker run -p 8000:8000 aws-python-app
```

---

## How the CI/CD pipeline works

1. Developer pushes code to the `main` branch
2. GitHub Actions triggers automatically
3. Pipeline installs dependencies and runs pytest
4. If all tests pass, Docker image is built
5. Failed tests block the build — nothing broken reaches deployment

---

## API endpoints

| Method | Endpoint | Description  |
| ------ | -------- | ------------ |
| GET    | /health  | Health check |
| GET    | /time    | UTC time     |
| GET    | /        | Service info |

---

## Environment variables

Copy `.env.example` to `.env` and fill in your values. Never commit `.env` to version control.

---

## Author

Harry Home — [github.com/EngHarryHome](https://github.com/EngHarryHome)
