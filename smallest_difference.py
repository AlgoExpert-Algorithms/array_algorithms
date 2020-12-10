"""
Smallest Difference
Write a function that takes in tow non-empty arrays of integers, finds the pair of numbers(one from each array)
whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from
the first array in the first position.

NOTE: The absolute difference of two integers is the distance between them on the real number line. For eample,
the absolute difference of -5 and 5 is 10. And the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.
"""

# 0(n log(n) + m log(m)) time | 0(1) space
def smallestDifference(arrayOne, arrayTwo): # Finds the smallest absolute difference between two numbers
    arrayOne.sort() # first start off by sorting arrays
    arrayTwo.sort()
    idxOne = 0 # set the initial index starting points (pointers)
    idxTwo = 0
    smallest = float("inf") # set smallest and current to "inf", later will place correct values
    current = float("inf")
    smallestPair = [] # will return the pair after finding it inside of the algorithm

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo): # setting the bounds for the while loop
        firstNum = arrayOne[idxOne] # will set firstNum to current idxOne
        secondNum = arrayTwo[idxTwo] # will set secondNum to current idxTwo
        if firstNum < secondNum:
            current = secondNum - firstNum # setting new current value
            idxOne += 1 # Incrementing idxOne because firstNum < secondNum, meaning that to get a number that == 0,
            # we must increment idxOne to achieve a greater number to be close to 0 to retrieve a better absolute dif.
        elif secondNum < firstNum:
            current = firstNum - secondNum # setting new current value
            idxTwo += 1 # Incrementing idxTwo because secondNum < firstNum, which means that to get a better
            # absolute difference that is close to 0, we must increment idxTwo to achieve this.
        else: # in the case that the two numbers being compared == eachother, then we know this is the best case.
            return [firstNum, secondNum]
        # at first run, current is initialized and making smallest > current
        if smallest > current: # if smallest number is greater than current, then we assign smallest to current.
            smallest = current # smallest is = to the current(current smallest found in algorithm)
            smallestPair = [firstNum, secondNum]
        else: # if smallest number found so far in algorithm is not smaller than the current number, then continue.
            continue
    return smallestPair

print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17])) # test