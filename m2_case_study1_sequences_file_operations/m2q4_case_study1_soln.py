'''
Question 4
Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
Hint: Use Loop to iterate through list elements.
'''
a = [4, 7, 3, 2, 5, 9]

for index, value in enumerate(a):
    print(f"Element at position {index} is: {value}")
