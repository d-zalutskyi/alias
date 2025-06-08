from fastapi import FastAPI
from tenacity import retry, stop_after_attempt, wait_fixed
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.router import base_router
from container import container


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
    await container.init_resources()
