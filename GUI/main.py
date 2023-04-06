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

          self.btnThemMonHoc.clicked.connect(self.addMonHoc)
          self.btnCapNhatMonHoc.clicked.connect(self.updateMonHoc)
          self.btnXoaMonHoc.clicked.connect(self.deleteMonHoc)

          self.btnThemKQ.clicked.connect(self.addKetQua)
          self.btnCapNhatKetQua.clicked.connect(self.updateKetQua)
          self.btnXoaKetQua.clicked.connect(self.deleteKetQua)

          self.btnThemHocLuc.clicked.connect(self.addHocLuc)
          self.btnCapNhatHocLuc.clicked.connect(self.updateHocLuc)
          self.btnXoaHocLuc.clicked.connect(self.deleteHocLuc)

          self.btnThemHanhKiem.clicked.connect(self.addHanhKiem)
          self.btnCapNhatHanhKiem.clicked.connect(self.updateHanhKiem)
          self.btnXoaHanhKiem.clicked.connect(self.deleteHanhKiem)

          self.btnQuyDinh.clicked.connect(self.quyDinh)
          self.btnResetQuyDinh.clicked.connect(self.resetQuyDinh)

          self.btnThemKhoi.clicked.connect(self.addKhoi)
          self.btnCapNhatKhoi.clicked.connect(self.updateKhoi)
          self.btnXoaKhoi.clicked.connect(self.deleteKhoi)

          self.btnThemHocKy.clicked.connect(self.addHocKy)
          self.btnCapNhatHocKy.clicked.connect(self.updateHocKy)
          self.btnXoaHocKy.clicked.connect(self.deleteHocKy)
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
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
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

          maKhoi = "KH" + str(random.randint(0,999)).zfill(3)
          self.lineMaKhoi.setText(maKhoi)

          query.execute("SELECT *FROM khoilop")
          data = query.fetchall()
          # populate the widget with the data from the database
          self.tableKhoi.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableKhoi.setItem(i, j, QTableWidgetItem(str(val)))

     def addKhoi(self):
          lineTenKhoi = self.lineTenKhoi.text()
          maKhoi ="KH" + str(random.randint(0,999)).zfill(3)
          if len(lineTenKhoi)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM khoilop WHERE tenKhoiLop = %s", (lineTenKhoi,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Loại kết quả này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO khoilop (maKhoiLop, tenKhoiLop) VALUES (%s, %s)", (maKhoi,lineTenKhoi))
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenKhoi.clear()
          self.stackLop()
     def updateKhoi(self):
          numRows = self.tableKhoi.rowCount()
          for i in range(numRows):
               maKhoi= self.tableKhoi.item(i,0).text()
               tenKhoi = self.tableKhoi.item(i,1).text()
               sql =" UPDATE khoilop SET tenKhoiLop = %s WHERE maKhoiLop =%s"
               val = (tenKhoi,maKhoi)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackLop()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
     
     def deleteKhoi(self):
          selected = self.tableKhoi.selectedItems()
          
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
                         maKhoi = self.tableKhoi.item(row, 0).text()
                         self.tableKhoi.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM khoilop WHERE maKhoiLop= %s"
                         val = (maKhoi,)
                         try:              
                              query.execute(sql,val)
                              db.commit()
                         except:
                         # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def stackHKNH(self):
          self.stackedWidget.setCurrentIndex(6)

          lineMaHocKy = "HK" + str(random.randint(0,999)).zfill(3)
          self.lineMaHocKy.setText(lineMaHocKy)
          query.execute("SELECT *FROM hocky")
          data = query.fetchall()
          # populate the widget with the data from the database
          self.tableHocKy.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableHocKy.setItem(i, j, QTableWidgetItem(str(val)))
     def addHocKy(self):
          lineTenHocKy = self.lineTenHocKy.text()
          lineMaHocKy = "HK" + str(random.randint(0,999)).zfill(3)
          cboxHeSoHocKy = self.cboxHeSoHocKy.currentText()
          if len(lineTenHocKy)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM hocky WHERE tenHocKy = %s", (lineTenHocKy,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Môn học này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO hocky (maHocKy, tenHocKy,heSo) VALUES (%s, %s,%s)", (lineMaHocKy,lineTenHocKy,cboxHeSoHocKy))
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenHocKy.clear()
          self.stackHKNH()

     def updateHocKy(self):
          pass
     def deleteHocKy(self):
          pass
     def stackMonHoc(self):
          self.stackedWidget.setCurrentIndex(7)

          query.execute("SELECT *FROM monhoc")
          data = query.fetchall()
          # populate the widget with the data from the database
          self.tableMonHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(val)))

          maMonHoc = "MH" + str(random.randint(0,999)).zfill(3)
          self.lineMaMonHoc.setText(maMonHoc)
     def addMonHoc(self):
          lineTenMonHoc = self.lineTenMonHoc.text()
          lineSoTiet = self.lineSoTiet.text()
          cboxHeSo = self.cboxHeSo.currentText()

          maMonHoc ="MH" + str(random.randint(0,999)).zfill(3)

          if len(lineTenMonHoc)==0 and len(lineSoTiet)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM monhoc WHERE tenMonHoc = %s", (lineTenMonHoc,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Môn học này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO monhoc (maMonHoc, tenMonHoc,soTiet,heSo) VALUES (%s, %s,%s,%s)", (maMonHoc,lineTenMonHoc,lineSoTiet,cboxHeSo))
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenMonHoc.clear()
          self.lineSoTiet.clear()
          self.stackMonHoc()
     def updateMonHoc(self):
          numRows = self.tableMonHoc.rowCount()
          for i in range(numRows):
               maMonHoc= self.tableMonHoc.item(i,0).text()
               tenMonHoc = self.tableMonHoc.item(i,1).text()
               soTietMonHoc = self.tableMonHoc.item(i,2).text()
               heSoMonHoc = self.tableMonHoc.item(i,3).text()
               sql =" UPDATE monhoc SET tenMonHoc = %s, soTiet = %s, heSo = %s WHERE maMonHoc =%s"
               val = (tenMonHoc,soTietMonHoc,heSoMonHoc,maMonHoc)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
               self.stackMonHoc()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
     
     
     def deleteMonHoc(self):
          selected = self.tableMonHoc.selectedItems()
          
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
                         maMonHoc = self.tableMonHoc.item(row, 0).text()
                         self.tableMonHoc.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM monhoc WHERE maMonHoc= %s"
                         val = (maMonHoc,)
                         try:              
                              query.execute(sql,val)
                              db.commit()
                         except:
                         # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def stackKetQua(self):
          self.stackedWidget.setCurrentIndex(8)
          sqlKetQua = "SELECT *FROM ketqua"
          query.execute(sqlKetQua)
          data = query.fetchall()
          self.tableKetQua.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableKetQua.setItem(i, j, QTableWidgetItem(str(val)))
          sqlHocLuc = "SELECT *FROM hocluc "
          query.execute(sqlHocLuc)
          dataHocLuc= query.fetchall()
          # populate the widget with the data from the database
          self.tableHocLuc.setRowCount(len(dataHocLuc))
          for i, row in enumerate(dataHocLuc):
               for j, val in enumerate(row):
                    self.tableHocLuc.setItem(i, j, QTableWidgetItem(str(val)))

          sqlHanhKiem = "SELECT * FROM hanhkiem"
          query.execute(sqlHanhKiem)
          dataHanhKiem = query.fetchall()
          self.tableHanhKiem.setRowCount(len(dataHanhKiem))
          for i, row in enumerate(dataHanhKiem):
               for j, val in enumerate(row):
                    self.tableHanhKiem.setItem(i, j, QTableWidgetItem(str(val)))
     
          


          maKetQua ="KQ" + str(random.randint(0,999)).zfill(3)
          self.lineMaKetQua.setText(maKetQua)

          maHocLuc ="HL"+str(random.randint(0,999)).zfill(3)
          self.lineMaHocLuc.setText(maHocLuc)

          maHanhKiem = "HK" + str(random.randint(0,999)).zfill(3)
          self.lineMaHanhKiem.setText(maHanhKiem)
     def addKetQua(self):
          lineTenKetQua = self.lineTenKetQua.text()
          maKetQua ="KQ" + str(random.randint(0,999)).zfill(3)
          if len(lineTenKetQua)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM ketqua WHERE tenKetQua = %s", (lineTenKetQua,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Loại kết quả này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO ketqua (maKetQua, tenKetQUa) VALUES (%s, %s)", (maKetQua,lineTenKetQua))
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenKetQua.clear()
          self.stackKetQua()
     def updateKetQua(self):
          numRows = self.tableKetQua.rowCount()
          for i in range(numRows):
               maKetQua= self.tableKetQua.item(i,0).text()
               tenKetQua = self.tableKetQua.item(i,1).text()
               sql =" UPDATE ketqua SET tenKetQua = %s WHERE maKetQua =%s"
               val = (tenKetQua,maKetQua)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackKetQua()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
     
     def deleteKetQua(self):
          selected = self.tableKetQua.selectedItems()
          
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
                         maMonHoc = self.tableKetQua.item(row, 0).text()
                         self.tableKetQua.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM ketqua WHERE maKetQua= %s"
                         val = (maMonHoc,)
                         try:              
                              query.execute(sql,val)
                              db.commit()
                         except:
                         # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def addHocLuc(self):
          lineTenHocLuc = self.lineTenHocLuc.text()
          lineDiemCD = self.lineDiemCD.text()
          lineDiemCT = self.lineDiemCT.text()
          lineDiemKhongChe = self.lineDiemKhongChe.text()
          maHocLuc ="HL"+str(random.randint(0,999)).zfill(3)
          
          if len(lineTenHocLuc)==0 and len(lineDiemCD)==0 and len(lineDiemCT)==0 and len(lineDiemKhongChe)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM hocluc WHERE tenHocLuc = %s", (lineTenHocLuc,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Loại học lực này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO hocluc (maHocLuc,tenHocLuc,diemCanDuoi,diemCanTren,diemKhongChe) VALUES (%s, %s,%s,%s,%s)", (maHocLuc,lineTenHocLuc,lineDiemCD,lineDiemCT,lineDiemKhongChe))
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenHocLuc.clear()
          self.lineDiemCD.clear()
          self.lineDiemCT.clear()
          self.lineDiemKhongChe.clear()
          self.stackKetQua()
     def updateHocLuc(self):
          numRows = self.tableHocLuc.rowCount()
          for i in range(numRows):
               maHocLuc= self.tableHocLuc.item(i,0).text()
               tenHocLuc= self.tableHocLuc.item(i,1).text()
               diemCD = self.tableHocLuc.item(i,2).text()
               diemCT = self.tableHocLuc.item(i,3).text()
               diemKhongChe = self.tableHocLuc.item(i,4).text()
               sql =" UPDATE hocluc SET tenHocLuc = %s,diemCanDuoi=%s,diemCanTren=%s,diemKhongChe=%s WHERE maHocLuc =%s"
               val = (tenHocLuc,diemCD,diemCT,diemKhongChe,maHocLuc)
               try:             
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackKetQua()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
    
     def deleteHocLuc(self):
          selected = self.tableHocLuc.selectedItems()
          
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
                         maHocLuc = self.tableHocLuc.item(row, 0).text()
                         self.tableHocLuc.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM hocluc WHERE maHocLuc = %s"
                         val = (maHocLuc,)
                         try:              
                              query.execute(sql,val)
                              db.commit()
                         except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                              return
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def addHanhKiem(self):
          lineTenHanhKiem = self.lineTenHanhKiem.text()
          maHanhKiem = "HK" + str(random.randint(0,999)).zfill(3)
          if len(lineTenHanhKiem)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM hanhkiem WHERE tenHanhKiem = %s", (lineTenHanhKiem,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Khoản phí này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO hanhkiem (maHanhKiem, tenHanhKiem) VALUES (%s, %s)", (maHanhKiem, lineTenHanhKiem))
                    #db.commit()
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenHanhKiem.clear()
          self.stackKetQua()
     def updateHanhKiem(self):
          numRows = self.tableHanhKiem.rowCount()
          for i in range(numRows):
               maHanhKiem= self.tableHanhKiem.item(i,0).text()
               tenHanhKiem = self.tableHanhKiem.item(i,1).text()
               sql =" UPDATE hanhkiem SET tenHanhKiem = %s WHERE maHanhKiem =%s"
               val = (tenHanhKiem,maHanhKiem)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackKetQua()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
    
     def deleteHanhKiem(self):
          selected = self.tableHanhKiem.selectedItems()
          
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
                         maHanhKiem = self.tableHanhKiem.item(row, 0).text()
                         self.tableHanhKiem.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM hanhkiem WHERE maHanhKiem = %s"
                         val = (maHanhKiem,)
                         try:              
                              query.execute(sql,val)
                              db.commit()
                         except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                              return
                    QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")
               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def quyDinh(self):
          spinTuoitToiThieu = self.spinTuoitToiThieu.value()
          spinTuoiToiDa = self.spinTuoiToiDa.value()
          spinLopToiThieu = self.spinLopToiThieu.value()
          spinLopToiDa = self.spinLopToiDa.value()
          spinDiem = self.spinDiem.value()
          query.execute("INSERT INTO quydinh (tuoiCanDuoi, tuoiCanTren,siSoCanDuoi,siSoCanTren,diemDat) VALUES (%s, %s,%s,%s,%s)", (spinTuoitToiThieu,spinTuoiToiDa,spinLopToiThieu,spinLopToiDa,spinDiem))
                    #db.commit()
          try:              
                    #query.execute(sql,val)
               db.commit()
          except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
               QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
               return
          QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.stackKetQua()
     def resetQuyDinh(self):
          self.spinTuoitToiThieu.setValue(0)
          self.spinTuoiToiDa.setValue(0)
          self.spinLopToiThieu.setValue(0)
          self.spinLopToiDa.setValue(0)
          self.spinDiem.setValue(0)

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
                    #db.commit()
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
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
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
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
                         try:              
                              query.execute(sql,val)
                              db.commit()
                         except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                              return
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
     