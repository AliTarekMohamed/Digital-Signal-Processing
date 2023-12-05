import numpy as np


def correlation(ysignal1, ysignal2):
    r = []
    correlationsignal = []

    N = len(ysignal1)

    for j in range(0, N):
        value = 0
        for n in range(0, N):
            d = n + j
            if (d >= N):
                d -= N
            value += (ysignal1[n] * ysignal2[d])
        r.append(value / N)

    denominator = 0
    y1square = 0
    y2square = 0

    for i in range(0, N):
        y1square += np.power(ysignal1[i], 2)
        y2square += np.power(ysignal2[i], 2)

    denominator = (np.sqrt(y1square * y2square)) / N

    for i in r:
        correlationsignal.append(i / denominator)

    return correlationsignal
