from fastapi import FastAPI
from routes import other

app = FastAPI()

app.include_router(other.router)