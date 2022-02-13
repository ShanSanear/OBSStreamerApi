from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/storage'
)


class StorageModel(BaseModel):
    message: str


@router.post("/")
def root():
    return StorageModel(
        message="Hello world!"
    )