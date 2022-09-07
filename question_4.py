import matplotlib.pyplot as plt
import numpy as np

from question_1 import get_data

N = 999
data_set = np.array(get_data())
sum1 = sum(data_set[:-1])  # sum of x_n from 0 to 999
sum2 = sum(data_set[1:])  # sum of x_n from 1 to 1000
sum3 = np.dot(data_set[:-1], data_set[:-1]) 
# sum of x_n^2 from 0 to 999
sum4 = np.dot(data_set[:-1], data_set[1:])  # sum of x_nx_n+1

plt.rc('font', size = 30)
plt.plot(data_set, color = 'C4')
plt.xlabel('$t$')
plt.ylabel('$x_{t}$')
plt.show()

determinant = N*sum3 - sum1**2
a_0 = (1 / determinant)*(sum2*sum3 - sum1*sum4)
a_1 = (1 / determinant)*(N*sum4 - sum1*sum2)

RSS = np.dot(data_set[1:] - a_0 - a_1 * data_set[:-1],  
                data_set[1:] - a_0 - a_1 * data_set[:-1])  
# ^ (notice this is N(sigma_bar)^2)
sigma_tilde_sq = RSS / (N-2)
SE = np.sqrt(sigma_tilde_sq*N/determinant)

print(sigma_tilde_sq)
print(SE)

