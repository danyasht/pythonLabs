"""
    This module is needed for lab №9
"""
from managers.SawManager import SawManager
from models.ChainSaw import ChainSaw
from models.ToySaw import ToySaw
from models.ElectricSaw import ElectricSaw


class SetManager:
    """
        Class which allow us to manage
        all the objects.
    """
    def __init__(self, saw_manager):
        """
            Constructor which creates an instance of SawManager class.
        """
        self.__saw_manager = saw_manager

    def __iter__(self):
        """
        Method for iterating through all the colors of saws
        """
        for saw in self.__saw_manager:
            for color in saw.color_of_saw:
                yield color

    def __len__(self):
        """
        Method which gets length of all the colors of saws
        :return: number of all colors
        """
        count = 0
        for saw in self.__saw_manager:
            count += len(saw.color_of_saw)
        return count

    def __getitem__(self, index):
        """
        Method which searches color of saw using an index
        :return: color by index
        """
        if index >= len(self):
            raise IndexError("Index not found")
        for saw in self.__saw_manager:
            if index < len(saw.color_of_saw):
                return list(saw.color_of_saw)[index]
            index -= len(saw.color_of_saw)

    def __next__(self):
        """
        Method which searching all the colors
        """
        for saw in self.__saw_manager:
            for color in saw.color_of_saw:
                return color


def main():
    """
    Main method which contains all the objects and methods realizations
    """
    saw_manager = SawManager()
    saw1 = ChainSaw
    saw1.color_of_saw = {"Black", "Orange"}
    saw2 = ElectricSaw
    saw2.color_of_saw = {"Blue", "White"}
    saw3 = ToySaw
    saw3.color_of_saw = {"Red", "Pink"}

    saw_manager.add_saw(saw1, saw2, saw3)

    manager = SetManager(saw_manager)
    for color in manager:
        print(color)

    print(len(manager))

    print(manager[4])


if __name__ == "__main__":
    main()

