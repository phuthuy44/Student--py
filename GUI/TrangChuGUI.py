import sys
from PyQt5 import QtWidgets,uic,QtGui
from PyQt5.QtWidgets import QMessageBox,QWidget
class TrangChu(QtWidgets.QMainWindow):
     def __init__(self):
          super(TrangChu,self).__init__()
          uic.loadUi("GUI/TrangChu.ui",self)
          self.stackedWidget.setCurrentIndex(0)
          self.btnHocSinh.clicked.connect(self.stackHocSinh)
         
     def stackHocSinh(self):
          self.stackedWidget.setCurrentIndex(1)


