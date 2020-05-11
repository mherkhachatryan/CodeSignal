"""
Problem:
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
"""

"""
Algorithm:
Create a list of empty park, with 0 at positions where were people and -1 of tree's positions. 
Get people heights from original list and save it to another list, then sort that list.
Iterate throught empty park and fill 0 values with people heights from sorted list. 
"""
def sortByHeight(a):
    tree_indices, people, park = [], [], []
    i = 0

    for item in range(len(a)):
        if a[item] == -1:
            tree_indices.append(item)
            park.insert(item, -1)
        else:
            people.append(a[item])
            park.insert(item, 0)
    people.sort()
    if not (all(people) or all(tree_indices)):
        return sorted(a)
    else:
        while i <= len(people):
            for position in range(len(park)):
                if park[position] == 0:
                    park[position] += people[i]
                    i+=1
            if all(park):
                break
        return park


