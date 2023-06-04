"""
    This module is needed for lab №9
"""
from models.ChainSaw import ChainSaw
from models.ToySaw import ToySaw
from models.ElectricSaw import ElectricSaw


class SawManager:
    """
        Class which allow us to manage
        all the objects.
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

    def __len__(self):
        """
        Method which prints length of list(saws)
        :return: length of the list
        """
        return len(self.saws)

    def __getitem__(self, place):
        """
        Method which searches and returns object by its place
        :param place: the same as index
        :return: object by index
        """
        return self.saws[place]

    def __iter__(self):
        """
        Method which iterating through the all list
        :return: all the list
        """
        return iter(self.saws)

    def receive_list(self):
        """
        Method which creates the list with all data from one method
        :return: list with data
        """
        return [saw.get_remaining_work_time() for saw in self.saws]

    def enumerated_objects(self):
        """
        Method which pasting from the object and its serial number in the list
        :return: pasting from the object and its serial number in the list
        """
        return [f"{place} index is {saw}" for place, saw in enumerate(self.saws)]

    def zipped_objects(self):
        """
        Returns a concatenation of the object and the result of the execution of method receive_list()
        """
        results = [saw.get_remaining_work_time() for saw in self.saws]
        return [f"{result} hours is for {saw}" for result, saw in zip(results, self.saws)]

    def check_condition(self, condition):
        """
        Uses the all() and any() functions to check whether all objects
        in the manager's list satisfy a certain condition, and if at least one does.
        :param condition: receives one function
        :return: returns a dictionary with the keys "all" and "any" and the corresponding boolean values.
        """
        all_condition = all(condition(saw) for saw in self.saws)
        any_condition = any(condition(saw) for saw in self.saws)
        return {"All saws": all_condition, "Any saw": any_condition}


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
    list_for_objects = saw_manager.receive_list()
    enum_objects = saw_manager.enumerated_objects()
    zip_objects = saw_manager.zipped_objects()
    attributes_of_class1 = saw1.get_attributes_of_class(str)
    attributes_of_class2 = saw2.get_attributes_of_class(str)
    attributes_of_class3 = saw3.get_attributes_of_class(int)

    def condition(saw):
        return saw.get_power >= 2500

    condition_check = saw_manager.check_condition(condition)

    print("\t")

    print("All the saws are:")
    for saw in saw_manager:
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

    print("\t")

    print(len(saw_manager.saws))

    print("\t")

    print(saw_manager[0])

    print("\t")

    print(list_for_objects)

    print("\t")

    for saw in enum_objects:
        print(saw)

    print("\t")

    for saw in zip_objects:
        print(saw)

    print("\t")

    print(attributes_of_class1)
    print(attributes_of_class2)
    print(attributes_of_class3)

    print("\t")

    print(condition_check)


if __name__ == "__main__":
    main()
