from fastapi import FastAPI

from booking.presentation.router import router

app = FastAPI()

app.include_router(router=router)
