from bs4 import BeautifulSoup as BS
import requests as r
#Be sure to Install BeautifulSoup and lxml lib
def Get_Soup(link):
  return BS( r.get(link).text, features="lxml")

def Last_Episode_file_Update(Ep):
    f = open("Last_Episode.txt","w+")
    f.write(Ep)
    f.close()
    return

def Anime():#This is main one - 3 outputs
  #Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode" #- slow updates 
  Site_Link = "https://gogoanime.film/category/detective-conan"
  Base_Soup = Get_Soup(Site_Link)
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

def AnimeBackup():
  Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode"

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
  Gogo_Link = "https://gogoanime.film/detective-conan-episode-" + str(EpisodeNumber)
  #print(f'''
  #New Episode #{EpisodeNumber} :- {EpisodeName}
  #Link:- {AniMix_Link}
  #'''
  #)
  return EpisodeNumber, EpisodeName ,AniMix_Link, Gogo_Link


########################################################## Manga ##########################################################

def MangaDex_Anime_ID_update():#DC ->Detective Conan 
  name = "detective conan"#this is just for the format
  name = name.replace(" ","-")
  Api_link = f'https://api.mangadex.org/manga?title={name}'
  json_data = r.get(Api_link).json()
  if len(json_data['data']) == 0:
    return False
  Anime_ID = ""
  for i in range(0,10):
    if json_data['data'][i]['attributes']['title']['en'] == "Detective Conan":
      print(str(json_data['data'][i]['attributes']['title']['en']))
      #To make sure that it's the same one,
      Anime_ID = json_data['data'][i]['id']
      break
  # Since I know, that Anime_ID is not supposed to Change
  f = open("Anime_ID.txt","w+")
  f.write(str(Anime_ID))
  f.close()
  return Anime_ID

def Last_Chapter_file_Update(Chapter):
    f = open("Last_Chapter.txt","w+")
    f.write(str(Chapter))
    f.close()
    return

def Last_Chapter_Update():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]
  Chapter = Link.split('-')[-1]
  Last_Chapter_file_Update(Chapter)
  return Chapter

def GroupUploader(json_data):
  if len(json_data['data'][0]["relationships"]) == 3:
    Group_ID = json_data['data'][0]["relationships"][0]["id"]
    Group_link = f'https://api.mangadex.org/group/{Group_ID}'
    Group_data = r.get(Group_link).json()
    GroupName = "Not Found"
    if Group_data["result"] == "ok":
      GroupName = Group_data["data"]["attributes"]["name"]
    Uploader_Id = json_data['data'][0]['relationships'][2]['id']
    Uploader_Link = f'https://api.mangadex.org/user/{Uploader_Id}'
    Uploader_data = r.get(Uploader_Link).json()
    UploaderName = "Not Found"
    if Uploader_data["result"] == "ok":
      UploaderName = Uploader_data["data"]["attributes"]["username"]

    return GroupName , UploaderName

