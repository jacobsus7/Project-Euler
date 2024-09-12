
import math

##logtable = {1:0, 2:1}
##def log2(n):
##    """returns the log base 2 of n"""
##    if n in logtable:
##        return logtable[n]
##    else:
##        i = 2
##        count = 2
##        while i <= n:
##            double = 2*i
##            if double not in logtable:
##                logtable[double] = count
##            i = double
##            count += 1
##        return logtable[n]
    
def last1(i):
    return ~i & (i + 1)

#this works, but is slow
def solve_slow(n):
    """returns number of cases where Player 1 loses up to max of n"""
    i = 1
    count = 0
    while i <= n:
        pos = last1(i)
        if pos > i:
            count += 2*pos-3
        else:
            count += 2*(pos-1)
        
        i += 2
    return count

def solve(n):
    count = 0
    power2 = 2

    #contains all the losses
    loss = []

    while power2 < n:
        update = loss + [power2 - 1] + loss
        loss = update
        power2 *= 2
        count += 1
    
    diff = n-(power2/2)-1
    if diff < 0:
        loss = loss + loss[0:-1*(diff)]
    elif diff > 0:
        loss = loss + [power2-1] + loss[0:diff]
    else:
        loss = loss + [power2-1]
    print(loss)

#go up to the highest power of 2 less than n
#add on repeats
    
    
    
