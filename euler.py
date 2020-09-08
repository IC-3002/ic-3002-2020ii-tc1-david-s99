def e_cuadratica(n):
    i=0
    res=0
    while (i<=n):
        res+= 1/(factorial(i))
        i+=1
    return res

def factorial(n):
    res=1
    while(n>0):
        res=res*n
        n=n-1
    return res


def e_lineal(n):
    # Implemente esta función
    return 0
