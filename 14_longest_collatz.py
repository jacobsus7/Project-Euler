#Collatz

def main_coll(n):
    def collatz(x,chain_len=1):
       ## print('collatzification: '+str(x))
        if x==1:
            return chain_len
        if not x%2:
            return collatz(x/2,chain_len+1)
        else:
            return collatz((3*x)+1, chain_len+1)

    max_len = 0
    best_boy = None
    for i in range(1,n):
        ## print('the int being observed is: ' + str(i))
        curr = collatz(i)
        if curr > max_len:
            max_len = curr
            best_boy = i
    return best_boy
