from fastapi import FastAPI
from tenacity import retry, stop_after_attempt, wait_fixed
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.router import base_router
from container import container
from common.enums import FindByEnum
from db_setup import DatabaseSetup

app = FastAPI()

app.include_router(base_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8666",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
@app.on_event("startup")
async def startup_event():

    await DatabaseSetup._create_all(engine=DatabaseSetup._create_engine())


@app.get("/")
async def word_service():
    word_service = await container.word_service()  # This is now a WordService instance
    await word_service.upload_words_from_csv()
    return {"status": "upload completed"}


@app.get("/get")
async def word_service():
    word_service = await container.word_service()
    word = await word_service.requests_repo.word_repo.get_by(
        sorting_word=FindByEnum.CATEGORY, value="people"
    )
    return word
