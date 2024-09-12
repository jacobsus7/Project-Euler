#Problem 2

fib1 = 1
fib2 = 2
fib3 = fib1+fib2

total = 2

while fib3 < 4000000:
    if fib3%2 == 0:
        total += fib3
    fib1=fib2
    fib2=fib3
    fib3=fib1+fib2

print(total)
