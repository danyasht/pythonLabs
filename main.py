from exceptions.decorators import logged
from exceptions.exceptions import ZeroDivisionException
from managers.saw_manager import SawManager
from managers.set_manager import SetManager
from models.chain_saw import ChainSaw
from models.toy_saw import ToySaw
from models.electric_saw import ElectricSaw


saw_manager = SawManager()
manager = SetManager(saw_manager)


@logged(ZeroDivisionException, mode='file')
def main():
    """
        Main method where I'm creating classes objects and
        using all the methods and printing results
    """
    saw1 = ElectricSaw("Makita", "Electric", 0, 2500, 100, True, 1.7, 20, 6, 10000)
    saw2 = ChainSaw("Stihl", "Gasoline", 0, 20250, 80, True, 1.4, 15, 4, 6000)
    saw3 = ToySaw("Child's saw", "None", 0, 0, 70, False, 1, 3, 10, 0)
    saw1.color_of_saw = {"Pink", "Yellow"}
    saw2.color_of_saw = {"Blue", "White"}
    saw3.color_of_saw = {"Red", "Black"}
    saw_manager.add_saw(saw1, saw2, saw3)
    list_for_objects = saw_manager.receive_list()
    enum_objects = saw_manager.enumerated_objects()
    zip_objects = saw_manager.zipped_objects()
    attributes_of_class1 = saw1.get_attributes_of_class(str)
    attributes_of_class2 = saw2.get_attributes_of_class(str)
    attributes_of_class3 = saw3.get_attributes_of_class(int)

    def condition(saw):
        return saw.power >= 2500

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
    print(f"Length of the list is: {len(saw_manager.saws)}")
    print("\t")
    print(f"Object with index 0 is: {saw_manager[0]}")
    print("\t")
    print(f"Remaining working time for saws is: {list_for_objects} hours")
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
    print("\t")
    for color in manager:
        print(color)
    print(len(manager))
    print(manager[2])
    print("\t")
    for saw in saw_manager.saws:
        saw.get_remaining_work_time()


if __name__ == "__main__":
    main()
