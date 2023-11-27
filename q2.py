def abs_err(p, p_):
    return abs(p - p_)

def rel_err(p, p_):
    return abs((p - p_) / p)

if __name__ == '__main__':
    p = 1
    p_ = 0.9

    print('abs error:', p)
    print('rel error:', p_)