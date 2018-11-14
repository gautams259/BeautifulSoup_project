import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')


def add(x,y):
	return x+y
def sum(x,y):
	return x-y


n=14
m=34
result=add(n,m)
logging.debug("Add {} + {}={}".format(n,m,result))
print("Add {} + {}={}".format(n,m,result))

result=sum(n,m)
logging.debug("sum {} - {}={}".format(n,m,result))

print("Add {} - {}={}".format(n,m,result))
