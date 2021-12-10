from datetime import datetime
from typing import List, Optional

import pydantic.dataclasses
from fastapi import APIRouter, HTTPException
from pydantic import Field

from booking import Schema
from booking.domain.booking import Booking

bookings: List[Booking] = []

router = APIRouter(prefix="/api/v1/booking")


@router.get("/")
async def get_bookings():
    return bookings


@router.get("/{booking_id}")
async def get_info(booking_id: int):
    return next((booking for booking in bookings if booking.id_ == booking_id), None)


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


@router.post("/", response_model=BookingCreateOut)
async def make_booking(booking_create: BookingCreateIn):
    new_booking = Booking(
        title=booking_create.title,
        description=booking_create.description,
        start_at=booking_create.time_range.start_at,
        end_at=booking_create.time_range.end_at,
    )
    bookings.append(new_booking)
    return new_booking


class BookingUpdateIn(BookingCreateIn):
    pass


class BookingUpdateOut(Schema):
    id_: int = Field(alias="id")
    updated_at: datetime


@router.put("/{booking_id}", response_model=BookingUpdateOut)
async def update_booking(booking_id: int, booking_update: BookingUpdateIn):
    if not bookings:
        raise HTTPException(status_code=404, detail="No Bookings")

    existing_booking_idx, existing_booking = next(
        ((booking_idx, booking) for booking_idx, booking in enumerate(bookings) if booking.id_ == booking_id), None
    )
    if not existing_booking:
        raise ValueError
    updated_booking: Booking = existing_booking.copy()
    for key, value in booking_update.dict().items():
        if key == "time_range":
            updated_booking.start_at = value.start_at
            updated_booking.end_at = value.end_at
            continue
        setattr(updated_booking, key, value)

    bookings[existing_booking_idx] = updated_booking
    return updated_booking


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int):
    existing_booking_idx = next(
        (booking_idx for booking_idx, booking in enumerate(bookings) if booking.id_ == booking_id), None
    )
    if existing_booking_idx is None:
        raise ValueError
    del bookings[existing_booking_idx]
