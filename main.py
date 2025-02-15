"""Reto 7 - Programación orientada a objetos"""

import random
from queue import Queue
from tabulate import tabulate

class MenuItem:
    """Class that represents a menu item"""
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_details(self):
        """Prints a table with the item details"""
        table = tabulate(
            [
                ["name", "description", "price"],
                [self.name, self.description, str(self.price) + "$"],
            ],
            headers="firstrow",
        )
        print(table)


class Beverage(MenuItem):
    """Class that represents a beverage menu item"""
    def __init__(
        self, name, description, price, volume, is_cold, is_milk_free, is_alcoholic
    ):
        super().__init__(name, description, price)
        self.volume = volume
        self.is_cold = is_cold
        self.is_milk_free = is_milk_free
        self.is_alcoholic = is_alcoholic

    def display_details(self):
        table = tabulate(
            [
                [
                    "name",
                    "description",
                    "price",
                    "volume",
                    "is_cold",
                    "is_milk_free",
                    "is_alcoholic",
                ],
                [
                    self.name,
                    self.description,
                    str(self.price) + "$",
                    str(self.volume) + "ml",
                    self.is_cold,
                    self.is_milk_free,
                    self.is_alcoholic,
                ],
            ],
            headers="firstrow",
        )
        print(table)


class Appetizer(MenuItem):
    """Class that represents an appetizer menu item"""
    def __init__(
        self, name, description, price, is_vegetarian, is_gluten_free, recommended_dip
    ):
        super().__init__(name, description, price)
        self.is_vegetarian = is_vegetarian
        self.is_gluten_free = is_gluten_free
        self.recommended_dip = recommended_dip

    def display_details(self):
        table = tabulate(
            [
                [
                    "name",
                    "description",
                    "price",
                    "is_vegetarian",
                    "is_gluten_free",
                    "recommended_dip",
                ],
                [
                    self.name,
                    self.description,
                    str(self.price) + "$",
                    self.is_vegetarian,
                    self.is_gluten_free,
                    self.recommended_dip,
                ],
            ],
            headers="firstrow",
        )
        print(table)


class MainCourse(MenuItem):
    """Class that represents a main course menu item"""
    def __init__(self, name, description, price, is_vegetarian, is_vegan, calories):
        super().__init__(name, description, price)
        self.is_vegetarian = is_vegetarian
        self.is_vegan = is_vegan
        self.calories = calories

    def display_details(self):
        table = tabulate(
            [
                ["name", "description", "price", "is_vegetarian", "is_vegan", "calories"],
                [
                    self.name,
                    self.description,
                    str(self.price) + "$",
                    self.is_vegetarian,
                    self.is_vegan,
                    self.calories,
                ],
            ],
            headers="firstrow",
        )
        print(table)


class Order:
    """Class that represents an order"""
    def __init__(self, menu_items, table_number):
        self.menu_items = menu_items
        self.table_number = table_number

    def add_items(self, menu_items):
        """Add menu items to the order"""
        self.menu_items.extend(menu_items)

    def remove_items(self, menu_items):
        """Remove menu items from the order"""
        for item in menu_items:
            self.menu_items.remove_items_items_items_items_items_items_items_items_items(item)

    def calculate_bill(self):
        """Calculate the total bill of the order"""
        total = 0
        for item in self.menu_items:
            total += item.price
        return total

    def display_order_details(self):
        """Display the details of the order"""
        print("Table Number: " + str(self.table_number))
        table = []
        for item in self.menu_items:
            table.append([item.name, str(item.price) + "$"])
        print(tabulate(table, headers=["Item", "Price"]))

        print("Total: " + str(self.calculate_bill()) + "$")


# Create objects of MenuItem, Beverage, Appetizer, MainCourse

cocaCola = Beverage("Coca Cola", "Refreshing drink", 2.5, 500, True, True, False)
beer = Beverage("Beer", "Alcoholic drink", 5, 500, True, True, True)
orangeJuice = Beverage("Orange Juice", "Fresh orange juice", 3, 300, True, True, False)
chicha = Beverage("Chicha", "Traditional Colombian drink", 2, 300, True, True, False)

beverages = [cocaCola, beer, orangeJuice, chicha]

nachos = Appetizer("Nachos", "Crispy chips with cheese", 6, True, False, "Cheddar")
onionRings = Appetizer("Onion Rings", "Fried onion rings", 5, True, True, "Ketchup")
frenchFries = Appetizer("French Fries", "Crispy fries", 4, True, True, "Mayonnaise")
patacones = Appetizer("Patacones", "Fried plantain", 4, True, True, "Guacamole")

appetizers = [nachos, onionRings, frenchFries, patacones]

beefSteak = MainCourse("Beef Steak", "Grilled beef steak", 15, False, False, 500)
pasta = MainCourse("Pasta", "Spaghetti with tomato sauce", 10, True, True, 300)
bandejaPaisa = MainCourse(
    "Bandeja Paisa", "Traditional Colombian dish", 12, False, False, 700
)
cuchuco = MainCourse("Cuchuco", "Traditional Colombian soup", 10, True, True, 500)

main_courses = [beefSteak, pasta, bandejaPaisa, cuchuco]

# ----------------------------------

# Create 100 random orders and add them into the queue

cola = Queue(maxsize=100)

for i in range(100):
    menu_items = random.choices(beverages + appetizers + main_courses, k=random.randint(1, 5))
    
    table_number = random.randint(1, 100)
    order = Order(menu_items, table_number)
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