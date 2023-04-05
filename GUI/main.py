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
          self.btnCapNhatChucVu.clicked.connect(self.updateChucVu)

          self.btnThemKhoanPhi.clicked.connect(self.addKhoanPhi)
          self.btnCapNhatKhoanPhi.clicked.connect(self.updateKhoanPhi)
          self.btnXoaKhoanPhi.clicked.connect(self.deleteKhoanPhi)
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
          maChucVu = "CV" + str(random.randint(0, 999)).zfill(3)
          self.lineMaChucVu.setText(maChucVu)
          maNhanVien ="NV" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaNhanVien.setText(maNhanVien)

     def updateChucVu(self):
          # `numRows = self.tableWidget.rowCount()` is getting the number of rows in the table widget
          # `tableWidget` and assigning it to the variable `numRows`. This is used in the
          # `updateChucVu()` and `deleteChucVu()` methods to iterate over all the rows in the table
          # widget.
          numRows = self.tableChucVu.rowCount()
          for i in range(numRows):
               maChucVu = self.tableChucVu.item(i,0).text()
               tenChucVu = self.tableChucVu.item(i,1).text()
               sql =" UPDATE chucvu SET tenChucVu = %s WHERE maChucVu =%s"
               val = (tenChucVu,maChucVu)
               query.execute(sql,val)
               db.commit()
          self.stackNhanVien()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")

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
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                    self.lineTenChucVu.clear()
                    self.stackNhanVien()
     def tabNhanVien(self):
          #lineMaNhanVien = self.lineMaNhanVien.text()
          pass

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
          query.execute("SELECT *FROM cackhoanphi")
          data = query.fetchall()
          # populate the widget with the data from the database
          self.tableKhoanPhi.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableKhoanPhi.setItem(i, j, QTableWidgetItem(str(val)))

          maPhi = "PH" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaPhi.setText(maPhi)

          maPhieu = "HD" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaPhieu.setText(maPhieu)
          self.listKhoanPhi()
     def listKhoanPhi(self):
          query.execute("SELECT *FROM cackhoanphi")
          data = query.fetchall()
          # populate the widget with the data from the database
          self.tableListKhoanPhi.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableListKhoanPhi.setItem(i, j, QTableWidgetItem(str(val)))
          self.tableListKhoanPhi.itemSelectionChanged.connect(self.displayItemData)
          
     def displayItemData(self):     
          selected = self.tableListKhoanPhi.selectedItems()
          if selected and len(selected) >= 2: 
               maPhi = selected[0].text()
               tenPhi = selected[1].text()
               self.lineListMaPhi.setText(maPhi)
               self.lineListTenKhoanPhi.setText(tenPhi)
          



     def addKhoanPhi(self):
          #lineMaPhi
          lineTenKhoanPhi = self.lineTenMaPhi.text()
          maPhi = "PH" + str(random.randint(0, 9999)).zfill(5)
          if len(lineTenKhoanPhi)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM cackhoanphi WHERE tenPhi = %s", (lineTenKhoanPhi,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Khoản phí này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO cackhoanphi (maPhi, tenPhi) VALUES (%s, %s)", (maPhi, lineTenKhoanPhi))
                    db.commit()
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                    self.lineTenMaPhi.clear()
                    self.stackHocPhi()
     def updateKhoanPhi(self):
          numRows = self.tableKhoanPhi.rowCount()
          for i in range(numRows):
               maPhi= self.tableKhoanPhi.item(i,0).text()
               tenPhi = self.tableKhoanPhi.item(i,1).text()
               sql =" UPDATE cackhoanphi SET tenPhi = %s WHERE maPhi =%s"
               val = (tenPhi,maPhi)
               query.execute(sql,val)
               db.commit()
          self.stackHocPhi()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
     def deleteKhoanPhi(self):
          selected = self.tableKhoanPhi.selectedItems()
          
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
                         maPhi = self.tableKhoanPhi.item(row, 0).text()
                         self.tableKhoanPhi.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM cackhoanphi WHERE maPhi = %s"
                         val = (maPhi,)
                         query.execute(sql,val)
                         db.commit()
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

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
     