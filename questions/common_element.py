""" Create a function common_element() that takes two lists as its parameters
    return the common elements.
    For instance, calling common_element([1,2,3], [3,43,1]) should
    return [1,3]
"""
def common_element(list1, list2):
	return [x for x in list1 if x in list2]
