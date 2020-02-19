class Camera:
    def __init__(
        self,
        cid: str,
        current_task: str = "",
        hardware_platform: str = "K2",
        address: str = "",
        system_state: str = "",
    ):
        self.id = cid
        self.current_task = current_task
        self.hardware_platform = hardware_platform
        self.address = address
        self.system_state = system_state

    @classmethod
    def from_json(
        cls,
        RowKey: str,
        currentTask: str = "",
        hardwarePlatform: str = "K2",
        address: str = "",
        systemState: str = "",
        *args,
        **kwargs
    ):
        return Camera(
            cid=RowKey,
            current_task=currentTask,
            hardware_platform=hardwarePlatform,
            address=address,
            system_state=systemState,
        )
