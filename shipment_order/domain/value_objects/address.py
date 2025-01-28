from pydantic import BaseModel, validator

class Address(BaseModel):

    street: str
    city: str
    state: str
    zip_code: str
    country: str

    @validator('street')
    def validate_address(cls, value):
        if not value.strip():
            raise ValueError("O campo street não pode ser vazio!")
        return value
    
    @validator('city')
    def validate_city(cls, value):
        if not value.strip():
            raise ValueError("O campo city não pode ser vazio!")
        return value
    
    @validator('state')
    def validate_state(cls, value):
        if not value.strip():
            raise ValueError("O campo state não pode ser vazio!")
        if len(value) != 2:
            raise ValueError("O campo state pode receber somente 2 dígitos!")
        return value.upper()
    
    @validator("country")
    def validate_country(cls, value):
        if not value.strip():
            raise ValueError("O campo country não pode ser vazio!")
        return value