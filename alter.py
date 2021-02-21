import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# possible categories
categories = [
    "weil es billig ist",
    "weil es umweltfreundlich ist",
    "weil es gesund ist",
    "weil es mir spass macht",
    "weil es schnell ist"
]

# list for storing the occurences of different categories
occurences = []

# extract the row with strings to sort and convert to series
df = pd.read_csv('data/bereinigt.csv')

#print(df['Grund'].str.count(categories[0]).sum())

for i in range(len(categories)):
    occurences.append(df['Grund'].str.count(categories[i]).sum())

plt.barh(categories, occurences)
plt.title('grund')
plt.tight_layout()
plt.show()