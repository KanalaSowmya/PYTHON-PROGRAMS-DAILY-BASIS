'''QUESTION - 5'''
'''Write a Python program that takes age = 25 and account_balance = 7000 as input values. Based on these values, determine the account type. If age is less than 18 → print "Not Eligible". If age is 18 or above and balance is 5000 or more → print "Premium Account". If age is 18 or above but balance is less than 5000 → print "Basic Account". If any value is negative → print "Invalid Input".'''

age = float(input("Enter age:"))
account_balance = float(input("Enter accountbalance:"))
if age < 18:
  print("Not Eligible")
elif age >= 18 and account_balance >= 5000:
  print("Premium Account")
elif age >= 18 and account_balance < 5000:
  print("Basic Account")
else:
  print("Invalid Input")
