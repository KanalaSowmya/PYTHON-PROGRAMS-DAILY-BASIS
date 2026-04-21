# QUESTION -3
# You are creating a job application form. Take input: name, city, expected_salary (monthly). Print a professional message and calculate annual salary.

name = input("Enter your name: ")
city = input("Enter your city: ")
expected_salary = float(input("Enter expected monthly salary: "))

annual_salary = expected_salary * 12
print("Dear", name, "Thank you for applying from", city, "Your expected monthly salary:", expected_salary, "Your expected annual salary:", annual_salary,)
