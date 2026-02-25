import json
import ipaddress
from importlib.resources import files


def load():
    data_path = files("lib_python_ip.data").joinpath("ip_data.json")
    with open(data_path, "r") as f:
        data = json.load(f)

    return [ipaddress.ip_network(ip) for ip in data]
