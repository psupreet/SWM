# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:05:03 2021

@author: vikky
"""

import pandas as pd
data = pd.read_csv("dataset.csv")
data= data[data['fraud']==1]
customers = list(data['customer'])
cus =[]
for c in customers :
    cus.append(c[1:-1])
customers=cus

merchant = list(data['merchant'])
cus =[]
for c in merchant :
    cus.append(c[1:-1])
merchant=cus




amount = list(data['amount'])
fraud =  list(data['fraud'])
#data=data[:2000]
size = len(customers)

d3 = {}
d3["nodes"] = [{"id" : "" , "group" : 0}]
d3["links"] = [{"source": "", "target": "", "value": 1}]

nodes= []
#customer
for c in set(customers) : 
    node = { }
    node['id'] = c 
    node['group'] =0
    nodes.append(node)
#merchant
for c in set(merchant) : 
    node = { }
    node['id'] = c 
    node['group'] =1
    nodes.append(node)    
    
#links    
links=[]
for i in range(len(data)) :
    link={}
    d =data.iloc[i,:]
    source = d['customer'][1:-1]
    target = d['merchant'][1:-1]
    value = d['amount']
   
    link['source']=source
    link['target'] =target
    link['value'] = int(0)
    link['amount']=d['amount']
    link['gender']=d['gender'][1:-1]
    links.append(link)


d3["nodes"]= nodes
d3["links"]=links



import json

with open('total.json', 'w') as json_file:
  json.dump(d3, json_file)







    
    
    

