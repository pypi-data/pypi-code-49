from .client import LogpressoClient

def connect(host: str, port: int, user: str, password: str, secure=False):
	client = LogpressoClient()
	client.connect(host, port, user, password, secure)
	return client
