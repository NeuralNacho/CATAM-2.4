from question_1 import get_data

import numpy as np
import matplotlib.pyplot as plt

data_set = np.array(get_data())

plt.rc('font', size = 16)
plt.hist(data_set, bins = 50, color = 'C2')
plt.xlabel('$x_{n}$')
plt.ylabel('Number of points')
plt.show()
