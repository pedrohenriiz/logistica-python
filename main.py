from customer.domain.entities.customer import Customer
from customer.domain.value_objects.email import Email

from shipment_order.domain.entities.shipment_order import Shipment_Order
from shipment_order.domain.value_objects.address import Address
from shipment_order.domain.value_objects.status import Status

customer = Customer(id=1, name="Pedro Henrique", email=Email(email="jose@gmail.com"))

print("Cliente cadastrado")
print(customer)

shipment_order = Shipment_Order(id = 1, weight=900, dimension = 3, address=Address(street="Rua dos Bobos", number=123, city="Avaré", state="SP", zip_code="18000000", country="Brasil"), status=Status(status="Criado"), customer=customer)

print(shipment_order)