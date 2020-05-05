"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
"""

def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    new_statues = []
    i = 0
    while i < len(statues)-1:
        
        if statues[i+1] -statues[i] !=1  :
            new_statues.append(statues[i]+1)
            statues.insert(i+1,statues[i]+1)
        i +=1
    return len(new_statues)
