"""
    This module is needed for lab №8
"""
from abc import ABC, abstractmethod


class Saw(ABC):
    """
    Abstract class which allow us to see the
    behavior of Saw object.
    ...
    Attributes

    -----------------------------------
    brand : str
        brand of the saw
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
    ...
    Methods

    -----------------------------------
    def __init__(self, brand, power=0, fuel_tank_capacity=0, fuel_level=0,
                 is_working=False, chain_length=0, weight=0, hours_of_work=0):
        Constructor which initializes object:
        brand, power, fuel tank capacity, fuel level, status of working(working / isn't),
        length of chain, weight, work hours.
    def get_remaining_work_time(self):
        pass
            Abstract method that should be overrided in other classes and
            allows us to see how much time remaining for saws to stop working.
    """

    def __init__(self, brand, power=0, fuel_tank_capacity=0, fuel_level=0,
                 is_working=False, chain_length=0, weight=0, hours_of_work=0):
        """
        Constructor which initializes object:
        :param brand: str
        :param power: int
        :param fuel_tank_capacity: int
        :param fuel_level: int
        :param is_working: bool
        :param chain_length: int
        :param weight: int
        :param hours_of_work: int
        """
        self.brand = brand
        self.power = power
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_level
        self.is_working = is_working
        self.chain_length = chain_length
        self.weight = weight
        self.hours_of_work = hours_of_work
        self.color_of_saw = set()

    @abstractmethod
    def get_remaining_work_time(self):
        """
            Abstract method that should be overrided in other classes and
            allows us to see how much time remaining for saws to stop working.
        """
        pass

    def get_attributes_of_class(self, data_type):
        """
        Method which searches attribute of class by data type
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def color_of_saw(self):
        """
        Method which should be overrided in other classes
        """
        pass

    def __iter__(self):
        pass

