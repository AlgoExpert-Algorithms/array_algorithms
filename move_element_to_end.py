"""
You're given an array of integers and an integer. Write a function that moves all instances of that integer in
the array to end of the array and returns the array.
The function should perform in this in place(i.e., it should mutate the input array) and doesn't need
to maintain the order of the other integers.
"""

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove: # condition to find the next j position that does not == toMove
            j -= 1 # will continue to decrement until a j index value != toMove to swap the array.
        if array[i] == toMove:
            # current i position == toMove(2), curent j position == current j position that != toMove(2).
            # swapping the position to correct the array list.
            array[j], array[i] = array[i], array[j]
        i += 1
    return array

print(moveElementToEnd([4,5,2,6,2,1,2,10,2,2,2],2))