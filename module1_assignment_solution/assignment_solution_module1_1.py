'''
Write a program which will find factors of given number and find whether the
factor is even or odd.
Hint: Use Loop with if-else statements
'''


#solution
# Taking input from the user
num = int(input("Enter a number: "))

# Initializing an empty list to store the factors
factors = []

# Looping from 1 to the number itself
for i in range(1, num+1):
    # Checking if the number is divisible by i
    if num % i == 0:
        # If yes, then i is a factor of the number
        factors.append(i)

# Printing the factors
print("Factors of", num, "are:", factors)

# Checking whether each factor is even or odd
for factor in factors:
    if factor % 2 == 0:
        print(factor, "is an even factor of", num)
    else:
        print(factor, "is an odd factor of", num)


# solution

# taking input from the user and convert it into an interger
#num = int(input("input a number: ")

# creating a list to store the factors
#factors = []


    
























          
