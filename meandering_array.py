"""
An array of integers is defined as being in meandering order when the first two elements are the respective largest and
smallest elements in the array and the subsequent elements alternate between its next largest and next smallest elements

Create a function that takes an array of integers and returns a meandering array.
"""

def meanderingArray(unsorted):
    unsorted.sort()  # First sort the array in ascending order.
    left_pointer = 0  # Setting the left pointer for the array.
    right_pointer = len(unsorted) - 1  # Setting the right pointer for the array.
    meander_array = []  # Array to be returned and modified in the loop.

    while (left_pointer < right_pointer):  # Setting the bounds and conditions for the while loop.
        meander_array.append(right_pointer)
        meander_array.append(left_pointer)
        right_pointer -= 1
        left_pointer += 1
    return meander_array


print(meanderingArray([7, 5, 2, 7]))