from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class OBSState(BaseModel):
    pid: Optional[int]
    name: Optional[str]


class ProcessKilled(BaseModel):
    pid: int
    name: str
    date: datetime


class OBSResult(BaseModel):
    message: str
    result: Any