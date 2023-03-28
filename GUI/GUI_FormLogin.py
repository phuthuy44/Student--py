import sys
from PyQt5 import QtWidgets,uic,QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
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
                    QMessageBox.warning(self, 'Đăng nhập', 'Đăng nhập thành công!')

     '''def msgButtonClick(self):
          print("Button clicked is")'''
app = QtWidgets.QApplication(sys.argv)
formLogin = FormLogin()
formLogin.show()
app.exec()