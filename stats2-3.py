import numpy as np


def H(ps):
    return -sum([p * np.log10(p) for p in ps])


if __name__ == '__main__':
    A0 = [a / 100 for a in [32, 19, 10, 24, 15]]
    A10 = [a / 100 for a in [28, 13, 18, 29, 12]]

    print('本年における出身地のエントロピー = {:.3f}'.format(H(A0)))
    print('10年前における出身地のエントロピー = {:.3f}'.format(H(A10)))
