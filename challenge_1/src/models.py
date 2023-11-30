from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    is_cool: bool = True


class Occupation(BaseModel):
    title: str
    salary: int


class UserWithOccupation(User):
    occupation: Occupation


class ExampleArticle(BaseModel):
    author: str
    title: str
    type: str
    url: str
    children: list
    created_at: datetime
    id: int
    parent_id: int | None
    points: int
