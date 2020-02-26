import numpy.random as rd

if __name__ == '__main__':
    # 今回は10万回試行する。
    N = 100_000
    rep = [1 if 6 in rd.randint(1, 6 + 1, 4) else 0 for x in range(N)]
    print(
        'さいころを4回投げ、6の目が1回も出ないかどうかのシュミレートを10万回行ったところ、その確率は  {:.4f}'.format(
            1 -
            sum(rep) /
            N))
