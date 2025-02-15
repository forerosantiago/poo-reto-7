"""Reto 7 - Programación orientada a objetos"""

from collections import namedtuple
import random
from queue import Queue

from restaurant import Order, beverages, appetizers, main_courses
import json

# Create 100 random orders and add them into the queue
cola = Queue(maxsize=100)

for i in range(100):
    items = random.choices(
        beverages + appetizers + main_courses, k=random.randint(1, 5)
    )

    number = random.randint(1, 100)
    order = Order(items, number)
    cola.put(order)
    print("\n")

print("Generated 100 random orders")

# ----------------------------------

# Cook and serve the orders in the queue order

while not cola.empty():
    order = cola.get()
    print("Order for table number " + str(order.table_number) + " is ready!")
    order.display_order_details()
    print("\n")

if cola.empty():
    print("All orders have been served!")

print("-----------------------------")
print("\n")
# ----------------------------------


# Tupla con nombre para representar un postre
Postre = namedtuple("Postre", ["nombre", "cantidad_de_azucar", "vegano"])

# Creación de un objeto postre
natilla = Postre("Natilla de coco", "55 gramos", False)

# Acceso a los elementos por nombre
print(f"Nombre del postre: {natilla.nombre}")
print(f"Cantidad de azucar: {natilla.cantidad_de_azucar}")
print(f"Vegano? {natilla.vegano}")


# ----------------------------------

orden = Order((beverages[0], appetizers[0], main_courses[0]), 1)

print(orden.export())

print("Saving the order in a json file...")
with open('order.json', 'w') as json_file:
    json.dump(orden.export(), json_file)

print("Order saved in order.json file")
