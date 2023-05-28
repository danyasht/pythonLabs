"""
    This module is needed for lab №8
"""
from Models.ChainSaw import ChainSaw
from Models.ToySaw import ToySaw
from Models.ElectricSaw import ElectricSaw


class SawManager:
    """
        Abstract class which allow us to manage
        all the objects.
    ...
        Methods
    ----------––––––-------------------------
        def find_all_with_type_of_engine(self, type_of_engine):
            return [saw for saw in self.saws if saw.get_engine == "Gasoline"]
                Method which returns all the objects with Gasoline engine type.

        def find_all_with_chain_length_more_than(self, chain_length):
            return [saw for saw in self.saws if saw.get_length > 1.1]
                Method which returns all the objects with chain length more than 1.1.

        def add_saw(self, *saws):
            for saw in saws:
                self.saws.append(saw)
                    Method which adding saw object to list.
    """

    def __init__(self):
        """
            Constructor which creates a list called saws.
        """
        self.saws = []

    def find_all_with_type_of_engine(self, type_of_engine):
        """
            Method which returns all the objects with Gasoline engine type.
        """
        return [saw for saw in self.saws if saw.get_engine == "Gasoline"]

    def find_all_with_chain_length_more_than(self, chain_length):
        """
            Method which returns all the objects with chain length more than 1.1.
        """
        return [saw for saw in self.saws if saw.get_length > 1.1]

    def add_saw(self, *saws):
        """
            Method which adding saw object to list.
        """
        for saw in saws:
            self.saws.append(saw)


def main():
    """
        Main method where I'm creating classes objects and
        using all the methods and printing results
    """
    saw_manager = SawManager()
    saw1 = ElectricSaw("Makita", "Electric", 2500, 2500, 100, True, 1.7, 20, 6, 10000)
    saw2 = ChainSaw("Stihl", "Gasoline", 1000, 20250, 80, True, 1.4, 15, 4, 6000)
    saw3 = ToySaw("Child's saw", "None", 10, 0, 70, False, 1, 3, 10, 0)

    saw_manager.add_saw(saw1, saw2, saw3)

    print("\t")

    print("All the saws are:")
    for saw in saw_manager.saws:
        print(saw)

    print("\t")

    print("Saws with gasoline engine are:")
    saws_to_find = saw_manager.find_all_with_type_of_engine("Gasoline")
    for saw in saws_to_find:
        print(saw)

    print("\t")

    print("Saws with chain length more than 1.1 are:")
    saws_to_find1 = saw_manager.find_all_with_chain_length_more_than(1.1)
    for saw in saws_to_find1:
        print(saw)

    print("\t")

    for saw in saw_manager.saws:
        print(f"Remaining work time for saws is: {saw.get_remaining_work_time()} hours")


if __name__ == "__main__":
    main()
