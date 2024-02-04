"""P(inside) * 4 = pi"""

import numpy as np
import matplotlib.pyplot as plt     


np.random.seed(2024)

def one_pi(trials):
      results = []
      x = np.random.uniform(0,1,trials)
      y = np.random.uniform(0,1,trials)
      for i in range(trials):
            if x[i] ** 2 + y[i] ** 2 <= 1:
                  results.append(True)
            else:
                  results.append(False)
      my_pi = 4 * np.mean(results)
      return my_pi

def repetition(trials, repetition):
      pi_list = []
      for i in range(repetition):
           pi_list.append(one_pi(trials))
      final_pi = np.mean(pi_list)
      return final_pi

print(repetition(1000, 10000)) # Trials reduce variance, repetition increase accuracy toward the true value 

