from bs4 import BeautifulSoup as bes
import requests, subprocess, pixeldrain, os

class kusonim:
    def indeed(self):
        self.judul = int(input("""
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
        2. Anime Ongoing 3 pages

        Pilih yg mana? """))
        if self.judul == 1:
            self.jdll = input("Cari anime apa? ")
            self.pilihan()
        elif self.judul == 2:
            kusoni().ongoing()
        
    def rekues(self,url):
        ses = requests.Session()
        ses.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 11; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                       "Cache-Control":"max-age=0"}
        req = ses.get(url)
        soup = bes(req.text, "html.parser")
        return [req, soup]
    
    def pilihan(self):
        link = []
        sop= self.rekues("https://kusonime.com/?s="+self.jdll+"&post_type")[1]
        for x,i in enumerate(sop.findAll("h2",{"class":"episodeye"}),1):
            link.append(i.find("a")["href"])
            print(x,i.find("a")["title"])
        pil = input("Pilih yg mana? ")
        self.pilihAnim(link[int(pil)-1])
    
    def pilihAnim(self,q):
        link = []
        anim = self.rekues(q)[1]
        nanim = anim.find("div","smokeddlrh")
        if nanim is None:
            nanim = anim.find("div","smokeddl")
        resolusi = nanim.findAll("div","smokeurlrh")
        if len(resolusi) == 0:
            resolusi = nanim.findAll("div","smokeurl")
        for i in resolusi[1].findAll("a"):
            if "Pixeldrain" in i.text:
                link.append(i["href"])
            else: pass
        if len(link) == 0: 
            print("Pixeldrain shorturl not found")
        else:
            self.download(link[0].split("/")[-1])

    def download(self,url):
        lin = "https://pixeldrain.com/api/file/"+url
        pdname = pixeldrain.info(url)["name"].replace(" ","")
        print(lin,pdname,"Downloading....!!")
        subprocess.call(["$HOME/./download_file -m 5 {}".format(lin)],shell=True)
        os.system(f"mv {url} {pdname}")
        if os.name == "posix":
            os.system(f"mv {pdname} {sdcard/Download/Video}")
            print("Downloads Saved in sdcard/Download/")
        elif os.name == "windows":
            os.system(f"mv {pdname} {C:/Users/Downloads}")
            print("Downloads Saved in C:/Users/Downloads")
        elif os.name == "linux":
            os.system("mv {pdname} {}".format("~/Downloads"))
            print("Downloads Saved in ~/Downloads")
        else: pass

class kusoni(kusonim):
    def ongoing(self):
        linkhr = []
        linkttl = []
        sop = [self.rekues(f"https://kusonime.com/page/{i}")[1] for i in range(1,4)]
        for i in sop:
            for x,i in enumerate(i.findAll("h2",{"class":"episodeye"})):
                linkhr.append(i.find("a")["href"])
                linkttl.append(i.find("a")["title"])
        print(linkttl)
        [print(n,i) for n,i in enumerate(linkttl,1)]
        pil = input("Pilih mana? ")
        self.pilihAnim(linkhr[int(pil)-1])

kusonim().indeed()
