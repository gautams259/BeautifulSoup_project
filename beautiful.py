import bs4
import requests
with open('index.html') as html_file:
     soup=bs4.BeautifulSoup(html_file,'lxml')
#print(soup.text)
a=soup.find('title')
b=[]
#b.append(a.text)
x=a.text
print(x[2:9])
