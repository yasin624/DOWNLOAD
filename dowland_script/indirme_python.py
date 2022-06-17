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
    def __init__(self,klasor,klas=True):
        self.klasor=klasor
        self.file=""
        self.klas=klas
        self.klasor_ismi = self.links_select()
        
        
        self.dosya_klasor_islemleri(klasor)
        self.video_list=self.dosya_ayikla()
        



    def links_select(self):
        print( "\n indirme linklerinizin olduğu dosyayı seçin ")
        print("-"*50)
        print("\n")
        
        links=[]
        s=1
        for i in os.listdir():
            if i.endswith(".txt"):
                links.append([s,i])
                print(f"{s}- {i}")
                s+=1
        links.append([s,"local"])
        print(f"{s}- başka bir konum ver \n\n")
        
        sel=input("select ==>> ")
        print("\n")
        
        err=False
        for k in links:
            if sel==str(k[0]):
                err=False
                if k[1]=="local":
                    self.file=input("url : ")
                else:
                    print("girdi")
                    self.file=k[1]
                break
            else:
                err=True
        if err:
            self.error("hata lütfen şıklardan birini seçin .. ")
            self.links_select()



        links_name =self.klasör_ismi() if self.klas == True else ""
        return links_name
    def klasör_ismi(self):
        ##################################### dosya isimleri alma
        
        icerik=None
        with open (self.file,"r",encoding="utf-8") as f:
            icerik=f.read()
        name=[]
        for i in icerik.split("\n"):
            if i.startswith("//**"):
               name.append(i[4:])

        if len(name)<1:
            self.error("dosyada indirilecek lik yok tekrar deneyiniz ")
            self.links_select()
            
        else:
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
    def error(self,text,sor=False):
        
        print("\n")
        print("-"*50)
        print(text)
        print("-"*50)
        print("\n")

        if sor :
            print("""

                {1} - YENİ LİNK DOSYASINI SEÇİN
                {2} - ÇIK
            
            """)

            sec=input("selec ==>> ")

            if sec=="1":
                self.links_select()
            else:
                print("\n\n çıkılıyor ...")
                exit()
    
    def dowland(self):
        new_dir=0
        dosya=True
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
                try:
                    if self.sorgula(new_l,i[0]) :
                        time.sleep(3)
                        file_name=new_l+"/"+i[0]
                        url=i[1]
                        self.start(file_name,url)
                except :
                    dosya=False 
        if dosya:
            self.error(" dosyadaki linkler hatalı veya dosya biçimi hatalı \n lütfen kontrol ediniz .. " ,sor=True)
        
                
                

indirici=indir(klasor="new_videos")
indirici.dowland()
