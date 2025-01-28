from pydantic import BaseModel, Field
from ....shipment_order.domain.entities.shipment_order import Shipment_Order
from ....customer.domain.entities.customer import Customer

from value_objects.category import Category
from value_objects.shipping_method import Shipping_Method

class Package(BaseModel):
    """args: ID, weight, dimension, content, reference_code, shipment_order, category, shipping_method, shipping_cost, customer"""

    id: int = Field(..., gt=0)
    weight: int = Field(..., gt=0, description="Peso do pacote em gramas")
    dimension:int = Field(..., gt=0, description="Dimensão do pacote em centímetros cúbicos")
    content: str
    reference_code: int
    category: Category
    shipping_method: Shipping_Method
    shipping_cost: float
    shipment_order: Shipment_Order
    customer: Customer


