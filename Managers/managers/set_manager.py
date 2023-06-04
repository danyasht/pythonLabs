"""
    This module is needed for lab №9
"""


class SetManager:
    """
        Class which allow us to manage
        all the objects.
    """

    def __init__(self, saw_manager):
        """
            Constructor which creates an instance of SawManager class.
        """
        self.saw_manager = saw_manager

    def __iter__(self):
        """
        Method for iterating through all the colors of saws
        """
        for saw in self.saw_manager:
            for color in saw.color_of_saw:
                yield color

    def __len__(self):
        """
        Method which gets length of all the colors of saws
        :return: number of all colors
        """
        count = 0
        for saw in self.saw_manager:
            count += len(saw.color_of_saw)
        return count

    def __getitem__(self, index):
        """
        Method which searches color of saw using an index
        :return: color by index
        """
        if index >= len(self):
            raise IndexError("Index not found")
        for saw in self.saw_manager:
            if index < len(saw.color_of_saw):
                return list(saw.color_of_saw)[index]
            index -= len(saw.color_of_saw)

    def __next__(self):
        """
        Method which searching all the colors
        """
        for saw in self.saw_manager:
            for color in saw.color_of_saw:
                return color
