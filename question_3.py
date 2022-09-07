import math
import numpy as np
import matplotlib.pyplot as plt
import math
from question_10 import generate_uniform, generate_exponential

# simulating H_1
uniform_sample = generate_uniform()
exp_sample = generate_exponential()
vec_cos = np.vectorize(math.cos)
normal_sample = np.sqrt(exp_sample) * \
        vec_cos(2*math.pi*uniform_sample)

x_n = 0
x_list = []
a_0 = 1
a_1 = -0.8
for i in range(50):
    x_n = a_0 + a_1*x_n + normal_sample[i]
    x_list.append(x_n)

plt.rc('font', size = 24)
plt.plot(x_list, color = 'C3')
plt.xlabel('$t$')
plt.ylabel('$x_{t}$')
plt.show()

plt.plot(normal_sample)
plt.show()