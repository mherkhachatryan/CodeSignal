"""
Given two strings, find the number of common characters between them.
"""

def commonCharacterCount(s1, s2):
    result = 0
    for letter in set(s1):
        s1_count = s1.count(letter)
        s2_count = s2.count(letter)
        result +=min([s1_count,s2_count])
    #it's easier to find common characters in sorted strings
    return result
