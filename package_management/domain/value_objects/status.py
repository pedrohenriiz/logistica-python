from typing import Literal
from pydantic import BaseModel, validator

class Status(BaseModel):
    status: str

    ALLOWED_VALUES = {
        "Em trânsito",
        "Entregue",
        "Aguardando retirada"
    }

    @validator("status")
    def validate_status(cls, value) -> Literal["Em trânsito","Entregue","Aguardando retirada"]:
        if value not in cls.ALLOWED_VALUES:
            raise ValueError(f"O status {value} é inválido")
        
        return value
