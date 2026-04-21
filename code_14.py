''' QUESTION - 14 '''

''' Write a Python program that asks the user to enter: (1) number of engineers, (2) total earnings, and (3) number of days. Then ask for a new number of engineers and number of days. Calculate and display the new total earnings based on the same earning rate. '''

engineers = float(input())
total_earnings = float(input())
days = float(input())
new_total_earnings = float(input())
total= total_earnings / (engineers * days )
one_engineer = days * total
total_earning_rate = one_engineer * new_total_earnings
print(total_earning_rate) 




