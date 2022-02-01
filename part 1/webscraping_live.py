import imp
import requests
from bs4 import BeautifulSoup

Site_Link = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

html_file = requests.get(Site_Link)
print(html_file)