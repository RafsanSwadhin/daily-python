import pandas as pd
import matplotlib.pyplot as plt


trainingdata = pd.read_csv('AirPassengers.csv')

plt.plot(trainingdata['Month'], trainingdata['#Passengers'])
plt.show()