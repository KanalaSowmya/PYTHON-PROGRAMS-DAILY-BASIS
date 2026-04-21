# QUESTION -2
#You are building a salary calculation system. Take input as strings: base_salary, bonus_percentage, experience_years. Convert them and calculate: base + (base * bonus / 100) + (experience_years * 1000).

base_salary = input("Enter base salary: ")
bonus_percentage = input("Enter bonus  ")
experience_years = input("Enter experience years: ")

base = float(base_salary)
bonus = float(bonus_percentage)
years = float(experience_years)

total_salary = base + (base * bonus / 100) + (years * 1000)
print("Total calculated salary:", total_salary)  

