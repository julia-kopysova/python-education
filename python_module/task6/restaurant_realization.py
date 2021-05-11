from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Tuple


class Dish:
    dishes_name_list: List[str] = []

    def __init__(self, name: str, available: bool, category: str, price: Decimal, *ingredients: str):
        self.__name: str = name
        self.__available: bool = available
        self.__ingredients: List[str] = [ingredient for ingredient in ingredients]
        self.__category: str = category
        self.price: Decimal = price
        self.dishes_name_list.append(self.__name)

    def __str__(self):
        return f"Dish: {self.__category} {self.__name} {self.__available} has ingredients {self.__ingredients}"


class Person(ABC):
    @abstractmethod
    def __init__(self, name: str, surname: str) -> None:
        self._name: str = name
        self._surname: str = surname

    @abstractmethod
    def __str__(self) -> str:
        ...


class Customer(Person):
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f"Customer: {self._name} {self._surname}"

    def set_delivery(self, address: str, phone: str):
        delivery_object: Delivery = Delivery(self, address, phone)
        return delivery_object


class Waiter(Person):
    def __init__(self, name, surname, working_now):
        self.working_now = working_now
        super().__init__(name, surname)

    def __str__(self):
        return f"Waiter: {self._name} {self._surname} \nWorking: {self.working_now}"


class Cook(Person):
    def __init__(self, name: str, surname: str, position: str):
        self.__position: str = position
        super().__init__(name, surname)

    def __str__(self):
        return f"{self.__position}: {self._name} {self._surname}"

    def add_dish(self, name: str, available: bool, category: str, *ingredients: str) -> None:
        if self.__position == "Chef":
            new_dish = Dish(name, available, category, *ingredients)
            print(f"Add new dish:{new_dish}")
        else:
            print("You don't have ability to add dish")


class Delivery:
    def __init__(self, customer: Customer, address: str, phone: str):
        self.__customer: Customer = customer
        self.__address: str = address
        self.__phone: str = phone

    def __str__(self):
        return f"Delivery to {self.__address} \nPhone number: {self.__phone} \n{self.__customer}"


class PositionInOrder:
    def __init__(self, dish: Dish, amount: int):
        self.dish = dish
        self.amount = amount
        self.price = self.dish.price * self.amount

    def __str__(self):
        return f"{self.dish} * {self.amount} = {self.price}"


class Order:
    id_order: int = 0

    def __init__(self, customer: Customer, waiter_info: Waiter,
                 delivery_info: Delivery, *positions_order: PositionInOrder):
        self.id: int = self.id_order
        Order.id_order = Order.id_order + 1
        self.status: str = "In processing"
        self.delivery: Delivery = delivery_info
        self.customer: Customer = customer
        self.waiter: Waiter = waiter_info
        self.positions_order: Tuple[PositionInOrder] = positions_order

    def __str__(self):
        return f"{self.id} : {self.status} \n{self.waiter} \n{self.customer}" \
               f"\n{self.delivery}"


class Admin(Person):
    """
    This class represent a person who creates orders
    """
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f"Admin: {self._name} {self._surname}"

    @staticmethod
    def create_position(dish: Dish, amount: int):
        new_position = PositionInOrder(dish, amount)
        return new_position

    @staticmethod
    def create_order(name: str, surname: str, address: str, phone: str,
                     *positions: PositionInOrder) -> Order:
        new_customer = Customer(name, surname)
        new_delivery = Delivery(new_customer, address, phone)
        new_order = Order(new_customer, None, new_delivery, *positions)
        return new_order


customer1 = Customer("Nina", "Simon")
customer2 = Customer("John", "Lee")
print(customer1)
waiter = Waiter("Alan", "Smith", True)
print(waiter)
delivery = Delivery(customer1, "Peace St, 9", "0784567835")
print(delivery)
print(customer2.set_delivery("Peace St, 8", "0784567835"))
dish1 = Dish("Pasta", True, "Main", Decimal(100), "flour", "water")
dish2 = Dish("Pasta", True, "Main", Decimal(100), "flour", "water")
dish3 = Dish("Pasta", True, "Main", Decimal(100), "flour", "water")
print(dish1)
cook1 = Cook("Ector", "Bravo", "Chef")
cook2 = Cook("Nikolay", "Romanskiy", "Cook")
cook1.add_dish("Lazania", True, "Main", "water", "meat")
cook2.add_dish("Lazania", True, "Main", "water", "meat")
print(Dish.dishes_name_list)
print("=" * 20)
position_in_order1 = PositionInOrder(dish1, 2)
position_in_order2 = PositionInOrder(dish2, 3)
order1 = Order(customer1, waiter, delivery, position_in_order1, position_in_order2)
order2 = Order(customer1, waiter, delivery, position_in_order1, position_in_order2)
print(order1)
print(order2)
print(Admin.create_order("Tom", "Kodd", "Polize St,7", "0996784566", Admin.create_position(dish1, 2),
                         Admin.create_position(dish2, 3)))
