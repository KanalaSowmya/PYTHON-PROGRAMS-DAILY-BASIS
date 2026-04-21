''' QUESTION - 15 '''

''' Write a Python program that asks the user to enter the number of requests a single server can handle per second and the percentage increase in traffic. Calculate the new total traffic and determine how many servers are required to handle the increased load. Display the result.'''

one_server = float(input())
increase = float(input())

increase_calculated = one_server * (increase / 100)
New_Load = one_server + increase_calculated
new_total_load = New_Load / one_server
print(new_total_load )
