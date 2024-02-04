import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2024)
trials = 100
replications = 1000

def one_event(trials):
      annie = np.random.uniform(10.5,12,1000)
      sam = np.random.uniform(10,11.5,1000)
      probablity_results = list()
      difference_results = list()
      for i in range(len(sam)):
            difference_results.append(annie[i]-sam[i])
            if sam[i] > annie[i]:
                  probablity_results.append(True)
            else:
                  probablity_results.append(False)
      probability = sum(probablity_results) / len(sam)
      difference_answer = np.mean(difference_results)
      return probability, difference_answer

def replicate(trials,replications):
      q1 = list()
      q2 = list()
      for i in range(replications):
            q1.append(one_event(trials)[0])
            q2.append(one_event(trials)[1])
      q1_result = np.mean(q1)
      q2_result = np.mean(q2)
      return  q1_result,q2_result


# print(replicate(1000,100))



def waiting(waiting_time,trials):
      waiting_results = list()
      sam = np.random.uniform(0,90,trials)
      annie = np.random.uniform(30,120,trials)
      for i in range(trials):
            if sam[i] < annie[i]:
                  if sam[i] + waiting_time > annie[i]:
                        waiting_results.append(True)
            elif annie[i] + waiting_time > sam[i]:
                  waiting_results.append(True)
            waiting_results.append(False)
      mean = sum(waiting_results) / trials
      return mean
      

def waiting_replicate(waiting_time,trials,replications):
      rstls = list()
      for i in range(replications+1):
            rstls.append(waiting(waiting_time,trials))
      return np.mean(rstls)

def question_5(trials = 100,replications = 500, upper_bound = None):
      chart = dict()
      for i in range(upper_bound):
            chart[i] = round(waiting_replicate(i,trials,replications),2)
      plt.plot(chart.keys(), chart.values(),"o-", label = "Probability")
      plt.legend()
      plt.axhline(y = .5, color = "r", linestyle = "-")
      plt.title('Probability of meeting for Sam and Annie')
      plt.ylabel('Probability of meeting')
      return plt.show()
      


print(question_5(upper_bound=60))
