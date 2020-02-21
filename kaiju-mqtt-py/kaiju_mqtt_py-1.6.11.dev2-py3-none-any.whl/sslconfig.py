# Copyright Netflix, 2019
import json
from pathlib import Path


class SslConfig:
    DEFAULT_PORT = 1883
    TLS_DEFAULT_PORT = 8883

    def __init__(self, name: str) -> None:
        self.dir = Path(name)
        self.rootcert = self.dir / "rootca.crt"
        self.publickey = self.dir / "public.key"
        self.privatekey = self.dir / "private.key"
        self.certificate = self.dir / "cert.pem"
        self.overridefile = self.dir / "host.json"
        self.host = str(self.dir.parts[-1])
        self.port = self.TLS_DEFAULT_PORT if self.iscomplete() else self.DEFAULT_PORT

        if self.overridefile.exists():
            try:
                overrides = json.loads(self.overridefile.read_text())
                if "host" in overrides:
                    self.host = overrides["host"]
                if "port" in overrides:
                    self.port = overrides["port"]
            except json.JSONDecodeError:
                print(f"Found invalid JSON in this file, ignoring it: {self.overridefile.as_posix()}")

    def __repr__(self) -> str:
        return self.dir.__repr__()

    def __str__(self) -> str:
        return "mqtt://" + self.host + ":" + str(self.port)

    def __bool__(self) -> bool:
        return self.dir.exists()

    def exists(self) -> bool:
        return self.dir.exists()

    def iscomplete(self) -> bool:
        files = [self.rootcert, self.publickey, self.privatekey, self.certificate]
        parts = [x.exists() for x in files]
        return all(parts)
