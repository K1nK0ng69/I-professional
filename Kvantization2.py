import math
import numpy as np
from scipy.stats import pearsonr

def solve():
    lambda_val = float(input())
    x0, x1, x2 = map(float, input().split(','))

    y_values = [0, 0, 0, 0]

    y1 = 0.31681 * (x0 / 2)
    y2 = 0.42933 * (x1 / 2)
    y3 = 0.84576 * (x2 / 2)

    norm_factor = 1.0 / math.sqrt(y1 ** 2 + y2 ** 2 + y3 ** 2)
    y1 *= norm_factor
    y2 *= norm_factor
    y3 *= norm_factor

    y_values[0] = 0
    y_values[1] = y1
    y_values[2] = y2
    y_values[3] = y3

    x = np.random.laplace(0, lambda_val, 10000)
    y = np.zeros_like(x)

    for i in range(len(x)):
        if abs(x[i]) <= x0:
            y[i] = y_values[0]
        elif x0 < abs(x[i]) <= x1:
            y[i] = y_values[1] if x[i] > 0 else -y_values[1]
        elif x1 < abs(x[i]) <= x2:
            y[i] = y_values[2] if x[i] > 0 else -y_values[2]
        else:
            y[i] = y_values[3] if x[i] > 0 else -y_values[3]

    correlation = pearsonr(x, y)[0]

    print(f"{correlation:.5f}")
    print(f"{y_values[0]:.5f},{y_values[1]:.5f},{y_values[2]:.5f},{y_values[3]:.5f}")

solve()
