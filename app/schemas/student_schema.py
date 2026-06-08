from pydantic import BaseModel, Field
from pydantic import ConfigDict


class StudentCreate(BaseModel):
    name: str
    branch: str
    marks: int | None = None


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3)
    branch: str | None = Field(default=None, min_length=2)
    marks: int | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    branch: str
    marks: int | None = None

    model_config = ConfigDict(from_attributes=True)
