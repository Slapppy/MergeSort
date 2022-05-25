import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Datasets/mergeSort.csv')
df.columns = ['elements' , 'time']

plt.ylim((None , 0.25))
plt.grid(True)
plt.plot(df['elements'] , df['time'])

plt.title('Сортировка слиянием ' , fontsize = 15)
plt.show()