import matplotlib.pyplot as plt

def plot_funcao(f, a, b, delta):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys, label='f(x)')

def df(x):
    return 2*x

def plot_bissecao(f, a, b, tol_bissec):
    a_bissec, b_bissec = a, b
    seq_bissec = []
    
    while (b_bissec - a_bissec) / 2 > tol_bissec:
        c_bissec = (a_bissec + b_bissec) / 2
        seq_bissec.append((c_bissec, f(c_bissec)))
        
        if f(a_bissec) * f(c_bissec) < 0:
            b_bissec = c_bissec
        else:
            a_bissec = c_bissec

    plt.plot(*zip(*seq_bissec), marker='o', linestyle='-', color='red', label='Bisseção Points')

def plot_newton(f, df, x0, tol_newton):
    seq_newton = [(x0, f(x0))]
    
    while abs(f(x0)) > tol_newton:
        x0 = x0 - f(x0) / df(x0)
        seq_newton.append((x0, f(x0)))
        
    plt.plot(*zip(*seq_newton), marker='o', linestyle='-', color='blue', label='Newton Points')

plt.figure(figsize=(15, 5))

# Bisseção e Newton
plt.subplot(1, 3, 1)
plot_funcao(lambda x: x**2 - 2, 0, 2, 0.1)
plot_bissecao(lambda x: x**2 - 2, 0, 2, 1e-6)
plot_newton(lambda x: x**2 - 2, df, 1, 1e-6)
plt.title('Ambos os métodos')

# Bisseção
plt.subplot(1, 3, 2)
plot_funcao(lambda x: x**2 - 2, 0, 2, 0.1)
plot_bissecao(lambda x: x**2 - 2, 0, 2, 1e-6)
plt.title('Método da Bisseção')

# Newton
plt.subplot(1, 3, 3)
plot_funcao(lambda x: x**2 - 2, 0, 2, 0.1)
plot_newton(lambda x: x**2 - 2, df, 1, 1e-6)
plt.title('Método de Newton')

plt.tight_layout()
plt.show()