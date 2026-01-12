# AWS Python CI/CD Deployment

A minimal Python service designed to be deployed on AWS EC2 and updated via CI/CD using GitHub Actions.

## Endpoints

- `GET /health` – health check
- `GET /time` – returns current UTC time

## Local run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
pytest
python app/main.py
```
