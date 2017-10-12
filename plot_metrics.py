# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:18:05 2017

@author: mwatson
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
column_index = 2

data = pd.read_csv('combined-wellbeing-indicators-ward-transposed.csv')

ward = data['Ward']
for index in range(len(data.columns)-2):
    x = []
    for i in range(len(ward)): x.append(i)
    metric = data[data.columns[column_index]] 
    metric_name = data.columns[column_index]
    
    
    
    
    
    plt.bar(x,metric,width=0.5,align="center")
    plt.axhline(np.mean(metric), linewidth=3, color='r')
    
    plt.xticks(x,ward)
    plt.tight_layout()
    plt.title("%s"%metric_name)
    plt.savefig("%s by ward.png"%metric_name)
    plt.clf()
    column_index+=1
