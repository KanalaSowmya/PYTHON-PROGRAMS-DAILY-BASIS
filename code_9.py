'''QUESTION - 9'''

''' Write a Python program using lambda functions with input value number = 10. One lambda should calculate the square of the number, and another should check whether the number is divisible by 5. Display both results.'''

''' WITH OUT USING LAMBDA FUNCTION'''
Number = int(input())
square = Number * Number
division = Number % 5 == 0
print(square)
print(division)

''' USING LAMBDA FUNCTION '''

number = int(input("Enter a number:"))
square = lambda x: x**2
division = lambda x: x%5 ==0
print(square(number))
print(division(number))




