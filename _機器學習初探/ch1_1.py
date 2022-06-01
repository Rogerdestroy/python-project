from IPython.display import YouTubeVideo
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

#YoutubeVideo('Z8t4k0Q8e8Y',width=640,height=360)

arr = np.random.normal(size=100000)
print(arr,end='\n------------------------\n')

fig = plt.figure()
ax = plt.axes()
ax.hist(arr,bins=50)
plt.show()

eps = 1e-06
p = np.linspace(0 + eps, 1-eps, 10000)
log_loss_0 = -np.log(1-p)
log_loss_1 = -np.log(p)
print(p)
print(log_loss_0)
print(log_loss_1)

