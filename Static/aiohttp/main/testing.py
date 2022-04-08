#this is for Episode.py call testing
import EpManga as e
import asyncio

if __name__ == "__main__":
    a,b,c=asyncio.run(e.Anime())
    print(a,b,c,sep='\n',end="\n#####\n")
    a,b,c,d=asyncio.run(e.AnimeBackup())
    print(a,b,c,d,sep='\n',end="\n#####\n")