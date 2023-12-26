from decimal import *

print('133 - 0.499\n')
exact = 133 - 0.499

print('truncamento com 3 digitos:')

getcontext().prec=3
getcontext().rounding=ROUND_DOWN

approx = Decimal("133") - Decimal("0.499")
print(f'exato: {exact}')
print(f'aproximacao: {approx}')

print(f'erro absoluto: {abs(exact - float(approx))}')
print(f'erro relativo: {abs(exact - float(approx)) / exact}\n')

# ------------------------------------------------------------

print('truncamento com 4 digitos:')

getcontext().prec=4
getcontext().rounding=ROUND_DOWN

approx = Decimal("133") - Decimal("0.499")
print(f'exato: {exact}')
print(f'aproximacao: {approx}')

print(f'erro absoluto: {abs(exact - float(approx))}')
print(f'erro relativo: {abs(exact - float(approx)) / exact}\n')

# ------------------------------------------------------------

print('arredondamento com 3 digitos:')

getcontext().prec=3
getcontext().rounding=ROUND_HALF_UP

approx = Decimal("133") - Decimal("000.499")
print(f'exato: {exact}')
print(f'aproximacao: {approx}')

print(f'erro absoluto: {abs(exact - float(approx))}')
print(f'erro relativo: {abs(exact - float(approx)) / exact}\n')

# ------------------------------------------------------------

print('arredondamento com 4 digitos:')

getcontext().prec=4
getcontext().rounding=ROUND_HALF_UP

approx = Decimal("133") - Decimal("000.499")
print(f'exato: {exact}')
print(f'aproximacao: {approx}')

print(f'erro absoluto: {abs(exact - float(approx))}')
print(f'erro relativo: {abs(exact - float(approx)) / exact}\n')