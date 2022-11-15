# definition of the sequence up to function
def sequenceUpTo(n):
    n = int(n)
    defaultArr = [1,2,4]
    # define defaults
    a = 1
    b = 2
    c = 4
    # return defaults
    if(n <= 0):
        return [-1]
    elif (n == 1):
        return [a]
    elif (n == 2):
        return [a, b]
    elif (n == 3):
        return [a, b, c]
    else:
        # if not default do the following
        for i in range(4,n+1):
            # add the last 3 nums to find the next
            newNum = defaultArr[len(defaultArr) - 1] + defaultArr[len(defaultArr) - 2] + defaultArr[len(defaultArr) - 3]
            defaultArr.append(newNum)
        return defaultArr

# main function where we execute from
def main():    
    x = input("please enter any number which you want to view a sequence up to: ")
    digit = int(x)
    # execute here
    return sequenceUpTo(digit)

# execute code here
print(main())