''' QUESTION - 10 '''

'''Write a Python program that asks the user to enter the number of days taken by Person A and Person B to complete a task individually. Calculate their work rates and determine how many days they will take to complete the task if they work together. Display the final answer clearly.'''

a = int(input())
b = int(input())
rate_a = 1 / a
rate_b = 1 / b
work_together = rate_a + rate_b
print(work_together)

