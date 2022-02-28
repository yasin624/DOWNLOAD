import os,time
from tqdm import tqdm
import requests as rq

###################    warning !!!!
"""


dosya için indirme arayüzsüz program
dosya biçimi şu şekildeolmalıdır


###########################################
# file_name
# url
# file_name
# url
#            !!! "//**" yazmak yeni bir klasör açmakla eşdeğerdir
# file_name
# url
###########################################




!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###########################################
klas = True ise "//**klasör adı" girilmesi lazim yoksa hata alınır
klas = True ise "//**" olmalı bu otomatik klasör indirme işlemi yapacaktır

"""







class indir():
    def __init__(self,klasor="",klas=True,file=None):
        self.klasor=klasor
        self.file=file
        self.klasor_ismi= self.klasör_ismi() if klas ==True else ""
        
        self.dosya_klasor_islemleri(klasor)
        self.video_list=self.dosya_ayikla()
    def klasör_ismi(self):
        ##################################### dosya isimleri alma
        icerik=None
        with open (self.file,"r",encoding="utf-8") as f:
            icerik=f.read()
        name=[]
        for i in icerik.split("\n"):
            if i.startswith("//**"):
               name.append(i[4:])
        return name
        
        
    def dosya_ayikla(self):
        ######################################  dosya işlemleri
        icerik=None
        with open (self.file,"r",encoding="utf-8") as f:
            icerik=f.read()
        bol=[]
        video=[]
        for i in icerik.split("\n"):
            
            if not (i.startswith("//**")):
                if i not in "\n":
                    video.append(i)
            
                    
            elif i.startswith("//**"):
                bol.append("new_dir")
            if len(video)==2:
                bol.append(video)
                video=[]
            
            
        return bol
    def dosya_klasor_islemleri(self,klasor):
        try:
            os.listdir(klasor)
        except:
            os.mkdir(klasor)

    def ilerlet(self,baslangic,size):

        ilerleme = int(100 * (int(baslangic) / size))
        ileri=f"|{'#'*int((ilerleme/4))}{' '*(25-int(ilerleme/4))}| % {ilerleme} | "
        yazı = " {:.5} / MB - {:.5} /MB     ".format((baslangic / 1048576), (size / 1048576))
        
        print("\r"+ileri+yazı,end="")

    def start(self,file_name,url):
        baslangic=0
        
        file_name=file_name
        url=url
        with open(file_name, "wb") as file:
            
            video = rq.get(str(url), stream=True)
            size = int(video.headers.get("content-length"))
            
            for i in video.iter_content(chunk_size=2048):
                if i :
                    baslangic += len(i)
                    file.write(i)
                    self.ilerlet(baslangic,size)
    
    def sorgula(self,new_l=None,file=None):
        if new_l!=None:
            try:
                os.listdir(new_l)
            except:
                os.mkdir(new_l)
        if file!= None:
            if file in os.listdir(new_l):
                print("indirildi ...")
            else:
                return True
    def dowland(self):
        new_dir=0
        for s,i in enumerate(self.video_list):
            if i=="new_dir":
                new_l=self.klasor+"/{}".format(self.klasor_ismi[new_dir])
                print(f"\n\n {self.klasor_ismi[new_dir]} klasörü indiriliyor lütfen bekleyin ..." )
                print("---- "*10)
                time.sleep(1)
                self.sorgula(new_l)
                new_dir+=1
            else:
                print(f"\n{i[0]}.dosyası indiriliyor lütfen bekleyin ..." )
                print("---- "*10)
                        
                if self.sorgula(new_l,i[0]) :
                    time.sleep(3)
                    file_name=new_l+"/"+i[0]
                    url=i[1]
                    self.start(file_name,url)
                
                

indirici=indir(klasor="deneme_videosu",file="deneme_video_linkleri.txt")
indirici.dowland()
                





            
