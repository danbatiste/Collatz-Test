def hs(n, total=1):
    if not n%2:
        return hs(n/2, total + 1)
    elif n == 1:
        return total
    elif not (n + 1)%2:
        return hs(3*n + 1, total + 1)

def invhs(n):
    p = False
    i = 0
    while not p:
        i += 1
        p = n == hs(i)
    return i

def nextinvhs(n):
    p = False
    i = 0
    while 1:
        while not p:
            i += 1
            p = n == hs(i)
            if i > 2**n:
                return None
        yield i
        p = False
        
def invhs_count(n):
    return [v for v in nextinvhs(n)]