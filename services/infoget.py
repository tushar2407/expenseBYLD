from bs4 import BeautifulSoup
import os
from django.conf import settings
with open(os.path.join(settings.BASE_DIR, 'lmao.html')) as fp:
    soup = BeautifulSoup(fp,"html.parser")
i=0
j=0
b=[]
c=[]
d=[]
def info2(a,j):
        b=a[3*j].span.string
        print(b[3:])
        return b[3:]

def info1(x,i):
        y = x[i].find("div", {"class": "data"})
        z = y.find_all("li")
        print(z[2].string ,z[3].string)
        return z[2].string, z[3].string


x = soup.find_all("div", {"class": "Cell Cell1"})
while i<len(x):
    c.append(info1(x,i))
    i=i+1


a = soup.find_all("div", {"class": "Cell Cell3"})
while j<len(a)/3:
    d.append(info2(a,j))
    j=j+1
def returns():
    return c,d


