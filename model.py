from enum import Enum
from sqlmodel import SQLModel, Field


class NovelStatus(Enum):
    NO_BUY = 0
    NO_READ = 1
    READING = 2
    FINISHED = 3


class Novel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    author: str
    nationality: str
    status: NovelStatus = Field(default=NovelStatus.NO_BUY)
    read_time: int = Field(default=-1)
