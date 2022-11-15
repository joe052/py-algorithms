# Question 1: Is the three time repetition of the last character of the reversed string
#   of "Birbeck" not greater than the acronym of the British BroadCasting Corporation?
# Question 2: Is the difference between 8 and 5 not smaller than or equal to the
#   product of 1 and 3
# Question 3: Is 2 raised to the power of 3 less than 3 raised to the power 2


# model to answer the three questions provided in either true or false
def threeQuestions():
    # question 1 answer
    my_str = "Birbeck"
    test_acronym = "BBC"
    # reverse the string
    new_str = my_str[::-1]
    # pick the last character
    lastChar = new_str[-1]
    # create the repeated acronym
    new_acronym = lastChar+lastChar+lastChar
    q1_answer = new_acronym > test_acronym

    # question 2 answer
    diff = 8-5
    prod = 1*3
    q2_answer = diff <= prod
    # question 3 answer
    arg1 = 2**3
    arg2 = 3**2
    q3_answer = arg1 < arg2

    # return answers
    return q1_answer, q2_answer, q3_answer


print(threeQuestions())
