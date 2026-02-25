from fastapi import Request
from ..core import IPDetector

detector = IPDetector()


async def ip_middleware(request: Request, call_next):
    ip = request.client.host

    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        ip = forwarded.split(",")[0].strip()

    request.state.is_allowed_ip = detector.is_allowed_ip(ip)

    response = await call_next(request)
    return response
