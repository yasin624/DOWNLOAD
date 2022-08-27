from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,main_menu,setings,random,dowland_layer



class setup(QMainWindow):
    def __init__(self):
        super().__init__()
        ##########################################################  table
        self.dowland_l = dowland_layer.menu_içerik()
        self.main_m = main_menu.menu_içerik()
        self.yol_k = setings.yol()
        ######################################################  setup settings
        self.setWindowTitle("VİDEO DOWLAND VS: 30.3 ")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setMaximumSize(900,600)
        self.setMinimumSize(700,450)
        ######################################################## they parameters
        self.içerik()

    def içerik(self):
        #######################################################  text menu
        menu=self.menuBar()
        self.dosya=menu.addMenu("file")
        self.konum=QAction("Dowland Local")
        self.konum2 = QAction("Dowland files")
        self.dosya.addAction(self.konum)
        self.dosya.addAction(self.konum2)

        ######################################################  table menu
        self.tablo=QTabWidget()
        self.tablo.tablo1=QWidget()
        self.tablo.tablo2=QWidget()
        self.tablo.tablo3=QWidget()

        self.tablo.addTab(self.tablo.tablo1,"MENU")
        self.tablo.addTab(self.tablo.tablo2, "DOWLAND FİLES")
        self.tablo.addTab(self.tablo.tablo3, "SETİNG")

        #####################################################  satatus bar (info the bar)
        self.status=QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Tüm hakları saklıdır © 2020 | yalcınyazılımcılık")



        ###################################################   full the tables
        self.tab1()
        self.tab2()
        self.tab3()
        self.setCentralWidget(self.tablo)
        ################################################################### file download location
        self.dosya.triggered.connect(self.konum_belirle)

        ################################################################### clicked the url button
        self.main_m.git.clicked.connect(self.dowloand)

    def tab1(self):
        ############################################################### main_menu fulling
        v = QVBoxLayout()
        v.addWidget(self.main_m)
        self.tablo.tablo1.setLayout(v)
    def tab2(self):
        ############################################################### dowland_l fulling
        v = QVBoxLayout()
        v.addWidget(self.dowland_l)
        self.tablo.tablo2.setLayout(v)
    def tab3(self):
        ############################################################### the settings fulling
        v = QVBoxLayout()
        v.addWidget(self.yol_k)
        v.addStretch()
        self.tablo.tablo3.setLayout(v)
    def dowloand(self):
        try:
            file_local = self.yol_k.link.text()
            url_local = self.main_m.url.text()
            self.main_m.url.setText("")
            self.dowland_l.send(" " if file_local== None else str(file_local) ," " if url_local== None else str(url_local))
        except:
            print("hata 2")
    def konum_belirle(self,dene):
        # cur_index = self.tabWidget.currentIndex() tablo indexleri
        if dene.text()=="Dowland Local":
            self.tablo.setCurrentIndex(2)
        elif dene.text() == "Dowland files":
            self.tablo.setCurrentIndex(1)


app=QApplication(sys.argv)
dowland=setup()
dowland.show()
sys.exit(app.exec_())
