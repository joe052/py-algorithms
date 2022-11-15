# digit checker
def digitChecker(number, digit):
    digArr = []
    result = 0
    stringified = str(number)

    # split number into digit array
    for i in range(len(stringified)):
        digArr.append(int(stringified[i]))
    # check if digit is present
    for i in digArr:
        if (i == digit):
            result = number * digit
            break
    return result


# define the function
def timeSingUp(digit):
    digitSeq = []
    # start the array
    for i in range(1, 100):
        digitSeq.append(i)
        if (i == digit):
            singUpDigit = i * i
            # print(singUpDigit)
            digitSeq.append(singUpDigit)
            break
    # keep counting and checking if the condition is met
    for i in range(0, 100):
        # break loop if 1000 is exceeded
        if (digitSeq[len(digitSeq)-1] >= 1000):
            break
        # check last digit first
        lastDigit = digitSeq[len(digitSeq)-1]
        result = digitChecker(lastDigit, digit)
        # restart loop after receiving new result
        if (result != 0):
            digitSeq.append(result)
            i = -1
            continue
        # break loop if 1000 is exceeded
        if (digitSeq[len(digitSeq)-1] >= 1000):
            break
        # count up
        newVal = digitSeq[len(digitSeq)-1] + 1
        digitSeq.append(newVal)
    print(digitSeq)


timeSingUp(2)
# print(digitChecker(15,3))
