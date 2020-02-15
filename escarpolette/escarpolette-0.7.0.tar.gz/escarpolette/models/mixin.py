from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, text


class BaseModelMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(
        DateTime,
        default=datetime.now,
        server_default=text("datetime()"),
        index=True,
        nullable=False,
    )
