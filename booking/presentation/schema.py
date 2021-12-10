from datetime import datetime
from typing import Optional

import pydantic.dataclasses
from pydantic import Field, BaseModel

from booking.domain import Model


@pydantic.dataclasses.dataclass
class BookingTimeRange:
    start_at: datetime
    end_at: datetime


class Schema(BaseModel):
    class Config(Model.Config):
        orm_mode = True


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
