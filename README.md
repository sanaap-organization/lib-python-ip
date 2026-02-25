# lib-python-ip

# Usage

## FastAPI
from ip_detector.frameworks.fastapi import ip_middleware

app.middleware("http")(ip_middleware)

## Django
MIDDLEWARE = [
    ...
    "ip_detector.frameworks.django.IPMiddleware",
]

# Test
pytest
uv run pytest