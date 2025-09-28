from pydantic import BaseModel
from dataclasses import dataclass


class Task(BaseModel):
    title : str
    description : str
    status : str

class TaskWithID(Task):
    id : int


class UpdateTask(BaseModel):
    title : str | None = None
    description : str | None = None
    status : str | None = None


