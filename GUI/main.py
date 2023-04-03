import sys
from PyQt5 import QtWidgets,uic,QtGui
from PyQt5.QtWidgets import QMessageBox,QWidget
class FormLogin(QtWidgets.QMainWindow) :
     def __init__(self):
          super(FormLogin, self).__init__()
          uic.loadUi("GUI/Form_Login.ui",self)
          px = QtGui.QPixmap("img/child-girl-schoolgirl-elementary-school-student-123686003.jpg")
          self.labelLogin.setPixmap(px)
          self.lineMatKhau.setEchoMode(QtWidgets.QLineEdit.Password )
          self.btnDangNhap.clicked.connect(self.LoginFunction)

     def LoginFunction(self):
          tenDangNhap = self.lineTenDangNhap.text()
          matKhau = self.lineMatKhau.text()

          if len(tenDangNhap)== 0 or len(matKhau)== 0:
              # self.textError.setText("Bạn chưa nhập tên đăng nhập hoặc mật khẩu!")
               '''msgBox = QMessageBox()
               msgBox.setIcon(QMessageBox.Information)
               msgBox.setText("Bạn chưa nhập tên đăng nhập hoặc mật khẩu!")
               msgBox.setWindowTitle("Thông báo !")
               msgBox.setStandardButtons(QMessageBox.Cancel)
               msgBox.buttonClicked.connect(self.msgButtonClick)
               returnValue = msgBox.exec()
               if returnValue == msgBox.Cancel:
                    print("Cancel!")'''
               QMessageBox.warning(self, 'Đăng nhập', 'Bạn chưa nhập tên đăng nhập hoặc mật khẩu!')

          else:
               '''conn = sqlite3.connect('StudentManager.db')
               cur = conn.cursor()
               query = 'SELECT password FROM login WHERE username = \' '+user+"\'"
               cur.execute(query)
               result_pass = cur.fetchone()[0]
               if result_pass == matKhau:
                    print("Success!")
               else:
                    self.textError.setText("Tên đăng nhập hoặc mâtk khẩu không đúng!")'''
               if tenDangNhap == 'admin' and matKhau =='1234':
                    #QMessageBox.warning(self, 'Đăng nhập', 'Đăng nhập thành công!')
                    #uic.loadUi("GUI/TrangChu.ui",self)
                    trangChu = TrangChu()
                    widget.addWidget(trangChu)
                    widget.setFixedSize(trangChu.width(),trangChu.height())
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    '''trangChu.show()
                    self.accept()'''

               else:
                    QMessageBox.warning(self, 'Đăng nhập', 'Đăng nhập khong thành công!')     
class TrangChu(QtWidgets.QMainWindow):
     def __init__(self):
          super(TrangChu,self).__init__()
          uic.loadUi("GUI/TrangChu.ui",self)
          self.stackedWidget.setCurrentIndex(0)
          #self.btnHSPL.clicked.connect(self.stackHSPL)
          self.btnHocSinh.clicked.connect(self.stackHocSinh)
          #self.btnGVPC.clicked.connect(self.stackGVPC)
          self.btnGiaoVien.clicked.connect(self.stackGiaoVien)    
          self.btnNhanVien.clicked.connect(self.stackNhanVien)
          self.btnQuyen.clicked.connect(self.stackQuyen)
          self.btnLop.clicked.connect(self.stackLop)
          self.btnDangXuat.clicked.connect(self.DangXuat)
          self.btnHKNH.clicked.connect(self.stackHKNH)
          self.btnMonHoc.clicked.connect(self.stackMonHoc)
          self.btnKetQua.clicked.connect(self.stackKetQua)
     #def stackHSPL(self):
          #self.stackedWidget.setCurrentIndex(10)
     def stackHocSinh(self):
          self.stackedWidget.setCurrentIndex(1)
     #def stackGVPC(self):
      #    self.stackedWidget.setCurrentIndex(11)
     def stackGiaoVien(self):
          self.stackedWidget.setCurrentIndex(2)
     def stackNhanVien(self):
          self.stackedWidget.setCurrentIndex(3)
     def stackQuyen(self):
          self.stackedWidget.setCurrentIndex(5)
     def stackLop(self):
          self.stackedWidget.setCurrentIndex(6)
     def stackHKNH(self):
          self.stackedWidget.setCurrentIndex(7)
     def stackMonHoc(self):
          self.stackedWidget.setCurrentIndex(8)
     def stackKetQua(self):
          self.stackedWidget.setCurrentIndex(9)
     def DangXuat(self):
          '''self.hide()
          #widget.resize(formLogin.width(),formLogin.height())
          widget.setCurrentIndex(0)
          widget.setFixedSize(800,500)     
          formLogin.lineTenDangNhap.setText(" ")
          formLogin.lineMatKhau.setText("")'''
          #widget.setCurrentIndex(0)
          ret = QMessageBox.question(self, 'MessageBox', "Bạn muốn đăng xuất khỏi hệ thống?", QMessageBox.Yes| QMessageBox.Cancel)
               
          if ret == QMessageBox.Yes:
               self.hide()
                    #widget.resize(formLogin.width(),formLogin.height())
               formLogin.lineTenDangNhap.text()
               formLogin.lineMatKhau.text()

               widget.setCurrentIndex(0)
          #formLogin.show()
               widget.setFixedSize(800,500)     






app = QtWidgets.QApplication(sys.argv)
formLogin = FormLogin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(formLogin)
#widget.setFixedHeight(500)
#widget.setFixedWidth(800)
widget.resize(formLogin.width(),formLogin.height())
widget.show()
#formLogin.show()
try:
     sys.exit(app.exec_())
except:
     print("Exiting!")
#app.exec()
     