import bs4
#import logging
import requests

#logging.basicConfig(filename='cric.log',level=logging.DEBUG)

url="https://www.cricbuzz.com/live-cricket-scores/20776/ban-vs-zim-2nd-test-zimbabwe-tour-of-bangladesh-2018"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')

for h in soup:
	print(h)
#b=soup.find_all('p',{'class':'cb-srch-suggest-content-title'})
#print(b)
