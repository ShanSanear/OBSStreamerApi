from datetime import datetime
from typing import Any

from pydantic import BaseModel


class OBSState(BaseModel):
    pid: int
    name: str


class ProcessKilled(BaseModel):
    pid: int
    name: str
    date: datetime


class OBSResult(BaseModel):
    message: str
    result: Any