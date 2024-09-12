def paths(x,y,bounds,path_ct):
    if x < bounds:
        path_ct = paths(x+1,y,bounds,path_ct)
    if y < bounds:
        path_ct = paths(x,y+1,bounds,path_ct)
    if (x == bounds) and (y == bounds):
        return path_ct + 1
    return path_ct

def memoize(f):
    memo = {}
    def helper(x,y,n):
        if n not in memo:            
            memo[n] = f(x,y,n)
        return memo[n]
    return helper

##@memoize
##def path_2(x,y,bounds,path_ct):
##    if (x==0) and (y==0):
##        path_2(x+1,y,bounds,path_ct)
##    if (x == y):
##        return path_2(0,0,bounds-x,0)
##    if x < bounds:
##        path_ct = path_2(x+1,y,bounds,path_ct)
##    if y < bounds:
##        path_ct = path_2(x,y+1,bounds,path_ct)
##    if (x == bounds) and (y == bounds):
##        return path_ct + 1
##    return path_ct

@memoize
def path_3(x,y,bounds):
    path_ct = 0
    if (x==0) and (y==0):
        path_ct += path_3(x+1,y,bounds)
    if (x == y):
        path_ct += path_3(0,0,bounds-x)
    if x < bounds:
        path_ct += path_3(x+1,y,bounds)
    if y < bounds:
        path_ct = path_3(x,y+1,bounds)
    if (x == bounds) and (y == bounds):
        path_ct += 1
    return path_ct



