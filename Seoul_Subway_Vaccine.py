# -*- coding: utf-8 -*-
"""Colaboratory에 오신 것을 환영합니다

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

from google.colab import files
files.upload()

import pandas as pd
import datetime
import matplotlib.pyplot as plt
data = pd.read_excel('seoul_subway.xlsx')
data2 = pd.read_excel('seoul_vaccine.xlsx')

subway_line_name = data['호선명'].drop_duplicates().sort_values().tolist()
print(subway_line_name)
print(len(subway_line_name))

#data[(data.사용월 == 202101) & (data.호선명 == subway_line_name[0])].loc[:,'04시-05시 승차인원' : '03시-04시 승차인원'].sum().sum()
a = pd.DataFrame()
for i in range(len(subway_line_name)) :
  c = []
  for k in range(9) :
    b = data[(data.사용월 == 202100+k+1) & (data.호선명 == subway_line_name[i])].loc[:,'04시-05시 승차인원' : '03시-04시 승차인원'].sum().sum()
    c.append(b) #호선별/월별 합산
  a[subway_line_name[i]] = c
a

plt.figure(figsize=(5,10))
plt.xlabel('MONTH')
x_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
y_values2 = [0, 0, 0, 3.3, 15.1, 27.1, 31.9, 30.9, 50.3]
ax1 = plt.subplot(2,1,2)
#ax2 = ax1.twinx()
ax2 = plt.subplot(2,1,1)
for j in range(a.shape[1]) :
  y_values = a[a.columns[j]].tolist()
  ax2.plot(x_values, y_values)
ax1.bar(x_values, y_values2, label = 'Vaccine (%)', alpha = 0.7) 
ax1.legend(loc='upper right')
ax2.set_ylabel("Total pessenger who ride subway")    
ax1.set_ylabel("Percent of vaccinated person (%)")    
plt.show()