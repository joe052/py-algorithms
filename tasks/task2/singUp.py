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
    return digitSeq

# main function where we execute from
def main():
    print("Welcome to the sing up game!!")
    x = input("please enter a digit between 2 and 9 to view the singUp sequence? ")
    digit = int(x)
    # execute here
    return timeSingUp(digit)


def longestSeq():
    # test all the possible sequences and return longest
    largest = 0
    tupleArr = []
    result = []
    # fill tuple array
    for i in range(2, 10):
        sequence = timeSingUp(i)
        tupleArr.append([i, len(sequence)])
    # find longest sequence
    for tuple in tupleArr:
        if (tuple[1] > largest):
            largest = tuple[1]
    # identify the longest found sequence and return it
    for tuple in tupleArr:
        if (tuple[1] == largest):
            result = tuple
    return result


# execute the code here
# option a) answer execution
main()
# option b) answer execution
print(longestSeq())
