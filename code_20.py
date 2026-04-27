'''QUESTION - 20 '''

''' Write a Python program using the dictionary {"name": "Rahul", "age": 25, "city": "Delhi"}. Print the value of "name" and "city". Then update age to 26 and add a new key "salary" with value 50000.'''

'''SWITH OUT USING USER INPUTS'''

person = {"name": "Rahul", "age": 25, "city": "Delhi"}

# Print values
print(person["name"], "and", person["city"])

# Update age
person["age"] = 26

# Add new key-value pair
person["salary"] = 50000

# Print updated dictionary
print("Updated dictionary:", person)



''' USING USER INPUTS'''

# Take inputs from user
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

# Create dictionary using inputs
person = {"name": name, "age": age, "city": city}
print("Created dictionary", person)

# Print values
print(person["name"], "and", person["city"])

# Update age
person["age"] = person["age"] + 1 
print(person["age"])

# Add new key-value pair
salary = int(input("Enter salary: "))
person["salary"] = salary

print("Updated dictionary:", person)