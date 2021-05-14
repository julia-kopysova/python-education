from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Tuple, Dict


class Dish:
    """
    Class represents a dish
    Attributes:
        dishes_name_dict: Dict[str, List[str]]: Dictionary where keys - categories,
                                                values - names of dishes
        __name: str: name of dish
        __ingredients: List[str]: ingredients of dish
        __category: str: type of dish
        price: Decimal: dish costs
    Methods:
        filter_by_category(cls, category: str) -> None: filter by category
    """
    dishes_name_dict: Dict[str, List[str]] = {}

    def __init__(self, name: str, category: str, price: Decimal, *ingredients: str):
        """
        Initializes Dish
        :param name:
        :param category:
        :param price:
        :param ingredients:
        """
        self.__name: str = name
        self.__ingredients: List[str] = [ingredient for ingredient in ingredients]
        self.__category: str = category
        self.category = category
        if category not in self.dishes_name_dict:
            self.dishes_name_dict[category] = []
        self.dishes_name_dict[category].append(self.__name)
        self.price: Decimal = price

    def __str__(self):
        """
        String view
        :return: None
        """
        return f"Dish: {self.__category} {self.__name} has ingredients {self.__ingredients}"

    @classmethod
    def filter_by_category(cls, category: str) -> None:
        """
        Method filters dishes by category that received
        :param category: str
        :return: None
        """
        if category in cls.dishes_name_dict.keys():
            print(cls.dishes_name_dict[category])
        else:
            print("Sorry, the category doesn't exist")


class Person(ABC):
    """
    Class for inheritance Persons
    """
    @abstractmethod
    def __init__(self, name: str, surname: str) -> None:
        """
        Initializes Peson
        :param name: str
        :param surname: str
        """
        self._name: str = name
        self._surname: str = surname

    @abstractmethod
    def __str__(self) -> str:
        """
        String view
        :return: str
        """
        ...


class Customer(Person):
    """
    Class represents Customer
    Method:
        set_delivery(self, address: str, phone: str): set info about delivery
    """
    def __init__(self, name: str, surname: str) -> None:
        """
        Initializes Customer
        :param name: str: name of customer
        :param surname: str: surname of customer
        """
        super().__init__(name, surname)

    def __str__(self) -> str:
        """
        String view
        :return:
        """
        return f"Customer: {self._name} {self._surname}"

    def set_delivery(self, address: str, phone: str):
        """
        Customer set a info about delivery
        :param address: str
        :param phone: str
        :return: Delivery
        """
        delivery_object: Delivery = Delivery(self, address, phone)
        return delivery_object


class Waiter(Person):
    """
    Class represents Waiter
    Attributes:
        working_now: bool: if a waiter is working now = True
    """
    def __init__(self, name, surname, working_now):
        """
        Initializes Waiter
        :param name:
        :param surname:
        :param working_now:
        """
        self.working_now = working_now
        super().__init__(name, surname)

    def __str__(self):
        """
        String view
        :return:str
        """
        return f"Waiter: {self._name} {self._surname} \nWorking: {self.working_now}"


class Cook(Person):
    """
    Class represents Cook
    Attribute:
    __position: str: a position of cook
    Method:
        add_dish(self, name: str, category: str, *ingredients: str) -> None
    """
    def __init__(self, name: str, surname: str, position: str):
        """
        Initialize Cook
        :param name:
        :param surname:
        :param position:
        """
        self.__position: str = position
        super().__init__(name, surname)

    def __str__(self):
        """
        String view
        :return: str
        """
        return f"{self.__position}: {self._name} {self._surname}"

    def add_dish(self, name: str, category: str, *ingredients: str) -> None:
        """
        Method allows Chef to add dish to list
        :param name: str
        :param category:  str
        :param ingredients: str
        :return: None
        """
        if self.__position == "Chef":
            new_dish = Dish(name, category, *ingredients)
            print(f"Add new dish:{new_dish}")
        else:
            print("You don't have ability to add dish")


class Delivery:
    """
    Class represents info of Delivery that was chosen to create order
    """
    def __init__(self, customer: Customer, address: str, phone: str):
        """
        Initializes Delivery
        :param customer: Customer
        :param address: str
        :param phone: str
        """
        self.__customer: Customer = customer
        self.__address: str = address
        self.__phone: str = phone

    def __str__(self):
        """
        String view
        :return:
        """
        return f"Delivery to {self.__address} \nPhone number: {self.__phone} \n{self.__customer}"


class PositionInOrder:
    """
    Class represents one position in order
    """
    def __init__(self, dish: Dish, amount: int):
        """
        Initializes PositionInOrder
        :param dish: Dish
        :param amount: int
        """
        self.dish = dish
        self.amount = amount
        self.price = self.dish.price * self.amount

    def __str__(self):
        """
        String view
        :return: str
        """
        return f"{self.dish} * {self.amount} = {self.price}"


class Discount:
    """
    Class represents Discount
    """
    def __init__(self, description: str, percent: float):
        """
        Initializes Discount
        :param description: str
        :param percent: float
        """
        self.__description = description
        self.percent = percent

    def __str__(self):
        """
        String view
        :return: str
        """
        return f"Discount: {self.percent} for {self.__description}"


