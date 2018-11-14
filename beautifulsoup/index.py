from bs4 import BeautifulSoup as bs
i=int(0)
with open('index.html') as html:
	soup=bs(html,'html.parser')

for b in soup.find_all('a'):
	b=b.get('href')
	print(b)



b=soup.name='h1'
print(b)
