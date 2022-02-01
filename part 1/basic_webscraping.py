from bs4 import BeautifulSoup
with open('home.html','r') as Home_html:
    Lines = Home_html.read()

soup = BeautifulSoup(Lines,features="lxml")
Content = soup.find_all('div', class_ = "card")

for item in Content:
    print(item.h5.text , "Costs" , item.a.text.split()[-1], "\n" + item.p.text)