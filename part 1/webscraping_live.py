import requests
from bs4 import BeautifulSoup

Site_Link = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

html_file = requests.get(Site_Link)
soup = BeautifulSoup(html_file.text,features="lxml")

def remove_rn(s):
    return s.replace('\r','').replace('\n','').strip()

def remove_rn_lst(lst):
    for i in range(len(lst)):
        lst[i] = remove_rn(lst[i])
    return lst

def check_dated(date):
    lst_temp = date.split(' ')
    if lst_temp[1] == "few":
        return True
    try:
        val = int(lst_temp[1])
        if val < 11:
            return True
        return False
    except:
        return False

Jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for j in Jobs:
    post = remove_rn(j.find('span' , class_="sim-posted").text)
    if(check_dated(post) is False):
        continue
    name = remove_rn(j.find('h3', class_ ="joblist-comp-name").text)
    temp = j.find_all('li')
    desc = remove_rn(temp[-2].text).split(':')[-1]
    skills = remove_rn(temp[-1].text).split(':')[-1].split(',')
    link = j.find('h2').a["href"]
    print(f'''
    Company Name: {name}
    Skills Required: {remove_rn_lst(skills)}
    Job Description: {desc[0:len(desc)-len("... More Details")]}.
    Link: {link}
    {post}
    ''')
    