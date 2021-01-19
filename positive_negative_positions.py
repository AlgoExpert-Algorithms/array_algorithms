"""
Answer all questions
You are given an integer N and an array A of M integers.
Your task is to create a string of length N consisting only of plus and minus signs.
Every integer in array A denotes the position of a plus sign in the resulting string.
In every other position there should be a minus sign in the resulting string. Positions are zero-indexed.

Write a function solution that, given an integer N and an array A of length M, returns a string created as described
above.
"""

# 0(n) time | 0(n) space
def solution(N: int, A: [int]) -> str:
    """
    N => Determines the length of the returning string.
    A => Array being passed to function.
    M => Determines the amount of integers(indeces) that array A contains.

    The function should return a string in which it contains a + for every integer index position that correlates to array A.
    For positions that array A does not contain, then add a - to indicate that being so.
    """

    solutionString = ""
    trackingArray = ["-" for _ in range(N)]

    for i in range(len(A)):
        if trackingArray[A[i]]:  # If valid index, then include a "+" at position that is true.
            trackingArray[A[i]] = "+"

    solutionString = solutionString.join(trackingArray)
    return solutionString


print(solution(3, []))