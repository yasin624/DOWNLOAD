from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os
class yol(QWidget):
    def __init__(self):
        super().__init__()
        self.yol_g()
    def yol_g(self):
        self.link=QLineEdit(self)
        self.ac=QPushButton(self)
        self.link.setText(os.getcwd())
        self.ac.setText("AÇ")

        self.ac.clicked.connect(self.konum)

        v = QHBoxLayout()
        v.addWidget(QLabel("<font size=4><b> KONUM :</b></font>"))
        v.addWidget(self.link)
        v.addWidget(self.ac)
        self.setLayout(v)

    def konum(self):
        self.dosya_k=QFileDialog.getExistingDirectoryUrl()
        self.link.setText(self.dosya_k.url())