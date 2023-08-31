'''
Question 11
By using list comprehension, please write a program to print the list after removing 
the 0th,4th,5th numbers in [12,24,35,70,88,120,155]. 
'''
original_list = [12, 24, 35, 70, 88, 120, 155]
indices_to_remove = [0, 4, 5]
result_list = [item for index, item in enumerate(original_list) if index not in indices_to_remove]
print(result_list)
