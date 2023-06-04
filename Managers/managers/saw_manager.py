"""
    This module is needed for lab №9
"""


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
        return [saw for saw in self.saws if saw.type_of_engine == "Gasoline"]

    def find_all_with_chain_length_more_than(self, chain_length):
        """
            Method which returns all the objects with chain length more than 1.1.
        """
        return [saw for saw in self.saws if saw.chain_length > 1.1]

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
        Returns a concatenation of the object and the result
        of the execution of method receive_list()
        """
        results = [saw.get_remaining_work_time() for saw in self.saws]
        return [f"{result} hours is for {saw}" for result, saw in zip(results, self.saws)]

    def check_condition(self, condition):
        """
        Uses the all() and any() functions to check whether all objects
        in the manager's list satisfy a certain condition, and if at least one does.
        :param condition: receives one function
        :return: returns a dictionary with the keys "all" and "any"
        and the corresponding boolean values.
        """
        all_condition = all(condition(saw) for saw in self.saws)
        any_condition = any(condition(saw) for saw in self.saws)
        return {"All saws": all_condition, "Any saw": any_condition}

    def remaining_time_for_saws(self):
        for saw in self.saws:
            saw.get_remaining_work_time()
