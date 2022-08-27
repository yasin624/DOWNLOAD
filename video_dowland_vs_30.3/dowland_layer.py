from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,time
import threading as thread
import requests as rq



class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()
        self.s=0
        self.history=0
        self.h = QVBoxLayout()
        self.baslangic=0
        self.size=0
        self.bilgi=None
        self.prog=None
        self.bitir=True
    def basla(self):
        while True:
            try:

                ilerleme = int(100 * (int(self.baslangic) / self.size))
                ilerleme= 100 if ilerleme >99 else ilerleme
                yazı = "{:.5} / MB - {:.5} /MB".format((self.baslangic / 1048576), (self.size / 1048576))
                self.bilgi.setText(yazı)
                time.sleep(1)

                if ilerleme==100:
                    break
                else:
                    print(ilerleme)
                    try:
                        self.prog.setValue(ilerleme)
                    except:
                        print("hata_bra")





            except:
                pass
        if self.bitir==False:
            print("burdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            try:
                self.prog.setValue(100)
            except:
                print("bra_vala_hata")
            self.bilgi.setText("kaydedildi ...")

    def olustur(self,url):
        devam=True
        try:
            video = rq.get(str(url), stream=True)
            size = int(video.headers.get("content-length"))

        except:
            devam=False
            print ("hata bağlantınızı kontrol ediniz")

        if devam:
            prog = QProgressBar()

            prog.setMaximum(100)
            prog.setMinimum(1)
            prog.setValue(0)
            yazı = " 0 / MB -  0 /MB"
            bilgi = QLabel(yazı)

            v = QVBoxLayout()
            v.addWidget(prog)
            h = QHBoxLayout()
            h.addStretch()
            h.addWidget(bilgi)
            v.addLayout(h)
            v.addStretch()
            return prog,bilgi,v,video
        else:
            return None

    def run(self,video,files):
        try:
            time.sleep(2)
            dosya = files + r"\video2.mp4"
            with open(dosya, "wb") as file:

                    self.size = int(video.headers.get("content-length"))
                    for i in video.iter_content(chunk_size=2048):
                        if i :
                            self.baslangic += len(i)
                            file.write(i)
            self.bitir=False

        except:
            print("hata")


    def send(self,file="",url=""):
        try:
            print(file)
            print(url)
            kontrol=self.olustur(url)

            if kontrol!=None:
                self.prog,self.bilgi, v,video=kontrol
                self.h.addLayout(v)
                self.setLayout(self.h)
                try:
                    self.t2 = thread.Thread(target=self.run, args=(video,file))
                    self.t2.start()

                    t1 = thread.Thread(target=self.basla)
                    t1.start()
                except:
                    print ("HATAAAAAAAAAAAAAAA")
        except:
            print("hata 3")



"""
    def olustur(self,baslangıc,size):
        ilerleme = int(100 * (baslangıc / size))
        self.prog.setValue(ilerleme)
        yazı = str(size / 1048576) + " / MB"
        self.bilgi = QLabel(yazı)

        self.v.addWidget(self.prog)
        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.bilgi)
        self.v.addLayout(h)
        self.v.addStretch()
        self.tablo.tablo2.setLayout(self.v)
   
    def run(self):
        self.start(priority=True)
        self.v = QVBoxLayout()
        self.prog = QProgressBar()

        self.prog.setMaximum(100)
        self.prog.setMinimum(1)

        video = rq.get(self.main_m.url.text(), stream=True)
        dosya = self.yol_k.link.text() + r"\video.mp4"
        with open(dosya, "wb") as file:
            baslangic = 0
            size = int(video.headers.get("content-length"))
            for i in video.iter_content(chunk_size=2048):
                baslangic += len(i)
                file.write(i)
                self.olustur(baslangic,size)
                
        def uret(self,s):
        yazı = QLabel(self)
        yazı.setText("<font size=4><b> KONUM_"+str(s)+":</b></font>")

        git = QPushButton(self)
        git.setText("denemeler_"+str(s))
        git.setFont(QFont("Ariel", 10))

        v = QVBoxLayout()

        k = QHBoxLayout()
        k.addWidget(yazı)
        k.addStretch()
        k.addStretch()
        k.addStretch()
        k.addWidget(git)
        v.addLayout(k)

        return v"""