#!/usr/bin/python
"""
Python  Functions
"""

# Write a function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)
def unique_list(a):
    Unique_list=[a[0]]
    for x in range(len(a)):
        if (a[x] in Unique_list) == False:
            Unique_list.append(a[x])
    return Unique_list

#Write a function multiply() to multiply all giving numbers in a list.
#Sample List : (9, 2, 3, -6, 7)
#Expected Output : -2268
def multiply(a):
    retun = 1
    for i in range(len(a)):
        retun *= a[i]
    return retun

# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12
def get_average(*args):
    summ = sum(args)
    return summ/len(args)
