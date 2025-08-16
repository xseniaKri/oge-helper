from fastapi import FastAPI
from app.api import ruler

app = FastAPI()

app.include_router(ruler.router, prefix="/api", tags=["rulers"])


