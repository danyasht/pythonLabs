class Chainsaw():

    chainsaws = []

    def __init__(self, brand, power=0, fuel_tank_capacity=0, fuel_level=0, is_working=False):
        """
        Конструктор, який ініціалізує кожну з бензопил:
        назва, потужність, ємність бака, рівень палива, стан роботи(працює/не працює)
        """
        self.__brand = brand
        self.__power = power
        self.__fuel_tank_capacity = fuel_tank_capacity
        self.__fuel_level = fuel_level
        self.__is_working = is_working

    @property
    def chainsaw_brand(self):
        return self.__brand

    @property
    def chainsaw_power(self):
        return self.__power

    @property
    def chainsaw_fuel_tank_capacity(self):
        return self.__fuel_tank_capacity

    @property
    def chainsaw_fuel_level(self):
        return self.__fuel_level
    
    @property
    def chainsaw_is_working(self):
         return self.__is_working

    @chainsaw_brand.setter
    def chainsaw_brand(self, oth_brand):
        self.__brand = oth_brand

    @chainsaw_power.setter
    def chair_owner(self, oth_power):
        self.__power = oth_power

    @chainsaw_fuel_tank_capacity.setter
    def chainsaw_fuel_tank_capacity(self, oth_capacity):
        self.__fuel_tank_capacity = oth_capacity

    @chainsaw_fuel_level.setter
    def chainsaw_fuel_level(self, oth_level):
        self.__fuel_level = oth_level

    @chainsaw_is_working.setter
    def chainsaw_is_working(self, oth_working):
         self.is_working = oth_working

    def start(self):
        self.__is_working = True

    def stop(self):
        self.__is_working = False

    def cut_wood(self, length):
        fuel_need_for_cutting = length / 10
        if self.__fuel_level >= fuel_need_for_cutting:
                self.__fuel_level -= fuel_need_for_cutting
                self.__is_working = True
        else:
                self.__is_working = False

    def __str__(self):
         return f"\nBrand: {self.__brand}, power: {self.__power}, tank capacity: {self.__fuel_tank_capacity}, fuel level after cutting: {self.__fuel_level}, working?: {self.__is_working}"

chainsaw1 = Chainsaw("Stihl", 2700, 120, 70, True)
chainsaw2 = Chainsaw("Makita", 2500, 100, 80, True)
chainsaw1.cut_wood(450)
chainsaw2.cut_wood(560)

Chainsaw.chainsaws.append(chainsaw1)  
Chainsaw.chainsaws.append(chainsaw2)

for saw in Chainsaw.chainsaws:
    print(saw)