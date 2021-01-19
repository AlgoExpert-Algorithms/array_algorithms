"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in
the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

def plusOne(digits):

    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9: # Simply add end element + 1 because it is not nine and then break.
            digits[i] += 1
            break
        else: # Else we know that the current element is 9 and convert to a 0.
            digits[i] = 0
            if i == 0 : # If and only if the first element of digits is 9, then we must add a 1 do the first index.
                digits.insert(0, 1)

    return digits

print(plusOne([1,2,3,9,9]))