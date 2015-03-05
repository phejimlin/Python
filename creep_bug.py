# coding=utf-8
from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen('https://tw.news.yahoo.com/nba-%E9%80%8F%E7%B4%8D0.2%E7%A7%92%E8%87%B4%E5%8B%9D%E7%90%83-%E5%A1%9E%E7%88%BE%E6%8F%90%E5%85%8B%E9%80%86%E8%BD%89-%E6%9D%B1%E6%96%B9%E4%B8%8D%E6%95%97-070900332--nba.html')  
html = response.read()
#print html



soup = BeautifulSoup(html)
tag=soup.h2
#print tag

#content=soup.find('div',id="mediaarticlebody")
# open file
f = open('test.txt', 'w')    # 也可使用指定路徑等方式，如： C:\A.txt


for link in soup.find_all('p'):
	text= link.get_text()
	f.write(text.encode('utf-8')+'\n')
f.close()



#for link in soup.find_all('div',id="mediaarticlebody"):
#	print link.p
#for link in soup.find_all('p'):
 #   print (link.get_text)
