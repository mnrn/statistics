import numpy as np


if __name__ == "__main__":
    B = np.array([0, 1, 2, 3, 5, 5, 7, 8, 9, 10])
    std_score = (B - B.mean()) / B.std()
    dev_score = 10 * std_score + 50

    np.set_printoptions(precision=3)
    print('標準得点(Z得点) = {}'.format(std_score))
    print('偏差値得点(T得点) = {}'.format(dev_score))
