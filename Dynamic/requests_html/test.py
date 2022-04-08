import requests as r 
from bs4 import BeautifulSoup as BS

link = "https://zeenews.india.com/"

soup = BS( r.get(link).text , features="lxml" )
f = open("ReqTest.txt","w",encoding="utf-8")
f.write(str(soup).replace("><",">\n<"))
f.close()
#print(soup)
