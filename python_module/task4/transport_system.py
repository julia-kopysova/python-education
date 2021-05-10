"""
This module organizes a class hierarchy of transport system
"""
from abc import ABC, abstractmethod


class Engine:
    """
    Class for inheritance to Transport
    Attributes:
         type_engine: str: type of engine
    Methods:
        print_message: None
    """

    def __init__(self, type_engine: str) -> None:
        """
        Initializes Engine
        :param type_engine: str
        """
        self.type_engine = type_engine

    def print_message(self) -> None:
        """
        Prints info
        :return: None
        """
        print(f"Has {self.type_engine} engine")


class Transport(Engine):
    """
    This class is used to represent a Transport
    Attributes
        country: str: manufacturer country
        avg_speed: float: maximum acceleration speed m/sec
    Methods
        __init__(self, type_engine: str, avg_speed: float)
        Initializes Transport
        __str__(self)
        String representation
        driving_time(self, distance: float)
        Calculates the time for which
        the transport can overcome the entered distance
        print_message(self): None
    """
    country: str = "Ukraine"

    @classmethod
    def print_country(cls):
        """
        Prints country
        :return: None
        """
        if cls.country == "Ukraine":
            print("Made in our country")

    def __init__(self, type_engine: str, avg_speed: float) -> None:
        """
        Initializes Transport class
        :param type_engine:
        :param avg_speed:
        """
        super().__init__(type_engine)
        self.avg_speed: float = avg_speed

    def __str__(self) -> str:
        """
        Returns string representation of info in instance
        """
        return f"Info: {self.type_engine} transport \n" \
               f"Average speed: {self.avg_speed} m/sec"

    def print_message(self) -> None:
        """
        Prints info
        :return: None
        """
        print(f"Has {self.avg_speed} m/sec transport")
        super().print_message()

    def driving_time(self, distance: float) -> float:
        """
        This method calculates the time for which
        the transport can overcome the entered distance

        Received:
        distance: float: number of kilometers (m)

        Returns:
        float: time (sec) - distance divided by max speed
        """
        return distance / self.avg_speed


class AutoTransport(Transport):
    """
    This class is used to represent a Auto transport
    Attributes
    power: int: horsepower
    Methods
    __init__(self, type_engine: str,
             avg_speed: float, power: int)
        Initializes AutoTransport
    __str__(self)
        String representation
    print_message(self) -> None
    """

    def __init__(self, type_engine: str,
                 avg_speed: float, power: int) -> None:
        """
        Initializes class AutoTransport class
        inherited from class Transport
        Received:
        bearing_capacity: float: how many kilograms of cargo can be lifted
        type_transport: TypeTransport: type of Transport
        avg_speed: float: maximum acceleration speed m/sec
        power: int: horsepower
        """
        self.power = power
        super().__init__(type_engine, avg_speed)

    def __str__(self):
        """
        Returns string representation of info in instance
        """
        return super().__str__() + f"\nHorsepower: {self.power} "

    def __lt__(self, other):
        """
        Defines behavior for the less-than operator, <
        :param other:
        :return: bool
        """
        return self.avg_speed < other.avg_speed

    def __gt__(self, other):
        """
        Defines behavior for the greater-than operator, >
        :param other:
        :return: bool
        """
        return self.power > other.power

    def __eq__(self, other):
        """
        Defines behavior for the equality operator, ==
        :param other:
        :return:
        """
        return self.type_engine == other.type_engine and self.power == other.power and self.avg_speed == other.avg_speed

    def __neg__(self):
        """
        Do nothing if operation -
        :return: self
        """
        return self

    def __round__(self, n=None):
        """
        Implements behavior for the built in round() function
        :param n: the number of decimal places to round to
        :return:
        """
        self.avg_speed = round(self.avg_speed, 2)
        return self

    @property
    def characteristic(self) -> str:
        """
        Combining two attributes
        :return: str
        """
        return f"{self.avg_speed}  {self.power}"

    def print_message(self) -> None:
        """
        Prints info
        :return: None
        """
        super().print_message()
        print(f"Has auto transport {self.power}")


class TransportableTransport(Transport):
    """
    Class for Transportable Transport
    """

    def __init__(self, type_engine: str, avg_speed: float):
        """
        Initializes Transportable Transport
        :param type_engine:
        :param avg_speed:
        """
        super().__init__(type_engine, avg_speed)

    def print_message(self) -> None:
        """
        Prints info
        :return: None
        """
        print(f"Has transportable transport")
        super().print_message()


class Bus(AutoTransport):
    """
    This class is used to represent a bus
    inherited from class AutoTransport, Transport
    Attributes
    passengers: int: roominess in passengers
    Methods
    __init__(self, type_engine: str, power: int,
            avg_speed: float, passengers: int)
        Initializes Bus
    __str__(self)
        String representation
    driving_time(self, distance: float)
        Calculates the time for which
        the transport can overcome the entered distance
    print_message(self): None
    """

    def __init__(self, type_engine: str, avg_speed: float,
                 power: int, passengers: int) -> None:
        """
        Initializes Bus
        :param type_engine:
        :param avg_speed:
        :param power:
        :param passengers:
        """
        super().__init__(type_engine, avg_speed, power)
        self.passengers = passengers

    def __str__(self) -> str:
        """
        Returns string representation of info in instance
        """
        return super().__str__() + f"\nAmount of passengers: {self.passengers}"

    def driving_time(self, distance: float) -> float:
        """
        This method calculates the time for which
        the bus can overcome the entered distance
        including time that will be spend in stations

        Received:
        distance: float: number of kilometers (m)

        Returns:
        float: time (sec) - distance divided by avg speed
                            with coefficient
        """
        return distance / self.avg_speed * 0.9


