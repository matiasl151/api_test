from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    first_name: str
    last_name: str
    email: EmailStr