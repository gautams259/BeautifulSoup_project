from bs4 import BeautifulSoup as bs
import requests
url="https://www.cricbuzz.com/live-cricket-scores/20776/ban-vs-zim-2nd-test-zimbabwe-tour-of-bangladesh-2018"
data=requests.get(url)
soup=bs(data.text,'html.parser')
x=[]
print(soup.text[15511:15550])

#
