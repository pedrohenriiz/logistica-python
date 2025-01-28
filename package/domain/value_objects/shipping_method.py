from typing import Literal
from pydantic import BaseModel, validator

class Shipping_Method(BaseModel):
    shipping_method: str

    ALLOWED_SHIPPING_METHODS = {
        "Normal",
        "Expresso"
    }

    @validator("shipping_method")
    def validate_shipping_method(cls, value) -> Literal["Normal", "Expresso"]:
        if value not in cls.ALLOWED_SHIPPING_METHODS:
            raise ValueError(f"O método de envio {value} é inválido!")
        return value
