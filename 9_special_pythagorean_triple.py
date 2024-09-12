#special triple
import math

def factor(n):
    factor_pairs = []
    sqrt = math.sqrt(n)
    i = 1
    while i <= sqrt:
        if n%i == 0:
            factor_pairs.append((i,n//i))
        i=i+1
    return factor_pairs

def pythagorize(r):
    if r%2==1:
        print('input must be an even integer')
        return
    r_p = (r**2)//2
    factors = factor(r_p)
    for i in factors:
        s = i[0]
        t = i[1]
        a = r+s
        b = r+t
        c = r+s+t
        if 3*r + 2*(s+t) == 1000:
            print('WE FOUND IT!')
            print(a,b,c,3*r + 2*(s+t))
            return True
    return False

def main():
    i=2
    while not pythagorize(i):
        i = i+2
    return

if __name__ == "__main__":
    main()
