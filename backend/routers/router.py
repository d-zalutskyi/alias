from fastapi import APIRouter
from backend.routers.router_manager import RouterManager


base_router = APIRouter(prefix="/v1")


@base_router.get("/health/")
async def health() -> str:
    return await RouterManager.check_health()
