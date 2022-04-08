import requests as r
from bs4 import BeautifulSoup

Site_Link = "https://www.readdetectiveconanarc.com/"

soup = BeautifulSoup( r.get(Site_Link).text , features="lxml")

Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
Link = str(Link["href"])
#I know it was initially a string, but it was in form of a slice, thus immutable
Link = Link[0:len(Link)-1]

Edition = int(Link.split('-')[-1])

soup = BeautifulSoup( r.get(Link).text , features="lxml")
Myalt = "Read Detective Conan Chapter " + str(Edition)+" - Page 1 For Free In The Highest Quality"
ImageLink = soup.find('img', alt=Myalt)["data-lazy-src"]

print(f'''
New Manga #{Edition}
Link:- {Link}
{ImageLink}
'''
)