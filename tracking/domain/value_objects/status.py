from typing import Literal
from pydantic import BaseModel, validator

class Status(BaseModel):
    status: str

    ALLOWED_VALUES = {
        "Criado",
        "Em trânsito",
        "Entregue"    
    }

    @validator(status)
    def validate_status(cls, value) -> Literal["Criado", "Em trânsito", "Entregue"]:
        """Validate if the status is allowed"""
        if value not in cls.ALLOWED_VALUES:
            raise ValueError(f"O status {value} é inválido")
        
        return value
