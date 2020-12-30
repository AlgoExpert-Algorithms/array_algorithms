"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
(the highest value in the peak), at which point they become strictly decreasing. At least three integers are required
to form a peak.

For example, the integers 1,4,10,2 form a peak, but the integers 4,0,10 don't and neither do the integers
1,2,2,0. Similarly, the integers 1,2,3 don't form a peak because there aren't any strictly decreasing integers after
the 3.
"""

# 0(n) time | 0(1) space complexity
def longestPeak(array):
    longestPeakLength = 0 # Starting peak length before finding any, if any at all.
    currentIndex = 1 # Starting index at start of algorithm

    while currentIndex < len(array) - 1:
        # Checking if the current position is a peak. Return true if current index is a current peak.
        isAPeak = array[currentIndex - 1] < array[currentIndex] and array[currentIndex] > array[currentIndex + 1]

        # If isAPeak is not true, continue to next iteration of loop and check for a peak there.
        if not isAPeak:
            currentIndex += 1
            continue
        elif isAPeak: # If isAPeak is true, then calculate the length of the peak found.

            leftIndex = currentIndex - 2 # This is because we already know currentIndex - 1 is a part of the peak.
            while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
                leftIndex -= 1

            rightIndex = currentIndex + 2 # This is because we already know currentIndex + 1 is a part of the peak.
            while rightIndex < len(array) and array[rightIndex] < array[rightIndex -1]:
                rightIndex += 1

            currentPeakLength = rightIndex - leftIndex - 1 # Finding the length of current peak found.
            longestPeakLength = max(currentPeakLength, longestPeakLength) # Assigning the correct longest length peak.
            currentIndex = rightIndex # Correcting currentIndex after finding the currentPeakLength of the array.
    return longestPeakLength

print(longestPeak([1,2,3,4,5,4,3,2,1]))