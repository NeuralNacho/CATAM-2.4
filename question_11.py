import numpy as np
import math
from matplotlib import pyplot as plt
from question_1 import get_data
from question_10 import generate_uniform, generate_exponential

uniform_sample = generate_uniform()
exp_sample = generate_exponential()

vec_cos = np.vectorize(math.cos)

normal_sample = np.sqrt(exp_sample) * \
   vec_cos(2*math.pi*uniform_sample)

a_0 = 0.3152583364332162
a_1 =  1.2525659122769783
a_2 =  -0.10077141891440472
a_3 =  -0.047440285420029184
sigma_sq = 0.6

model_normal_sample = math.sqrt(0.6)*normal_sample

y_n = 0
y_list = [0]
for i in range(999):
    y_n = a_0 + a_1*y_n + a_2*y_n**2 + a_3*y_n**3 + \
                    model_normal_sample[i]
#    if y_n < -5.5:
#        y_n = 0
    y_list.append(y_n)

S_n = 0
Sn_list = []
for n in range(1000):
    S_n += y_list[n]
    Sn_list.append(S_n)

xS_n = 0 
xSn_list = []
data_set = get_data()
for n in range(1000):
    xS_n += data_set[n]
    xSn_list.append(xS_n)

y_list_x = y_list.copy() # for diagram (iii)  
y_list_x.pop(-1) 
y_list_y = y_list.copy()
y_list_y.pop(0)

plt.rc('font', size = 24)

plt.figure(1) # plot of S_n
plt.grid(linestyle = '--', linewidth = 0.5)
plt.subplot2grid(shape = (1, 5), loc = (0, 0), colspan = 2)
plt.plot(Sn_list, color = 'C2')
plt.xlabel('$n$')
plt.ylabel('$S_{n}$')
plt.title('Model data')
plt.subplot2grid(shape = (1, 5), loc = (0, 3), colspan = 2)
plt.plot(xSn_list, color = 'C6')
plt.xlabel('$n$')
plt.ylabel('$S_{n}$')
plt.title('Actual data')

plt.figure(2) # histogram
plt.hist(y_list, bins = 20, color = 'C7')
plt.xlabel('$y_{n}$')
plt.ylabel('Number of points')

plt.figure(3) # y_{n+1} against y_{n}
plt.grid(linestyle = '--', linewidth = 0.5)
plt.scatter(y_list_x, y_list_y, s = 7, color = 'C4')
plt.xlabel('$y_{n}$')
plt.ylabel('$y_{n+1}$') 

plt.show()

