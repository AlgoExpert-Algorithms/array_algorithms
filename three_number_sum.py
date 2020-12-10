"""
Write a function that takes in a non-empty array of distinct integers and an integer representing
a target sum. The function should find all triplets in the array that sum up to the target sum
and return a two-dimensional array of all these triplets. The numbers in each triplet should be
ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.
"""

def threeNumberSum(array, targetSum):
    array.sort()
    matches = []
    for i in range(len(array)-2): # Outter for loop tracking the current number for iteration
        # defining left and right here so that it resets for each current number position
        left = i+1 # defining the left pointer
        right = len(array)-1 # defining the right pointer
        while left < right: # defining the bounds in which comparisons are permitted
            currentSum = array[i] + array[left] + array[right] # Current sum for comparions.
            if currentSum == targetSum: # if there is a match
                matches.append([array[i] , array[left] , array[right]])
                left += 1 # Increment/decrement left and right because both numbers have been evaluated and added.
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return matches # returns the array that hols all matches from the array in regards to targetSum

print(threeNumberSum([8,5,1,4,2,6,3],8))