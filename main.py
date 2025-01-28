from customer.domain.entities.customer import Customer
from customer.domain.value_objects.email import Email

customer = Customer(id=1, name="Pedro Henrique", email=Email(email="jose@gmail.com"))

print("Cliente cadastradoss")
print(customer)