from ..config import AiopikaDriverConfig, QueuePropertyConfig


class QueueRPCPropertyConfig(QueuePropertyConfig):
    name: str = 'rpc_queue'
    auto_delete: bool = False
    durable: bool = True


class AiopikaRPCDriverConfig(AiopikaDriverConfig):

    logo: str = """
 _____       _
|  __ \     (_)               
| |  | |_ __ ___   _____ _ __ 
| |  | | '__| \ \ / / _ \ '__|
| |__| | |  | |\ V /  __/ |   
|_____/|_|  |_| \_/ \___|_|aiopika_rpc
"""

    queue: QueueRPCPropertyConfig = QueueRPCPropertyConfig()

    # Processing
    default_expire_call: int = 30
