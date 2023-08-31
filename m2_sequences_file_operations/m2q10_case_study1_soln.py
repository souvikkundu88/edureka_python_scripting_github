'''
Question 10
By using list comprehension, please write a program to print the list after removing 
the value 24 in [12,24,35,24,88,120,155].
'''
original_list = [12, 24, 35, 24, 88, 120, 155]
result_list = [item for item in original_list if item != 24]
print(result_list)
