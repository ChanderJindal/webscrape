from requests_html import HTMLSession

link = "https://zeenews.india.com/"

s = HTMLSession()
r = s.get(link)

r.html.render(sleep=1)

f = open("ReqHTMLTest.txt","w",encoding="utf-8")
f.write(str(r.html.text).replace("><",">\n<"))
f.close()
#Beautiful!
#print(r.html)
