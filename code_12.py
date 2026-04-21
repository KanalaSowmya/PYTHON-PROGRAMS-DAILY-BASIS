'''QUESTION - 12'''

''' Write a Python program that asks the user to enter a sequence of numbers (as a list). Identify the pattern in the sequence and print the next number.'''


Sequence = list(map(int,input().split()))
difference = Sequence[1] - Sequence[0]
next_num = Sequence[-1] + difference

print(next_num)