def Manga():# For MangaDex 
  Chapter = 1087
  try:#If we got the Last_Chapter Number good, otherwise call the function above and make API call and get it
    f = open("Last_Chapter.txt","r")
    Chapter = f.read()
    f.close()
  except:
    Chapter = Last_Chapter_Update()

  Chapter = int(Chapter) + 1 #incase an update has been made

  Anime_ID = ""

  try:#If Anime ID is in file cool, otherwise make an API call
    f = open("Anime_ID.txt","r")
    Anime_ID = f.read()
    f.close()
  except:
    Anime_ID = MangaDex_Anime_ID_update()
  
  Manga_ID = ""
  #print(Anime_ID,Chapter)
  GroupName = ""
  UploaderName = ""
  Name = ""
  try:
  #Got the one for the newest expected Chapter
    link = f'https://api.mangadex.org/chapter?manga={Anime_ID}&chapter={str(Chapter)}&translatedLanguage[]=en'
    #Passing chapter as a string is best
    response = r.get(link)
    json_data = response.json()
    #print(link)
    Manga_ID = json_data['data'][0]['id']
    GroupName , UploaderName = GroupUploader(json_data=json_data)
    Name = json_data['data'][0]['attributes']['title']
    Last_Chapter_file_Update(Chapter=str(Chapter))
    #Since now it's Chapter + 1

  except:
    #So, chapter +1 is now out yet, so back to previous one
      #print("here1")
      Chapter = int(Chapter) - 1
      link = f'https://api.mangadex.org/chapter?manga={Anime_ID}&chapter={str(Chapter)}&translatedLanguage[]=en'
      response = r.get(link)
      json_data = response.json()
      #print(link)
    #Since last chapter update function sent me this detail, this chapter exists for sure
      Manga_ID = json_data['data'][0]['id']
      GroupName , UploaderName = GroupUploader(json_data=json_data)
      Name = json_data['data'][0]['attributes']['title']
  
  #^This is the main Thing!

  PageNumber = 1 #This one is for sake of format only

  Final_Link = f'https://mangadex.org/chapter/{Manga_ID}/{PageNumber}'
  ImageLink = GetFrontPage(MangaID=Manga_ID)
  
  return str(Chapter) , Final_Link , GroupName , UploaderName,ImageLink,Name

def GetFrontPage(MangaID):
  BaseLink = f"https://api.mangadex.org/at-home/server/{MangaID}"
  json_data = r.get(BaseLink).json()
  if json_data["result"] != "ok":
      return json_data["result"]
  Link = json_data["baseUrl"]+"/data/"+json_data["chapter"]["hash"]+"/"
  ImageLink = Link + json_data["chapter"]["data"][0]
  return ImageLink

def GetCover(AnimeID):
  BaseLink = f'https://api.mangadex.org/manga/{AnimeID}?includes[]=cover_art'
  '''
  In the link above, there is an API call to Mangadex.org
  It say it's Specifying the Manga
  Then it gives the MangaID
  ?` is for those it doesn't know and needs
  includes` lists them 1 at a time
  []` is so an array ,as per the api call instructions, is returned
  = cover_Art` is to compare it to the type 
  &` it is used to pick more values, after this just repeat all from include till before
  '''
  json_data = r.get(BaseLink).json()
  for i in range(0,len(json_data["data"]["relationships"])):
    if json_data["data"]["relationships"][i]["type"] == "cover_art":
      #print(AnimeID)
      #print(json_data["data"]["relationships"][i]["attributes"]["fileName"])
      CoverFileName = json_data["data"]["relationships"][i]["attributes"]["fileName"]
      return f'https://uploads.mangadex.org/covers/{AnimeID}/{CoverFileName}.512.jpg'
      #PS here ".256.jpg" and ".512.jpg" in end are formats, if not specified then it will give original work


def AllPages(MangaID):#To be used to Read the Manga Not implemented yet
    BaseLink = f"https://api.mangadex.org/at-home/server/{MangaID}"
    json_data = r.get(BaseLink).json()
    if json_data["result"] != "ok":
        return json_data["result"]
    Link = json_data["baseUrl"]+"/data/"+json_data["chapter"]["hash"]+"/"
    ImageLst = json_data["chapter"]["data"]
    for i in ImageLst:
        print(Link,i,sep="")
    return "Done"

def Manga_Backup():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]

  Chapter = Link.split('-')[-1]

  '''
  To get first Page of Manga, but it already comes with the manga link
  soup = Get_Soup(Link)
  ImageLink = soup.find('img', alt="Read Detective Conan Chapter "+str(Chapter)+" - Page 1 For Free In The Highest Quality")["data-lazy-src"]
  '''

  return Chapter , Link 
  #f'''
  #New Manga #{Chapter}
  #Link:- {Link}
  #{ImageLink}
  #'''



if __name__ == "__main__":
  '''
  print("Here")
  print(Anime())
  print(MangaDex_Anime_ID_update())
  print("Here")
  print(Manga())
  print("Here")
  '''
  f = open("Anime_ID.txt","r")
  print(GetCover(f.read()))
  f.close()
  