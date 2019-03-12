# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:48:04 2019

@author: Michael
"""

#### import pakcages

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import pandas as pd
import numpy as np

##### declare global variables
to_excel = 0
#####read excel file
data = pd.read_excel('Example_data.xlsx')


##### intial analytics
data.info()
d_data = data.describe()

d = data['Category']




datacol = data.columns
### export to excel
country = data.groupby('Delivery Location Plant Country').size()
if to_excel == 1:
    country.to_excel('country_bmip.xlsx')

'''
for x in datacol:
    print(x)
    d = data[x]
    plt.figure()
    sns.countplot(x=d, data=data)
'''

	



'''
	
# Set the size of the plot
plt.figure(figsize=(14,7))
 
# Create a colormap
colormap = np.array(['red', 'lime', 'black'])
 
# Plot Sepal
plt.subplot(1, 2, 1)
plt.scatter(data.Category, data.LOTS, s=40)
plt.title('Sepal')

plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, c=colormap[data.LOTS], s=40)
plt.title('Petal')


model = KMeans(n_clusters=3)
model.fit(x)

# Set the size of the plot
plt.figure(figsize=(14,7))
 
# Create a colormap
colormap = np.array(['red', 'lime', 'black'])
# Plot the Models Classifications
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('K Mean Classification')
'''



