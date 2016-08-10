# create a function compare_elements that takes two lists as arguments
def compare_elements(lst1,lst2):
    # make sure the arguments passed are lists
    lst1 =list(lst1)
    lst2 = list(lst2)

    # create an empty list
    common_list = []

    # sort the lists
    sorted_1 = sorted(lst1)
    sorted_2 = sorted(lst2)

    # iterate through sorted_1 to compare its elements with sorted_2's
    for element in sorted_1:
        for number in sorted_2:
            if number == element:
                common_list.append(number)
    return common_list



