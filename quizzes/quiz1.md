**Question 1: Variables and Data Types**
*   **Part A:**  What is a variable in Python?  Explain in your own words.

its a place for holding data to later usage 

*   **Part B:**  Give three different examples of assigning a value to a variable.  Each example should use a different data type (e.g., integer, string, boolean).  Include comments to explain what each variable represents.

# example1 : integer
Age = 23
# example2  : string
Name = Joe
# example3  : Boolean
is_amazing = True

**Question 2: Arithmetic Operators**

*   **Part A:** Write a program that does the following:
    1.  Asks the user to enter two numbers.
    2.  Stores these numbers in variables named `num1` and `num2`.
    3.  Calculates the sum, difference, product, and quotient (division) of `num1` and `num2`.
    4.  Prints each result with a descriptive label (e.g., "The sum is: ...").

num1 = input("Enter first number")
num2 = input("Enter second number")

sum = num1 + num2
difference = num1-num2
product = num1 * num2
quotient = num1 / num2

Print ("sum is :, sum")
Print ("difference is:", difference)
Print ("product is:", product)
Print ("quotient is:" , quotient )


*   **Part B:** In the program above, what data type will be assigned to num1 and num2?
Integer

**Question 3: Comparison and Logical Operators**

*   **Part A:** Write a program that asks the user to enter their age.

Age = input("What is your age?")

print(Age)



*   **Part B:** Use `if`, `elif`, and `else` statements along with comparison operators (`>`, `<`, `==`, `>=`, `<=`) to do the following:
    *   If the age is less than 13, print "You are a child."
    *   If the age is between 13 and 19 (inclusive), print "You are a teenager."
    *   If the age is 20 or older, print "You are an adult."
*   **Part C:** Now, add a check to the beginning of your program. If the age entered is less than 0 or greater than 120, print "Invalid age" and stop the program.  Use the `or` logical operator in this check.

**Question 4: Assignment Operators**

*   **Part A:**  What is the difference between `=` and `==` in Python?
   = is used for Assignment or when assigning a variable 
   == is used to compare two things whether its true or false 

*   **Part B:**  Write a program that:
    1.  Initializes a variable `x` to the value 5.
    2.  Increments `x` by 3 using the `+=` assignment operator.
    3.  Multiplies `x` by 2 using the `*=` assignment operator.
    4.  Prints the final value of `x`.
