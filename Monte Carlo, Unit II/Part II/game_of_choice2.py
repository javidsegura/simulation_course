import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

""" What is the probability that 1st player wins 5€"""
np.random.seed(2023)

def peter_paul(n = 50):
  win = np.random.choice([-1,1],n,True)
  cumul_win = np.cumsum(win)
  results = [sum(win), sum(cumul_win > 0), max(cumul_win)]
  return(np.array(results))

def peter_paul_rep(n_replicas = 1000, n = 50):
  results = np.zeros((n_replicas,3))
  for i in range(n_replicas):
    exp = peter_paul(n)
    results[i,] = exp
  return(results)

S = peter_paul_rep(1000,50)

df = pd.DataFrame(S)
df.columns = ["Final balance", "On the lead", "Maximum chance"]

print(df.describe())
