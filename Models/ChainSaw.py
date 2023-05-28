"""
    This module is needed for lab №8
"""
from Models.Saw import Saw


class ChainSaw(Saw):
    """
        Class which allows us to see
        behaviour of ChainSaw class object
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
        self.__type_of_engine = type_of_engine
        self.__battery_capacity = battery_capacity

    def get_remaining_work_time(self):
        """
            Method which calculates remaining work time for saw
        """
        return self.__battery_capacity / self.get_power

    @property
    def get_engine(self):
        """
            Getter for engine_type
        """
        return self.__type_of_engine

    def __str__(self):
        """
            Converting object to string
        """
        return f"Chainsaw : brand: {self.get_brand}, engine type: {self.get_engine}, " \
               f"power: {self.get_power}, " \
               f"fuel tank capacity: {self.get_capacity}, fuel level: {self.get_level}, " \
               f"working?: {self.get_working}, chain length: {self.get_length}, " \
               f"weight: {self.get_weight}, " \
               f"hours of work remaining: {self.get_hours}, " \
               f"battery capacity: {self.__battery_capacity}."