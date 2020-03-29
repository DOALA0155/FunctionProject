import matplotlib.pyplot as plt
import numpy as np
def kansu1(k,x,y):
    a = k * x
    b = y - a
    if b == 0:
        if k == 0:
            print("y = 0")
            x = np.arange(0, 10, 0.1)
            y = 0
            plt.plot(x, y)
            plt.show()
        elif k == 1:
            print("y = x ")
            x = np.arange(0, 10, 0.1)
            y = x
            plt.plot(x, y)
            plt.show()
        else:
            print("y = {}x".format(k))
            x = np.arange(0, 10, 0.1)
            y = k * x
            plt.plot(x, y)
            plt.show()

    elif b > 0:
        if k == 0:
            print("y = {}".format(b))
            x = np.arange(0, 10, 0.1)
            y = b
            plt.plot(x, y)
            plt.show()
        elif k == 1:
            print("y = x+{}".format(b))
            x = np.arange(0, 10, 0.1)
            y = x + b
            plt.plot(x, y)
            plt.show()
        else:
            print("y = {}x+{}".format(k, b))
            x = np.arange(0, 10, 0.1)
            y = k * x + b
            plt.plot(x, y)
            plt.show()
    else:
        if k == 0:
            print("y = {}".format(b))
            x = np.arange(0, 10, 0.1)
            y = b
            plt.plot(x, y)
            plt.show()
        elif k == 1:
            print("y = x{}".format(b))
            x = np.arange(0, 10, 0.1)
            y = x + b
            plt.plot(x, y)
            plt.show()
        else:
            print("y = {}x{}".format(k, b))
            x = np.arange(0, 10, 0.1)
            y = k * x + b
            plt.plot(x, y)
            plt.show()
k = input()
x = input()
y = input()
k = int(k)
x = int(x)
y = int(y)
print(kansu1(k,x,y))





