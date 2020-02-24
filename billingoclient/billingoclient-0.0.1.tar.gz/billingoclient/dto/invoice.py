import datetime
from typing import List, Dict

from pydantic import BaseModel


class Invoice(BaseModel):
    """https://billingo.readthedocs.io/en/latest/invoices/"""
    uid: int = None
    fulfillment_date: datetime.date
    due_date: datetime.date
    comment: str
    currency: str
    payment_method: Dict
    client_uid: int
    block_uid: int
    template_lang_code: str
    electronic_invoice: bool
    type_string: str
    items: List
    client_uid: int = None
    client: Dict = None
    company: Dict = None
    exchange_rate: str = None
    invoice_no: str = None
    status: int = None
    last_payment_date: datetime.date = None
    net_total: float = None
    total: float = None
    total_paid: float = None
    vat_group_sum_converted: Dict = None
    vat_groups: Dict = None
