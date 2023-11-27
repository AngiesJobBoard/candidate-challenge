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
