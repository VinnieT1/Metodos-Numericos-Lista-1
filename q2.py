import math

def abs_err(p, p_):
    return abs(p - p_)

def rel_err(p, p_):
    return abs((p - p_) / p)

if __name__ == '__main__':
    print(f'abs error for p=1 and p*=0.9994:', abs_err(1, 0.9994))
    print(f'rel error for p=1 and p*=0.9994:', rel_err(1, 0.9994))
    print('')

    print(f'abs error for p=124 and p*=7:', abs_err(124, 7))
    print(f'rel error for p=124 and p*=7:', rel_err(124, 7))
    print('')
    
    print(f'abs error for p=e^10 and p*=22000:', abs_err(math.exp(10), 22000))
    print(f'rel error for p=e^10 and p*=22000:', rel_err(math.exp(10), 22000))
    print('')
    
    print(f'abs error for p=8! and p*=39900:', abs_err(math.factorial(8), 39900))
    print(f'rel error for p=8! and p*=39900:', rel_err(math.factorial(8), 39900))
    print('')