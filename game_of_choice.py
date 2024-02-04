import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

""" What is the probability that 1st player wins 5€"""
np.random.seed(2023)


def single_game(trials):
      z = np.sum(np.random.choice([-1,1], trials))
      return z

def repetition(trials,repetition):
      results = []
      for i in range(repetition):
            results.append(single_game(trials))
      return results

repetitions_value  = 1000
cool = repetition(50,repetitions_value)

value,count = np.unique(cool, return_counts = True)

table = dict(zip(value,count))

for key in table.keys():
     if key == 0:
           z = table[key]/repetitions_value
print(z,table)


