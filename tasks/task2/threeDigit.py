# function definition
# To print all three digit values that satisfy the ratio 1:2:3
def threeDigit():
    # digits happen to lie within the bound 100 <= x <= 999
    # greatest atio digit is 999/3 which is 333
    for i in range(100,334):
        # find product satisfying the ratio 1:2:3
        i2 = i * 2
        i3 = i * 3
        print("\n",i,i2,i3)

# execute the code
threeDigit()