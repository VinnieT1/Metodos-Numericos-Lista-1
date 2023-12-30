def bissecao(f, a, b, TOL):
    p = (a + b) / 2
    pn = [p]
    
    while abs(f(p)) > TOL:
        if f(a) * f(p) < 0:
            b = p
       
        else:
            a = p
       
        p = (a + b) / 2
        pn.append(p)
   
    return pn

def f(x):
    return x**2 - 2

a = 0
b = 2
TOL = 1e-6

raiz_bissecao = bissecao(f, a, b, TOL)
print(raiz_bissecao)