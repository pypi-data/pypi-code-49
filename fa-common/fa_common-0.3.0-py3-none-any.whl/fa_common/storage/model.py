from typing import Optional

from pydantic import BaseModel
from fa_common import sizeof_fmt


# Shared properties
class File(BaseModel):
    size: str  # e.g. '3 KB'
    url: Optional[str] = None  # download url
    id: str  # id can be path or database id
    dir: bool  # is current node dir?
    path: str  # path to current item (e.g. /folder1/someFile.txt)
    # optional (but we are using id as name if name is not present) (e.g. someFile.txt)
    name: Optional[str] = None

    def set_size(self, bytes: int):
        self.size = sizeof_fmt(bytes)
