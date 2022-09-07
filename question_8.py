import numpy as np
import matplotlib.pyplot as plt

a_0 = 0.1456657383510946
a_1 = 0.8647726496931831
a_2 = -0.03182985839655377

f_x = lambda x : a_0 + a_1*x + a_2*x**2
vf = np.vectorize(f_x)

x = np.linspace(-6, 5, 1000)
curve_data = vf(x)
a, b = np.polyfit(x, curve_data, 1)

print(a,b)

h_x = lambda x: a*x + b
vh = np.vectorize(h_x)

if __name__ == '__main__':
    plt.rc('font', size = 16)
    plt.plot(x, vh(x), color = 'C2', label = '$h(x)$')
    plt.plot(x, vf(x), color = 'C3', label = '$f(x)$')
    plt.legend(loc = 'lower right')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()