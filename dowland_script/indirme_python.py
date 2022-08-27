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




main_str="""
                                                                      
     |||||      ||||     || ||| ||    ||         ||      ||| |||    |||||       
     #####|    |#####    |# |## ##    ##        |##|     ### |#|    #####|      
     ## |##    ##| ##|   |#|###|##    ##        ####     ###||#|    ## |#|      
     ## |##   |##  |#|   |#|#|#|#|    ##       |#||#     ######|    ## |##      
     ## |##    ##  |#|    ###|###|    ##       |####|    ## ###|    ## |##      
     #####|    |#####     ### |##     #####    ######    ## |##|    #####|      
     ####|      |###      |#| |##     #####   |#|  ##|   ##  ##|    ####|       
                                                                                
                                                                                
                                                                                
                                                                                
                                             #|                                 
                                             ||                                 
               |###      |##|     |####|    |#|    |####    |#####|             
              |#||##    |#####    |#####    |#|    |####|   |#####|             
              |###|     ##  #|    |#| ##    |#|    |#||##     |#|               
               |####    ##        |####|    |#|    |####|     |#|               
              |#||##    ##| ##    |#|##|    |#|    |###|      |#|               
              |####|    |####|    |#||##|   |#|    |#|        |#|               
               ||||      ||||     ||  |||   |||    |||        |||               
                                                                                
                                                                                
                                                                                
                                                                                
                                ##########                                      
                               |###########                                     
                               |###########                                     
                               |##      ###                                     
                               |##      ###                                     
                               |##      ###                                     
                               |##      ###                                     
                               |##      ###                                     
                               |##      ###                                     
                            ######      ######|                                 
                           #######      #######                                 
                           |######      |#####|                                 
                            |###|        |###|                                  
                             |###|      |###|                                   
                              |###      |##|                                    
                               |###    |###                                     
                                ####  ####                                      
                                 ########                                       
                                  ######                                        
                                   ####                                         
                                    ##|                                         
                                      
"""










class indir():
    def __init__(self,klasor,klas=True):
        self.klasor=klasor
        self.file=""
        self.klas=klas
        self.links_select()
        
        self.klasor_ismi =self.alt_klasör_ismi() if self.klas == True else "" 
        
        
        self.dosya_klasor_islemleri(klasor)
        self.video_list=self.dosya_ayikla()
        


    def Menu(self):
        print(main_str)
        print( "\n indirme linklerinizin olduğu dosyayı seçin ")
        print("-"*50)
        print("\n")
        
        links=[]
        menu=os.listdir()+["başka bir konum ver","url ver","çıkış"]
        s=1
        for i in menu:
            if i.endswith(".txt") or i in menu[-3:]:
                links.append([s,i])
                print(f"{s}- {i}")
                s+=1
        return links
    
    def links_select(self):
        
        
        links=self.Menu()
        sel=input("\n\n select ==>> ")
        print("\n")
        
        err=False
        for k in links:
            if sel==str(k[0]):
                err=False
                if k[1]=="başka bir konum ver":
                    self.dosyalari_iceri_aktar(input("file_localetion : "))
                elif k[1] =="url ver":
                    
                    file_name=input("file_name : ")
                    url=input("url : ")
                    try:
                        self.start(file_name,url)
                    except:
                        self.error("link hatalı tekrar dene",True)
                    
                elif k[1]=="çıkış":
                    print("çıkılıyor ...")
                    time.sleep(2)
                    exit()
                else:
                    self.dosyalari_iceri_aktar(k[1])
                break
                
            else:
                err=True
        if err:
            self.error("hata lütfen şıklardan birini seçin .. ")
            self.links_select()



        

    def dosyalari_iceri_aktar(self,file_local):
        try:
            with open (file_local,"r",encoding="utf-8") as f:
                self.file=f.read()
        except:
            self.error("dosya konumu hatalı lüten dosya konumunu düzgün yazın")
            self.links_select()
            
    def alt_klasör_ismi(self):
        ##################################### dosya isimleri alma
        name=[]
        for i in self.file.split("\n"):
             if i.startswith("//**"):
                  name.append(i[4:])
                                           

        if len(name)<1:
             self.error("dosyada indirilecek lik yok tekrar deneyiniz ")
             self.links_select()
                                        
        else:
            return name
        
        
    def dosya_ayikla(self):
        ######################################  dosya işlemleri
        
        bol=[]
        video=[]
        for i in self.file.split("\n"):
            
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
            self.links_select()
    
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
