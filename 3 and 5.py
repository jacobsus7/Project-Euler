n = 1
total = 0

while n < 1000:
    if ((n%3 == 0) or (n%5 == 0)):
        total = total + n
    n = n+1

print(total)
