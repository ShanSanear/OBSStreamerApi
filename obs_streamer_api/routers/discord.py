from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/discord'
)


class DiscordModel(BaseModel):
    message: str


@router.post("/")
def root():
    return DiscordModel(
        message="Hello world!"
    )