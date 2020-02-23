from logging import getLogger
from typing import Union

from gumo.core.injector import injector
from gumo.task_emulator.domain.configuration import TaskEmulatorConfiguration
from gumo.task_emulator.bind import task_emulator_bind


logger = getLogger('gumo.task')


class ConfigurationFactory:
    DEFAULT_SERVER_PORT = 8080

    @classmethod
    def build(
            cls,
            server_host: str,
            server_port: Union[str, int, None],
    ) -> TaskEmulatorConfiguration:
        if isinstance(server_port, str):
            if server_port.isdigit():
                port = int(server_port)
            else:
                raise ValueError(f'Invalid format of server_port={server_port}')
        elif isinstance(server_port, int):
            port = server_port
        else:
            port = cls.DEFAULT_SERVER_PORT

        return TaskEmulatorConfiguration(
            server_host=server_host,
            server_port=port,
        )


def configure(
        server_host: str,
        server_port: Union[str, int, None] = None,
) -> TaskEmulatorConfiguration:
    config = ConfigurationFactory.build(
        server_host=server_host,
        server_port=server_port,
    )
    logger.debug(f'Gumo.TaskEmulator is configured, config={config}')

    injector.binder.bind(TaskEmulatorConfiguration, to=config)
    injector.binder.install(task_emulator_bind)

    return config
