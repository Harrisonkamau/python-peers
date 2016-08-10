def compare(list1, list2):

    b = [i for i in list1 if i in list1 and i in list2]
    return b
        
        
print compare([0, 9, 8, 7], [0, 3, 1, 7])

