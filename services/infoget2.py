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
                d=[]
                d.append(b[3:])
                z[1]=z[1].string
                q=z[1].find('#')
                z[1]=z[1][:q]
                d.append(z[1])
                d.append(z[3].string[:10])
                print(z[3].string[:10], b[3:])           
                #print(type(d))
                return d
                #return b[3:], z[1].string, z[3].string[:10]
                #return q, z[2].string, z[3].string


x = soup.find_all("div", {"class": "Cell Cell1"})
a = soup.find_all("div", {"class": "Cell Cell3"})
while i<len(x):
    if info(a,x,i) != None:
            c.append(info(a,x,i))
    i=i+1

def returns():
   # print(c)
    return c



