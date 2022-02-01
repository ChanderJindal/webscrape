from bs4 import BeautifulSoup as BS
import requests as r

Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode"

def Get_Soup(link):
    return BS( r.get(link).text, features="lxml")

Base_Soup = Get_Soup(Site_Link)
#Initial Page

EpRange = Base_Soup.find('div', class_ = "pagination ac")
#Getting the range

LatestOne = EpRange.find_all('a',class_ = "link")[-1]
#Picked the Last Range

Correct_Page_Link = LatestOne["href"]

Correct_Soup = Get_Soup(Correct_Page_Link)
#Onto the page with Latest Ep

LatestEp = Correct_Soup.find_all('a', class_="fl-l fw-b")[-1]
#got the tag with correct info

EpisodeName = LatestEp.text
EpisodeNumber = LatestEp["href"].split('/')[-1]

AniMix_Link = "https://animixplay.to/v1/detective-conan/ep" + str(EpisodeNumber)

print(f'''
New Episode #{EpisodeNumber} :- {EpisodeName}
Link:- {AniMix_Link}
'''
)

