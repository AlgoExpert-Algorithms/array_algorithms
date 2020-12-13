"""
Write a function that takes in an array of integers and returns a boolean representing whether the
array is monotonic. An array is said to be monotonic if its elements, from left to right, are
entirely non-increasing or entirely non-decreasing. Non-increasing elements aren't necessarily
exculisvely decreasing; they simply don't increase. Similarly, non-decreasing elements aren't
necessarily exclusively increasing; they simply don't decrease.

NOTE: empty arrays and arrays of one element are monotonic.
"""

# 0(n) time | 0(1) space
def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1],array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0

print(isMonotonic([1,2,3,4,5]))


# alternative (simpler to read method)
# 0(n) time | 0(1) space
def isMonotonic(array):
    # Initializing isIncreasing and isDecreasing as we assume it can be either at the start of the algorithm.
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(array)):
        currentDifference = array[i] - array[i-1] # adding currentDifference to evaluate each iteration of for loop.
        if(currentDifference >= 1): # currentDifference >= 1, meaning the array is currently increasing.
            isDecreasing = False
        elif(currentDifference <= -1): # currentDifference <= -1, meaning the array is currently decreasing
            isIncreasing = False
        else: # currentDifference == 0, therefore we do nothing and continue to determine a monotonic array.
            continue

    return isIncreasing or isDecreasing

print(isMonotonic([1,2,3,4,5,5]))