import numpy as np
import math
import matplotlib.pyplot as plt
def kansu2(x2,y2):
    a2 = x2 ** 2
    b2 = y2 % a2
    if x2 == 0 or y2 == 0:
        print("これは二次関数ではありません")
    if b2 == 0:
        c2 = y2 // a2
        if c2 == 0:
            print("y = 0")
            x2 = np.arange(-10,10,0.1)
            y2 = 0
            plt.plot(x2,y2)
            plt.show()
        elif c2 == 1:
            print("y = x^2")
            x2 = np.arange(-10,10,0.1)
            y2 = x2 ** 2
            plt.plot(x2,y2)
            plt.show()
        else:
            ("y = {}x^2".format(c2))
            x2 = np.arange(-10,10,0.1)
            y2 = c2 * x2 ** 2
            plt.plot(x2,y2)
            plt.show()
    else:
        f = math.gcd(y2,a2)
        y2 = y2 // f
        a2 = a2 // f
        f = y2 / a2
        if y2 < 0:
            print("y = -{}/{}x^2".format(y2, a2))
            x2 = np.arange(-10,10,0.1)
            y2 = y2 / a2 * x2 ** 2
            plt.plot(x2,y2)
            plt.show()
        print("y = {}/{}x^2".format(y2,a2))
        x2 = np.arange(-10,10,0.1)
        y2 = f * x2 ** 2
        plt.plot(x2,y2)
        plt.show()

x2 = input()
y2 = input()
x2 = int(x2)
y2 = int(y2)


kansu2(x2,y2)


