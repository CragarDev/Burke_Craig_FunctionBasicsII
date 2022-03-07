"""
Assignment: Functions Basic II

Objectives:

Learn how to create basic functions in Python
Get comfortable using lists
Get comfortable having the function return an expression/value

? 1. Countdown -
#   Create a function that accepts a number as an input.
    Return a new list that counts down by one, from the number
    (as the 0th element) down to 0 (as the last element).
    Example: countdown(5) should return [5,4,3,2,1,0]
"""


def countDown(num):
    newList = []
    for x in range(num, -1, -1):
        newList.append(x)

    return newList


print("Countdown...")
print(countDown(42))
print("")
print(countDown(23))
print("")
print(countDown(3))
print("")


"""

? 2. Print and Return -
    Create a function that will receive a list with two numbers.
    Print the first value and return the second.
    Example: print_and_return([1,2]) should print 1 and return 2

"""


def printAndReturn(arr):
    print("First Number:", arr[0])
    return arr[1]


print("Print and Return...")
print("Second Number:", printAndReturn([2, 3]))
print("")
print("Second Number:", printAndReturn([6, 5]))
print("")
print("Second Number:", printAndReturn([75, 50]))
print("")

"""

? First Plus Length -
    Create a function that accepts a list and returns
    the sum of the first value in the list plus the list's length.
    Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

"""


def firstPlusLength(arr):
    sum = arr[0] + len(arr)
    return sum


print("First Plus Length...")
print(firstPlusLength([1, 2, 3, 4, 5]))
print("")
print(firstPlusLength([30, 92, 63, 72, 550, 7, 23, 87]))
print("")
print(firstPlusLength([3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]))
print("")

"""

? Values Greater than Second - 
    Write a function that accepts a list and creates a new list containing
    only the values from the original list that are greater than its 2nd value.
    Print how many values this is and then return the new list.
    If the list has less than 2 elements, have the function return False
    Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
    Example: values_greater_than_second([3]) should return False

"""


def valuesGreaterThanSecond(arr):
    if (len(arr) < 2):
        return False
    newList = []
    checkSum = arr[1]
    count = 0
    for item in arr:
        if(item > checkSum):
            newList.append(item)
            count += 1
    print(f"There are {count} numbers greater than {arr[1]} in the list")
    return newList


print("Values Greater than Second...")
print(valuesGreaterThanSecond([5, 2, 3, 2, 1, 4]))
print("")
print(valuesGreaterThanSecond([3]))
print("")
print(valuesGreaterThanSecond([514, 65, 49, 104, 119, 431]))
print("")

"""


? This Length, That Value -
    Write a function that accepts two integers as parameters: size and value.
    The function should create and return a list whose length is
    equal to the given size, and whose values are all the given value.
    Example: length_and_value(4,7) should return [7,7,7,7]
    Example: length_and_value(6,2) should return [2,2,2,2,2,2]

"""


def thisLengthThatValue(size, value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList


print("This Length, That Value...")
print(thisLengthThatValue(4, 7))
print("")
print(thisLengthThatValue(6, 2))
print("")
print(thisLengthThatValue(22, 9))
print("")
