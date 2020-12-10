"""
Validating whether a possible subsequent array is inside of a main array.
"""

"""
Solution 1:

To find the subsequent of an array, if any, you must traverse through the main array while checking if the
current pointer of the possible subsequent(2nd array) matches the current pointer of the main array being
traversed through the while loop. This is because a subsequent is only true/valid if the order of the subsequent
array matches the order of the main array, while being able to ignore in-between integers that do not
belong to the possible subsequent array.

Given example:
Main array: [1,2,3,4,5]
Subsequent array: [1,3,5]
"""
# AlgoExpert solution 1: 0(n) time | 0(1) space = where n is the length of the array.
def isValidSubsequence(array, subsequence):
    """
    :param array: main array
    :param subsequence: possible subsequent array
    :return: true/false if any subsequent is found.
    """

    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(subsequence): # While we have not traversed through whole array, or
                                                             # have not traversed/found through whole subsequence array.
        if(array[arrIdx] == subsequence[seqIdx]):
            seqIdx += 1
        arrIdx += 1 # Regardless of case in while loop, we continue to add on to arrIdx to make comparisons to array.
    return seqIdx == len(subsequence)

print(isValidSubsequence([1,2,3,4,5], [1,3,5])) # returns true/false if any subsequence is present.

"""
Solution 2:

Instead of using a while loop, we use a for loop to iterate over each element inside of the main array.
In doing so, we compare each element to the current position of the possible subsequent array. If the
current subsequent array element == main array element in the for loop, increase subIdx += 1 to keep track
of how the elements found in the subsequent from the main element. Keep doing so until all elements are found and
if not, iterate over the whole array and return true/false to indicate if a subsequence was found.
"""
# AlgoExpert solution 2: 0(n) time | 0(1) space = where n is the length of the array.
def isValidSubsequence(array, sequence):
    """
    :param array: main array
    :param sequence: possible subsequent array
    :return: true/false if any subsequent is found.
    """
    subIdx = 0
    for element in array:
        if subIdx == len(sequence):
            break
        if element == sequence[subIdx]:
            subIdx += 1
    return subIdx == len(sequence)

print(isValidSubsequence([1,2,3,4,5], [1,3,5])) # returns true/false if any subsequence is present.