class Truck(AutoTransport, TransportableTransport):
    """
    This class is used to represent a truck
    inherited from class AutoTransport, TransportableTransport

    Attributes
    type_transport: TypeTransport: type of Transport
    avg_speed: float: maximum acceleration speed m/sec
    power: int: horsepower


    Methods
    __init__(self, type_engine: str, avg_speed: float,
             power: int, capacity_body: float)
        Initializes Truck
    print_message(self): None
    """

    @staticmethod
    def calculate_dimensions(length: float, width: float, height: float) -> float:
        """
        Static method for calculation
        :param length:
        :param width:
        :param height:
        :return: float
        """
        return length * width * height

    def __init__(self, type_engine: str, avg_speed: float, power: int):
        """
        Initializes Truck
        :param type_engine:
        :param avg_speed:
        :param power:
        """
        super().__init__(type_engine, avg_speed, power)

    def print_message(self) -> None:
        super().print_message()


class AirTransport(Transport):
    """
    This class is used to represent an Air Transport
    inherited from class Transport

    Attributes
    type_transport: TypeTransport: type of Transport
    avg_speed: float: maximum acceleration speed m/sec
    assignment: str: in which area is it used

    Methods
    __init__(self, type_engine: str, avg_speed: float,
            assignment: str)
        Initializes Air Transport
    __str__(self)
        String representation
    """

    def __init__(self, type_engine: str, avg_speed: float,
                 assignment: str):
        """
        Initializes Air Transport class with parameters

        Received:
        type_transport: TypeTransport: type of Transport
        avg_speed: float: maximum acceleration speed m/sec
        assignment: str: in which area is it used
        """
        super().__init__(type_engine, avg_speed)
        self.assignment = assignment

    def __str__(self):
        """
        Returns string representation of info in instance
        """
        return super().__str__() + f"\nAssignment:{self.assignment}"


class PassengerTransportation(ABC):
    """
    This class is used to represent an Passenger function
    of transport
    """

    @abstractmethod
    def movement(self):
        """
        Displays type of movement
        :return: None
        """

    @abstractmethod
    def capability(self):
        """
        Displays advantages and capabilities
        :return: None
        """
        print("Designed for passenger transportation")


class Plane(AirTransport, PassengerTransportation):
    """
    Class Plane for realization abstract class
    """

    def __init__(self, type_engine: str, avg_speed: float, assignment: str):
        """
        Initializes Plane
        :param type_engine:
        :param avg_speed:
        :param assignment:
        """
        super().__init__(type_engine, avg_speed, assignment)

    def movement(self) -> None:
        """
        Prints movement
        :return: None
        """
        print("Fly")

    def capability(self) -> None:
        """
        Prints capability
        :return: None
        """
        super().capability()


if __name__ == "__main__":
    # Test Transport
    print('=' * 19)
    my_transport = Transport("Electric", 70.90)
    print(f"Time {'%.4f' % my_transport.driving_time(1500)} sec "
          f"with average speed {my_transport.avg_speed}")

    # Test AutoTransport
    print('=' * 19)
    auto_transport = AutoTransport("Electric", 70.90, 100)
    print(auto_transport)
    print(auto_transport.characteristic)
    print(f"Time {'%.2f' % auto_transport.driving_time(1500)} sec "
          f"with average speed {auto_transport.avg_speed}")

    # Test Bus
    print('=' * 19)
    bus_transport = Bus("Electric", 70.90, 100, 109)
    print(bus_transport)
    print(f"Time {'%.2f' % bus_transport.driving_time(1500)} sec "
          f"with average speed {bus_transport.avg_speed}")

    # Test Air Transport
    print('=' * 19)
    air_transport = AirTransport("Electric", 100, "Military")
    print(air_transport)
    print(f"Time {'%.2f' % air_transport.driving_time(1500)} sec "
          f"with average speed {air_transport.avg_speed}")

    # Test Plane
    print('=' * 19)
    plane_transport = Plane("Electric", 100.0, "Passenger")
    print(plane_transport)
    plane_transport.movement()
    plane_transport.capability()
    # Truck Test
    truck = Truck("Electric", 100.0, 150)
    truck.print_message()
    # Class method
    Transport.print_country()
    # Static method
    print(Truck.calculate_dimensions(10.0, 33.0, 60.5))
    # __lt__
    auto_transport_1 = AutoTransport("Electric", 1000, 1)
    print(auto_transport < auto_transport_1)
    # __gt__
    print(auto_transport > auto_transport_1)
    # __eq__
    print(auto_transport == auto_transport_1)
    auto_transport_2 = AutoTransport("Electric", 1000, 1)
    print(auto_transport_2 == auto_transport_1)
    # __neg__
    print(-auto_transport)
    # __round__
    auto_transport_4 = AutoTransport("Electric", 1000.97483975, 1)
    print(round(auto_transport_4))

