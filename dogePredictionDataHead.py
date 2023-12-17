import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
sns.set()
# print(plt.style.available)
plt.style.use('seaborn-v0_8-white')

data = pd.read_csv("DOGE-USD.csv")
print(data.head())
