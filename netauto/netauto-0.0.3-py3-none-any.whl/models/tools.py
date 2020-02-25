from typing import List

from pydantic import BaseModel


class PortScanResp(BaseModel):
    ip: str
    status: str


class SendMail(BaseModel):
    to: List[str]
    subject: str
    content: str