class Order:
    """
    Class represents Order
    Attributes:
        id_order: int class attribute: increment with creating new order
        __id: identified order
        status: str: status of Order
        __delivery: Delivery
        __cusmoer: Customer
        percent: percent for creation a Discount
        description: for creation a Discount
        __positions_order: Tuple[PositionInOrder]
    Method:
    calculate_total_sum(self) -> Decimal : return a sum of order
    """
    id_order: int = 0

    def __init__(self, customer: Customer, waiter_info,
                 delivery_info: Delivery, *positions_order: PositionInOrder, percent=None, description=None):
        """
        Initializes Order
        :param customer: Customer
        :param waiter_info: Waiter
        :param delivery_info: Delivery
        :param positions_order: Tuple[PositionInOrder]
        :param percent: float
        :param description: str
        """
        self.__id: int = self.id_order
        Order.id_order = Order.id_order + 1
        self.status: str = "In processing"
        self.__delivery: Delivery = delivery_info
        self.__customer: Customer = customer
        self.waiter = waiter_info
        if percent is not None and description is not None:
            self.__discount = Discount(description, percent)
        else:
            self.__discount = None
        self.__positions_order: Tuple[PositionInOrder] = positions_order

    def __str__(self):
        """
        String view
        :return: str
        """
        return f"{self.__id} : {self.status} \n{self.waiter} \n{self.__customer}" \
               f"\n{self.__delivery}"

    def calculate_total_sum(self) -> Decimal:
        """
        Method calculates a total sum of order
        :return: Decimal
        """
        total_sum: Decimal = Decimal(0)
        for position in self.__positions_order:
            total_sum += position.price
        if self.__discount is not None:
            total_sum = total_sum * Decimal(self.__discount.percent) / Decimal(100)
        return total_sum


class Admin(Person):
    """
    This class represent a person who creates orders
    """
    def __init__(self, name: str, surname: str) -> None:
        """
        Initialize Admin
        :param name: str
        :param surname: str
        """
        super().__init__(name, surname)

    def __str__(self) -> str:
        """
        String view
        :return: str
        """
        return f"Admin: {self._name} {self._surname}"

    @staticmethod
    def create_position(dish: Dish, amount: int) -> PositionInOrder:
        """
        Create position for adding to order
        :param dish: Dish
        :param amount: int
        :return: PositionInOrder
        """
        new_position = PositionInOrder(dish, amount)
        return new_position

    @staticmethod
    def create_order(name: str, surname: str, current_delivery: Delivery,
                     *positions: PositionInOrder) -> Order:
        """
        Method creates Order
        :param current_delivery: Delivery
        :param name: str
        :param surname: str
        :param address: str
        :param phone: str
        :param positions: PositionInOrder
        :return: Order
        """
        new_customer = Customer(name, surname)
        new_order = Order(new_customer, None, current_delivery, *positions)
        return new_order

    @staticmethod
    def set_waiter(order: Order, set_waiter: Waiter) -> None:
        """
        Sets a waiter to service Order
        :param order: Order
        :param set_waiter: Waiter
        :return: None
        """
        if set_waiter.working_now:
            order.waiter = set_waiter
            order.status = "Waiter was set"
            print("Waiter was set")
        else:
            print(f"Sorry {set_waiter} doesn't work")

    @staticmethod
    def change_status(order: Order, new_status: str) -> None:
        """
        Change status in process
        :param order: Order
        :param new_status: str
        :return: None
        """
        order.status = new_status


if __name__ == "__main__":
    # Create customers
    customer1 = Customer("Nina", "Simon")
    customer2 = Customer("John", "Lee")
    print(customer1)
    # Create waiters
    waiter = Waiter("Alan", "Smith", True)
    waiter2 = Waiter("Simon", "Smith", False)
    waiter3 = Waiter("Simon", "Smith", True)
    print(waiter)
    # Create delivery
    delivery = Delivery(customer1, "Peace St, 9", "0784567835")
    print(delivery)
    print(customer2.set_delivery("Peace St, 8", "0784567835"))
    # Create dishes
    dish1 = Dish("Pasta", "Main", Decimal(100), "flour", "water")
    dish2 = Dish("Pasta", "Main", Decimal(100), "flour", "water")
    dish3 = Dish("Pasta", "Main", Decimal(100), "flour", "water")
    dish4 = Dish("Cake", "Dessert", Decimal(80), "chocolate", "eggs")
    print(dish1)
    # Create cook and add dishes
    cook1 = Cook("Ector", "Bravo", "Chef")
    cook2 = Cook("Nikolay", "Romanskiy", "Cook")
    cook1.add_dish("Lazania", "Main", "water", "meat")
    cook2.add_dish("Lazania", "Main", "water", "meat")
    print(Dish.dishes_name_dict)
    Dish.filter_by_category("Ma")
    Dish.filter_by_category("Main")
    print("=" * 20)
    # Work with orders
    position_in_order1 = PositionInOrder(dish1, 2)
    position_in_order2 = PositionInOrder(dish2, 3)
    order1 = Order(customer1, waiter, delivery, position_in_order1, position_in_order2)
    order2 = Order(customer1, waiter, delivery, position_in_order1, position_in_order2)
    print(order1)
    print(order2)
    order3 = Admin.create_order("Tom", "Kodd", delivery, Admin.create_position(dish1, 2),
                                Admin.create_position(dish2, 3))
    print(order3)
    Admin.set_waiter(order3, waiter)
    print(order3)
    Admin.set_waiter(order3, waiter2)
    print(order3)
    Admin.set_waiter(order3, waiter3)
    print(order3)
    Admin.change_status(order3, "Accept")
    print(order3)
    print(order1.calculate_total_sum())
    order4 = Order(customer1, waiter, delivery, position_in_order1, position_in_order2,
                   description="For b-day", percent=50.0)
    print(order4)
    print(order4.calculate_total_sum())
