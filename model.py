from enum import Enum
from sqlmodel import SQLModel, Field


class NovelStatus(Enum):
    NO_BUY = 0
    NO_READ = 1
    READING = 2
    FINISHED = 3


class NovelNationality(Enum):
    WESTERN = 0
    JAPANESE = 1
    CHINESE = 2


class Novel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    author: str = Field(index=True)
    nationality: NovelNationality = Field(index=True)
    status: NovelStatus = Field(default=NovelStatus.NO_BUY, index=True)
    read_time: int = Field(default=0, index=True)
