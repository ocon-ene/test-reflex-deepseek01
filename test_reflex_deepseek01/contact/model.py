import reflex as rx
import asyncio

from datetime import datetime, timezone

import sqlalchemy
from sqlmodel import Field

from .. import utils


class ContactEntryModel(rx.Model, table = True): #parent class as part of the name
    user_id: int | None = None
    first_name: str
    last_name: str | None = None #the same
    email: str | None = None # better this than  = Field(nullable=True) even if they are the same
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now()
        },
        nullable=False,
    )
    
