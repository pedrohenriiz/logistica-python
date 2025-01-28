from pydantic import BaseModel, Field
from ....shipment_order.domain.entities.shipment_order import Shipment_Order
from ..value_objects.status import Status
from datetime import datetime

class Tracking(BaseModel):
    """args: ID, shipment_order_id, status, updated_at"""

    id: int= Field(..., gt=0)
    shipment_order: Shipment_Order
    status: Status
    updated_at: datetime
