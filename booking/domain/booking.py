from datetime import datetime
from typing import Optional

from booking.domain import Model, IDModelMixin, DateTimeModelMixin


class Booking(IDModelMixin, DateTimeModelMixin, Model):
    title: str
    description: Optional[str]
    start_at: datetime
    end_at: datetime
