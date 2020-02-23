
class Endpoint:
    def __init__(self, service_name, ipv4, port=8000, **kwargs):
        self.serve_name = service_name
        self.ipv4 = ipv4
        self.port = port

    def to_dict(self):
        return {
            "servicename": self.serve_name,
            "ipv4": self.ipv4,
            "ipv6": "",
            "port": self.port
        }


