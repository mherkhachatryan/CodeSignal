"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
"""


def centuryFromYear(year): 
    if year % 100 != 0:
        if year>= 101:
            return int(year/100)+1
        else:
            return 1
    elif year % 100 == 0:
        return int(year/100)

