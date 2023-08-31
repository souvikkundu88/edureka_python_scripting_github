'''
Question 12
By using list comprehension, please write a program to print the list after removing 
delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''

original_list = [12, 24, 35, 70, 88, 120, 155]
result_list = [item for item in original_list if item % 5 != 0 or item % 7 != 0]
print(result_list)
