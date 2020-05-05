"""
Given an array of strings, return another array containing all of its longest strings.


"""

def allLongestStrings(inputArray):
    max_size = 0
    new_list = []
    for i in inputArray:
        if len(i) > max_size:
            max_size = len(i)
    for j in inputArray:
        if len(j) == max_size:
            new_list.append(j)
    return new_list

