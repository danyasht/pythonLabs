"""
This module is needed for lab №7
"""


class ChainSaw:
    """
    Class which allow us to see the
    behavior of Saw object
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
    ...
    Methods

    -----------------------------------
    def __init__(self, brand, power=0, fuel_tank_capacity=0, fuel_level=0, is_working=False):
        Constructor which initializes object:
        brand, power, fuel_tank_capacity, fuel_level, status of working(working / isn't)

    def cut_wood(self, length):
        cutting a wood with given length
        if fuel level of saw more than needed fuel for cutting, start saw(working == True)
        if fuel level of saw less than needed fuel for cutting, stop saw(working == False)

    def start(self):
        starting saw

    def stop(self):
        stopping saw
    """

    chainsaws = []

    def __init__(self, brand, power=0, fuel_tank_capacity=0, fuel_level=0, is_working=False):
        """
        Constructor which initializes object:
        brand, power, fuel_tank_capacity, fuel_level, status of working(working / isn't)
        """
        self.__brand = brand
        self.__power = power
        self.__fuel_tank_capacity = fuel_tank_capacity
        self.__fuel_level = fuel_level
        self.__is_working = is_working

    def start(self):
        """
        starting saw
        """
        self.__is_working = True

    def stop(self):
        """
        stopping saw
        """
        self.__is_working = False

    def cut_wood(self, length):
        """
        cutting a wood with given length
        if fuel level of saw more than needed fuel for cutting, start saw(working == True)
        if fuel level of saw less than needed fuel for cutting, stop saw(working == False)
        """
        fuel_need_for_cutting = length / 10
        if self.__fuel_level >= fuel_need_for_cutting:
            self.__fuel_level -= fuel_need_for_cutting
            self.__is_working = True
        else:
            self.__is_working = False

    def __str__(self):
        """
        Method which returns line with camera object parameters
        """
        return f"\nBrand: {self.__brand}, power: {self.__power}," \
               f" tank capacity: {self.__fuel_tank_capacity},"\
               f" fuel level after cutting: {self.__fuel_level}," \
               f" working?: {self.__is_working}"

    @staticmethod
    def get_instance():
        if ChainSaw.__instance is None:
            ChainSaw.__instance = ChainSaw()
            return ChainSaw.__instance


chainsaw1 = ChainSaw("Stihl", 2700, 120, 70, True)
chainsaw2 = ChainSaw("Makita", 2500, 100, 80, True)
chainsaw1.cut_wood(450)
chainsaw2.cut_wood(560)

ChainSaw.chainsaws.append(chainsaw1)
ChainSaw.chainsaws.append(chainsaw2)

for saw in ChainSaw.chainsaws:
    print(saw)
