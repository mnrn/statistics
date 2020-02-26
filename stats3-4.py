import numpy as np
import matplotlib.pyplot as plt

xs = [71, 68, 66, 67, 70, 71, 70, 73, 72, 65, 66]
ys = [69, 64, 65, 63, 65, 62, 65, 64, 66, 59, 62]


def exercise1():
    return np.random.randint(0, 11, 11)


def exercise2():
    rs = exercise1()
    rxys = [[xs[r], ys[r]]for r in rs]
    rxs, rys = zip(*rxys)
    co = np.corrcoef(rxs, rys)
    print(co)


def exercise3():
    cs = []
    for i in range(0, 200):
        rs = exercise1()
        rxys = [[xs[r], ys[r]]for r in rs]
        rxs, rys = zip(*rxys)
        co = np.corrcoef(rxs, rys)
        cs.append(co[0, 1])
    plt.hist(cs)
    plt.show()


if __name__ == '__main__':
    exercise2()
    exercise3()
