from ..core import IPDetector

detector = IPDetector()


class IPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")

        forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
        if forwarded:
            ip = forwarded.split(",")[0]

        request.is_allowed_ip = detector.is_allowed_ip(ip)
        return self.get_response(request)
