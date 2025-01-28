from pydantic import BaseModel, Field
from ..value_objects import address, status
from customer.domain.entities.customer import Customer

class Shipment_Order(BaseModel):

    """args: ID, address, status, customer"""
    id: int = Field(..., gt=0)
    address: address.Address
    status: status.Status
    customer: Customer

