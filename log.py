import logging 

logging.basicConfig(filename='cl.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class test:
	def sum(self,a,b):
		return a+b;
	def sub(self,a,b):
		return a-b;

ob=test()
a=20
b=30
r=ob.sum(a,b);
logging.debug(f"sum of {a} + {b} = {r}")
r=ob.sub(a,b)
logging.debug(f"sum of {a} + {b} = {r}")
