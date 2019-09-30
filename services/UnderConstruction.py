#!/usr/bin/env python
# coding: utf-8

# In[129]:


#Merchant models, spent and expected


# In[147]:

import os
import numpy as np
from datetime import *
import matplotlib.dates
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import shutil

# In[148]:


from bs4 import BeautifulSoup
with open("lmao.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")
i=0
j=0
b=[]
c=[]
d=[]
e=[]
def info(a,x,j):
        b=a[3*j].span.string
        y = x[j].find("div", {"class": "data"})
        z = y.find_all("li")
        if z[0].string!="Payment received":
                #print(z[3].string[:10], b[3:])           
                return b[3:]
                #return q, z[2].string, z[3].string

def info1(a,x,j):
        b=a[3*j].span.string
        y = x[j].find("div", {"class": "data"})
        z = y.find_all("li")
        if z[0].string!="Payment received":
                #print(z[3].string[:10], b[3:])  
                dstr=z[3].string[:10]
                return dstr[5:7]+'/'+dstr[-2:]+'/'+dstr[:4]
                #return q, z[2].string, z[3].string
        
x = soup.find_all("div", {"class": "Cell Cell1"})
a = soup.find_all("div", {"class": "Cell Cell3"})
while i<(len(x)-1):
        add=info(a,x,i)
        add1=info1(a,x,i)
        if(add!=None):
                e.append(add1)
                c.append(add)
        i=i+1

e=e[::-1]
c=c[::-1]


# In[149]:


limit=5000
dates=[]
values=[]
x=[]
xnp=np.array([])
sd=date(int(e[0][-4:]),int(e[0][:2]),int(e[0][3:5]))
ed=date(int(e[-1][-4:]),int(e[-1][:2]),int(e[-1][3:5]))
diff=ed-sd
for i in range(diff.days):
    dstr=str(sd+timedelta(days=i))
    dstr=dstr[5:7]+'/'+dstr[-2:]+'/'+dstr[:4]
    dates.append(dstr)
for j in range(len(dates)):
    values.append(-999)
for k in range(1,len(dates)+1):
    x.append(k)
for o in range(1,len(dates)+1):
    xnp=np.append(xnp,o)


# In[150]:
def givesum(i,count):
    d=i
    rsum=0
    while(i<(d+count)):
        rsum+=float(c[i])
        i+=1
    return rsum    


i=0
values_final=[]
while i<len(dates):
    count=e.count(dates[i])
    if(count>0):
        k=e.index(dates[i])
        getsum=givesum(k,count)
        index=dates.index(dates[i])
        values[index]=getsum
        values_final.append(getsum)
    i+=1


# In[151]:




# In[152]:


"""values[0]=100
values[1]=100
values[2]=200
values[3]=300
values[4]=450"""


# In[153]:


date_objects = [datetime.strptime(date, '%m/%d/%Y').date() for date in dates]


# In[154]:


def can_calculate():
    check=-999
    if (values[0]!=check) & (values[1]!=check) & (values[2]!=check) & (values[3]!=check) & (values[4]!=check):
        return True
    else: 
        return False


# In[155]:


def mean(list):
    sum=0
    for i in range(count):
        sum+=list[i]
    return sum/count


# In[166]:


num=0
den=0
count=0
for i in range(len(values)):
    if(values[i]!=-999):
        count+=1
for i in range(len(values)):
    if(values[i]!=-999):
        num += (x[i]-mean(x))*(values[i]-mean(values))
        den += (x[i]-mean(x))*(values[i]-mean(values))

m=num/den
c=mean(values) - (m*mean(x)) + 50
Y=m*xnp+c

Y1=np.array([])
Y1=np.append(Y1,Y[0])
i=1
while i<Y.size:
    j=0
    sumnp=0
    while j<=i:
        sumnp+=Y[j]
        j+=1
    Y1=np.append(Y1,sumnp)
    i+=1


sumvalues=values[:]
i=1
while i<len(values):
    j=0
    sumval=0
    if values[i]!=-999:
        while j<=i:
            if(values[j]!=-999):
                sumval+=values[j]
            j+=1
        sumvalues[i]=sumval
    i+=1


# In[167]:


date_anchors=[sd,ed]
prob_expenditure=[np.sum(Y),np.sum(Y)]
limit_expenditure=[limit,limit]


# In[168]:


if can_calculate():
    
    fig, ax = plt.subplots()
    ax.plot_date(date_objects, values, markerfacecolor='CornflowerBlue', markeredgecolor='white')
    fig.autofmt_xdate()
    ax.set_xlim([sd, ed])
    ax.set_ylim([0, 1000])
    plt.scatter(date_objects, values, color='navy')
    plt.plot(date_objects,Y)
    plt.title("Daily Expenditure")
    plt.xlabel("Date -->", fontdict=None, labelpad=None)
    plt.ylabel("Rupees -->", fontdict=None, labelpad=None)
    plt.savefig('foo1.png', bbox_inches='tight')
    shutil.copy('foo1.png', 'C:\Users\Tushar\expense\static')


# In[169]:


if can_calculate():
    fig, ax = plt.subplots()
    ax.plot_date(date_objects, sumvalues, markerfacecolor='PinK', markeredgecolor='white')
    fig.autofmt_xdate()
    ax.set_xlim([sd, ed])
    ax.set_ylim([0, 10000])
    plt.plot(date_anchors,limit_expenditure)
    if(limit_expenditure[0]>prob_expenditure[0]):
        plt.plot(date_anchors,prob_expenditure,color="Green")
    else:
        plt.plot(date_anchors,prob_expenditure,color="Red")
    
    #plt.plot(date_objects,Y1,color='Grey')
    plt.title("Probable Monthly Expenditure")
    plt.xlabel("Date -->", fontdict=None, labelpad=None)
    plt.ylabel("Rupees -->", fontdict=None, labelpad=None)
    plt.savefig('foo2.png', bbox_inches='tight')
    shutil.copy('foo2.png', 'C:\Users\Tushar\expense\static')

# In[ ]:


#Color codes: 
"""
Graph1: 
blue: your expenditures on that day
orange: avg daily expenditures on that shop

Graph2:
pink: total expenditures on that shop day wise
gray: probabale total expenditures on that shop
orange: your set monthly limit
red: if probable sum crosses your limit 
green : if probable sum doesnt cross your limit
"""
def returns1():
    return int(sumvalues[-1])
