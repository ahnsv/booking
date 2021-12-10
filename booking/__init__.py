from pydantic import BaseModel

from booking.domain import Model


class Schema(BaseModel):
    class Config(Model.Config):
        orm_mode = True
