from datetime import datetime
from typing import Optional

import pydantic.dataclasses
from pydantic import Field

from booking import Schema


@pydantic.dataclasses.dataclass
class BookingTimeRange:
    start_at: datetime
    end_at: datetime


class BookingCreateIn(Schema):
    title: str
    description: Optional[str]
    time_range: BookingTimeRange


class BookingCreateOut(Schema):
    id_: int = Field(alias="id")


class BookingUpdateIn(BookingCreateIn):
    pass


class BookingUpdateOut(Schema):
    id_: int = Field(alias="id")
    updated_at: datetime
