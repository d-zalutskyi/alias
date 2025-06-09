from fastapi import APIRouter
from backend.routers.router_manager import RouterManager
from common.schema import IDSchema
from game.schema import GameInitializeSchema
from member.schema import MemberCreateSchema
from team.schema import TeamCreateSchema

base_router = APIRouter(prefix="/v1")


@base_router.get("/health/")
async def health() -> str:
    return await RouterManager.check_health()


@base_router.post(path="/game", response_model=IDSchema, status_code=200)
async def init_game(data: GameInitializeSchema) -> IDSchema:
    return await RouterManager.initialize_game(data=data)


@base_router.post(path="/team", response_model=IDSchema, status_code=200)
async def create_team(data: TeamCreateSchema) -> IDSchema:
    return await RouterManager.create_team(data=data)


@base_router.post(path="/member", response_model=IDSchema, status_code=200)
async def create_member(data: MemberCreateSchema) -> IDSchema:
    return await RouterManager.create_member(data=data)
