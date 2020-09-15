# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:59:22 2020

@author: nipunn
"""

import pandas as pd
import numpy as np
import array as arr
import tables as tb
dataset=pd.read_csv('mobiles dataset.csv')

dataset=dataset.iloc[:,1:]

m=dataset.shape

coloumn_rms=[]

for j in range(0,m[1]):
    sum=0
    for i in range(0,m[0]):
        sum=sum+((dataset.iloc[i,j])**2)
    coloumn_rms.append(sum**0.5)
    
 
new_dataset=dataset    
   
ideal_best=[]
ideal_worst=[]

weights_ratio=[]

impacts=[]

for j in range(0,m[1]):
    weights_ratio.append(1)
    impacts.append('+')
    
impacts[7]='-'
impacts[8]='-'


for j in range(0,m[1]):
    for i in range(0,m[0]):
        new_dataset.iloc[i,j]=new_dataset.iloc[i,j]/coloumn_rms[j]




for j in range(0,m[1]):
    if impacts[j]=='+':
        ideal_best.append(max(new_dataset.iloc[j,:]))
        ideal_worst.append(min(new_dataset.iloc[j,:]))
    else:
        ideal_worst.append(max(new_dataset.iloc[j,:]))
        ideal_best.append(min(new_dataset.iloc[j,:]))

best_ed=[]
worst_ed=[]

for i in range(0,m[0]):
    sum1=0
    sum2=0
    for j in range(0,m[1]):
        sum1=sum1+(new_dataset.iloc[i,j]-ideal_best[j])**2
        sum2=sum2+(new_dataset.iloc[i,j]-ideal_worst[j])**2
    best_ed.append(sum1**0.5)
    worst_ed.append(sum2**0.5)    


new_dataset['best_ed']=best_ed
new_dataset['worst_ed']=worst_ed

perfomance_score=[]

for i in range(0,m[0]):
    perfomance_score.append(worst_ed[i]/(worst_ed[i]+best_ed[i]))

new_dataset['Perfomance Score']=perfomance_score

new_dataset['Rank']=new_dataset['Perfomance Score'].rank(ascending=False)

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)

result_data=new_dataset.iloc[:,(m[1]+2):(m[1]+4)]


ID=[]
for i in range(0,m[0]):
    ID.append(i+1)

result_data['ID']=ID

result_data=result_data[['ID','Perfomance Score','Rank']]

print(result_data)

