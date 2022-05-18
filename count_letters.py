# Author: Faith Elledge
# Grithubusername: Elledgef
# Date: 5/18
# Description: Takes the parameter of the string and returns a dictonary that tabulates how many of each letter
# is in that string
import string


def count_letters(string):
    result = {}

    for x in string.upper():
        if (x > 'A' and x <= 'Z'):
            if not result.get(x):
                result[x] = 1
            else:
                result[x] += 1


