import requests
from bs4 import BeautifulSoup as bs

_ANO = '2013/'
_MES = '01/'
_MATERIAS = 'matematica/'
_CONTEXT = 'wp-content/uploads/' + _ANO + _MES
_URL = 'http://www.desconversa.com.br/' + _MATERIAS + _CONTEXT

r = requests.get(_URL)
soup = bs(r.text)

for i, link in enumerate(soup.findAll('a')):
    _FULLURL = _URL + link.get('href')

    for x in range(i):
        output = open('file[%d].pdf' % x, 'wb')
        output.write(_FULLURL.read())
        output.close()
