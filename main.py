#coding utf=8
import requests, pixeldrain, wget, tqdm
from bs4 import BeautifulSoup as bes
import time, os, subprocess

def get(url):
    ses = requests.Session()
    ses.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 11; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36","Cache-Control":"max-age=0"}
    req = ses.get(url)
    bs = bes(req.text,"html.parser")
    return [req, bs]

def kusonime():
    link = []
    query = input("Mau cari anime apa? ")
    sop = get(f"https://kusonime.com/?s={query}&post_type")[1]
    for x,i in enumerate(sop.findAll("h2",attrs={"class":"episodeye"}),1):
        link.append(i.find("a")["href"])
        print(x,i.find("a")["title"])
    pil = int(input("Pilih yg mana? "))-1
    pilihAnim(link[pil])

def ongoing():
    linkhr = []
    linkttl = []
    sop = [get(f"https://kusonime.com/page/{i}")[1] for i in range(1,4)]
    for i in sop:
        for n,x in enumerate(i.findAll("h2",attrs={"class":"episodeye"})):
            linkhr.append(x.find("a")["href"])
            linkttl.append(x.find("a")["title"])
    [print(n,i) for n,i in enumerate(linkttl,1)]
    pil = int(input("Pilih yg mane banh: "))-1
    pilihAnim(linkhr[pil])
    
def pilihAnim(q):
    link = []
    anim = get(q)[1]
    nanim = anim.find("div","smokeddlrh") 
    if nanim is None:
        nanim = anim.find("div","smokeddl")
    resolusi = nanim.findAll("div","smokeurlrh")
    if len(resolusi) == 0:
        resolusi = nanim.findAll("div","smokeurl")
    for x,i in enumerate(resolusi[1].findAll("a"),1):
        if "Pixeldrain" in i.text:
            link.append(i["href"])
        else:
            pass
    if len(link) == 0:
        print("Pixeldrain downloader not found")
    else:
        download(link[0].split("/")[-1])

def download(url):
    global folder
    folder = "/sdcard/Download/video"
    don = "https://pixeldrain.com/api/file/"+url
    pdname = pixeldrain.info(url)['name']
    print(pdname, "Downloading")
    wget.download(don,out=folder)
    
if __name__ == "__main__":
    print("""
   __ __                   _             
  / //_/_ _____ ___  ___  (_)_ _  ___    
 / ,< / // (_-</ _ \/ _ \/ /  ' \/ -_)   
/_/|_|\_,_/___/\___/_//_/_/_/_/_/\__/    
       ____                              
      / __/__________ ____  ___  ___ ____
     _\ \/ __/ __/ _ `/ _ \/ _ \/ -_) __/
    /___/\__/_/  \_,_/ .__/ .__/\__/_/   
                    /_/  /_/             
        1. Cari Anime
        2. Ongoing 3 pages
    """)
    try:
        pil = int(input("Pilih mn? "))
        if pil == 1:
            kusonime()
        elif pil == 2:
            ongoing()
    except ValueError:
        os.system("python main.py")
    except KeyboardInterrupt:
        exit()
