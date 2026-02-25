import ipaddress


class IPDetector:
    def __init__(self, networks=None):
        if networks is None:
            networks = []
        self.networks = [ipaddress.ip_network(n) for n in networks]

    def check(self, ip: str) -> bool:
        ip_obj = ipaddress.ip_address(ip)
        return any(ip_obj in net for net in self.networks)

# import ipaddress
# from functools import lru_cache
# from .loader import load


# class IPDetector:
#     def __init__(self):
#         self.networks = load()

#     @lru_cache(maxsize=10000)
#     def check(self, ip: str) -> bool:
#         ip_obj = ipaddress.ip_address(ip)
#         return any(ip_obj in net for net in self.networks)
