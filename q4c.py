from decimal import *
from math import e

exact = (13/14 - 6/7) / (2*e - 5.4)

print(f'valor exato: {exact}')
# ----------------------------------------
getcontext().prec = 3
getcontext().rounding = ROUND_DOWN
print(f'truncamento 3 digitos: {(Decimal(13)/Decimal(14) - Decimal(6)/Decimal(7)) / (Decimal(2)*Decimal(e) - Decimal(5.4))}')
# ---------------------------------------------------------
getcontext().prec = 4
getcontext().rounding = ROUND_DOWN
print(f'truncamento 4 digitos: {(Decimal(13)/Decimal(14) - Decimal(6)/Decimal(7)) / (Decimal(2)*Decimal(e) - Decimal(5.4))}')
# ---------------------------------------------------------
getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP
print(f'arredondamento 3 digitos: {(Decimal(13)/Decimal(14) - Decimal(6)/Decimal(7)) / (Decimal(2)*Decimal(e) - Decimal(5.4))}')
# ---------------------------------------------------------
getcontext().prec = 4
getcontext().rounding = ROUND_HALF_UP
print(f'arredondamento 4 digitos: {(Decimal(13)/Decimal(14) - Decimal(6)/Decimal(7)) / (Decimal(2)*Decimal(e) - Decimal(5.4))}')