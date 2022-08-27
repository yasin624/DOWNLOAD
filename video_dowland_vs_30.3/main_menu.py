from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings



class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()
        self.etiketler()

    def etiketler(self):
        ###############################################   app main icon
        self.yazı = QLabel(self)
        self.yazı.setPixmap(QPixmap("logo.ico"))
        self.yazı.setGeometry(200, 30, 200, 200)
        ###############################################   files the url
        self.url = QLineEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        ###############################################   the button dowloand files
        self.git = QPushButton(self)
        self.git.setText("GİT")
        self.git.setFont(QFont("Ariel", 10))

        ###############################################   arrangement
        v = QVBoxLayout()
        l=QHBoxLayout()
        l.addStretch()
        l.addWidget(QLabel("<h1><i> MOVİE SAVE & DOWLAND </i></h1>"))
        l.addStretch()
        v.addLayout(l)

        k=QHBoxLayout()
        k.addStretch()
        k.addWidget(self.yazı)
        k.addStretch()
        v.addLayout(k)

        h = QHBoxLayout()
        h.addWidget(QLabel("<h3> URL gir : </h3>"))
        h.addWidget(self.url)
        h.addWidget(self.git)

        v.addLayout(h)
        v.addStretch()

        self.setLayout(v)


