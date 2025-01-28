from typing import Literal
from pydantic import BaseModel, validator

class Category(BaseModel):
    category: str

    ALLOWED_CATEGORIES = {
        "Frágil",
        "Perigoso",
        "Comum"
    }

    @validator("category")
    def validate_category(cls, value) -> Literal["Frágil", "Perigoso", "Comum"]:
        if value not in cls.ALLOWED_CATEGORIES:
            raise ValueError(f"A categoria {value} é inválida!")
        return value