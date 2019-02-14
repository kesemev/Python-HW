"""Kesem Even-Hen,208055483,Work2 "func" """
'-------------------ex3------------------------'

def myFilter(L,func):
    """function that works like ilter() method filters
    the given iterable with the help of a function that
    tests each element in the iterable to be true or not.

    Parameters: list of numbers, function
    Returns: new list of numbers for which a function returns true"""

    new = []
    for elem in L:
        if func(elem)==True:
            new.append(elem)
            """he method append() appends a passed obj into the existing list."""
    return new


def myFilterMulti(L,funcL):
    """function that enables filtering based on functions on numbers from the list

    Parameters: list of numbers, list of functions
    Returns: A filtered list of number for which all the functions returns true"""
    new = L
    for func in funcL:
        for elem in L:
            new = myFilter(new, func)
    return new


def myQuadric(x):
    """Parameters: int value
     Returns: True or False if the value is square"""
    sum=0
    k=1
    while sum < x:
        sum+=(2*k-1)
        k=k+1
    if sum==x:
        return True
    else:
        return False


def isDiv3(x):
    """Parameters: int value
     Returns: True or False if the value is divided into 3"""
    return x%3==0


print(myFilter([9,10,16,24,29,36],myQuadric))
print(myFilterMulti([9,10,16,24,29,36],[myQuadric,isDiv3]))

'-------------------ex4------------------------'
from functools import reduce

def gimetric_value(string):
    """function that calculates the gematric value of all letters in string and returns the sum
    it will filter out all characters that are not letters by isalpha() method,
    will change the string to lower case by lower() method
    change the list to the ASCII code of each letter in the list by ord() method,
    subtracting from each one 96 and calculating the total results tp sum by reduce()

    Parameters: string
    Returns: int sum of the gematric value of all letters in string"""
    new=list(map(ord,(filter(lambda x: x.isalpha(), string.lower()))))
    sum=reduce((lambda x,y: x+y-96),new,0)
    return sum


print(gimetric_value("a?cD2b"))

