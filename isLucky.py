"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

def isLucky(n):
    n = str(n)
    input_list = list(n)
    first = 0
    second = 0
    for i in range(len(input_list)//2):
        first +=int(input_list[i])
    for j in range(len(input_list)//2,len(input_list)):
        second += int(input_list[j])
    if first == second:
        return True
    else:
        return False

