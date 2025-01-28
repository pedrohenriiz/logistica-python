from pydantic import BaseModel, Field
from ..value_objects import address, status

class Shipment_Order(BaseModel):

    """args: ID, weight, dimension, address, status"""
    id: int = Field(..., gt=0)
    weight: int = Field(..., gt=0, description="Peso do pacote em gramas")
    dimension: int = Field(..., gt=0, description="Dimensão do pacote em centímetros cúbicos")
    address: address.Address
    status: status.Status
