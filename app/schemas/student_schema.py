from pydantic import BaseModel
from pydantic import ConfigDict


class StudentCreate(BaseModel):
    name: str
    branch: str
    marks: int | None = None


class StudentUpdate(BaseModel):
    branch: str
    marks: int | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    branch: str
    marks: int | None = None

    model_config = ConfigDict(from_attributes=True)
