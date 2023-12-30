from math import sin, cos, pi, log

def newton_approx(f, df, x0, tol):
    prev = 1e+100
    curr = x0

    i = 0
    while abs(curr - prev) > tol:
        prev = curr
        curr = curr - f(curr) / df(curr)
        i += 1

    return i, curr

def bisection_approx(f, a, b, tol):
    curr = (a + b) / 2
    i = 0
    while abs(b - a) > tol:
        f_c = f(curr)

        if f(a) * f_c < 0:
            b = curr
        else:
            a = curr

        curr = (a + b) / 2
        i += 1
    
    return i, curr

a = lambda x: x - 2 ** (-x)
dfa = lambda x: log(2) * 2 ** (-x) + 1

b = lambda x: x + 1 - 2*sin(pi*x)
dfb = lambda x: 1 - 2*pi*cos(pi*x)

c = lambda x: 2*x*cos(2*x) - (x + 1) ** 2
dfc = lambda x: -2*(1 + x - cos(2*x) + 2*x*sin(2*x))

d = lambda x: log(x) - 2 ** x + x ** 2
dfd = lambda x: 1/x + 2*x - log(2) * 2 ** x

a_bisection = bisection_approx(a, 0, 1, 1e-4)
a_newton = newton_approx(a, dfa, 0.5, 1e-4)

b_bisection = bisection_approx(b, 0, 0.5, 1e-4)
b_newton = newton_approx(b, dfb, 0.25, 1e-4)

c_bisection = bisection_approx(c, -3, -2, 1e-4)
c_newton = newton_approx(c, dfc, -2.5, 1e-4)

d_bisection = bisection_approx(d, 3, 5, 1e-4)
d_newton = newton_approx(d, dfd, 4, 1e-4)

print('a) iteracoes p/ bisecao:', a_bisection[0], '\nvalor aproximado:', a_bisection[1])
print('a) iteracoes p/ newton:', a_newton[0], '\nvalor aproximado:', a_newton[1])

print('\nb) iteracoes p/ bisecao:', b_bisection[0], '\nvalor aproximado:', b_bisection[1])
print('b) iteracoes p/ newton:', b_newton[0], '\nvalor aproximado:', b_newton[1])

print('\nc) iteracoes p/ bisecao:', c_bisection[0], '\nvalor aproximado:', c_bisection[1])
print('c) iteracoes p/ newton:', c_newton[0], '\nvalor aproximado:', c_newton[1])

print('\nd) iteracoes p/ bisecao:', d_bisection[0], '\nvalor aproximado:', d_bisection[1])
print('d) iteracoes p/ newton:', d_newton[0], '\nvalor aproximado:', d_newton[1])