import numpy as np
from numpy.linalg import inv

from question_1 import get_data

data_set = np.array(get_data())
N = 999
sum1 = sum(data_set[:-1])
sum2 = sum(data_set[:-1]**2)
sum3 = sum(data_set[:-1]**3)
sum4 = sum(data_set[:-1]**4)

XTX = np.array([N, sum1, sum2, sum1, sum2, sum3, 
                sum2, sum3, sum4]).reshape((3, 3))
XTX_inv = inv(XTX)
XTY = np.array([sum(data_set[1:]), np.dot(data_set[:-1], 
    data_set[1:]), np.dot(data_set[:-1]**2, data_set[1:])])

beta = np.dot(XTX_inv, XTY)
a_0, a_1, a_2 = beta[0], beta[1], beta[2]
sigma_sq = sum((data_set[1:] - a_0 - a_1*data_set[:-1] 
                - a_2*data_set[:-1]**2)**2) / N

print('a_0 = ', a_0)
print('a_1 = ', a_1)
print('a_2 = ', a_2)
print('sigma^2 = ', sigma_sq)
