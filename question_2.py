from question_1 import get_data
import numpy as np

data_set = np.array(get_data())

N = 999
sum1 = sum(data_set[:-1])  # sum of x_n from 0 to 998
sum2 = sum(data_set[1:])  # sum of x_n from 1 to 999
sum3 = np.dot(data_set[:-1], data_set[:-1]) 
# sum of x_n^2 from 0 to 998
sum4 = np.dot(data_set[:-1], data_set[1:])  # sum of x_nx_n+1
determinant = N*sum3 - sum1**2
print(determinant)

a_0 = (1 / determinant)*(sum2*sum3 - sum1*sum4)
a_1 = (1 / determinant)*(N*sum4 - sum1*sum2)
sigma_sq = (1 / N)*np.dot(data_set[1:] - a_0 - a_1 * 
    data_set[:-1], data_set[1:] - a_0 - a_1 * data_set[:-1])

print('a_0 = ', a_0)
print('a_1 = ', a_1)
print('sigma^2 = ', sigma_sq)
