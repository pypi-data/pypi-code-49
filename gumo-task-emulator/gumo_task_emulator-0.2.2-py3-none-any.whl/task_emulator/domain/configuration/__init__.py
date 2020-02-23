import dataclasses


@dataclasses.dataclass(frozen=True)
class TaskEmulatorConfiguration:
    server_host: str
    server_port: int = 8080
