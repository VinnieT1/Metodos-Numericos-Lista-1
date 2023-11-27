# p - |p|/100 <= p* <= p + |p|/100
def find_interval(p, max_rel_err):
    return (p - abs(p)/100, p + abs(p)/100)

if __name__ == '__main__':
    print('interval for p=150 and max relative error of 1/100:', find_interval(150, 1/100))
    print('interval for p=900 and max relative error of 1/100:', find_interval(900, 1/100))
    print('interval for p=1500 and max relative error of 1/100:', find_interval(1500, 1/100))
    print('interval for p=90 and max relative error of 1/100:', find_interval(90, 1/100))