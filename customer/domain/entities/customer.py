from pydantic import BaseModel, Field
from ..value_objects.email import Email

class Customer(BaseModel):
    """args: ID, name, email"""
    id: int = Field(..., gt=0)
    name: str
    email: Email