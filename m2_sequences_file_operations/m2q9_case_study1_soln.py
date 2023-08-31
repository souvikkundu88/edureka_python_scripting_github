'''
Question 9
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this 
list after removing all duplicate values with original order reserved.
'''
original_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
