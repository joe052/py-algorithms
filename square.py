# define a testing array
array = [9, 5, 28, 25, 47, 55]
# array = [24,15,18,18,42, 22]
# function to check if squares exist in array
def checkSquares(arr):
    # loop through array and record square
    for i in arr:
        square = i*i
        # loop through array and check if the square matches any number in array
        for j in array:
            # return true if there is a match
            if (square == j):
                print(i, j)
                return True
    # return false if none matches
    return False


print(checkSquares(array))
