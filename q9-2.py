from math import sin, cos, pi, log
import matplotlib.pyplot as plt

def newton_approx(f, df, x0, tol):
    prev = 1e+100
    curr = x0
    f_c = f(curr)

    xs = [curr]
    ys = [f_c]

    while abs(curr - prev) > tol:
        prev = curr
        curr = curr - f(curr) / df(curr)
        f_c = f(curr)

        xs.append(curr)
        ys.append(f_c)

    return xs, ys

def bisection_approx(f, a, b, tol):
    prev = 1e+100
    curr = (a + b) / 2
    f_c = f(curr)

    xs = [curr]
    ys = [f_c]
    while abs(curr - prev) > tol:
        if f(a) * f_c < 0:
            b = curr
        else:
            a = curr

        prev = curr
        curr = (a + b) / 2
        f_c = f(curr)

        xs.append(curr)
        ys.append(f_c)
    
    return xs, ys

def plot_funcao(f, a, b, delta):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys, label='f(x)')

def plot_bissecao(f, a, b, tol):
    approx = bisection_approx(f, a, b, tol)
    plt.plot(approx[0], approx[1], marker='o', linestyle='-', color='red', label='Bisseção Points')

def plot_newton(f, df, x0, tol):
    approx = newton_approx(f, df, x0, tol)
    plt.plot(approx[0], approx[1], marker='o', linestyle='-', color='blue', label='Newton Points')

def plot_tudo(function, derivative, lower, upper, x0):
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plot_funcao(function, lower, upper, 0.05)
    plot_bissecao(function, lower, upper, 1e-6)
    plot_newton(function, derivative, x0, 1e-6)
    plt.title('Ambos os métodos')

    # Bisseção
    plt.subplot(1, 3, 2)
    plot_funcao(function, lower, upper, 0.05)
    plot_bissecao(function, lower, upper, 1e-6)
    plt.title('Método da Bisseção')

    # Newton
    plt.subplot(1, 3, 3)
    plot_funcao(function, lower, upper, 0.05)
    plot_newton(function, derivative, x0, 1e-6)
    plt.title('Método de Newton')

    plt.tight_layout()
    plt.show()

a = lambda x: x - 2 ** (-x)
dfa = lambda x: log(2) * 2 ** (-x) + 1
xa = 0.5
la = 0
ua = 1

b = lambda x: x + 1 - 2*sin(pi*x)
dfb = lambda x: 1 - 2*pi*cos(pi*x)
xb = 0.25
lb = 0
ub = 0.5

c = lambda x: 2*x*cos(2*x) - (x + 1) ** 2
dfc = lambda x: -2*(1 + x - cos(2*x) + 2*x*sin(2*x))
xc = -2.5
lc = -3
uc = -2

d = lambda x: log(x) - 2 ** x + x ** 2
dfd = lambda x: 1/x + 2*x - log(2) * 2 ** x
xd = 4
ld = 3
ud = 5

for function, derivative, lower, upper, x0 in [(a, dfa, la, ua, xa), (b, dfb, lb, ub, xb), (c, dfc, lc, uc, xc), (d, dfd, ld, ud, xd)]:
    plot_tudo(function, derivative, lower, upper, x0)