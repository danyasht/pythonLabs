"""
    This module is needed for lab №8
"""
from models.saw import Saw
from exceptions.decorators import logged


class ToySaw(Saw):
    """
        Class which allows us to see 
        behaviour of ToySaw class object
        ...
        Attributes

        -----------------------------------
        brand : str
            brand of the saw
        type_of_engine : str
            engine type of the saw
        power : int
            power of the saw
        fuel_tank_capacity : int
            fuel tank capacity of the saw
        fuel_level : int
            fuel level of the saw
        is_working : bool
            status of the saw
        chain_length : int
            length of the saw's chain
        weight : int
            weight of the saw
        hours_of_work : int
            hours of work for saw
        battery_capacity : int
            capacity of saw's battery
        Methods
        -----------------------------------
            def __init__(self, brand, type_of_engine, power=0, fuel_tank_capacity=0, fuel_level=0,
                 is_working=False, chain_length=0, weight=0, hours_of_work=0, battery_capacity=0):
        super().__init__(brand, power, fuel_tank_capacity, fuel_level,
        is_working, chain_length, weight, hours_of_work)
        self.__type_of_engine = type_of_engine
        self.__battery_capacity = battery_capacity
            Constructor for class

    """

    def __init__(self, brand, type_of_engine, power=0, fuel_tank_capacity=0, fuel_level=0,
                 is_working=False, chain_length=0, weight=0, hours_of_work=0, battery_capacity=0):
        """
            Constructor for class
        """
        super().__init__(brand, power, fuel_tank_capacity, fuel_level,
                         is_working, chain_length, weight, hours_of_work)
        self.type_of_engine = type_of_engine
        self.battery_capacity = battery_capacity
        self.color_of_saw = set()

    @logged(Exception, mode='file')
    def get_remaining_work_time(self):
        """
            Method which calculates remaining work time for saw
        """
        return self.battery_capacity / self.power

    def __str__(self):
        """
            Converting object to string
        """
        return f"Toy saw : brand: {self.brand}, engine type: {self.type_of_engine}, " \
               f"power: {self.power}, " \
               f"fuel tank capacity: {self.fuel_tank_capacity}, fuel level: {self.fuel_level}, " \
               f"working?: {self.is_working}, chain length: {self.chain_length}, " \
               f"weight: {self.weight}, " \
               f"hours of work remaining: {self.hours_of_work}, " \
               f"battery capacity: {self.battery_capacity}."

    def color_of_saw(self):
        """
        Method which returns colors of saw of this class
        """
        return self.color_of_saw
