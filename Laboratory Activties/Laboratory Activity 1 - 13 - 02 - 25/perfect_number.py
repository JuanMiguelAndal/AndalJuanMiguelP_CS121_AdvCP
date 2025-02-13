num1 = int(input("Enter a Number: "))
div = 0

for i in range(1, num1):
   if (num1 % i == 0):
    div += i
    
if (num1 == div):
    print(f"{num1} is a perfect number.")
else:
    print(f"{num1} is not a perfect number.")