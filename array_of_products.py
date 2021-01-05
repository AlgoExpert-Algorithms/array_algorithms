"""
Write a function that takes in a non-empty array of integers and returns an array of the same length, where each
element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

NOTE: You are expected to solve this problem without using division.
"""

# Most efficient method to solve problem.
# 0(n) time | 0(n) space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]  # Assigning 1 to each element == length of n
    leftProducts = [1 for _ in range(len(array))]  # Assigning 1 to each element == length of n
    rightProducts = [1 for _ in range(len(array))]  # Assigning 1 to each element == length of n

    leftRunningProduct = 1 # Originally 1 to cover furthest left number in leftProducts array.
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct # Current number to add (starts at 1 initially)
        leftRunningProduct *= array[i] # Next number

    rightRunningProduct = 1 # Originally 1 to cover furthest right number in rightProducts array.
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct # Current number to add (starts at 1 initially)
        rightRunningProduct *= array[i] # Next number

    for i in range(len(array)): # Multiply the current index of leftProducts and rightProducts to find correct totals.
        products[i] = leftProducts[i] * rightProducts[i]

    return products


print(arrayOfProducts([3,5,7,8,10]))

# Least efficient method to solve the problem.
# 0(n^2) time | 0(n) space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]  # Assigning 1 to each element == length of n

    for i in range(len(array)):  # Parent loop will take care of tracking current number to ignore in multiplying.
        runningProduct = 1  # Base case 1
        for j in range(len(array)):  # Nested loop to iterate over the entire list, ignoring current number from parent.
            if i != j:  # Making sure to ignore the current element from the parent loop.
                runningProduct *= array[
                    j]  # Multiplying the base at the start and then multiplying the rest of elements.
        products[i] = runningProduct  # After iterating the nested for loop, add the runningProduct to products[i].

    return products

print(arrayOfProducts([3, 5, 7, 8, 10]))

