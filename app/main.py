from fastapi import FastAPI
from app.schemas import PingResponse
from app.api.ping import ping as ping_service

app = FastAPI()

@app.get("/api/ping", response_model=PingResponse)
async def ping_route() -> PingResponse:
    """HTTP GET /api/ping route — delegates to app.api.ping.ping for business logic."""
    return await ping_service()
