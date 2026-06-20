from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def info():
    return {"message": "Hello, World! This is from Mood Report.", "version": "1.0"}