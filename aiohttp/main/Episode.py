from bs4 import BeautifulSoup as BS
import aiohttp
import asyncio
#Be sure to Install BeautifulSoup and lxml lib
async def Get_Soup(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return BS( await response.text(), features="lxml")

def Last_Episode_file_Update(Ep):
    f = open("Last_Episode.txt","w+")
    f.write(Ep)
    f.close()
    return

async def Anime():#This is main one - 3 outputs
  #Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode" #- slow updates 
  Site_Link = "https://gogoanime.film/category/detective-conan"
  Base_Soup = await Get_Soup(Site_Link)
  #Initial Page

  Main_div = Base_Soup.find('div',class_ = "anime_video_body")
  #This is lower half o page

  Sub_div = Main_div.find_all('li')[-1]
  #This containts the Last range of ep
  #Format 1000-1037 , 1037 being the last ep at that time

  EpNumber = Sub_div.a['ep_end']
  #This is the end of range marker

  Link_base = "https://gogoanime.film/detective-conan-episode-"
  #just add ep number at end, just in case of decimals need to add a dash

  GogoLink = Link_base + EpNumber.replace(".","-")
  #Incase of decimal


  Last_Episode_file_Update(EpNumber)

  AniMixPlay_Link = f'https://animixplay.to/v1/detective-conan/ep' + EpNumber

  #statement = f'{EpNumber}  {EP_Type}\nThis Episode is Available on\n{AniMixPlay_Link}\n{GogoLink}'

  return EpNumber , AniMixPlay_Link , GogoLink
  #f'''
  #New Episode #{EpisodeNumber} :- {EpisodeName}
  #Link:- {AniMix_Link}
  #'''

async def AnimeBackup():
  Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode"

  Base_Soup = await Get_Soup(Site_Link)
  #Initial Page

  EpRange = Base_Soup.find('div', class_ = "pagination ac")
  #Getting the range

  LatestOne = EpRange.find_all('a',class_ = "link")[-1]
  #Picked the Last Range

  Correct_Page_Link = LatestOne["href"]

  Correct_Soup = await Get_Soup(Correct_Page_Link)
  #Onto the page with Latest Ep

  LatestEp = Correct_Soup.find_all('a', class_="fl-l fw-b")[-1]
  #got the tag with correct info

  EpisodeName = LatestEp.text
  EpisodeNumber = LatestEp["href"].split('/')[-1]

  AniMix_Link = "https://animixplay.to/v1/detective-conan/ep" + str(EpisodeNumber)
  Gogo_Link = "https://gogoanime.film/detective-conan-episode-" + str(EpisodeNumber)
  #print(f'''
  #New Episode #{EpisodeNumber} :- {EpisodeName}
  #Link:- {AniMix_Link}
  #'''
  #)
  return EpisodeNumber, EpisodeName ,AniMix_Link, Gogo_Link

if __name__ == "__main__":
    a,b,c=asyncio.run(Anime())
    print(a,b,c,sep='\n',end="\n#####\n")
    a,b,c,d=asyncio.run(AnimeBackup())
    print(a,b,c,d,sep='\n',end="\n#####\n")