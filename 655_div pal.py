div = 10000019

limit = 10**32

##def digitCount(n):
##    count = 1
##    while n < 10:
##        n = n//10
##        count +=1
##    return count    

def isPal(n):
    numstr = str(n)
    left = 0
    right = len(numstr)-1
    while left < right:
        if numstr[left] != numstr[right]:
            return False
        left+=1
        right-=1
        
    return True

total = div
count = 0
while total < limit:
    if isPal(total):
        count+=1
    total+=div

print(count)
