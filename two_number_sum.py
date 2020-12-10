"""
Find whether 2 integers inside of an array add to equal a target number.
"""

# Array of integers will pass through the function.
# A target will be passed as well, indicating the sum of any two numbers of the array that equals the targetSum.
# If any two numbers from the array equal the targetSum, return the integers inside of an array.
# Otherwise return an empty array.
# Note- a single element in the array cannot add to itself to equal the targetSum.

# My answer:
def twoNumberSum(array, targetSum):
    """
    My answer function
    :param array: list of integers.
    :param targetSum: integer as the target for any two added integers in the list that may equal to the targetSum.
    :return: returns the list of the two integers that equal targetSum, if any. Otherwise return an empty list.
    """
    # Parent for loop will take care of the current integer in the list to compare with rest of list.
    for current_num in array:
        # Child loop will take care of accessing rest of integers in the list for comparisons.
        for index, next_num in enumerate(array):

            # if the current_num == next_num, continue to next iteration.
            if current_num == next_num:
                continue
            # if the current_num from parent loop == next_num, return list.
            if current_num + next_num == targetSum:
                return [current_num, next_num]

    # If no two numbers in the array = target, then return an empty array.
    return []

def algoTwoNumberSum(array, targetSum): # 0(n^2) time | 0(1) space
    """
    AlgoExpert's answer solution 1
    :param array: list of integers.
    :param targetSum: integer as the target for any two added integers in the list that may equal to the targetSum.
    :return: returns the list of the two integers that equal targetSum, if any. Otherwise return an empty list.
    """
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1,len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
        return []

def algoTwoNumberSum2(array, targetSum): # 0(n) time | 0(n) space using a hash table
    """
    AlgoExpert's answer solution 2
    :param array: list of integers.
    :param targetSum: integer as the target for any two added integers in the list that may equal to the targetSum.
    :return: returns the list of the two integers that equal targetSum, if any. Otherwise return an empty list.
    """
    nums = {}
    for num in array:
        potentialMatch = targetSum - num # equation => x + y = 10 => x = 10 - y
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

def algoTwoNumberSum3(array, targetSum): # 0(nlog(n)) | 0(1) space
    """
    AlgoExpert's answer solution 3
    :param array: list of integers.
    :param targetSum: integer as the target for any two added integers in the list that may equal to the targetSum.
    :return: returns the list of the two integers that equal targetSum, if any. Otherwise return an empty list.
    """
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

"""

AlgoExpert solution(s) reflection:

#### Solution 1 0(n^2) time | 0(1) space

Using a nested for loop to find the 2 integers(if any) that equal targetToFind. The problem with this approach is that 
the function is traversing through the list more than once,  which is not efficient. Below is an example of retrieving 
the pair(s) that equal the target number.

array = [1,2,3,4,5,6,7,8,9,10]
target = 11
for i in range(len(array)-1): 
    firstNum = array[i]
    for j in range(i+1, len(array)):
        secondNum = array[j]
        if firstNum + secondNum == 11:
            print(f"pair: {firstNum},{secondNum} = {target}")

#### Solution 2  0(n) time | 0(n) space

As part of the video explanation, the equation x+y = targetToFind comes up. Once you decide to solve for x, the 
equations shows as x = targetToFind - y

Given example => x = targetToFind(10) - (y)3 = 7. It is at this point in which you obtain the x, y values. X from the 
result of the equation, y from the array list. 

Now we can use a dictionary or a hash table to find the 2 value pairs that = the targetToFind value that are available 
in our array list(non- repeated). For each number that our program iterates to inside of the given array list, our 
equation will test each passing integer as y to the equation, and if the result of the equation is stored inside of the 
hash table already, then we know that the two values to add is y value(found in the current element) and the value equal
 to the equation, which is found in the hash table. This is the case because any 2 numbers given from the equation 
 (y and the result of the equation) will always = targetToFind from the equation. So if the result of the equation = 
 a number found in the hash table, then we have found our 2 variables x and y. 


#### Solution 3 0(nlog(n)) | 0(1) space

Start off by sorting the array => list.sort() so that the right pointer will always be pointing to the current highest 
number, and the left pointer pointing towards the current lowest.

Given array [-4, -1, 1, 3, 5, 6, 8, 11], targetToFind(10)
              ^	                     ^
              L(pointer)	         R(pointer)

I this case, -4 + 11 = 7. Because this is not the answer, we must move either the left or right pointer.


Given array [-4, -1, 1, 3, 5, 6, 8, 11], targetToFind(10)
              ^	                 ^
              L(pointer)	     R(pointer)

Notice that if you move the right pointer towards the center, the result will be a lower over all number. 

-4 + 8 = 4

Similary, if you move the left pointer towards the center, the result will = a higher number than moving the right 
pointer towards the center. 

Given array [-4, -1, 1, 3, 5, 6, 8, 11], targetToFind(10)
	              ^	             ^
	              L(pointer)     R(pointer)

-1 + 8 = 7

Finding the solution: Now that the basics are covered as to how the pointers work to find the targetToFind(10) integer, 
the solution is as given below. By first testing -4 + 11 = 7, we know that we need a higher number by moving the left 
pointer towards the center.

Given array [-4, -1, 1, 3, 5, 6, 8, 11], targetToFind(10)
                  ^	                ^
	            L(pointer)          R(pointer)


-1 + 11 = targetToFind(10) <= SOLUTION


NOTE: You never go back with the L or R pointers, as you will then be checking the same values more than once. Instead, 
always move the Left or Right  pointers towards the center. Wherever the L pointer is located exactly after moving the 
R pointer towards the center, that is up to and including the integer that have all been previously checked on from the 
previous R pointer. 

EXTRA PSUDO CODE EXAMPLE:
SOLUTION 3: 
unsorted array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
sorted array = [-47, -21, 4, 9, 12, 56, 65, 210, 301, 356]
target => 121
answer => [56, 65]

1. 309 -right * - Right because we need a smaller number.
2. 254 -right * - Right because we need a smaller number.
3. 163 -right * - Right because we need a smaller number.
4. 18  +left  * + Left because we need a bigger number.
5. 44  +left  * + Left because we need a bigger number.
6. 69  +left  * + Left because we need a bigger number.
7. 74  +left  * + Left because we need a bigger number.
8. 77  +left  * + Left because we need a bigger number.
9. 121 ANSWER return [56,65]

1-3: We are taking down all the numbers that are greater than answer,
but stopping at the highest number of the right pointer once we find
the right pointer that = a number lower than the answer we are looking
for.
4-9: Then we are taking down all numbers that are lower than answer,
moving towards the center until we reach the lowest highest number(left
pointer), paired with the highest lowest number (right pointer) to
find our answer, if any are presented. 
For this reason, we do not move backwards from left or right pointer(s).
"""
