from pydantic import BaseModel

class Permission(BaseModel):
    id: int
    group_name: str
    group_description: str