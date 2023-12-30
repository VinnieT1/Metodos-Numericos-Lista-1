def bissecao(f, a, b, tol):
    prev = 1e+100
    curr = (a + b) / 2
    
    while abs(curr - prev) > tol:
        f_c = f(curr)
        
        if f_c == 0:
            return curr
        elif f(a) * f(curr) < 0:
            b = curr
        else:
            a = curr

        prev = curr
        curr = (a + b) / 2

    return (a+b) / 2

def newton(f, df, x0, tol):
    prev = 1e+100
    curr = x0
    
    while abs(curr - prev) > tol:
        prev = curr
        curr = curr - f(curr) / df(curr)
    
    return curr

f = lambda x: x**2 - 2
df = lambda x: 2*x

a = 0
b = 2
x0 = 1
tol = 1e-6

print(f'Método da bisseção: {bissecao(f, a, b, tol)}')
print(f'Método de newton: {newton(f, df, x0, tol)}')