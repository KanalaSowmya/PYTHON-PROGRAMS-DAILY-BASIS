# QUESTION -4
# You are working on a pricing analytics tool. Take two product prices. Perform all operations: sum, difference, multiplication, division, remainder, floor division, power. Also print which product is more expensive.

p1 = float( input("Enter price 1:"))
p2 = float(input("Enter price 2:"))
print("sum:", p1+p2)
print("diffence:", p1-p2)
print("multiplication:", p1*p2)
print("division:", p1/p2)
print("Remainder:", p1 % p2)          
print("Floor Division:", p1 // p2)    
print("Power:", p1 ** 2) 
if p1 > p2:
    print("Product 1 is costly")
elif p2 > p1:
    print("Product 2 is costly")
else:
    print("same price")             
