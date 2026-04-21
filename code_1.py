# QUESTION-1 
# You are building a user profile system. Create variables: name (string), age (integer), height (float in meters), and is_employed (boolean: True/False). Assign values and print: “User is years old, m tall, Employment Status: <True/False>.

name = input("Enter name:")
age = int(input("Enter age:"))
height = float(input("Enter height:"))
is_employed = bool(input("Enter employed:"))
print(name, "is", age, "years old,", height, "m tall,", "Employment Status:", is_employed )