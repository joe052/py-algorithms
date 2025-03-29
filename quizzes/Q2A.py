# PROMPT USER INPUT
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# CHECK TYPE
print(type(num1))

# convert to integer
num1, num2 = int(num1), int(num2)

# SUM
sum = num1 + num2

# DIFFERENCE
difference = num1 - num2

# PRODUCT
product = num1 * num2

# QUOTIENT
quotient = num1 // num2

# PRINT RESULTS
print("sum is :", sum)
print("difference is:", difference)
print("product is:", product)
print("quotient is:", quotient)
