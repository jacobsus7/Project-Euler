#668 Square Root Smooth Numbers
import math

def sieve(n): #primes upto and including n
    sqrt = math.sqrt(n)
    primes = [1]*(n+1)
    primes[0]=0
    primes[1]=0
    i=2
    while i <= sqrt:
        if primes[i] == 1:
            j = 2
            while i*j <= n:
                primes[i*j] = 0
                j=j+1
        i=i+1
    return primes

#counts sqrt smooth numbers up to n inclusive
def naive_smooth(n):
    if n < 2:
        return
    count = 1 #not testing 1
    curr = 2
    prime_list = sieve(n)
    smooth_list = [1]
    while curr <= n:
        #print(prime_list)
        sqrt = math.sqrt(curr)
        smooth = True
        i = 2
        while i<=curr and smooth:
            if prime_list[i] and (i >= sqrt) and curr%i==0:
                #print(curr,i)
                #debug^
                smooth = False
            i=i+1
        if smooth:
            count = count + 1
            smooth_list.append(curr)
        curr = curr + 1
    return count, smooth_list
