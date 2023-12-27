import matplotlib.pyplot as plt

def graph_f(f, a, b, delta):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys)
    plt.show()

graph_f(lambda x: x**2 + 1, -5, 5, 0.5)