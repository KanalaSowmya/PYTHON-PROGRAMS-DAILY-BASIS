'''QUESTION - 9'''

'''Write a Python function that calculates total cost using price = 2000 and quantity = 6. The function should return total = price × quantity. After that, if total amount is greater than 10000, apply a 10% discount and print the final amount.'''


''' USING FUNCTIONS '''

def calculate_total(price, quantity):
    total = price * quantity

    if total > 10000:
        discount = total * 0.10
        final_amount = total - discount
        return final_amount # returns discounted amount
    else:
        return total # returns original amount

# Take input outside function
price = int(input())
quantity = int(input())

# Call function and store result
print(calculate_total(price, quantity))