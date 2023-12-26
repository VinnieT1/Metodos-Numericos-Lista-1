from decimal import *

def bisection_exact(f, a, b, N):
    if f(a) * f(b) >= 0:
        return None
    
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return m_n
        else:
            return None
    return (a_n + b_n)/2

def bisection_approx(f, a, b, N):
    if f(a) * f(b) >= 0:
        return None
    
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return Decimal(m_n) / Decimal(1)
        else:
            return None
    return Decimal(a_n + b_n) / Decimal(2)

f = lambda x: ((x / 3 - 123 / 4) * x) + 1/6
f_approx = lambda x: ((Decimal(x) / Decimal(3) - Decimal(123) / Decimal(4)) * Decimal(x)) + Decimal(1)/Decimal(6)

exact1 = bisection_exact(f, -10, 10, 1000)
exact2 = bisection_exact(f, 90, 100, 1000)

print(f'raizes exatas: {exact1}, {exact2}')
# ---------------------------------------------------------
getcontext().prec = 3
getcontext().rounding = ROUND_DOWN
print(f'truncamento 3 digitos: {bisection_approx(f_approx, -10, 10, 1000)}, {bisection_approx(f_approx, 90, 100, 1000)}')
# ---------------------------------------------------------
getcontext().prec = 4
getcontext().rounding = ROUND_DOWN
print(f'truncamento 4 digitos: {bisection_approx(f_approx, -10, 10, 1000)}, {bisection_approx(f_approx, 90, 100, 1000)}')
# ---------------------------------------------------------
getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP
print(f'arredondamento 3 digitos: {bisection_approx(f_approx, -10, 10, 1000)}, {bisection_approx(f_approx, 90, 100, 1000)}')
# ---------------------------------------------------------
getcontext().prec = 4
getcontext().rounding = ROUND_HALF_UP
print(f'arredondamento 4 digitos: {bisection_approx(f_approx, -10, 10, 1000)}, {bisection_approx(f_approx, 90, 100, 1000)}')