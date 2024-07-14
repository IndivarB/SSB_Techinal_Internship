import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('bmh')
df = pd.read_csv('Dataset.csv')
x=df['category_name_1']
y=df['payment_method']
plt.xlabel('X axis',fontsize=18)
plt.ylabel('Y axis',fontsize=18)
plt.bar(x,y)
plt.show()