from pydantic import BaseModel
from typing import Optional
from pydantic.errors import IntegerError

class User(BaseModel):
    id: Optional[int] #Cambio
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    id: Optional[int]    #Cambio
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

