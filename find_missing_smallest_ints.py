"""
You are given a string S consisting of characters '1', '2', '3' and '?'.
Replace every '?' with exactly one of the remaining digits, so that the resulting string has no adjacent digits the same
and is as small as possible when interpreted as a number.

If S = "1??13", the only replacements with no identical adjacent digits are "12313" and "13213".
"12313" is the solution because it's the smaller alternative.

You may assume that there is at least one valid replacement solution for string S, i.e.
one in which all question marks may be replaced without the use of identical adjacent digits.
"""

# SOLUTION NOT YET SOLVE.
def solution(S: str) -> str:
    """
    S => String in which to find the missing "?" smallest value (no identical adjacent values).
    N => The length of given string to find and replace missing values.
    """
    stringList = list(S)

    for i in range(len(stringList)):
        if stringList[i] == "?":
            stringList[i] = "0"

    numberList = [int(stringList[i]) for i in range(len(stringList))]


    print(stringList)
    print(numberList)
    return ""

print(solution("??3??"))
