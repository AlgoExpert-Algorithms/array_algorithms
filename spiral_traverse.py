"""
Write a function that takes in an n x m two-dimensional array(that can be square-shaped when n == m) and returns a
one-dimensional array of all the array's elements in spiral order.
Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral
pattern all the way until every element has been visited.
"""

array = [
	[1,2,3,4],
	[12,13,14,5],
	[11,16,15,6],
	[10,9,8,7],
]

# 0(n) time | 0(n) space
def spiralTraverse(array):
    result = []  # Will contain the correct format of an array that is traversed in spiral fashion.
    startCol, endCol = 0, len(array[0]) - 1  # Will be the starting and ending index for the array to be iterated.
    startRow, endRow = 0, len(array) - 1  # Will be the starting row and ending row index for the array to e iterated.

    while startCol <= endCol and startRow <= endRow:  # As we increment the cols and rows, we break after conditions.

        for col in range(startCol, endCol + 1):  # Going through each column to append to result for the startRow.
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):  # Going through each row to append endCol for each row to result.
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):  # Going through each column and appending in reversed order.
            if startRow == endRow:  # We break at this point because we don't need to iterate when there's only one
                break  # row, which has already been accounted and appended to result.
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):  # Going through each row in reversed order to append
            # the firstCol for each row.
            if startCol == endCol:  # We break in case startCol == endCol, because in reversed(range(x + 1,
                # y)) accounts for
                # and will only run in the case that there are currently 3 rows in the spiral to traverse. The if
                # statement accounts for the second condition, which will break if startCol == endCol, which means
                # that it has been accounted for already in previous for loop.
                break
            result.append(array[row][startCol])

        # Increment/Decrement the values for each iteration of the spiral traversal to ensure all numbers are iterated.
        startCol += 1
        endCol -= 1
        startRow += 1
        endRow -= 1

    return result

print(spiralTraverse(array))

# Recursive example
# 0(n) time | 0(n) space
def spiralTraverse(array):
    result = [] # making array to store all spiral integer values and return end of function
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):  # Going through each column to append to result for the startRow.
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):  # Going through each row to append endCol for each row to result.
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):  # Going through each column and appending in reversed order.
        if startRow == endRow:  # We break at this point because we don't need to iterate when there's only one
            break  # row, which has already been accounted and appended to result.
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):  # Going through each row in reversed order to append
        # the firstCol for each row.
        if startCol == endCol:  # We break in case startCol == endCol, because in reversed(range(x + 1,
            # y)) accounts for
            # and will only run in the case that there are currently 3 rows in the spiral to traverse. The if
            # statement accounts for the second condition, which will break if startCol == endCol, which means
            # that it has been accounted for already in previous for loop.
            break
        result.append(array[row][startCol])

    spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)

print(spiralTraverse(array))


