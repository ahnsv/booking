import datetime
import json

from pydantic import BaseModel, BaseConfig, Field


def convert_datetime_to_realworld(dt: datetime.datetime) -> str:
    return dt.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")


class Model(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {datetime.datetime: convert_datetime_to_realworld}


class IDModelMixin(BaseModel):
    id_: int = Field(default=0, alias="id")


class DateTimeModelMixin(BaseModel):
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
