import numpy as np
import matplotlib.pyplot as plt

a_0 = 0.1456657383510946
a_1 = 0.8647726496931831
a_2 = -0.03182985839655377

f_x = lambda x : a_0 + a_1*x + a_2*x**2
vf = np.vectorize(f_x)

x = np.linspace(-10, 10, 1000)

print(a, b)

if __name__ == '__main__':
    plt.rc('font', size = 16)
    plt.plot(x, color = 'C0', label = '$h(x)$')
    plt.plot(x, vf(x), color = 'C1', label = '$f(x)$')
    plt.legend(loc = 'lower right')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()