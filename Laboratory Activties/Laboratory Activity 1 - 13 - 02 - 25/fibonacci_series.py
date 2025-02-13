num1 = int(input("Enter the number of terms: "))
fib1 = 0
fib2 = 1
fib = 1


count = 1

print("Fibonacci Series: ", end="")
while count <= num1:
    print(fib1, end=" ")
    count += 1
    
    fib1 = fib2
    fib2 = fib
    fib = fib1 + fib2