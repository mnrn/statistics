import numpy as np


def average_difference(xs):
    n = len(xs)
    return sum([abs(xi - xj) for xj in xs for xi in xs]) / (n * n)


def GI(xs):
    me = np.mean(xs)
    ad = average_difference(xs)
    return ad / (2 * me)


if __name__ == '__main__':
    A = [0, 3, 3, 5, 5, 5, 5, 7, 7, 10]
    B = [0, 1, 2, 3, 5, 5, 7, 8, 9, 10]
    C = [3, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    print('Aの平均差 = {:.2f}, ジニ係数 = {:.3f}'.format(average_difference(A), GI(A)))
    print('Bの平均差 = {:.2f}, ジニ係数 = {:.3f}'.format(average_difference(B), GI(B)))
    print('Cの平均差 = {:.2f}, ジニ係数 = {:.3f}'.format(average_difference(C), GI(C)))
