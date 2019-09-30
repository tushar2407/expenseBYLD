import os
from django.conf import settings

from bs4 import BeautifulSoup
with open(os.path.join(settings.BASE_DIR, 'lmao.html')) as fp:
    soup = BeautifulSoup(fp,"html.parser")
i=0
j=0
b=[]
c=[]
d=[]
def info(a,x,j):
        b=a[3*j].span.string
        y = x[j].find("div", {"class": "data"})
        z = y.find_all("li")
        if z[0].string!="Payment received":
                print(b[3:])
                return b[3:]
                print(q, z[1].string ,z[3].string)
                return q, z[1].string, z[3].string


x = soup.find_all("div", {"class": "Cell Cell1"})
a = soup.find_all("div", {"class": "Cell Cell3"})
while i<len(x):
    c.append(info(a,x,i))
    i=i+1
    
    
def returns():
    return c


