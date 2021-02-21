import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_excel('data/velozaehler.xlsx', sheet_name='data')

plt.subplot(3, 1, 1).plot(df['Tiefenaustrasse 2020'])
plt.subplot(3, 1, 1).plot(df['Tiefenaustrasse 2019'])
plt.subplot(3, 1, 1).plot(df['Tiefenaustrasse 2018'])
plt.subplot(3, 1, 1).set_title('Tiefenaustrasse')

plt.subplot(3, 1, 2).plot(df['Schwarzenburgstrasse 2020'])
plt.subplot(3, 1, 2).plot(df['Schwarzenburgstrasse 2019'])
plt.subplot(3, 1, 2).plot(df['Schwarzenburgstrasse 2018'])
plt.subplot(3, 1, 2).set_title('Schwarzenburgstrasse')

plt.subplot(3, 1, 3).plot(df['Falkenplatz 2020'])
plt.subplot(3, 1, 3).plot(df['Falkenplatz 2019'])
plt.subplot(3, 1, 3).plot(df['Falkenplatz 2018'])
plt.subplot(3, 1, 3).set_title('Falkenplatz')

plt.tight_layout()
plt.show()