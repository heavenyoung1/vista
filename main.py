from fastapi import FastAPI

from core.settings import settings
from routes.record import router as record_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
)

app.include_router(record_router)
