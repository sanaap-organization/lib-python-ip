# lib-python-ip

IP Detector → is_allowed_ip (Generic IP List Detector)

A lightweight Python package to detect whether an incoming request comes from a specific list of IPs.
Works seamlessly with FastAPI, Django, or any Python web framework.

⚡ Features

✅ IP Range Detection: Check if an IP belongs to a predefined list or CIDR ranges.

✅ Middleware-Ready: Attach detection to every request in Django or FastAPI.

✅ Fast Performance: Built-in lru_cache for caching repeated IP lookups.

✅ Flexible & Testable: Inject IP ranges for testing or dynamic configuration.

✅ Framework Agnostic: Works with any Python HTTP framework with minimal integration.

# Installation
### with pip
pip install git+https://github.com/sanaap-organization/lib-python-ip.git

### with uv
uv add git+https://github.com/sanaap-organization/lib-python-ip.git

# Usage

## FastAPI
### Step 1
```
from lib_python_ip.frameworks.fastapi_middleware import ip_middleware

app.middleware("http")(ip_middleware)
```
### Step 2
```
@app.get("/")
async def sample_view(request: Request):
    if request.state.is_allowed_ip:
        return {"message": "Valid"}
    return {"message": "Not Valid"}
```

## Django
### Step 1
```
MIDDLEWARE = [
    ...
    "lib_python_ip.frameworks.django_middleware.IPMiddleware",
]
```
### Step 2
```
def sample_view(request):
    if request.is_allowed_ip:
        return HttpResponse("Valid")
    return HttpResponse("Not Valid")
```

# Test
pytest
uv run pytest