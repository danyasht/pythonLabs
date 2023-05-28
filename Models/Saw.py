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
        self.__brand = brand
        self.__power = power
        self.__fuel_tank_capacity = fuel_tank_capacity
        self.__fuel_level = fuel_level
        self.__is_working = is_working
        self.__chain_length = chain_length
        self.__weight = weight
        self.__hours_of_work = hours_of_work

    @abstractmethod
    def get_remaining_work_time(self):
        """
            Abstract method that should be overrided in other classes and
            allows us to see how much time remaining for saws to stop working.
        """
        pass

    @property
    def get_working(self):
        """
            Getter for is_working
        """
        return self.__is_working

    @property
    def get_brand(self):
        """
            Getter for brand
        """
        return self.__brand

    @property
    def get_power(self):
        """
            Getter for power
        """
        return self.__power

    @property
    def get_capacity(self):
        """
            Getter for fuel_tank_capacity
        """
        return self.__fuel_tank_capacity

    @property
    def get_level(self):
        """
            Getter for fuel_level
        """
        return self.__fuel_level

    @property
    def get_length(self):
        """
            Getter for chain_length
        """
        return self.__chain_length

    @property
    def get_weight(self):
        """
            Getter for weight
        """
        return self.__weight

    @property
    def get_hours(self):
        """
            Getter for hours_of_work
        """
        return self.__hours_of_work
