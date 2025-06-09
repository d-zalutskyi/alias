from fastapi import APIRouter
from backend.routers.router_manager import RouterManager
from game.schema import GameIDSchema, GameInitializeSchema

base_router = APIRouter(prefix="/v1")


@base_router.get("/health/")
async def health() -> str:
    return await RouterManager.check_health()


@base_router.post(path="/game", response_model=GameIDSchema, status_code=200)
async def init_game(data: GameInitializeSchema) -> GameIDSchema:
    return await RouterManager.initialize_game(data=data)
