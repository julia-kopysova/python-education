"""
This module organizes a class hierarchy of transport system
"""
from abc import ABC, abstractmethod


class Transport:
    """
    This class is used to represent a transport

    Attributes
    country: str: manufacturer country
    type_engine: TypeTransport: type of Transport
    avg_speed: float: maximum acceleration speed m/sec

    Methods
    __init__(self, type_engine: str, avg_speed: float)
        Initializes Transport
    __str__(self)
        String representation
    driving_time(self, distance: float)
        Calculates the time for which
        the transport can overcome the entered distance
    """
    country: str = "Ukraine"

    def __init__(self, type_engine: str, avg_speed: float) -> None:
        """
        Initializes Transport class with parameters

        Received:
        type_transport: TypeTransport: type of Transport
        avg_speed: float: maximum acceleration speed m/sec
        """
        self.type_engine: str = type_engine
        self.avg_speed: float = avg_speed

    def __str__(self) -> str:
        """
        Returns string representation of info in instance
        """
        return f"Info: {self.type_engine} transport \n" \
               f"Average speed: {self.avg_speed} m/sec"

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
    country: str: manufacturer country
    type_engine: TypeTransport: type of Transport
    avg_speed: float: maximum acceleration speed m/sec
    power: int: horsepower

    Methods
    __init__(self, type_engine: str,
             avg_speed: float, power: int)
        Initializes AutoTransport
    __str__(self)
        String representation
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


class Bus(AutoTransport, Transport):
    """
    This class is used to represent a bus
    inherited from class AutoTransport, Transport

    Attributes
    type_transport: TypeTransport: type of Transport
    avg_speed: float: maximum acceleration speed m/sec
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
    """

    def __init__(self, type_engine: str, avg_speed: float,
                 power: int, passengers: int) -> None:
        """
        Initializes Bus class with parameters

        Received:
        bearing_capacity: float: how many kilograms of cargo can be lifted
        type_transport: TypeTransport: type of Transport
        avg_speed: float: maximum acceleration speed m/sec
        passengers: int: roominess in passengers
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


class Truck(AutoTransport, Transport):
    """
    This class is used to represent a truck
    inherited from class AutoTransport, Transport

    Attributes
    type_transport: TypeTransport: type of Transport
    avg_speed: float: maximum acceleration speed m/sec
    power: int: horsepower
    capacity_body: float: capacity of body

    Methods
    __init__(self, type_engine: str, avg_speed: float,
             power: int, capacity_body: float)
        Initializes Truck
    __str__(self)
        String representation
    """

    def __init__(self, type_engine: str, avg_speed: float,
                 power: int, capacity_body: float):
        """
        Initializes Truck class with parameters

        Received:
        type_transport: TypeTransport: type of Transport
        avg_speed: float: maximum acceleration speed m/sec
        power: int: horsepower
        capacity_body: float: capacity of body
        """
        super().__init__(type_engine, avg_speed, power)
        self.capacity_body = capacity_body

    def __str__(self):
        """
        Returns string representation of info in instance
        """
        return super().__str__() + f"\nCapacity of body: {self.capacity_body} m"


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
    level_comfort: str: price policy
    type_transport: str: type of transportation in
        geographical  consideration: intercity or international
    """

    def __init__(self, level_comfort: str, type_transport: str) -> None:
        """
        Initializes Passenger Transportation class with parameters
        :param level_comfort: str: price policy
        :param type_transport: str: type of transportation in
        """
        self.level_comfort: str = level_comfort
        self.type_transport: str = type_transport

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


class Plane(PassengerTransportation, AirTransport):
    def __init__(self, level_comfort: str, type_transport: str,
                 type_engine: str, avg_speed: float,
                 assignment: str):
        PassengerTransportation.__init__(self, level_comfort, type_transport)
        AirTransport.__init__(self, type_engine, avg_speed, assignment)

    def movement(self) -> None:
        print("Fly")

    def capability(self) -> None:
        super(Plane, self).capability()


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
    print(f"Time {'%.2f' % auto_transport.driving_time(1500)} sec "
          f"with average speed {auto_transport.avg_speed}")

    # Test Bus
    print('=' * 19)
    bus_transport = Bus("Electric", 70.90, 100, 109)
    print(bus_transport)
    print(f"Time {'%.2f' % bus_transport.driving_time(1500)} sec "
          f"with average speed {bus_transport.avg_speed}")

    # Test Truck
    print('=' * 19)
    truck_transport = Truck("Electric", 70.70, 100, 600)
    print(truck_transport)
    print(f"Time {'%.2f' % truck_transport.driving_time(1500)} sec "
          f"with average speed {truck_transport.avg_speed}")

    # Test Air Transport
    print('=' * 19)
    air_transport = AirTransport("Electric", 100, "Military")
    print(air_transport)
    print(f"Time {'%.2f' % truck_transport.driving_time(1500)} sec "
          f"with average speed {truck_transport.avg_speed}")

    # Test Plane
    print('=' * 19)
    plane_transport = Plane("VIP", "International", "Fuel", 1000.0, "Passenger")
    print(plane_transport)
    plane_transport.movement()
    plane_transport.capability()
