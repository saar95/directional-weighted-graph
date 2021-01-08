from random import random
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    x = [0.15, 0.3, 0.45, 0.6, 0.75]
    y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
    n = [58, 651, 393, 203, 123]
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i, txt in enumerate(n):
        ax.annotate(n[i], (x[i] + 0.005, y[i] + 0.005),arrowprops=dict(headwidth=7, width=0.5,shrink=0.0))

    plt.plot(x, y)
    plt.show()




