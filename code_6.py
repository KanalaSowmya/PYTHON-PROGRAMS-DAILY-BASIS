'''QUESTION - 6 '''

'''Write a Python program that processes sales data for 5 days using the following values: [5000, 12000, 8000, 15000, 7000]. Using a loop, calculate the total sales and average sales. Also identify which days had sales greater than 10,000.'''
data=int(input())
values= list(map(int,input().split()))
total_sales=0
for i in range (data):
  total_sales=total_sales + values[i]
  average_sales = total_sales / data
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)

for i in range(data):
  if values[i] > 10000:
    day=i+1
    print("Day", day, "Sales:", values[i])


