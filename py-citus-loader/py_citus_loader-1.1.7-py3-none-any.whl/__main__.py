from .commands.citus_loader import dump_and_restore
from .commands.citus_dump import citus_dump
from .commands.citus_restore import citus_restore

dump_and_restore()
citus_dump()
citus_restore()
