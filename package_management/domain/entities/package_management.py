from pydantic import BaseModel, Field
from ..value_objects import status

class Package_Management(BaseModel):

    """args: ID, status, checkpoint"""
    id: int = Field(..., gt=0)
    status: status.Status
    checkpoint: str