import base64
import sys
import re
from PyQt5 import QtWidgets,uic,QtGui,QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap,QIcon,QImage
import random
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QFileDialog
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
          self.img_base64 = None 
          self.maHocSinh=None
          self.maChucVu = None
          self.maNhanVien = None
          self.maKhoi = None
          self.maHocKy = None
          self.maNamHoc = None
          self.maMonHoc = None
          self.maKetQua = None
          self.MaHocLuc = None
          self.MaHanhKiem = None
          self.maPhi = None
          self.maPhieu = None
          self.maGiaoVien = None
          self.maLop = None
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

          self.btnThemNamHoc.clicked.connect(self.addNamHoc)
          self.btnCapNhatNamHoc.clicked.connect(self.updateNamHoc)
          self.btnXoaNamHoc.clicked.connect(self.deleteNamHoc)

          self.btnThemHocSinh.clicked.connect(self.addHocSinh)
          self.btnCapNhatHocSinh.clicked.connect(self.updateHocSinh)
          self.btnXoaHocSinh.clicked.connect(self.deleteHocSinh)
          self.btnLayAnhOfHocSinh.clicked.connect(self.imageHocSinh)

          self.btnThemGiaoVien.clicked.connect(self.addGiaoVien)
          self.btnCapNhatGiaoVien.clicked.connect(self.updateGiaoVien)
          self.btnXoaGiaoVien.clicked.connect(self.deleteGiaoVien)
          self.btnGetImageGiaoVien.clicked.connect(self.imageGiaoVien)

          self.btnThemLopHoc.clicked.connect(self.addLop)
          self.btnCapNhatLopHoc.clicked.connect(self.updateLop)
          self.btnXoaLopHoc.clicked.connect(self.deleteLop)
     def stackHocSinh(self):
          self.stackedWidget.setCurrentIndex(1)

          maHocSinh="HS" + str(random.randint(1000,9999)).zfill(3)
          #maHocSinh = self.maHocSinh
          self.lineMaHocSinh.setText(maHocSinh)
          self.maHocSinh = maHocSinh

          sqlHocSinh = "SELECT * FROM hocsinh"
          try:
               query.execute(sqlHocSinh)
               data = query.fetchall()
               # populate the widget with the data from the database
               self.tableHocSinh.setRowCount(len(data))
               for i, row in enumerate(data):
                    #self.tableHocSinh.insertRow(i)
                    for j, val in enumerate(row):
                         item = str(val)
                         if j == 8:
                              item = self.getImageLabel(val)
                              self.tableHocSinh.setCellWidget(i, j,item)
                         else:
                              self.tableHocSinh.setItem(i,j,QtWidgets.QTableWidgetItem(item))
               self.tableHocSinh.verticalHeader().setDefaultSectionSize(180)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          self.displayInforInTabPhanLop()
          '''# populate the widget with the data from the database
          self.tableHocSinh.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    self.tableHocSinh.setItem(i, j, QTableWidgetItem(str(val)))
          self.tableHocSinh.itemSelectionChanged.connect(self.displayItemDataHocSinh)
          

     def displayItemDataHocSinh(self):     
          selected = self.tableHocSinh.selectedItems()
          if selected and len(selected) >= 9: 
               lineMaHS = selected[0].text()
               tenHocSinh = selected[1].text()
               ngaySinh = selected[2].text()
               gioitinh = selected[3].text()
               email = selected[4].text()
               diachi = selected[5].text()
               tenphuhuynh = selected[6].text()
               sodienthoai = selected[7].text()
               hinhanh = selected[8].text()
               self.lineMaHocSinh.setText(lineMaHS)
               self.lineTenHocSinh.setText(tenHocSinh)
               self.dateNgaySinhOfHS.setDate(QDate.fromString(ngaySinh,"%d-%m-%Y"))
               self.cboxGioiTinhOfHocSinh.setCurrentText(gioitinh)
               self.lineEmailOfHocSinh.setText(email)
               self.lineDiaChiOfHocSinh.setText(diachi)
               self.lineTenPhuHuynh.setText(tenphuhuynh)
               self.lineSoDienThoaiOfPhuHuynh.setText(sodienthoai)
               #pixmap = QPixmap()
               if isinstance(hinhanh, bytes): # kiểm tra kiểu dữ liệu
                    pixmap = self.getImageLabel(hinhanh)
                    if pixmap:
                         self.lblImageHocSinh.setPixmap(pixmap)
                    else:
                         self.lblImageHocSinh.clear()
          print("Hiển thị thông tin")
     def getImageFromData(self, image_data):
          try:
               #byte_data = QtGui.QPixmaploadFromData(image_data,'jpg')
               pixmap = QPixmap()
               pixmap.loadFromData(image_data)
               return pixmap
          except:
               return None'''
     def displayInforInTabPhanLop(self):
          sqlNamHocInTabPhanLop = "SELECT tenNamHoc FROM namhoc"
          try:
               query.execute(sqlNamHocInTabPhanLop)
               data = query.fetchall()
               for row in data:
                    self.cBoxNH.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          
          sqlKhoiLopInTabPhanLop = "SELECT tenKhoiLop FROM khoilop "
          try :
               query.execute(sqlKhoiLopInTabPhanLop)
               data = query.fetchall()
               for row in data:
                    self.cBoxKhoi.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)

          sqlListHocSinhInTabPhanLop="SELECT tenHocSinh FROM hocsinh WHERE maHocSinh NOT IN (SELECT maHocSinh FROM phanlop,lop WHERE phanlop.maLop = lop.maLop)"
          try: 
               query.execute(sqlListHocSinhInTabPhanLop)
               data = query.fetchall()
               for row in data:
                    self.cBoxHocSinh.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:",e)
          #sqlLopHocInTabPhanLop = "SELECT tenLop FROM n"
     def getImageLabel(self,image):
          imageLabel = QtWidgets.QLabel(self.centralwidget)
          imageLabel.setText("")
          imageLabel.setScaledContents(True)
          '''pixmap = QtGui.QPixmap()
          pixmap.loadFromData(image, 'jpg')'''
          qimage = QtGui.QImage.fromData(image, '*.png *.jpg *.bmp')
          pixmap = QtGui.QPixmap.fromImage(qimage)
          imageLabel.setPixmap(pixmap)
          return imageLabel          
     def addHocSinh(self):
          lineTenHocSinh  = self.lineTenHocSinh.text()
          dateNgaySinhOfHS = self.dateNgaySinhOfHS.date().toPyDate()
          date = dateNgaySinhOfHS.strftime("%Y-%m-%d")
          cboxGioiTinhOfHocSinh = self.cboxGioiTinhOfHocSinh.currentText()
          lineEmailOfHocSinh = self.lineEmailOfHocSinh.text()
          lineDiaChiOfHocSinh = self.lineDiaChiOfHocSinh.text()
          lineTenPhuHuynh = self.lineTenPhuHuynh.text()
          lineSoDienThoaiOfPhuHuynh = self.lineSoDienThoaiOfPhuHuynh.text()
          img_base64 = self.img_base64
          maHocSinh = self.maHocSinh
          if len(lineTenHocSinh)==0 and len(lineEmailOfHocSinh) == 0 and len(lineDiaChiOfHocSinh) == 0 and len(lineTenPhuHuynh) == 0 and len(lineSoDienThoaiOfPhuHuynh) == 0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT COUNT(*) FROM hocsinh WHERE maHocSinh = %s",(maHocSinh,))
               checkMaHS = query.fetchone()
               if checkMaHS[0]>0:
                    self.stackHocSinh()
               else:
                    print("Email:", lineEmailOfHocSinh) 
                    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", lineEmailOfHocSinh):
                         query.execute("SELECT * FROM hocsinh WHERE email = %s",(lineEmailOfHocSinh,))
                         check = query.fetchone()
                         if check is not None:
                              QMessageBox.information(self,"Thông báo","Email này đã tồn tại trong danh sách!")
                         else:
                              print("Số điện thoai:",lineSoDienThoaiOfPhuHuynh)
                              if  re.match(r"^\d{10}$", lineSoDienThoaiOfPhuHuynh):
                                   query.execute("INSERT INTO hocsinh (maHocSinh , tenHocSinh,ngaySinh,gioitinh,email,diaChi,tenPhuHuynh,soDienThoai,hinhAnh) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)", (maHocSinh,lineTenHocSinh,date,cboxGioiTinhOfHocSinh,lineEmailOfHocSinh,lineDiaChiOfHocSinh,lineTenPhuHuynh,lineSoDienThoaiOfPhuHuynh,img_base64))
                                   try:              
                                        #query.execute(sql,val)
                                        db.commit()
                                        QMessageBox.information(self,"Thông báo",f"Thêm học sinh {lineTenHocSinh} vào danh sách thành công!")
                                   #query.execute("SELECT * FROM hocsinh ORDER BY maHocSinh DESC")

                                   except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                                        QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                                        db.rollback()
                                   self.lineTenHocSinh.clear()
                                   self.lineEmailOfHocSinh.clear()
                                   self.lineDiaChiOfHocSinh.clear()
                                   self.lineTenPhuHuynh.clear()
                                   self.lineSoDienThoaiOfPhuHuynh.clear()
                                   self.dateNgaySinhOfHS.clear()
                                   self.lblImageHocSinh.clear()
     
                                   self.stackHocSinh()
                              else: 
                                   QMessageBox.warning(self, "Cảnh bảo",f"Số điện thoại{lineSoDienThoaiOfPhuHuynh} không hợp lệ")
                    else:
                         QMessageBox.information(self,"Thông báo","Email bạn nhập không hợp lệ!") 
     def imageHocSinh(self):
          choose = QFileDialog.getOpenFileName(None, 'HinhAnh', '', 'FILE img (*.png *.jpg *.bmp)')
          # If the user did not select a file, return immediately
          if not choose[0]:
               return
          with open(choose[0], 'rb') as f:
               img_bytes = f.read()
          px = QtGui.QPixmap(choose[0])
          self.lblImageHocSinh.setPixmap(px)
          self.img_base64 = img_bytes
     def imageGiaoVien(self):
          choose = QFileDialog.getOpenFileName(None, 'HinhAnh', '', 'FILE img (*.png *.jpg *.bmp)')
          # If the user did not select a file, return immediately
          if not choose[0]:
               return
          with open(choose[0], 'rb') as f:
               img_bytes = f.read()
          px = QtGui.QPixmap(choose[0])
          self.lblImageGiaoVien.setPixmap(px)
          self.img_base64 = img_bytes     
     def updateHocSinh(self):
          numRows = self.tableHocSinh.rowCount()
          for i in range(numRows):
               maHocSinh = self.tableHocSinh.item(i,0).text()
               tenHocSinh = self.tableHocSinh.item(i,1).text()
               date = self.tableHocSinh.item(i,2).text()
               gioiTinh = self.tableHocSinh.item(i,3).text()
               email = self.tableHocSinh.item(i,4).text()
               diachi = self.tableHocSinh.item(i,5).text()
               tenPH = self.tableHocSinh.item(i,6).text()
               soDT = self.tableHocSinh.item(i,7).text()
               sql =" UPDATE hocsinh SET tenHocSinh = %s, ngaySinh = %s, gioitinh =%s, email= %s, diaChi = %s, tenPhuHuynh = %s,soDienThoai = %s WHERE maHocSinh =%s"
               val = (tenHocSinh,date,gioiTinh,email,diachi,tenPH,soDT,maHocSinh)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackHocSinh()
          QMessageBox.information(self,"Thông báo",f"Cập nhật dữ liệu cho học sinh có mã {maHocSinh} thành công!")

     def deleteHocSinh(self):
          selected = self.tableHocSinh.selectedItems()
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
                         maHocSinh = self.tableHocSinh.item(row, 0).text()
                         self.tableHocSinh.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM hocsinh WHERE maHocSinh= %s"
                         val = (maHocSinh,)
                         try:
                              query.execute(sql,val)
                              db.commit()
                              QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công")
                         except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def stackGiaoVien(self):
          self.stackedWidget.setCurrentIndex(2)
          maGiaoVien = "GV" + str(random.randint(1000,9999)).zfill(3)
          self.lineMaGV.setText(maGiaoVien)
          self.maGiaoVien = maGiaoVien
          '''maMonHoc = self.maMonHoc
          maChucVu = self.maChucVu'''
          sqlGiaoVien = "SELECT maGiaoVien,tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,monhoc.tenMonHoc,chucvu.tenChucVu,hinhAnh FROM giaovien,monhoc,chucvu WHERE giaovien.maMonHoc = monhoc.maMonHoc AND giaovien.maChucVu = chucvu.maChucVu ORDER BY maGiaoVien ASC"
          #value =(maMonHoc,maChucVu)
          try:
               query.execute(sqlGiaoVien)
               data = query.fetchall()
               self.tableGiaoVien.setRowCount(len(data))
               for i, row in enumerate(data):
                    #self.tableHocSinh.insertRow(i)
                    for j, val in enumerate(row):
                         item = str(val)
                         if j == 9:
                              item = self.getImageLabel(val)
                              self.tableGiaoVien.setCellWidget(i, j,item)
                         else:
                              self.tableGiaoVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
               self.tableGiaoVien.verticalHeader().setDefaultSectionSize(180)
          
          except mysql.connector.errors.InternalError as e:
               print("Error executing query MYSQL query:",e)

          sqlChuyenMon = "SELECT tenMonHoc FROM monhoc"
          try:
               query.execute(sqlChuyenMon)
               data = query.fetchall()
               for row in data:
                    self.CboxChuyenMon.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing query MYSQL query:",e)
          sqlChucVuInTabGiaoVien = "SELECT tenChucVu FROM chucvu"
          try:
               query.execute(sqlChucVuInTabGiaoVien)
               data = query.fetchall()
               for row in data:
                    self.CboxChucVu.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing query MYSQL query:",e)
     def displayInforInTabPhanCong(self):
          pass
     def addGiaoVien(self):
          lineTenGV  = self.lineTenGV.text()
          dateNgaySinhOfGV = self.DatBirthOfGV.date().toPyDate()
          date = dateNgaySinhOfGV.strftime("%Y-%m-%d")
          cboxGioiTinhOfGV = self.gioiTinhOfGV.currentText()
          lineDiaChiOfGV = self.diaChiOfGV.text()          
          lineEmailOfGV = self.emailOfGV.text()
          lineSoDienThoaiOfGV = self.soDienThoaiOfGV.text()
          CboxChuyenMon = self.CboxChuyenMon.currentText()
          CboxChucVu = self.CboxChucVu.currentText()
          img_base64 = self.img_base64
          maGiaoVien = self.maGiaoVien
          if len(lineTenGV)==0 and len(lineEmailOfGV) == 0 and len(lineDiaChiOfGV) == 0 and len(lineSoDienThoaiOfGV) == 0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT COUNT(*) FROM giaovien WHERE maGiaoVien = %s",(maGiaoVien,))
               checkMaGV = query.fetchone()
               if checkMaGV[0]>0:
                    self.stackGiaoVien()
               else:
                    print("Email:", lineEmailOfGV) 
                    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", lineEmailOfGV):
                         query.execute("SELECT * FROM giaovien WHERE email = %s",(lineEmailOfGV,))
                         check = query.fetchone()
                         if check is not None:
                              QMessageBox.information(self,"Thông báo",f"Email {lineEmailOfGV} đã tồn tại trong danh sách!")
                         else:
                              print("Số điện thoai:",lineSoDienThoaiOfGV)
                              if  re.match(r"^\d{10}$", lineSoDienThoaiOfGV):
                                   sqlGetMonHoc = "SELECT maMonHoc FROM monhoc WHERE tenMonHoc = %s"
                                   val = (CboxChuyenMon,)
                                   try : 
                                        query.execute(sqlGetMonHoc, val)
                                        maMonHoc = query.fetchone()[0]
                                   except mysql.connector.errors.InternalError as e:
                                        print("Error executing MySQL query:",e)
                                   sqlGetChucVu = "SELECT maChucVu FROM chucvu WHERE tenChucVu = %s"
                                   val = (CboxChucVu,)
                                   try : 
                                        query.execute(sqlGetChucVu, val)
                                        maChucVu = query.fetchone()[0]
                                   except mysql.connector.errors.InternalError as e:
                                        print("Error executing MySQL query:",e)   
                                   query.execute("INSERT INTO giaovien (maGiaoVien , tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,maMonHoc,maChucVu,hinhAnh) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (maGiaoVien,lineTenGV,date,cboxGioiTinhOfGV,lineDiaChiOfGV,lineEmailOfGV,lineSoDienThoaiOfGV,maMonHoc,maChucVu,img_base64))
                                   try:              
                                        #query.execute(sql,val)
                                        db.commit()
                                        QMessageBox.information(self,"Thông báo",f"Thêm giáo viên {lineTenGV} vào danh sách thành công!")
                                   #query.execute("SELECT * FROM hocsinh ORDER BY maHocSinh DESC")

                                   except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                                        QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                                        db.rollback()
                                   self.lineTenGV.clear()
                                   self.emailOfGV.clear()
                                   self.diaChiOfGV.clear()
                                   self.lineTenPhuHuynh.clear()
                                   self.soDienThoaiOfGV.clear()
                                   self.dateNgaySinhOfHS.clear()
                                   self.lblImageGiaoVien.clear()
                                   self.CboxChuyenMon.clear()
                                   self.CboxChucVu.clear()     
                                   self.stackGiaoVien()
                              else: 
                                   QMessageBox.warning(self, "Cảnh bảo",f"Số điện thoại {lineSoDienThoaiOfGV} không hợp lệ")
                    else:
                         QMessageBox.information(self,"Thông báo","Email bạn nhập không hợp lệ!") 
     def updateGiaoVien(self):
          numRows = self.tableGiaoVien.rowCount()
          for i in range(numRows):
               maGiaoVien = self.tableGiaoVien.item(i,0).text()
               tenGiaoVien = self.tableGiaoVien.item(i,1).text()
               date = self.tableGiaoVien.item(i,2).text()
               gioiTinh = self.tableGiaoVien.item(i,3).text()
               diachi = self.tableGiaoVien.item(i,4).text()
               email = self.tableGiaoVien.item(i,5).text()
               soDT = self.tableGiaoVien.item(i,6).text()
               chuyenmon = self.tableGiaoVien.item(i,7).text()
               chucvu = self.tableGiaoVien.item(i,8).text()
               sqlGetMonHoc = "SELECT maMonHoc FROM monhoc WHERE tenMonHoc = %s"
               val = (chuyenmon,)
               try : 
                    query.execute(sqlGetMonHoc, val)
                    maMonHoc = query.fetchone()[0]
               except mysql.connector.errors.InternalError as e:
                    print("Error executing MySQL query:",e)
               sqlGetChucVu = "SELECT maChucVu FROM chucvu WHERE tenChucVu = %s"
               val = (chucvu,)
               try : 
                    query.execute(sqlGetChucVu, val)
                    maChucVu = query.fetchone()[0]
               except mysql.connector.errors.InternalError as e:
                    print("Error executing MySQL query:",e)   
                                   
               sql =" UPDATE giaovien SET tenGiaoVien = %s, ngaySinh = %s, gioiTinh =%s, diaChi= %s, email = %s, soDienThoai = %s,maMonHoc = %s, maChucVu =%s WHERE maGiaoVien=%s"
               val = (tenGiaoVien,date,gioiTinh,diachi,email,soDT,maMonHoc,maChucVu,maGiaoVien)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackGiaoVien()
          QMessageBox.information(self,"Thông báo",f"Cập nhật dữ liệu cho giáo viên có mã {maGiaoVien} thành công!")

     def deleteGiaoVien(self):
          selected = self.tableGiaoVien.selectedItems()
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
                         maGiaoVien = self.tableGiaoVien.item(row, 0).text()
                         self.tableGiaoVien.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM giaovien WHERE maGiaoVien= %s"
                         val = (maGiaoVien,)
                         try:
                              query.execute(sql,val)
                              db.commit()
                              QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công")
                         except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def stackNhanVien(self):
          self.stackedWidget.setCurrentIndex(3)
           # Generate a new unique ID for the new record
          sqlChucVu  = "SELECT *FROM chucvu"
          try : 
               query.execute(sqlChucVu)
               data = query.fetchall()
          # populate the widget with the data from the database
               self.tableChucVu.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableChucVu.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          maChucVu = "CV" + str(random.randint(0, 999)).zfill(3)
          self.lineMaChucVu.setText(maChucVu)
          self.maChucVu = maChucVu
          maNhanVien ="NV" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaNhanVien.setText(maNhanVien)
          self.maNhanVien = maNhanVien

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
                         try:
                              query.execute(sql,val)
                              db.commit()
                              QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công")
                         except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return  

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def tabChucVu(self):
          #self.lineMaChucVu.setText(maChucVu)
          lineTenChucVu = self.lineTenChucVu.text()
          maChucVu = self.maChucVu
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
          self.maKhoi= maKhoi
          maLop = "LH" + str(random.randint(0,99)).zfill(3)
          self.lineMaLop.setText(maLop)
          self.maLop = maLop
          sqlKhoiLop = "SELECT *FROM khoilop"
          try:
               query.execute(sqlKhoiLop)
               data = query.fetchall()
               # populate the widget with the data from the database
               self.tableKhoi.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableKhoi.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)

          self.displayInforInTabLopHoc()
     def displayInforInTabLopHoc(self):
          sqlNamHocInTabLopHoc = "SELECT tenNamHoc FROM namhoc ORDER BY tenNamHoc DESC"
          try :
               query.execute(sqlNamHocInTabLopHoc)
               data = query.fetchall()
               for row in data:
                    self.CboxNamHoc.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)

          sqlKhoiInTabLopHoc = "SELECT tenKhoiLop FROM khoilop ORDER BY tenKhoiLop ASC"
          try:
               query.execute(sqlKhoiInTabLopHoc)
               data = query.fetchall()
               for row in data:
                    self.CboxKhoiLop.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          
          sqlGiaoVienInTabLopHoc = "SELECT tenGiaoVien FROM giaovien"
          try:
               query.execute(sqlGiaoVienInTabLopHoc)
               data = query.fetchall()
               for row in data:
                    self.cBoxGVCN.addItem(row[0])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          
          sqlLopHoc = "SELECT maLop, tenLop, khoilop.tenKhoiLop, namhoc.tenNamHoc,siSo, giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE lop.maKhoiLop = khoilop.maKhoiLop AND lop.maNamHoc = namhoc.maNamHoc AND LOP.maGiaoVien = giaovien.maGiaoVien "
          try:
               query.execute(sqlLopHoc)
               data = query.fetchall()
               self.tableLopHoc.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableLopHoc.setItem(i,j,QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
     def addLop(self):
          lineTenlop = self.lineTenlop.text()
          CboxKhoiLop = self.CboxKhoiLop.currentText()
          CboxNamHoc = self.CboxNamHoc.currentText()
          spinBoxSiso = self.spinBoxSiso.value()
          cBoxGVCN = self.cBoxGVCN.currentText()
          maLop = self.maLop
          if len(lineTenlop) == 0 or spinBoxSiso == 0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu! Sỉ số của lớp học phải lớn hơn 15")
          else: 
               query.execute("SELECT COUNT(*) FROM lop WHERE maLop = %s",(maLop,))
               checkMaLop = query.fetchone()
               if checkMaLop[0]>0:
                    self.stackLop()
               else:
                    sqlGetKhoi = "SELECT maKhoiLop FROM khoilop WHERE tenKhoiLop = %s"
                    val =(CboxKhoiLop,)
                    try:
                         query.execute(sqlGetKhoi,val)
                         maKhoiLop = query.fetchone()[0]
                    except mysql.connector.errors.InternalError as e:
                         print("Error executing MySQL query:",e)
                    sqlGetNamHoc = "SELECT maNamHoc FROM namhoc WHERE tenNamHoc = %s"
                    val =(CboxNamHoc,)
                    try:
                         query.execute(sqlGetNamHoc,val)
                         maNamHoc = query.fetchone()[0]
                    except mysql.connector.errors.InternalError as e:
                         print("Error executing MySQL query:",e)

                    sqlGetGiaoVien = "SELECT maGiaoVien FROM giaovien WHERE tenGiaoVien = %s"
                    val =(cBoxGVCN,)
                    try:
                         query.execute(sqlGetGiaoVien,val)
                         maGiaoVien = query.fetchone()[0]
                    except mysql.connector.errors.InternalError as e:
                         print("Error executing MySQL query:",e)
                    
                    sqlCheckGVOfNamHoc = "SELECT COUNT(*) FROM lop WHERE maGiaoVien = %s AND maNamHoc = %s"
                    val = (maGiaoVien,maNamHoc)
                    query.execute(sqlCheckGVOfNamHoc, val)
                    if query.fetchone()[0] >= 1:
                         QMessageBox.warning(self, "Thông báo", f"Giáo viên {cBoxGVCN} đã quản lý lớp trong năm học {CboxNamHoc}. Không thể thêm lớp mới!")
                    else:
                         if spinBoxSiso < 15 and spinBoxSiso >= 45 :
                              QMessageBox.warning(self, "Thông báo", "Sỉ số của lớp học tối thiểu là 15 học sinh và tối đa là 45 học sinh!")
                         else:
                              sqlLop = "INSERT INTO lop (maLop,tenLop,maKhoiLop,maNamHoc,siSo,maGiaoVien) VALUES (%s,%s,%s,%s,%s,%s)"   
                              val =(maLop,lineTenlop,maKhoiLop,maNamHoc,spinBoxSiso,maGiaoVien)
                              try:
                                   query.execute(sqlLop,val)
                                   db.commit()
                                   QMessageBox.information(self,"Thông báo",f"Thêm {lineTenlop} do giáo viên {cBoxGVCN} quản lý vào danh sách thành công!")
                              except Exception as e:
                                   # Hiển thị thông báo lỗi nếu truy vấn không thành công
                                   QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công:",e)
                                   db.rollback()
                              self.lineTenlop.clear()
                              self.spinBoxSiso.clear()
                              self.CboxKhoiLop.clear()
                              self.CboxNamHoc.clear()
                              self.cBoxGVCN.clear()
                              self.stackLop()                
               
     def updateLop(self):
          numRows = self.tableLopHoc.rowCount()
          for i in range(numRows):
               maLopHoc = self.tableLopHoc.item(i,0).text()
               tenLopHoc = self.tableLopHoc.item(i,1).text()
               khoiLop = self.tableLopHoc.item(i,2).text()
               namhoc = self.tableLopHoc.item(i,3).text()
               spinBoxSiso = self.tableLopHoc.item(i,4).text()
               GVCN = self.tableLopHoc.item(i,5).text()
               sqlGetKhoiLop = "SELECT maKhoiLop FROM khoilop WHERE tenKhoiLop = %s"
               val = (khoiLop,)
               try : 
                    query.execute(sqlGetKhoiLop, val)
                    maKhoiLop = query.fetchone()[0]
               except mysql.connector.errors.InternalError as e:
                    print("Error executing MySQL query:",e)
               sqlGetNamHoc = "SELECT maNamHoc FROM namHoc WHERE tenNamHoc = %s"
               val = (namhoc,)
               try : 
                    query.execute(sqlGetNamHoc, val)
                    maNamHoc = query.fetchone()[0]
               except mysql.connector.errors.InternalError as e:
                    print("Error executing MySQL query:",e)   
               sqlGetGiaoVien = "SELECT maGiaoVien FROM giaovien WHERE tenGiaoVien = %s"
               val = (GVCN,)
               try : 
                    query.execute(sqlGetGiaoVien, val)
                    maGiaoVien = query.fetchone()[0]
               except mysql.connector.errors.InternalError as e:
                    print("Error executing MySQL query:",e)
               
               sql =" UPDATE lop SET tenLop = %s, maKhoiLop = %s, maNamHoc =%s, siSo= %s, maGiaoVien = %s WHERE maLop = %s"
               val = (tenLopHoc,maKhoiLop,maNamHoc,spinBoxSiso,maGiaoVien,maLopHoc)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")

          self.stackLop()
     def deleteLop(self):
          selected = self.tableLopHoc.selectedItems()
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
                         maLop = self.tableLopHoc.item(row, 0).text()
                         self.tableLopHoc.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM lop WHERE maLop= %s"
                         val = (maLop,)
                         try:
                              query.execute(sql,val)
                              db.commit()
                              QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công")
                         except:
                              # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     
     def addKhoi(self):
          lineTenKhoi = self.lineTenKhoi.text()
          maKhoi = self.maKhoi
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
                              QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")

                         except:
                         # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def stackHKNH(self):
          self.stackedWidget.setCurrentIndex(6)
          sqlHocKy = "SELECT * FROM hocky"
          sqlNamHoc = "SELECT * FROM namhoc"
          try: 
               query.execute(sqlHocKy)
               data = query.fetchall()
               self.tableHocKy.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableHocKy.setItem(i, j, QTableWidgetItem(str(val)))

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          try: 
               query.execute(sqlNamHoc)
               dataNamHoc = query.fetchall()
               self.tableNamHoc.setRowCount(len(dataNamHoc))
               for i, row in enumerate(dataNamHoc):
                    for j, val in enumerate(row):
                         self.tableNamHoc.setItem(i, j, QTableWidgetItem(str(val)))
         
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e) 
          # populate the widget with the data from the database
          lineMaHocKy = "HK" + str(random.randint(0,999)).zfill(3)
          self.lineMaHocKy.setText(lineMaHocKy)
          self.maHocKy = lineMaHocKy

          lineMaNamHoc ="NH"+str(random.randint(0,9999)).zfill(6)
          self.lineMaNamHoc.setText(lineMaNamHoc)
          self.maNamHoc = lineMaNamHoc
     def addHocKy(self):
          lineTenHocKy = self.lineTenHocKy.text()
          lineMaHocKy = self.maHocKy
          cboxHeSoHocKy = self.cboxHeSoHocKy.currentText()
          if len(lineTenHocKy)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM hocky WHERE tenHocKy = %s", (lineTenHocKy,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Loại học kỳ này đã có trong danh sách!")
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
          numRows = self.tableHocKy.rowCount()
          for i in range(numRows):
               maHocKy= self.tableHocKy.item(i,0).text()
               tenHocKy = self.tableHocKy.item(i,1).text()
               heSoHocKy = self.tableHocKy.item(i,2).text()
               sql =" UPDATE hocky SET tenHocKy = %s,heSo = %s WHERE maHocKy =%s"
               val = (tenHocKy,heSoHocKy,maHocKy)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackHKNH()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
     def deleteHocKy(self):
          selected = self.tableHocKy.selectedItems()
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
                         maHocKy = self.tableHocKy.item(row, 0).text()
                         self.tableHocKy.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM hocky WHERE maHocKy= %s"
                         val = (maHocKy,)
                         try:              
                              query.execute(sql,val)
                              db.commit()
                              QMessageBox.information(self,"Thông báo","Xóa dữ liệu thành công!")

                         except:
                         # Hiển thị thông báo lỗi nếu truy vấn không thành công
                              QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
                              return               

          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def addNamHoc(self):
          lineTenNamHoc = self.lineTenNamHoc.text()
          maNamHoc=self.maNamHoc
          if len(lineTenNamHoc)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM namhoc WHERE tenNamHoc= %s", (lineTenNamHoc,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Loại năm học này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO namhoc (maNamHoc, tenNamHoc) VALUES (%s, %s)", (maNamHoc,lineTenNamHoc))
                    try:              
                    #query.execute(sql,val)
                         db.commit()
                    except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
                         return
                    QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
          self.lineTenNamHoc.clear()
          self.stackHKNH()
     def updateNamHoc(self):
          numRows = self.tableNamHoc.rowCount()
          for i in range(numRows):
               maNamHoc= self.tableNamHoc.item(i,0).text()
               tenNamHoc = self.tableNamHoc.item(i,1).text()
               sql =" UPDATE namhoc SET tenNamHoc = %s WHERE maNamHoc =%s"
               val = (tenNamHoc,maNamHoc)
               try:              
                    query.execute(sql,val)
                    db.commit()
               except:
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                    QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
                    return
          self.stackHKNH()
          QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
     def deleteNamHoc(self):
          selected = self.tableNamHoc.selectedItems()
          
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
                         maNamHoc = self.tableNamHoc.item(row, 0).text()
                         self.tableNamHoc.removeRow(row)  # xóa dòng khỏi bảng
                         sql = "DELETE FROM namhoc WHERE maNamHoc= %s"
                         val = (maNamHoc,)
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

     def stackMonHoc(self):
          self.stackedWidget.setCurrentIndex(7)
          sqlMonHoc="SELECT *FROM monhoc"
          try:
               query.execute(sqlMonHoc)
               data = query.fetchall()
               # populate the widget with the data from the database
               self.tableMonHoc.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          maMonHoc = "MH" + str(random.randint(0,999)).zfill(3)
          self.lineMaMonHoc.setText(maMonHoc)
          self.maMonHoc = maMonHoc
     def addMonHoc(self):
          lineTenMonHoc = self.lineTenMonHoc.text()
          lineSoTiet = self.lineSoTiet.text()
          cboxHeSo = self.cboxHeSo.currentText()

          maMonHoc =self.maMonHoc

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
          try:
               query.execute(sqlKetQua)
               data = query.fetchall()
               self.tableKetQua.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableKetQua.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          sqlHocLuc = "SELECT *FROM hocluc "
          try:
               query.execute(sqlHocLuc)
               dataHocLuc= query.fetchall()
               # populate the widget with the data from the database
               self.tableHocLuc.setRowCount(len(dataHocLuc))
               for i, row in enumerate(dataHocLuc):
                    for j, val in enumerate(row):
                         self.tableHocLuc.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          sqlHanhKiem = "SELECT * FROM hanhkiem"
          try:
               query.execute(sqlHanhKiem)
               dataHanhKiem = query.fetchall()
               self.tableHanhKiem.setRowCount(len(dataHanhKiem))
               for i, row in enumerate(dataHanhKiem):
                    for j, val in enumerate(row):
                         self.tableHanhKiem.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          
          sqlQuyDinh ="SELECT MAX(tuoiCanDuoi),MAX(tuoiCanTren),MAX(siSoCanDuoi),MAX(siSoCanTren),MAX(diemDat) FROM quydinh  "
          try:
               query.execute(sqlQuyDinh)
               dataQuyDinh = query.fetchone()
               self.spinTuoitToiThieu.setValue(dataQuyDinh[0])
               self.spinTuoiToiDa.setValue(dataQuyDinh[1])
               self.spinLopToiThieu.setValue(dataQuyDinh[2])
               self.spinLopToiDa.setValue(dataQuyDinh[3])
               self.spinDiem.setValue(dataQuyDinh[4])
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)

          maKetQua ="KQ" + str(random.randint(0,999)).zfill(3)
          self.lineMaKetQua.setText(maKetQua)
          self.maKetQua = maKetQua

          maHocLuc ="HL"+str(random.randint(0,999)).zfill(3)
          self.lineMaHocLuc.setText(maHocLuc)
          self.MaHocLuc = maHocLuc

          maHanhKiem = "HK" + str(random.randint(0,999)).zfill(3)
          self.lineMaHanhKiem.setText(maHanhKiem)
          self.MaHanhKiem = maHanhKiem
     def addKetQua(self):
          lineTenKetQua = self.lineTenKetQua.text()
          maKetQua =self.maKetQua
          if len(lineTenKetQua)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               query.execute("SELECT * FROM ketqua WHERE tenKetQua = %s", (lineTenKetQua,))
               check = query.fetchone()
               if check is not None:
                    QMessageBox.information(self,"Thông báo","Loại kết quả này đã có trong danh sách!")
               else:
                    query.execute("INSERT INTO ketqua (maKetQua, tenKetQua) VALUES (%s, %s)", (maKetQua,lineTenKetQua))
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
          maHocLuc =self.MaHocLuc
          
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
          maHanhKiem = self.MaHanhKiem
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
          query.fetchall()
          query.execute("INSERT INTO quydinh (tuoiCanDuoi, tuoiCanTren,siSoCanDuoi,siSoCanTren,diemDat) VALUES (%s, %s,%s,%s,%s)", (spinTuoitToiThieu,spinTuoiToiDa,spinLopToiThieu,spinLopToiDa,spinDiem))
          db.commit()
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
          sqlHocPhi = "SELECT *FROM cackhoanphi"
          try:
               query.execute(sqlHocPhi)
               data = query.fetchall()
               # populate the widget with the data from the database
               self.tableKhoanPhi.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableKhoanPhi.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)

          maPhi = "PH" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaPhi.setText(maPhi)
          self.maPhi = maPhi
          maPhieu = "HD" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaPhieu.setText(maPhieu)
          self.maPhieu = maPhieu
          self.listKhoanPhi()
     def listKhoanPhi(self):
          sqlListKhoanPhi = "SELECT *FROM cackhoanphi"
          try:
               query.execute(sqlListKhoanPhi)
               data = query.fetchall()
          # populate the widget with the data from the database
               self.tableListKhoanPhi.setRowCount(len(data))
               for i, row in enumerate(data):
                    for j, val in enumerate(row):
                         self.tableListKhoanPhi.setItem(i, j, QTableWidgetItem(str(val)))
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
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
          maPhi = self.maPhi
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
query.close()
     