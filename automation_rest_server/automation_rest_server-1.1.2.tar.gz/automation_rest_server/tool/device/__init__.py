import sys
if "win" in sys.platform:
    from .windows import NVME
else:
    from .linux import NVME