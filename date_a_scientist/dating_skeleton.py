import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Create your df here:
df = pd.read_csv('profiles.csv')
print(df.drinks.value_counts())

print(df[['essay1','sex']].iloc[1])

plt.hist(df.age, bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(16, 80)
plt.show()

plt.cla()

plt.bar(range(len(df.sex)),df.sex.value_counts().values)
plt.show()
