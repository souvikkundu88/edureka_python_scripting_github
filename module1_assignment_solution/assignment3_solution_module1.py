'''
Write a program, which will find all the numbers between 1000 and 3000 (both
included) such that each digit of a number is an even number. The numbers
obtained should be printed in a comma separated sequence on a single line.
Hint: In case of input data being supplied to the question, it should be assumed to
be a console input. Divide each digit with 2 and verify is it even or not.
'''


even_nums = []
for i in range(1000, 3001):
    num = str(i)
    if int(num[0]) % 2 == 0 and int(num[1]) % 2 == 0 and int(num[2]) % 2 == 0 and int(num[3]) % 2 == 0:
        even_nums.append(num)
print(", ".join(even_nums))


'''
result = []
for num in range(1000, 3001):
    # Check if all digits of the number are even
    if all(int(digit) % 2 == 0 for digit in str(num)):
        # Append the number to the result list
        result.append(str(num))
# Print the comma-separated sequence of even-digit numbers
print(",".join(result))

'''

