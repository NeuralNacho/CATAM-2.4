import numpy as np
import random
import math


def F_inverse(x):
    return -2 * math.log(1-x)
vF_inv = np.vectorize(F_inverse)

N = 1000

def generate_uniform():
    uniform_random_sample = []
    for i in range(1000):
        point = random.random()
        uniform_random_sample.append(point)
    return np.array(uniform_random_sample)

def generate_exponential():
    return vF_inv(generate_uniform())

if __name__ == '__main__':
    uniform_sample = generate_uniform()
    exp_sample = generate_exponential()
    
    uniform_mean = sum(uniform_sample) / N
    exp_mean = sum(exp_sample) / N

    uniform_variance = sum(uniform_sample**2) \
                        / N - uniform_mean**2
    exp_variance = sum(exp_sample**2) / N - exp_mean**2

    print('Uniform mean = ', uniform_mean, 
        '\nUniform variance = ', uniform_variance)
    print('Exponential mean = ', exp_mean, 
        '\nExponential variance = ', exp_variance)
