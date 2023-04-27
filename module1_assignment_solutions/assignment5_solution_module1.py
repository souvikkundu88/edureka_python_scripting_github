'''
Design a code in python which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.
'''

number = input("Enter a number: ")
if number == number[::-1]:
    print(number, "is a Palindrome number.")
else:
    print(number, "is not a Palindrome number.")