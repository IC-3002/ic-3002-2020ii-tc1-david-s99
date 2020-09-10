import math
def e_cuadratica(n):
    i=0
    res=0
    while (i<=n):
        res+= 1/fact(i)
        i+=1
    return res

def e_lineal(n):
        i=0
        res=0
        while (i<=n):
            factorial = fact(i)
            res+= 1/factorial
            i+=1
        return res
def fact(n):
    res=1
    while(n>0):
        res=res*n
        n=n-1
    return res
