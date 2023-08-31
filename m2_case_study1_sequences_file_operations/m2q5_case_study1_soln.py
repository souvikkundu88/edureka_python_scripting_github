'''
Question 5
Please write a program which accepts a string from console and print the
characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
'''
input_string = input("Enter a string: ")
result = ""

for index in range(0, len(input_string), 2):
    result += input_string[index]

print(result)

