import sys
from PyQt5 import QtWidgets,uic,QtGui
import random
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem
import mysql.connector
db = mysql.connector.connect(
               host ="localhost",
               user ="root",
               password ="",
               database ="studentmanager"
               )
query = db.cursor()
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
               QMessageBox.warning(self, 'Đăng nhập', 'Bạn chưa nhập tên đăng nhập hoặc mật khẩu!')

          else:
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
          self.btnHocPhi.clicked.connect(self.stackHocPhi)
          '''Loadata'''
          '''Xu lý cac nut trong tabWidget'''  
          self.btnThemCV.clicked.connect(self.tabChucVu)
          self.btnXoaChucVu.clicked.connect(self.deleteChucVu)
     
     def stackHocSinh(self):
          self.stackedWidget.setCurrentIndex(1)
     def stackGiaoVien(self):
          self.stackedWidget.setCurrentIndex(2)
     def stackNhanVien(self):
          self.stackedWidget.setCurrentIndex(3)
           # Generate a new unique ID for the new record
          query.execute("SELECT *FROM chucvu")
          data = query.fetchall()
# populate the widget with the data from the database
          self.tableChucVu.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableChucVu.setItem(i, j, QTableWidgetItem(str(val)))

          #count = query.fetchone()[0]
          maChucVu = "NV" + str(random.randint(0, 999)).zfill(3)
          self.lineMaChucVu.setText(maChucVu)
     def deleteChucVu(self):
          selected = self.tableChucVu.selectedItems()
          
          if selected:
               ret = QMessageBox.question(self, 'MessageBox', "Bạn muốn xóa đối tượng này?", QMessageBox.Yes| QMessageBox.Cancel)
               
               if ret == QMessageBox.Yes:
                    rows = set()
                    for item in selected:
                         rows.add(item.row())  # lưu trữ chỉ số hàng của các phần tử được chọn
                    rows = list(rows)  # chuyển set thành list
                    rows.sort()  # sắp xếp các chỉ số hàng theo thứ tự tăng dần
                    rows.reverse()  # đảo ngược thứ tự để xóa từ cuối lên đầu
                    for row in rows:
                         maChucVu = self.tableChucVu.item(row, 0).text()
                         self.tableChucVu.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM chucvu WHERE maChucVu = %s"
                         val = (maChucVu,)
                         query.execute(sql,val)
                         db.commit()
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def tabChucVu(self):
          #self.lineMaChucVu.setText(maChucVu)
          lineTenChucVu = self.lineTenChucVu.text()
          maChucVu = "NV" + str(random.randint(0, 999)).zfill(3)
          if len(lineTenChucVu)== 0:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa nhập dữ liệu!")
          else:
               
               query.execute("SELECT * FROM chucvu WHERE tenChucVu = %s", (lineTenChucVu,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Chức vụ này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO chucvu (maChucVu, tenChucVu) VALUES (%s, %s)", (maChucVu, lineTenChucVu))
                    db.commit()
                    QMessageBox.information(self,"Thông báo","Đã thêm vào danh sách!")
                    self.lineTenChucVu.clear()
                    self.stackNhanVien()
     def stackQuyen(self):
          self.stackedWidget.setCurrentIndex(4)
     def stackLop(self):
          self.stackedWidget.setCurrentIndex(5)
     def stackHKNH(self):
          self.stackedWidget.setCurrentIndex(6)
     def stackMonHoc(self):
          self.stackedWidget.setCurrentIndex(7)
     def stackKetQua(self):
          self.stackedWidget.setCurrentIndex(8)
     def stackHocPhi(self):
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
               formLogin.lineTenDangNhap.clear()
               formLogin.lineMatKhau.clear()

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
     