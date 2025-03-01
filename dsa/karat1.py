"""

Imagine we are reading sensor input for a self-driving car, and one of the foundational sensor readings is an image one pixel tall. 

We'll represent this image as an array where every pixel is a 1 or a 0. The image you get is known to have exactly one 0 in it, which represents a single obstacle.

Write a function that takes the image as input and returns the index of the 0.

For this problem, you cannot call index() or other search functions on the image.

Sample input and output:

image1 = [1, 1, 1, 0, 1, 1, 1] => 3
image2 = [1, 1, 1, 1, 1, 1, 0] => 6
image3 = [0, 1, 1, 1, 1, 1, 1] => 0
image4 = [0] => 0

Complexity Analysis variables:

n: the number of pixels in the array

"""

# TODO --- Write your function, returning the result


def first_zero(image):
    for index, value in enumerate(image): # i is the value
        if value == 0:
            return index
            
image1 = [1, 1, 1, 0, 1, 1, 1]
print(first_zero(image1)) # 3

image2 = [1, 1, 1, 1, 1, 1, 0]
print(first_zero(image2)) # 6

image3 = [0, 1, 1, 1, 1, 1, 1]
print(first_zero(image3)) # 0

image4 = [0]
print(first_zero(image4)) # 0
