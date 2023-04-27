'''
Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

words = input("Enter a sequence of words: ").split()
sorted_words = sorted(words)
print("Sorted words:", sorted_words)