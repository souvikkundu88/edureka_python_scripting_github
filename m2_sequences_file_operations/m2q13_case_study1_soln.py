'''
Question 13
Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are 
divisible by 5 and 7 , between 1 and 1000 inclusive.
'''

import random

def generate_divisible_numbers():
    divisible_numbers = []
    while len(divisible_numbers) < 5:
        num = random.randint(1, 1000)
        if num % 5 == 0 and num % 7 == 0:
            divisible_numbers.append(num)
    return divisible_numbers

random_numbers = generate_divisible_numbers()
print(random_numbers)
