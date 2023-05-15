# -*- coding: utf-8 -*-
import base64
import string
import openpyxl 
import win32com.client as win32
import sys
import re
import os
import time
import pandas as pd
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from BUS.ChucVuBUS import ChucVuBUS
from DTO.ChucVuDTO import ChucVuDTO
from BUS.CacKhoanPhiBUS import CacKhoanPhiBUS
from DTO.CacKhoanPhi import CacKhoanPhi
from BUS.MonHocBUS import MonHocBUS
from DTO.MonHocDTO import MonHocDTO
from BUS.LoaiDiemBUS import LoaiDiemBUS
from DTO.LoaiDiemDTO import LoaiDiemDTO
from BUS.KetQuaBUS import KetQuaBUS
from DTO.KetQuaDTO import KetQuaDTO
from BUS.HocLucBUS import HocLucBUS
from DTO.HocLucDTO import HocLucDTO
from BUS.HanhKiemBUS import HanhKiemBUS
from DTO.HanhKiemDTO import HanhKiemDTO
from BUS.QuyDinhBUS import QuyDinhBUS
from DTO.QuyDinhDTO import QuyDinhDTO
from BUS.KhoiBUS import KhoiBUS
from DTO.KhoiDTO import KhoiDTO
from BUS.HocKyBUS import HocKyBUS
from DTO.HocKyDTO import HocKyDTO
from BUS.NamHocBUS import NamHocBUS
from DTO.NamHocDTO import NamHocDTO
from BUS.GiaoVienBUS import GiaoVienBUS
from DTO.GiaoVienDTO import GiaoVienDTO
from BUS.HocSinhBUS import HocSinhBUS
from DTO.HocSinhDTO import HocSinhDTO
from BUS.LopHocBUS import LopHocBUS
from DTO.LopHocDTO import LopHocDTO
from BUS.NhanVienBUS import NhanVienBUS
from DTO.NhanVienDTO import NhanVienDTO
from BUS.PhanLopBUS import PhanLopBUS
from DTO.PhanLopDTO import PhanLopDTO
from BUS.PhanCongBUS import PhanCongBUS
from DTO.PhanCongDTO import PhanCongDTO
from BUS.DiemBUS import DiemBUS
from DTO.DiemDTO import DiemDTO
from BUS.NguoiDungBUS import NguoiDungBUS
from DTO.NguoiDungDTO import NguoiDungDTO
from BUS.DiemTBMonHocBUS import DiemTBMonHocBUS
from DTO.KQMHDTO import KQMHDTO
from BUS.BaoCaoBUS import BaoCaoBUS
from DTO.KetQuaLopHocMonHocDTO import KetQuaLopHocMonHocDTO
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
global_username = ''
class FormLogin(QtWidgets.QMainWindow):
     def __init__(self):
          super(FormLogin, self).__init__()
          self.username = ' '
          uic.loadUi("GUI/Form_Login.ui",self)
          px = QtGui.QPixmap("img/child-girl-schoolgirl-elementary-school-student-123686003.jpg")
          self.labelLogin.setPixmap(px)
          self.lineMatKhau.setEchoMode(QtWidgets.QLineEdit.Password)
          self.btnDangNhap.clicked.connect(self.LoginFunction)

     def LoginFunction(self):
          nguoidung = NguoiDungBUS()
          tenDangNhap = self.lineTenDangNhap.text()
          matKhau = self.lineMatKhau.text()
          if len(tenDangNhap)== 0 or len(matKhau)== 0:
              # self.textError.setText("Bạn chưa nhập tên đăng nhập hoặc mật khẩu!")
               QMessageBox.warning(self, 'Đăng nhập', 'Bạn chưa nhập tên đăng nhập hoặc mật khẩu!')

          else:
               '''if tenDangNhap == 'admin' and matKhau =='1234':
                    #QMessageBox.warning(self, 'Đăng nhập', 'Đăng nhập thành công!')
                    #uic.loadUi("GUI/TrangChu.ui",self)
                    trangChu = TrangChu()
                    widget.addWidget(trangChu)
                    widget.setFixedSize(trangChu.width(),trangChu.height())
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    trangChu.show()
                    self.accept()'''
               if nguoidung.checkTenDN_Pass(tenDangNhap,matKhau):
                         global global_username 
                         global_username = tenDangNhap
                         trangChu = TrangChu()
                         widget.addWidget(trangChu)
                         widget.setFixedSize(trangChu.width(),trangChu.height())
                         widget.setCurrentIndex(widget.currentIndex()+1)
               else:
                    QMessageBox.warning(self, 'Đăng nhập', 'Sai tên đăng nhập hoặc mật khẩu!')  
class TrangChu(QtWidgets.QMainWindow):
     def __init__(self):
          super(TrangChu,self).__init__()
          uic.loadUi("GUI/TrangChu.ui",self)
          self.img_base64 = None
          self.role =None
          self.stackedWidget.setCurrentIndex(0)
          #self.btnHSPL.clicked.connect(self.stackHSPL)
          self.getTenDangNhap()          #self.loadlistCV()
     def getTenDangNhap(self):
          nguoiDung = NguoiDungBUS()
          #tenDangNhap = nguoiDung.getList()
          tenDangNhap = global_username
          self.tenDangNhap.setText(tenDangNhap)
          LabelTenNguoiDung = nguoiDung.getUsername(tenDangNhap)
          self.tenNguoiDung.setText(LabelTenNguoiDung[0])
          self.role = nguoiDung.get_role_code(tenDangNhap)
          if self.role == 'CV001':
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
               self.btnBaoCao.clicked.connect(self.stackBaoCao)
          elif self.role =='CV004':
               self.btnMonHoc.clicked.connect(self.stackMonHoc)
               self.btnHocSinh.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnDangXuat.clicked.connect(self.DangXuat)
               self.btnHocPhi.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnGiaoVien.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnLop.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnQuyen.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnHKNH.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnNhanVien.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnKetQua.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
          elif self.role =='CV003':
               self.btnHocPhi.clicked.connect(self.stackHocPhi)
               self.btnDangXuat.clicked.connect(self.DangXuat)
               self.btnMonHoc.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnGiaoVien.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnLop.clicked.connect(lambda:QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnQuyen.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnHKNH.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnKetQua.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnHocSinh.clicked.connect(lambda:QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
     def stackBaoCao(self):
          self.stackedWidget.setCurrentIndex(10)
          self.comboBox_10.currentTextChanged.connect(self.BaoCao_lop_loadlist)
          self.btnMH_HK.clicked.connect(self.display_BaoCao)
          self.loadlistBaoCao()
     def loadlistBaoCao(self):
          namhoc = NamHocBUS()
          list = namhoc.getlistNH()
          self.comboBox_10.clear()
          for row in list:
               self.comboBox_10.addItem(row[1]) #cboxnamhoc
          hocky = HocKyBUS()
          self.comboBox_12.clear()
          list = hocky.getlistHocKy()
          for row in list:
               self.comboBox_12.addItem(row[1])
     def BaoCao_lop_loadlist(self,namhoc):
          diem = DiemBUS()
          self.comboBox_11.clear() #cboxLopHoc
          listLop = diem.getLopDiem(namhoc)
          for lops in listLop:
               self.comboBox_11.addItem(lops)
     def display_BaoCao(self):
          baocao = BaoCaoBUS()
          lophoc = LopHocBUS()
          namhoc = NamHocBUS()
          monhoc = MonHocBUS()
          hocky = HocKyBUS()
          flag = True
          comboBox_10 = self.comboBox_10.currentText()
          comboBox_11 = self.comboBox_11.currentText()
          comboBox_12 = self.comboBox_12.currentText()
          listTiLe = baocao.getListHSDiem(comboBox_11,comboBox_12,comboBox_10)
          self.tableLH_MH.setRowCount(len(listTiLe))
          for i, row in enumerate(listTiLe):
               for j,val in enumerate(row):
                    self.tableLH_MH.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableLH_MH.rowCount() 
          for i in range(numRows):
               self.tableLH_MH.item(i, 0).setFlags(self.tableLH_MH.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLH_MH.item(i, 1).setFlags(self.tableLH_MH.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLH_MH.item(i, 2).setFlags(self.tableLH_MH.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLH_MH.item(i, 3).setFlags(self.tableLH_MH.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
          '''listTileHocky = baocao.getListHocKyLop(comboBox_11,comboBox_12,comboBox_10)
          self.tableLH_HK.setRowCount(len(listTileHocky))
          for i, row in enumerate(listTileHocky):
               for j,val in enumerate(row):
                    self.tableLH_HK.setItem(i, j, QTableWidgetItem(str(val)))
          num = self.tableLH_HK.rowCount() 
          for i in range(num):
               self.tableLH_HK.item(i, 0).setFlags(self.tableLH_HK.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLH_HK.item(i, 1).setFlags(self.tableLH_HK.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLH_HK.item(i, 2).setFlags(self.tableLH_HK.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLH_HK.item(i, 3).setFlags(self.tableLH_HK.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)'''
          for row in range(numRows):
               getNamHoc = namhoc.getma(comboBox_10)
               getMaLop = lophoc.getma(comboBox_11,getNamHoc)
               getMonHoc = monhoc.getMamon(self.tableLH_MH.item(row, 0).text())
               getHocKy = hocky.getma(comboBox_12)
               getTiLeDat = self.tableLH_MH.item(row, 3).text()
               getdata = KetQuaLopHocMonHocDTO(getMaLop,getNamHoc,getMonHoc,getHocKy,getTiLeDat)
               if not baocao.insertDiem(getdata):
                    flag = False
          if flag:
               print("Thêm thành công!")
          else:
               print("Thêm không thành công !")
                    


     def stackHocSinh(self):
          self.stackedWidget.setCurrentIndex(1)
          #HocSinh
          self.btnThemHocSinh.clicked.connect(self.addHocSinh)
          self.btnCapNhatHocSinh.clicked.connect(self.updateHocSinh)
          self.btnXoaHocSinh.clicked.connect(self.deleteHocSinh)
          self.btnLayAnhOfHocSinh.clicked.connect(self.imageHocSinh)
          self.pushButton_82.clicked.connect(self.clear)
          self.btnTimKiemHS.clicked.connect(self.findHS)
          self.cboxSortGV_HS.activated.connect(self.findSortHS)
          self.cboxGTofHS.activated.connect(self.findGioiTinhOfHS)
          self.btnExportExcelHS.clicked.connect(self.exportExcelHS)
          #PhanLop
          self.cBoxNH.currentTextChanged.connect(self.load_khoi_combocbox)
          self.cbBoxKhoi.currentTextChanged.connect(self.load_lop_combobox)
          self.btnThemHocSinhIntoList.clicked.connect(self.insertPhanLop)
          self.cBoxNH.currentTextChanged.connect(self.load_HS_combocbox)
          self.btnXoaHocSinhRemoveList.clicked.connect(self.deletePhanLop)
          #Danh sach
          self.cboxlistNH.currentTextChanged.connect(self.load_khoi_combocbox)
          self.cboxlistKhoi.currentTextChanged.connect(self.load_lop_combobox)
          self.btnDisplayListHS.clicked.connect(self.displayListHocSinh)
          self.btnExportPhanLop.clicked.connect(self.ExportPhanLop)
          self.loadlistHS()
          #self.displayInforInTabPhanLop()
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
     def displayListHocSinh(self):
          phanlop = PhanLopBUS()
          #self.cBoxLop.get()
          list = phanlop.getlisths(self.cboxlistLop.currentText(),self.cboxlistNH.currentText())
          self.tablelistHocSinhInLop.setRowCount(len(list))
          for i,row in enumerate(list): 
               for j,val in enumerate(row): 
                    self.tablelistHocSinhInLop.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tablelistHocSinhInLop.rowCount() 
          for i in range(numRows):
               self.tablelistHocSinhInLop.item(i, 0).setFlags(self.tablelistHocSinhInLop.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablelistHocSinhInLop.item(i, 1).setFlags(self.tablelistHocSinhInLop.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablelistHocSinhInLop.item(i, 2).setFlags(self.tablelistHocSinhInLop.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablelistHocSinhInLop.item(i, 3).setFlags(self.tablelistHocSinhInLop.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablelistHocSinhInLop.item(i, 4).setFlags(self.tablelistHocSinhInLop.item(i, 4).flags() & ~QtCore.Qt.ItemIsEditable)
          self.clear()
          self.loadlistHS()
     def ExportPhanLop(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tablelistHocSinhInLop.model().columnCount()):
               columnHeader.append(self.tablelistHocSinhInLop.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tablelistHocSinhInLop.rowCount()):
               for col in range(self.tablelistHocSinhInLop.columnCount()):
                    item = self.tablelistHocSinhInLop.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenlop = self.tablelistHocSinhInLop.item(0, 4).text()
          tenFile = r"FileExcel\PhanLop\DanhsachLop{}_{}.xlsx".format(tenlop,currentTime)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    
  

     def loadlistHS(self):
          hs = HocSinhBUS()
          self.lineMaHocSinh.setText(str(HocSinhBUS.CheckgetID(self)))
          listHS = hs.getlistHS()
          self.tableHocSinh.setRowCount(len(listHS))
          for i,row in enumerate(listHS): 
               for j,val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableHocSinh.setCellWidget(i, j,item)
                    else:
                         self.tableHocSinh.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableHocSinh.verticalHeader().setDefaultSectionSize(180) 
          numRows = self.tableHocSinh.rowCount()
          for i in range(numRows):
               #maChucVu = self.tableChucVu.item(i, 0).text()
               self.tableHocSinh.item(i, 0).setFlags(self.tableHocSinh.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableHocSinh.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))  
          namhoc = NamHocBUS()
          list = namhoc.getlistNH()
          self.cBoxNH.clear()
          self.cboxlistNH.clear()
          for row in list:
               self.cBoxNH.addItem(row[1])
               self.cboxlistNH.addItem(row[1])
          phanlop = PhanLopBUS()
          listphanlop = phanlop.getlist()
          self.tableListHocSinh.setRowCount(len(listphanlop))
          for i,row in enumerate(listphanlop): 
               for j,val in enumerate(row): 
                    self.tableListHocSinh.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableListHocSinh.rowCount() 
          for i in range(numRows):
               self.tableListHocSinh.item(i, 0).setFlags(self.tableListHocSinh.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListHocSinh.item(i, 1).setFlags(self.tableListHocSinh.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListHocSinh.item(i, 2).setFlags(self.tableListHocSinh.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListHocSinh.item(i, 3).setFlags(self.tableListHocSinh.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
     def load_khoi_combocbox(self,year):
          phanlop = PhanLopBUS()
          self.cbBoxKhoi.clear()
          self.cboxlistKhoi.clear()
          khoi = phanlop.getKhoi(year)
          for khois in khoi:
               self.cbBoxKhoi.addItem(khois)
               self.cboxlistKhoi.addItem(khois)
     def load_HS_combocbox(self,year):
          phanlop = PhanLopBUS()
          self.cBoxHocSinh.clear()
          hs = phanlop.getHocSinh(year)
          for khois in hs:
               self.cBoxHocSinh.addItem(khois)
     def load_lop_combobox(self,khoi):
          phanlop = PhanLopBUS()
          self.cBoxLop.clear()
          self.cboxlistLop.clear()
          lop1 = phanlop.getLop(khoi,self.cBoxNH.currentText())
          lop2 = phanlop.getLop(khoi,self.cboxlistNH.currentText())
          for lops in lop1:
               self.cBoxLop.addItem(lops)
          for lops in lop2:
               self.cboxlistLop.addItem(lops)
     def insertPhanLop(self):
          cBoxNH = self.cBoxNH.currentText()
          cbBoxKhoi = self.cbBoxKhoi.currentText()
          cBoxLop = self.cBoxLop.currentText()
          cBoxHocSinh = self.cBoxHocSinh.currentText()
          namhoc = NamHocBUS()
          maNamHoc = namhoc.getma(cBoxNH)
          khoi = KhoiBUS()
          maKhoi = khoi.getma(cbBoxKhoi)
          lop = LopHocBUS()
          maLop = lop.getma(cBoxLop,maNamHoc)
          hocsinh = HocSinhBUS()
          maHocSinh = hocsinh.getma(cBoxHocSinh)
          addPhanLop = PhanLopDTO(maNamHoc,maKhoi,maLop,maHocSinh)
          phanlop = PhanLopBUS()
          if phanlop.insert(addPhanLop):
               QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
               self.cBoxNH.clear()
               self.cbBoxKhoi.clear()
               self.cBoxLop.clear()
               self.cBoxHocSinh.clear()
               self.loadlistHS()
          else:
               QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
     def deletePhanLop(self):
          selected = self.tableListHocSinh.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 3: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tableListHocSinh.item(row, col).text()
                         lop = self.tableListHocSinh.item(row, 2).text()
                         hs = HocSinhBUS()
                         getma = hs.getma(ma)
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa học sinh {ma} ra khỏi lớp {lop}?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              phanlop=PhanLopBUS()
                              #self.tableChucVu.removeRow(row)
                              if phanlop.delete(getma):
                                   for col in range(self.tableListHocSinh.columnCount()):
                                        item = self.tableListHocSinh.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.cBoxNH.clear()
                                   self.cbBoxKhoi.clear()
                                   self.cBoxLop.clear()
                                   self.cBoxHocSinh.clear()
                                   self.loadlistHS()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

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
     def addHocSinh(self):
          hs = HocSinhBUS()
          lineTenHocSinh  = self.lineTenHocSinh.text()
          dateNgaySinhOfHS = self.dateNgaySinhOfHS.date().toPyDate()
          date = dateNgaySinhOfHS.strftime("%Y-%m-%d")
          cboxGioiTinhOfHocSinh = self.cboxGioiTinhOfHocSinh.currentText()
          lineEmailOfHocSinh = self.lineEmailOfHocSinh.text()
          lineDiaChiOfHocSinh = self.lineDiaChiOfHocSinh.text()
          lineTenPhuHuynh = self.lineTenPhuHuynh.text()
          lineSoDienThoaiOfPhuHuynh = self.lineSoDienThoaiOfPhuHuynh.text()
          img_base64 = self.img_base64
          addHS = HocSinhDTO(None,lineTenHocSinh,date,cboxGioiTinhOfHocSinh,lineEmailOfHocSinh,lineDiaChiOfHocSinh,lineTenPhuHuynh,lineSoDienThoaiOfPhuHuynh,img_base64)
          if len(lineTenHocSinh)==0 or len(lineEmailOfHocSinh) == 0 or len(lineDiaChiOfHocSinh) == 0 or len(lineTenPhuHuynh) == 0 or len(lineSoDienThoaiOfPhuHuynh) == 0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               print("Email:", lineEmailOfHocSinh) 
               if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", lineEmailOfHocSinh):
                    if hs.Checkten(lineEmailOfHocSinh):
                         QMessageBox.information(self,"Thông báo",f"Email {lineEmailOfHocSinh} đã tồn tại trong danh sách!")
                    else:
                         print("Số điện thoai:",lineSoDienThoaiOfPhuHuynh)
                         if  re.match(r"^\d{10}$", lineSoDienThoaiOfPhuHuynh):
                              if hs.insert(addHS):
                                   QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                                   self.clear()
                                   self.loadlistHS()
                              else:
                                   QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
                         else:
                              QMessageBox.warning(self, "Cảnh bảo",f"Số điện thoại {lineSoDienThoaiOfPhuHuynh} không hợp lệ")
               else:
                    QMessageBox.information(self,"Thông báo","Email bạn nhập không hợp lệ!")     
     def updateHocSinh(self):
          hs = HocSinhBUS()
          numRows = self.tableHocSinh.rowCount()
          flag = True
          for i in range(numRows):
               maHocSinh = self.tableHocSinh.item(i,0).text()
               tenHocSinh = self.tableHocSinh.item(i,1).text()
               date = self.tableHocSinh.item(i,2).text()
               gioiTinh = self.tableHocSinh.item(i,3).text()
               email = self.tableHocSinh.item(i,4).text()
               diachi = self.tableHocSinh.item(i,5).text()
               tenPH = self.tableHocSinh.item(i,6).text()
               soDT = self.tableHocSinh.item(i,7).text()
               hinhAnh = self.tableHocSinh.item(i,8)
               update = HocSinhDTO(maHocSinh,tenHocSinh,date,gioiTinh,email,diachi,tenPH,soDT,hinhAnh)
               if not hs.update(update):
                    flag = False
          if flag :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.clear()
               self.loadlistHS()
          else:
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
               
     def deleteHocSinh(self):
          selected = self.tableHocSinh.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tableHocSinh.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa học sinh có mã {ma} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              hs = HocSinhBUS()
                              #self.tableChucVu.removeRow(row)
                              if hs.delete(ma):
                                   for col in range(self.tableHocSinh.columnCount()):
                                        item = self.tableHocSinh.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.clear()
                                   self.loadlistHS()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def findSortHS(self):
          hs = HocSinhBUS()
          self.tableHocSinh.clearContents()
          order = self.cboxSortGV_HS.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = hs.findsort(order)
          #self.tableChucVu.clearContents()
          self.tableHocSinh.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableHocSinh.setCellWidget(i, j,item)
                    else:
                         self.tableHocSinh.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableHocSinh.verticalHeader().setDefaultSectionSize(180) 
     def findGioiTinhOfHS(self):
          hs = HocSinhBUS()
          self.tableHocSinh.clearContents()
          order = self.cboxGTofHS.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = hs.findGT(order)
          #self.tableChucVu.clearContents()
          self.tableHocSinh.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableHocSinh.setCellWidget(i, j,item)
                    else:
                         self.tableHocSinh.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableHocSinh.verticalHeader().setDefaultSectionSize(180) 
     def findHS(self):
          hs = HocSinhBUS()
          txtTimKiem = self.txtTimKiemhs.text()
          data = hs.find(txtTimKiem)
          self.tableHocSinh.clearContents()
          self.tableHocSinh.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableHocSinh.setCellWidget(i, j,item)
                    else:
                         self.tableHocSinh.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableHocSinh.verticalHeader().setDefaultSectionSize(180) 
     def exportExcelHS(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tableHocSinh.model().columnCount()):
               columnHeader.append(self.tableHocSinh.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tableHocSinh.rowCount()):
               for col in range(self.tableHocSinh.columnCount()):
                    item = self.tableHocSinh.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenFile = "FileExcel\HocSinh\DanhsachHocSinh_{}.xlsx".format(currentTime)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    
     '''def importExcelHS(self):
          # Mở hộp thoại chọn file
          file_path, _ = QFileDialog.getOpenFileName(self, "Chọn file Excel", "", "GiaoVien (*.xlsx)")

          # Nếu người dùng chọn file
          if file_path:
          # Đọc dữ liệu từ file excel
               workbook = openpyxl.load_workbook(filename=file_path)
               worksheet = workbook.active
               data = []
               for row in worksheet.iter_rows(min_row=2, values_only=True):
                    data.append(row)

          # So sánh dữ liệu với dữ liệu trong bảng và thêm vào bảng nếu cần
          for row in data:
            # Kiểm tra nếu dữ liệu trong excel giống với dữ liệu trong bảng
               match_found = False
               for r in range(self.tableHocSinh.rowCount()):
                    row_match = True
                    for c in range(self.tableHocSinh.columnCount()):
                         cell = self.tableHocSinh.item(r, c)
                         if cell is None or cell.text() != str(row[c]):
                              row_match = False
                              break
                         if row_match:
                              match_found = True
                              break
            
            # Nếu không tìm thấy dữ liệu trong bảng
               if not match_found:
                # Thêm vào bảng
                    row_count = self.tableHocSinh.rowCount()
                    self.tableWidget.insertRow(row_count)
                    for c in range(self.tableWidget.columnCount()):
                         item = QtWidgets.QTableWidgetItem(str(row[c]))
                         self.tableWidget.setItem(row_count, c, item)

        # Hiển thị thông báo
          QtWidgets.QMessageBox.information(self, "Thông báo", "Import file thành công!")
     '''

     def stackGiaoVien(self):
          self.stackedWidget.setCurrentIndex(2)
          #Giao vien
          self.btnThemGiaoVien.clicked.connect(self.addGiaoVien)
          self.btnCapNhatGiaoVien.clicked.connect(self.updateGiaoVien)
          self.btnXoaGiaoVien.clicked.connect(self.deleteGiaoVien)
          self.btnGetImageGiaoVien.clicked.connect(self.imageGiaoVien)
          self.pushButton_78.clicked.connect(self.clear)
          self.cboxSortGV.activated.connect(self.findSortGV)
          self.cboxSortGT.activated.connect(self.findGioiTinhOfGV)
          self.btnXuatExcelGV.clicked.connect(self.exportExcelGV)
          #Phan cong
          self.cboxNHInPC.currentTextChanged.connect(self.phancong_lop_combobox)
          self.cboxLopPC.currentTextChanged.connect(self.phancong_monhoc_combobox)
          self.cboxMonHocPC.currentTextChanged.connect(self.phancong_giaovien_combobox)
          self.btnInsertPhanCong.clicked.connect(self.insertPhanCong)
          self.btnXoaPhanCong.clicked.connect(self.deletePhanCong)
          #Danh sach
          self.cboxlistNH_2.currentTextChanged.connect(self.phancong_lop_combobox)
          self.btnDisplayListHS_2.clicked.connect(self.displayListPhanCong)
          self.btnExportPhanCong.clicked.connect(self.ExportPhanCong)

          self.loadlistGV()
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
     def loadlistGV(self):
          gv = GiaoVienBUS()
          self.lineMaGV.setText(str(GiaoVienBUS.CheckgetID(self)))
          listgv = gv.getlistGV()
          self.tableGiaoVien.setRowCount(len(listgv))
          for i,row in enumerate(listgv): 
               for j,val in enumerate(row):
                    item = str(val)
                    if j == 9:
                         item = self.getImageLabel(val)
                         self.tableGiaoVien.setCellWidget(i, j,item)
                    else:
                         self.tableGiaoVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableGiaoVien.verticalHeader().setDefaultSectionSize(180) 
          numRows = self.tableGiaoVien.rowCount()
          for i in range(numRows):
               #maChucVu = self.tableChucVu.item(i, 0).text()
               self.tableGiaoVien.item(i, 0).setFlags(self.tableGiaoVien.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableGiaoVien.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))  
          monhoc = MonHocBUS()
          listmh = monhoc.getListMonHoc()
          for row in listmh:
               self.CboxChuyenMon.addItem(row[1])
          chucvu = ChucVuBUS()
          listcv = chucvu.getListCV()
          for row in listcv:
               self.CboxChucVu.addItem(row[1])
          #phancong
          namhoc = NamHocBUS()
          self.cboxNHInPC.clear()
          self.cboxlistNH_2.clear()
          list = namhoc.getlistNH()
          for row in list:
               self.cboxNHInPC.addItem(row[1])
               self.cboxlistNH_2.addItem(row[1])
          phancong = PhanCongBUS()
          listphancong = phancong.getlist()
          self.tablePhanCong.setRowCount(len(listphancong))
          for i,row in enumerate(listphancong): 
               for j,val in enumerate(row): 
                    self.tablePhanCong.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tablePhanCong.rowCount() 
          for i in range(numRows):
               self.tablePhanCong.item(i, 0).setFlags(self.tablePhanCong.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablePhanCong.item(i, 1).setFlags(self.tablePhanCong.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablePhanCong.item(i, 2).setFlags(self.tablePhanCong.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tablePhanCong.item(i, 3).setFlags(self.tablePhanCong.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
     def phancong_lop_combobox(self,year):
          phancong = PhanCongBUS()
          self.cboxLopPC.clear()
          self.cboxlistLop_2.clear()
          pc = phancong.getLop(year)
          for lop in pc:
               self.cboxLopPC.addItem(lop)
               self.cboxlistLop_2.addItem(lop)
     def phancong_monhoc_combobox(self,lophoc):
          phancong = PhanCongBUS()
          self.cboxMonHocPC.clear()
          pc = phancong.getMon(self.cboxNHInPC.currentText(),lophoc)
          for lop in pc:
               self.cboxMonHocPC.addItem(lop)
     def phancong_giaovien_combobox(self,mon):
          phancong = PhanCongBUS()
          self.cboxGiaoVien.clear()
          pc = phancong.getGiaoVien(mon)
          for lop in pc:
               self.cboxGiaoVien.addItem(lop)
     def displayListPhanCong(self):
          phancong = PhanCongBUS()
          #self.cBoxLop.get()
          list = phancong.getlistGV(self.cboxlistLop_2.currentText())
          self.tableListPhanCong.setRowCount(len(list))
          for i,row in enumerate(list): 
               for j,val in enumerate(row): 
                    self.tableListPhanCong.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableListPhanCong.rowCount() 
          for i in range(numRows):
               self.tableListPhanCong.item(i, 0).setFlags(self.tableListPhanCong.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListPhanCong.item(i, 1).setFlags(self.tableListPhanCong.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListPhanCong.item(i, 2).setFlags(self.tableListPhanCong.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListPhanCong.item(i, 3).setFlags(self.tableListPhanCong.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListPhanCong.item(i, 4).setFlags(self.tableListPhanCong.item(i, 4).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListPhanCong.item(i, 5).setFlags(self.tableListPhanCong.item(i, 5).flags() & ~QtCore.Qt.ItemIsEditable)
          self.clear()
          self.loadlistGV()
     def ExportPhanCong(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tableListPhanCong.model().columnCount()):
               columnHeader.append(self.tableListPhanCong.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tableListPhanCong.rowCount()):
               for col in range(self.tableListPhanCong.columnCount()):
                    item = self.tableListPhanCong.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenlop = self.tableListPhanCong.item(0, 5).text()
          tenFile = r"FileExcel\PhanCong\DanhsachPhanCongLop{}_{}.xlsx".format(tenlop,currentTime)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    

     def insertPhanCong(self):
          namhoc = NamHocBUS()
          lop = LopHocBUS()
          monhoc = MonHocBUS()
          giaovien = GiaoVienBUS()
          maNamHoc = namhoc.getma(self.cboxNHInPC.currentText())
          maLop = lop.getma(self.cboxLopPC.currentText(),maNamHoc)
          maMonHoc = monhoc.getMamon(self.cboxMonHocPC.currentText())
          maGiaoVien = giaovien.getma(self.cboxGiaoVien.currentText())
          addPhanCong = PhanCongDTO(maNamHoc,maLop,maMonHoc,maGiaoVien)
          phancong = PhanCongBUS()
          if phancong.insert(addPhanCong):
               QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
               self.cboxNHInPC.clear()
               self.cboxLopPC.clear()
               self.cboxMonHocPC.clear()
               self.cboxGiaoVien.clear()
               self.loadlistGV()
          else:
               QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
     def deletePhanCong(self):
          selected = self.tablePhanCong.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 3: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tablePhanCong.item(row, col).text()
                         lop = self.tablePhanCong.item(row, 1).text()
                         nam = self.tablePhanCong.item(row, 0).text()
                         gv = GiaoVienBUS()
                         lophoc = LopHocBUS()
                         namhoc = NamHocBUS()
                         getNam = namhoc.getma(nam)
                         getma = gv.getma(ma)
                         getlop = lophoc.getma(lop,getNam)
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa lịch phân công của giáo viên {ma} ra khỏi lớp {lop}?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              phancong = PhanCongBUS()
                              #self.tableChucVu.removeRow(row)
                              if phancong.delete(getma,getlop):
                                   for col in range(self.tablePhanCong.columnCount()):
                                        item = self.tablePhanCong.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.cboxNHInPC.clear()
                                   self.cboxLopPC.clear()
                                   self.cboxMonHocPC.clear()
                                   self.cboxGiaoVien.clear()
                                   self.loadlistGV()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def addGiaoVien(self):
          giaovien = GiaoVienBUS()
          monhoc = MonHocBUS()
          chucvu = ChucVuBUS()
          maChuyenMon = monhoc.getMamon(self.CboxChuyenMon.currentText())
          maChucVu = chucvu.getmaMon(self.CboxChucVu.currentText())
          lineTenGV  = self.lineTenGV.text()
          dateNgaySinhOfGV = self.DatBirthOfGV.date().toPyDate()
          date = dateNgaySinhOfGV.strftime("%Y-%m-%d")
          cboxGioiTinhOfGV = self.gioiTinhOfGV.currentText()
          lineDiaChiOfGV = self.diaChiOfGV.text()          
          lineEmailOfGV = self.emailOfGV.text()
          lineSoDienThoaiOfGV = self.soDienThoaiOfGV.text()
          #CboxChuyenMon = self.CboxChuyenMon.currentText()
          #CboxChucVu = self.CboxChucVu.currentText()
          img_base64 = self.img_base64
          addGiaoVien = GiaoVienDTO(None,lineTenGV,date,cboxGioiTinhOfGV,lineDiaChiOfGV,lineEmailOfGV,lineSoDienThoaiOfGV,maChuyenMon,maChucVu,img_base64)

          if len(lineTenGV)==0 or len(lineEmailOfGV) == 0 or len(lineDiaChiOfGV) == 0 or len(lineSoDienThoaiOfGV) == 0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               print("Email:", lineEmailOfGV) 
               if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", lineEmailOfGV):
                    if giaovien.Checkten(lineEmailOfGV):
                         QMessageBox.information(self,"Thông báo",f"Email {lineEmailOfGV} đã tồn tại trong danh sách!")
                    else:
                         print("Số điện thoai:",lineSoDienThoaiOfGV)
                         if  re.match(r"^\d{10}$", lineSoDienThoaiOfGV):
                              if giaovien.ChecksoDT(lineSoDienThoaiOfGV):
                                   QMessageBox.information(self,"Thông báo",f"Số điện thoại {lineSoDienThoaiOfGV} đã tồn tại trong danh sách!")
                              else:
                                   if giaovien.insert(addGiaoVien) :
                                        QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                                        self.CboxChuyenMon.clear()
                                        self.CboxChucVu.clear()
                                        self.loadlistGV()
                                        
                                   else: 
                                        QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
                                 
                         else: 
                              QMessageBox.warning(self, "Cảnh bảo",f"Số điện thoại {lineSoDienThoaiOfGV} không hợp lệ")
               else:
                    QMessageBox.information(self,"Thông báo","Email bạn nhập không hợp lệ!") 
     def updateGiaoVien(self):
          monhoc = MonHocBUS()
          chucvu = ChucVuBUS()
          numRows = self.tableGiaoVien.rowCount()
          flag = True
          for i in range(numRows):
               maGiaoVien = self.tableGiaoVien.item(i,0).text()
               tenGiaoVien = self.tableGiaoVien.item(i,1).text()
               date = self.tableGiaoVien.item(i,2).text()
               gioiTinh = self.tableGiaoVien.item(i,3).text()
               diachi = self.tableGiaoVien.item(i,4).text()
               email = self.tableGiaoVien.item(i,5).text()
               soDT = self.tableGiaoVien.item(i,6).text()
               chuyenmon = self.tableGiaoVien.item(i,7).text()
               tenchucvu = self.tableGiaoVien.item(i,8).text()
               hinhAnh = self.tableGiaoVien.item(i,9)
               giaovien = GiaoVienBUS()
               maChuyenMon = monhoc.getMamon(chuyenmon)
               maChucVu = chucvu.getmaMon(tenchucvu)
               updateGiaoVien = GiaoVienDTO(maGiaoVien,tenGiaoVien,date,gioiTinh,diachi,email,soDT,maChuyenMon,maChucVu,hinhAnh)   
               if not giaovien.update(updateGiaoVien):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.CboxChuyenMon.clear()
               self.CboxChucVu.clear()
               self.loadlistGV()
          else:
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
     def deleteGiaoVien(self):
          selected = self.tableGiaoVien.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tableGiaoVien.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa giáo viên có mã {ma} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              giaovien = GiaoVienBUS()
                              #self.tableChucVu.removeRow(row)
                              if giaovien.delete(ma):
                                   for col in range(self.tableGiaoVien.columnCount()):
                                        item = self.tableGiaoVien.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.CboxChuyenMon.clear()
                                   self.CboxChucVu.clear()
                                   self.loadlistGV()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def findSortGV(self):
          giaovien = GiaoVienBUS()
          self.tableGiaoVien.clearContents()
          order = self.cboxSortGV.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = giaovien.findsort(order)
          #self.tableChucVu.clearContents()
          self.tableGiaoVien.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 9:
                         item = self.getImageLabel(val)
                         self.tableGiaoVien.setCellWidget(i, j,item)
                    else:
                         self.tableGiaoVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableGiaoVien.verticalHeader().setDefaultSectionSize(180) 

     def findGioiTinhOfGV(self):
          giaovien = GiaoVienBUS()
          self.tableGiaoVien.clearContents()
          order = self.cboxSortGT.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = giaovien.findGT(order)
          #self.tableChucVu.clearContents()
          self.tableGiaoVien.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 9:
                         item = self.getImageLabel(val)
                         self.tableGiaoVien.setCellWidget(i, j,item)
                    else:
                         self.tableGiaoVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableGiaoVien.verticalHeader().setDefaultSectionSize(180) 
     def exportExcelGV(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tableGiaoVien.model().columnCount()):
               columnHeader.append(self.tableGiaoVien.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tableGiaoVien.rowCount()):
               for col in range(self.tableGiaoVien.columnCount()):
                    item = self.tableGiaoVien.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenFile = "FileExcel\GiaoVien\DanhsachGiaoVien_{}.xlsx".format(currentTime)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    
     
     def stackNhanVien(self):
          self.stackedWidget.setCurrentIndex(3)
          #nhanvien
          self.btnThemNV.clicked.connect(self.addNhanVien)
          self.btnSuaNhanVien.clicked.connect(self.updateNhanVien)
          self.btnXoaNhanVien.clicked.connect(self.deleteNhanVien)
          self.btnExportNhanVien.clicked.connect(self.ExportNhanVien)
          self.btnClearNhanVien.clicked.connect(self.clear)

          #self.btnTimKiemHS.clicked.connect(self.findHS)
          self.cboxSortNV.activated.connect(self.findSortNV)
          self.cboxGTofNV.activated.connect(self.findGioiTinhOfNV)
          self.btnGetImgNV.clicked.connect(self.imageNhanVien)
          #ChucVu
          self.btnThemCV.clicked.connect(self.tabChucVu)
          self.btnXoaChucVu.clicked.connect(self.deleteChucVu)
          self.btnCapNhatChucVu.clicked.connect(self.updateChucVu)
          self.btnClearChucVu.clicked.connect(self.clear)
          self.btnTimKiemCV.clicked.connect(self.findCV)
          self.cbSortCV.activated.connect(self.fineSortASC)
          maNhanVien ="NV" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaNhanVien.setText(maNhanVien)
          self.maNhanVien = maNhanVien
          #self.fineSortASC()
          self.loadlistCV()

     def fineSortASC(self):
          cv = ChucVuBUS()
          self.tableChucVu.clearContents()
          order = self.cbSortCV.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = cv.findSortASC(order)
          #self.tableChucVu.clearContents()
          self.tableChucVu.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableChucVu.setItem(i, j, QTableWidgetItem(str(item)))
     def loadlistCV(self):
          #nhanvien
          nhanvien = NhanVienBUS()
          self.lineMaNhanVien.setText(str(NhanVienBUS.CheckgetID(self)))
          listnv = nhanvien.getlistNV()
          self.tableNhanVien.setRowCount(len(listnv))
          for i,row in enumerate(listnv): 
               for j,val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableNhanVien.setCellWidget(i, j,item)
                    else:
                         self.tableNhanVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableNhanVien.verticalHeader().setDefaultSectionSize(180) 
          numRows = self.tableNhanVien.rowCount()
          for i in range(numRows):
               #maChucVu = self.tableChucVu.item(i, 0).text()
               self.tableNhanVien.item(i, 0).setFlags(self.tableNhanVien.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableNhanVien.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          
          #chucvu
          chucvu = ChucVuBUS()
          #chucvu.checkidChucVu()
          self.lineMaChucVu.setText(str(ChucVuBUS.checkidChucVu(self)))
          listChucVu = chucvu.getListCV()
          # Đặt số lượng hàng và cột cho QTableWidget
          self.tableChucVu.setRowCount(len(listChucVu))
          #self.tableChucVu.setColumnCount(len(listChucVu[0]))

          for i,row in enumerate(listChucVu): 
               for j,val in enumerate(row): 
                    self.tableChucVu.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableChucVu.rowCount()
          for i in range(numRows):
               #maChucVu = self.tableChucVu.item(i, 0).text()
               self.tableChucVu.item(i, 0).setFlags(self.tableChucVu.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableChucVu.item(i, 0).setBackground(QtGui.QColor(200, 200, 150)) 
          #LayMaChucVu them voa combobox
          for row in listChucVu:
               self.cboxCVOGNV.addItem(row[1]) 
     def imageNhanVien(self):
          choose = QFileDialog.getOpenFileName(None, 'HinhAnh', '', 'FILE img (*.png *.jpg *.bmp)')
          # If the user did not select a file, return immediately
          if not choose[0]:
               return
          with open(choose[0], 'rb') as f:
               img_bytes = f.read()
          px = QtGui.QPixmap(choose[0])
          self.imgNhanVien.setPixmap(px)
          self.img_base64 = img_bytes 
     def addNhanVien(self):
          nhanvien = NhanVienBUS()
          chucvu = ChucVuBUS()
          maChucVu = chucvu.getmaMon(self.cboxCVOGNV.currentText())
          lineTenNhanVien = self.lineTenNhanVien.text()
          dateNgaySinhOfNV = self.dateNhanVien.date().toPyDate()
          date = dateNgaySinhOfNV.strftime("%Y-%m-%d")
          cboxGTNV = self.cboxGTNV.currentText()
          lineDiaChiNV = self.lineDiaChiNV.text()
          lineEmaiNV = self.lineEmaiNV.text()
          lineSDT = self.lineSDT.text()
          img_base64 = self.img_base64
          addNV = NhanVienDTO(None,lineTenNhanVien,date,cboxGTNV,lineDiaChiNV,lineEmaiNV,lineSDT,maChucVu,img_base64)
          if len(lineTenNhanVien)==0 or len(lineDiaChiNV)==0 or len(lineEmaiNV)==0 or len(lineSDT)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else:
               print("Email:", lineEmaiNV)
               if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", lineEmaiNV):
                    if nhanvien.Checkten(lineEmaiNV):
                         QMessageBox.information(self,"Thông báo",f"Email {lineEmaiNV} đã tồn tại trong danh sách!")
                    else:
                         print("Số điện thoai:",lineSDT)
                         if  re.match(r"^\d{10}$", lineSDT):
                              if nhanvien.CheckSDT(lineSDT):
                                   QMessageBox.information(self,"Thông báo",f"Số điện thoại {lineSDT} đã tồn tại trong danh sách!")
                              else:
                                   if nhanvien.insert(addNV):
                                        QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                                        self.cboxCVOGNV.clear()
                                        self.clear()
                                        self.loadlistCV()
                                   else:
                                        QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")

                         else:
                              QMessageBox.warning(self, "Cảnh bảo",f"Số điện thoại {lineSoDienThoaiOfGV} không hợp lệ")
                         
               else:
                    QMessageBox.information(self,"Thông báo","Email bạn nhập không hợp lệ!") 

     def updateNhanVien(self):
          nhanvien = NhanVienBUS()
          chucvu = ChucVuBUS()
          numRows = self.tableNhanVien.rowCount()
          flag = True
          for i in range(numRows):
               maNhanVien = self.tableNhanVien.item(i,0).text()
               tenNhanVien = self.tableNhanVien.item(i,1).text()
               date = self.tableNhanVien.item(i,2).text()
               gioiTinh = self.tableNhanVien.item(i,3).text()
               diachi = self.tableNhanVien.item(i,4).text()
               email = self.tableNhanVien.item(i,5).text()
               soDT = self.tableNhanVien.item(i,6).text()
               tenchucvu = self.tableNhanVien.item(i,7).text()
               hinhAnh = self.tableNhanVien.item(i,8)
               maChucvu = chucvu.getmaMon(tenchucvu)
               updateNhanVien = NhanVienDTO(maNhanVien,tenNhanVien,date,gioiTinh,diachi,email,soDT,maChucvu,hinhAnh)
               if not nhanvien.update(updateNhanVien):
                    flag = False
          if flag :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.cboxCVOGNV.clear()
               self.loadlistCV()
          else: 
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
     def deleteNhanVien(self):
          nhanvien = NhanVienBUS()
          selected = self.tableNhanVien.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tableNhanVien.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa nhân viên có mã {ma} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              if nhanvien.delete(ma):
                                   for col in range(self.tableNhanVien.columnCount()):
                                        item = self.tableNhanVien.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.cboxCVOGNV.clear()
                                   self.loadlistCV()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def ExportNhanVien(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tableNhanVien.model().columnCount()):
               columnHeader.append(self.tableNhanVien.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tableNhanVien.rowCount()):
               for col in range(self.tableNhanVien.columnCount()):
                    item = self.tableNhanVien.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenFile = r"FileExcel\NhanVien\DanhsachNhanVien_{}.xlsx".format(currentTime)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    

     def findSortNV(self):
          hs = NhanVienBUS()
          self.tableNhanVien.clearContents()
          order = self.cboxSortNV.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = hs.findSortNV(order)
          #self.tableChucVu.clearContents()
          self.tableNhanVien.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableNhanVien.setCellWidget(i, j,item)
                    else:
                         self.tableNhanVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableNhanVien.verticalHeader().setDefaultSectionSize(180) 
     def findGioiTinhOfNV(self):
          hs = NhanVienBUS()
          self.tableNhanVien.clearContents()
          order = self.cboxGTofNV.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = hs.findSortGT(order)
          #self.tableChucVu.clearContents()
          self.tableNhanVien.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, val in enumerate(row):
                    item = str(val)
                    if j == 8:
                         item = self.getImageLabel(val)
                         self.tableNhanVien.setCellWidget(i, j,item)
                    else:
                         self.tableNhanVien.setItem(i,j,QtWidgets.QTableWidgetItem(item))
          self.tableNhanVien.verticalHeader().setDefaultSectionSize(180) 


     def updateChucVu(self):
          chucVuBUS = ChucVuBUS()
          numRows = self.tableChucVu.rowCount()
          flag =  True
          for i in range(numRows):
               maChucVu = self.tableChucVu.item(i, 0).text()
               #self.tableChucVu.item(i, 0).setFlags(self.tableChucVu.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               #self.tableChucVu.item(i, 0).setBackground(QtGui.QColor(200, 200, 200))
               tenChucVu = self.tableChucVu.item(i,1).text()
               cv = ChucVuDTO(maChucVu, tenChucVu)
               if not chucVuBUS.updateChucVu(cv):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistCV()
          else:
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")

     def deleteChucVu(self):
          selected = self.tableChucVu.selectedItems()
          
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         maChucVu = self.tableChucVu.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa chức vụ có mã {maChucVu} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              chucVuBUS = ChucVuBUS()
                              #self.tableChucVu.removeRow(row)
                              if chucVuBUS.deleteChucVu(maChucVu):
                                   for col in range(self.tableChucVu.columnCount()):
                                        item = self.tableChucVu.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {maChucVu} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistCV()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def tabChucVu(self):
          #self.lineMaChucVu.setText(maChucVu)
          Chucvu = ChucVuBUS()
          lineTenChucVu = self.lineTenChucVu.text()
          #maChucVu = self.maChucVu
          chucvu = ChucVuDTO(None, lineTenChucVu)
          if len(lineTenChucVu)== 0:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa nhập dữ liệu!")
          else:
               if Chucvu.checkChucVuTonTai(lineTenChucVu):
                    QMessageBox.information(self,"Thông báo","Chức vụ này đã có trong danh sách!")
               else:
                    if Chucvu.addChucVu(chucvu):
                         print("Inserted record:", chucvu.idChucVu, chucvu.tenChucVu)
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                         self.loadlistCV()
                         self.clear()
                    else:
                         QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")

     def findCV(self):
          dd = ChucVuBUS()
          txtTimKiem = self.txtTimKiem.text()
          list = dd.find(txtTimKiem)
          rowcount = 0
          self.tableChucVu.clearContents()
          self.tableChucVu.rowCount()
          if list is not None:
               for row in list :
                    self.tableChucVu.setItem(rowcount, 0, QTableWidgetItem(row[0]))
               #self.tableChucVu.item(i, 0).setFlags(self.tableChucVu.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               #self.tableChucVu.item(i, 0).setBackground(QtGui.QColor(200, 200, 200))
                    self.tableChucVu.setItem(rowcount, 1, QTableWidgetItem(row[1]))
                    rowcount += 1

     def clear(self):
          self.lineTenChucVu.clear()
          self.txtTimKiem.clear()
          self.lineTenMaPhi.clear()
          self.lineTimKiemPhi.clear()
          self.lineTenMonHoc.clear()
          self.lineSoTiet.clear()
          self.txtTimKiem_2.clear()
          self.lineTenLoaiDiem.clear()
          self.lineTenKetQua.clear()
          self.lineTenHocLuc.clear()
          self.lineDiemCD.clear()
          self.lineDiemCT.clear()
          self.lineDiemKhongChe.clear()
          self.lineTenHanhKiem.clear()
          self.lineTenKhoi.clear()
          self.lineTenHocKy.clear()
          self.lineTenNamHoc.clear()
          self.lineEdit_69.clear()
          self.lineTenGV.clear()
          self.emailOfGV.clear()
          self.diaChiOfGV.clear()
          self.soDienThoaiOfGV.clear()
          self.dateNgaySinhOfHS.clear()
          self.lblImageGiaoVien.clear()
          self.lineTenHocSinh.clear()
          self.lineEmailOfHocSinh.clear()
          self.lineDiaChiOfHocSinh.clear()
          self.lineTenPhuHuynh.clear()
          self.lineSoDienThoaiOfPhuHuynh.clear()
          self.dateNgaySinhOfHS.clear()
          self.lblImageHocSinh.clear()
          self.lineTenlop.clear()
          self.spinBoxSiso.setValue(0)
          self.txtTimKiemLH.clear()
          self.lineTenNhanVien.clear()
          self.lineDiaChiNV.clear()
          self.lineEmaiNV.clear()
          self.lineSDT.clear()
          self.imgNhanVien.clear()
          self.cboxlistKhoi.clear()
          self.cboxlistNH.clear()
          self.cboxlistLop.clear()
          self.cboxlistNH_2.clear()
          self.cboxlistLop_2.clear()
     def stackQuyen(self):
          self.stackedWidget.setCurrentIndex(4)
          #Tao tai khoan
          self.cboxChucVuList.currentTextChanged.connect(self.comboBox_TenNguoiDung)
          self.cboxTenNguoiDung.currentTextChanged.connect(self.comboBox_tenDangNhap)
          self.btnThemNguoiDung.clicked.connect(self.insertNguoiDung)
          self.btnUpdateNguoiDung.clicked.connect(self.updateNguoiDung)
          self.btnDeleteNguoiDung.clicked.connect(self.deleteNguoiDung)
          self.loadlistNguoiDung()
     def loadlistNguoiDung(self):
          #taotaikhoan
          nguoiDung = NguoiDungBUS()
          listND = nguoiDung.getList()
          self.tabelNguoiDUng.setRowCount(len(listND))
          for i,row in enumerate(listND):
               for j,val in enumerate(row):
                    self.tabelNguoiDUng.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tabelNguoiDUng.rowCount() 
          for i in range(numRows):
               self.tabelNguoiDUng.item(i, 0).setFlags(self.tabelNguoiDUng.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tabelNguoiDUng.item(i, 1).setFlags(self.tabelNguoiDUng.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tabelNguoiDUng.item(i, 2).setFlags(self.tabelNguoiDUng.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
          chucvu = ChucVuBUS()
          listCV = chucvu.getListCV()
          self.cboxChucVuList.clear()
          self.lineMatKhau.clear()

          for row in listCV:
               self.cboxChucVuList.addItem(row[1])
          self.lineMatKhau.setText(self.generate_password(10))
     def comboBox_TenNguoiDung(self,tenChucVu):
          nguoiDung = NguoiDungBUS()
          self.cboxTenNguoiDung.clear()
          tenND = nguoiDung.getTenDN(tenChucVu)
          for row in tenND:
               self.cboxTenNguoiDung.addItem(row)
     def comboBox_tenDangNhap(self,tenNguoiDung):
          nguoiDung = NguoiDungBUS()
          self.LineTenDangNhap.clear()
          tenDN = nguoiDung.getMa(tenNguoiDung)
          for row in tenDN:
               self.LineTenDangNhap.setText(row)
          
     def generate_password(self,length):
          letters = string.ascii_uppercase + string.digits
          return ''.join(random.choice(letters) for i in range(length))
     def insertNguoiDung(self):
          chucvu = ChucVuBUS()
          maChucVu = chucvu.getmaMon(self.cboxChucVuList.currentText())
          cboxTenNguoiDung = self.cboxTenNguoiDung.currentText()
          LineTenDangNhap = self.LineTenDangNhap.text()
          lineMatKhau = self.lineMatKhau.text()
          addNguoiDung = NguoiDungDTO(maChucVu,LineTenDangNhap,cboxTenNguoiDung,lineMatKhau)
          nguoiDung = NguoiDungBUS()
          if nguoiDung.insert(addNguoiDung):
               QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
               self.loadlistNguoiDung()
          else:
               QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
     def updateNguoiDung(self):
          chucvu = ChucVuBUS()
          flag = True
          numRows = self.tabelNguoiDUng.rowCount()
          flag = True
          for i in range(numRows):
               tenChucVu = self.tabelNguoiDUng.item(i,0).text()
               maChucVu = chucvu.getmaMon(tenChucVu)
               tenDangNhap = self.tabelNguoiDUng.item(i,1).text()
               tenNguoiDung = self.tabelNguoiDUng.item(i,2).text()
               matKhau = self.tabelNguoiDUng.item(i,3).text()
               nguoiDung = NguoiDungBUS()
               update = NguoiDungDTO(maChucVu,tenDangNhap,tenNguoiDung,matKhau)
               if not nguoiDung.update(update):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistNguoiDung()
          else:
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
     def deleteNguoiDung(self):
          selected = self.tabelNguoiDUng.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 1: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tabelNguoiDUng.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa tài khoản có tên đăng nhập {ma} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              nguoiDung = NguoiDungBUS()
                              #self.tableChucVu.removeRow(row)
                              if nguoiDung.delete(ma):
                                   for col in range(self.tabelNguoiDUng.columnCount()):
                                        item = self.tabelNguoiDUng.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistNguoiDung()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def stackLop(self):
          self.stackedWidget.setCurrentIndex(5)
          #khoi
          nguoiDung = NguoiDungBUS()
          tenDangNhap = global_username
          self.role = nguoiDung.get_role_code(tenDangNhap)
          if self.role == 'CV001':
               self.btnThemKhoi.clicked.connect(self.addKhoi)
               self.btnCapNhatKhoi.clicked.connect(self.updateKhoi)
               self.btnXoaKhoi.clicked.connect(self.deleteKhoi)
               self.pushButton_71.clicked.connect(self.clear)
               #lop
               self.btnThemLopHoc.clicked.connect(self.addLop)
               self.btnCapNhatLopHoc.clicked.connect(self.updateLop)
               self.btnXoaLopHoc.clicked.connect(self.deleteLop)
               self.CboxNamHoc.currentTextChanged.connect(self.update_teacher_combobox)
               self.pushButton_70.clicked.connect(self.clear)
               self.btnTimLH.clicked.connect(self.findLH)
               self.cboxMaLH.activated.connect(self.findSortLH)
               self.cBoxTenLop.activated.connect(self.findSortTenLop)
               self.btnExportExOFLH.clicked.connect(self.exportExcelLH)
          else: 
               self.btnThemKhoi.setEnabled(False)
               self.btnCapNhatKhoi.setEnabled(False)
               self.btnXoaKhoi.setEnabled(False)
               self.pushButton_71.setEnabled(False)
               #lop
               self.btnThemLopHoc.setEnabled(False)
               self.btnCapNhatLopHoc.setEnabled(False)
               self.btnXoaLopHoc.setEnabled(False)
               self.CboxNamHoc.currentTextChanged.connect(self.update_teacher_combobox)
               self.pushButton_70.clicked.connect(self.clear)
               self.btnTimLH.clicked.connect(self.findLH)
               self.cboxMaLH.activated.connect(self.findSortLH)
               self.cBoxTenLop.activated.connect(self.findSortTenLop)
               self.btnExportExOFLH.clicked.connect(self.exportExcelLH)       
          self.loadlistlop()
          #self.displayInforInTabLopHoc()
     def update_teacher_combobox(self, year):
          giaovien = GiaoVienBUS()
          self.cBoxGVCN.clear()
          teachers = giaovien.get_giaovien(year)
          for teacher in teachers:
               self.cBoxGVCN.addItem(teacher)
     def loadlistlop(self):
          #Khoi
          khoi = KhoiBUS()
          self.lineMaKhoi.setText(str(KhoiBUS.CheckgetID(self)))
          listkhoi = khoi.getKhoi()
          self.tableKhoi.setRowCount(len(listkhoi))
          #self.tableMonHoc.setColumnCount(len(listmonHoc[0]))

          for i,row in enumerate(listkhoi): 
               for j,val in enumerate(row): 
                    self.tableKhoi.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableKhoi.rowCount() 
          for i in range(numRows):
               self.tableKhoi.item(i, 0).setFlags(self.tableKhoi.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableKhoi.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          #Lop 
          lophoc = LopHocBUS()
          self.lineMaLop.setText(str(LopHocBUS.CheckgetID(self)))
          listlop = lophoc.getListLH()
          self.tableLopHoc.setRowCount(len(listlop))
          for i,row in enumerate(listlop): 
               for j,val in enumerate(row): 
                    self.tableLopHoc.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableLopHoc.rowCount() 
          for i in range(numRows):
               self.tableLopHoc.item(i, 0).setFlags(self.tableLopHoc.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLopHoc.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          for row in listkhoi:
               self.CboxKhoiLop.addItem(row[1])
          namhoc = NamHocBUS()
          listnamhoc = namhoc.getlistNH()
          for row in listnamhoc:
               self.CboxNamHoc.addItem(row[1])

     def addLop(self):
          lop = LopHocBUS()
          lineTenlop = self.lineTenlop.text()
          CboxKhoiLop = self.CboxKhoiLop.currentText()
          CboxNamHoc = self.CboxNamHoc.currentText()
          spinBoxSiso = self.spinBoxSiso.value()
          cBoxGVCN = self.cBoxGVCN.currentText()
          khoi = KhoiBUS()
          makhoi = khoi.getma(CboxKhoiLop)
          namhoc = NamHocBUS()
          maNamHoc = namhoc.getma(CboxNamHoc)
          giaovien = GiaoVienBUS()
          maGiaoVien = giaovien.getma(cBoxGVCN)
          addLop = LopHocDTO(None,lineTenlop,makhoi,maNamHoc,spinBoxSiso,maGiaoVien)
          if len(lineTenlop) == 0 or spinBoxSiso == 0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu! Sỉ số của lớp học phải lớn hơn 15")
          else: 
               if lop.Checkten(CboxNamHoc,lineTenlop):
                    QMessageBox.information(self,"Thông báo",f"Lớp {lineTenlop} đã tồn tại vào năm {CboxNamHoc}trong danh sách!")
               else:
                    if spinBoxSiso < 15 and spinBoxSiso >= 45 :
                         QMessageBox.warning(self, "Thông báo", "Sỉ số của lớp học tối thiểu là 15 học sinh và tối đa là 45 học sinh!")
                    else: 
                         if lop.insert(addLop):
                              QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                              self.spinBoxSiso.clear()
                              self.CboxKhoiLop.clear()
                              self.CboxNamHoc.clear()
                              self.loadlistlop()
                         else:
                              QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
     def findSortLH(self):
          lophoc = LopHocBUS()
          self.tableLopHoc.clearContents()
          order = self.cboxMaLH.currentText()
          data = lophoc.findSortMa(order)
          #self.tableChucVu.clearContents()
          self.tableLopHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableLopHoc.setItem(i, j, QTableWidgetItem(str(item)))
     def findSortTenLop(self):
          lophoc = LopHocBUS()
          self.tableLopHoc.clearContents()
          order = self.cBoxTenLop.currentText()
          data = lophoc.findSortTen(order)
          #self.tableChucVu.clearContents()
          self.tableLopHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableLopHoc.setItem(i, j, QTableWidgetItem(str(item)))
     def findLH(self):
          lophoc = LopHocBUS()
          txtTimKiem_2 = self.txtTimKiemLH.text()
          list = lophoc.findLH(txtTimKiem_2)
          '''self.tableLopHoc.clearContents()
          self.tableLopHoc.setRowCount(len(list))
          for i, row in enumerate(list):
               for j, item in enumerate(row):
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(item)))'''
          rowcount = 0
          self.tableLopHoc.clearContents()
          self.tableLopHoc.rowCount()
          if list is not None:
               for row in list :
                    self.tableLopHoc.setItem(rowcount, 0, QTableWidgetItem(row[0]))
               #self.tableChucVu.item(i, 0).setFlags(self.tableChucVu.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               #self.tableChucVu.item(i, 0).setBackground(QtGui.QColor(200, 200, 200))
                    self.tableLopHoc.setItem(rowcount, 1, QTableWidgetItem(row[1]))
                    self.tableLopHoc.setItem(rowcount, 2, QTableWidgetItem(row[2]))
                    self.tableLopHoc.setItem(rowcount, 3, QTableWidgetItem(row[3]))
                    self.tableLopHoc.setItem(rowcount, 4, QTableWidgetItem(str(row[4])))
                    self.tableLopHoc.setItem(rowcount, 5, QTableWidgetItem(row[5]))
                    
                    rowcount += 1
     def exportExcelLH(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tableLopHoc.model().columnCount()):
               columnHeader.append(self.tableLopHoc.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tableLopHoc.rowCount()):
               for col in range(self.tableLopHoc.columnCount()):
                    item = self.tableLopHoc.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenFile = "FileExcel\LopHoc\Danhsach_{}.xlsx".format(currentTime)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    


     def updateLop(self):
          nhoc = NamHocBUS()
          khoi = KhoiBUS()
          giaovien = GiaoVienBUS()
          numRows = self.tableLopHoc.rowCount()
          flag = True
          for i in range(numRows):
               maLopHoc = self.tableLopHoc.item(i,0).text()
               tenLopHoc = self.tableLopHoc.item(i,1).text()
               khoiLop = self.tableLopHoc.item(i,2).text()
               namhoc = self.tableLopHoc.item(i,3).text()
               spinBoxSiso = self.tableLopHoc.item(i,4).text()
               GVCN = self.tableLopHoc.item(i,5).text()
               maKhoi = khoi.getma(khoiLop)
               maNamHoc = nhoc.getma(namhoc)
               maGiaoVien = giaovien.getma(GVCN)
               lophoc = LopHocBUS()
               updateLop = LopHocDTO(maLopHoc,tenLopHoc,maKhoi,maNamHoc,spinBoxSiso,maGiaoVien)
               if not lophoc.update(updateLop):
                    flag = False
          if flag :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.spinBoxSiso.clear()
               self.CboxKhoiLop.clear()
               self.CboxNamHoc.clear()
               self.loadlistlop()
          else:
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")

     def deleteLop(self):
          selected = self.tableLopHoc.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         ma = self.tableLopHoc.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa lớp học có mã {ma} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              lophoc = LopHocBUS()
                              #self.tableChucVu.removeRow(row)
                              if lophoc.delete(ma):
                                   for col in range(self.tableLopHoc.columnCount()):
                                        item = self.tableLopHoc.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {ma} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.spinBoxSiso.clear()
                                   self.CboxKhoiLop.clear()
                                   self.CboxNamHoc.clear()
                                   self.loadlistlop()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     
     def addKhoi(self):
          khoi = KhoiBUS()
          lineTenKhoi = self.lineTenKhoi.text()
          addKhoi = KhoiDTO(None,lineTenKhoi)
          if len(lineTenKhoi)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if khoi.Checkten(lineTenKhoi):
                    QMessageBox.information(self,"Thông báo","Khối này đã có trong danh sách!")
               else:
                    if khoi.insert(addKhoi):
                         print("Inserted record:", addKhoi.idKhoi,addKhoi.tenKhoi)
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu thành công!")
                         self.loadlistlop()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")
     
     def updateKhoi(self):
          khoi = KhoiBUS()
          numRows = self.tableKhoi.rowCount()
          flag = True
          for i in range(numRows):
               ma= self.tableKhoi.item(i,0).text()
               ten= self.tableKhoi.item(i,1).text()
               update = KhoiDTO(ma,ten)
               if not khoi.update(update):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistlop()
          else : 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")

     def deleteKhoi(self):
          selected = self.tableKhoi.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableKhoi.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa khối có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              khoi = KhoiBUS()
                              #self.tableChucVu.removeRow(row)
                              if khoi.delete(mamon):
                                   for col in range(self.tableKhoi.columnCount()):
                                        item = self.tableKhoi.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistlop()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

     def stackHKNH(self):
          self.stackedWidget.setCurrentIndex(6)
          #HocKy
          self.btnThemHocKy.clicked.connect(self.addHocKy)
          self.btnCapNhatHocKy.clicked.connect(self.updateHocKy)
          self.btnXoaHocKy.clicked.connect(self.deleteHocKy)
          self.pushButton_85.clicked.connect(self.clear)
          #NamHoc
          self.btnThemNamHoc.clicked.connect(self.addNamHoc)
          self.btnCapNhatNamHoc.clicked.connect(self.updateNamHoc)
          self.btnXoaNamHoc.clicked.connect(self.deleteNamHoc)
          self.pushButton_86.clicked.connect(self.clear)
          self.btnTimNH.clicked.connect(self.findNH)
          self.cbSortCV_2.activated.connect(self.fineSortASCMaInNH)
          self.cbSortCV_3.activated.connect(self.fineSortASCTenInNH)
          self.loadlistHKNH()
          '''try: 
               query.execute(sqlNamHoc)
               dataNamHoc = query.fetchall()
               self.tableNamHoc.setRowCount(len(dataNamHoc))
               for i, row in enumerate(dataNamHoc):
                    for j, val in enumerate(row):
                         self.tableNamHoc.setItem(i, j, QTableWidgetItem(str(val)))
         
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e) 
          # populate the widget with the data from the database
          

          lineMaNamHoc ="NH"+str(random.randint(0,9999)).zfill(6)
          self.lineMaNamHoc.setText(lineMaNamHoc)
          self.maNamHoc = lineMaNamHoc'''
     def loadlistHKNH(self):
          #hocky
          hocky = HocKyBUS()
          self.lineMaHocKy.setText(str(HocKyBUS.CheckgetID(self)))
          listHK = hocky.getlistHocKy()
          self.tableHocKy.setRowCount(len(listHK))
          for i,row in enumerate(listHK): 
               for j,val in enumerate(row): 
                    self.tableHocKy.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableHocKy.rowCount() 
          for i in range(numRows):
               self.tableHocKy.item(i, 0).setFlags(self.tableHocKy.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableHocKy.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          #namhoc
          namhoc = NamHocBUS()
          self.lineMaNamHoc.setText(str(NamHocBUS.CheckgetID(self)))
          listNH = namhoc.getlistNH()
          self.tableNamHoc.setRowCount(len(listNH))
          for i,row in enumerate(listNH): 
               for j,val in enumerate(row): 
                    self.tableNamHoc.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableNamHoc.rowCount() 
          for i in range(numRows):
               self.tableNamHoc.item(i, 0).setFlags(self.tableNamHoc.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableNamHoc.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     

     def addHocKy(self):
          hocky = HocKyBUS()
          lineTenHocKy = self.lineTenHocKy.text()
          cboxHeSoHocKy = self.cboxHeSoHocKy.currentText()
          addHK = HocKyDTO(None,lineTenHocKy,cboxHeSoHocKy)
          if len(lineTenHocKy)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if hocky.Checkten(lineTenHocKy):
                    QMessageBox.information(self,"Thông báo","Loại học kỳ này đã có trong danh sách!")
               else:
                    if hocky.insert(addHK):
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu thành công!")
                         self.loadlistHKNH()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")

     def updateHocKy(self):
          hocky = HocKyBUS()
          numRows = self.tableHocKy.rowCount()
          flag = True
          for i in range(numRows):
               maHocKy= self.tableHocKy.item(i,0).text()
               tenHocKy = self.tableHocKy.item(i,1).text()
               heSoHocKy = self.tableHocKy.item(i,2).text()
               update = HocKyDTO(maHocKy,tenHocKy,heSoHocKy)
               if not hocky.update(update):
                    flag = False
          if flag :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistHKNH()
          else :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")
     def deleteHocKy(self):
          selected = self.tableHocKy.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableHocKy.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa loại học kỳ có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              hk = HocKyBUS()
                              if hk.delete(mamon):
                                   #self.tableHocLuc.removeRow(row)
                                   for col in range(self.tableHocKy.columnCount()):
                                        item = self.tableHocKy.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistHKNH()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def addNamHoc(self):
          namhoc = NamHocBUS()
          lineTenNamHoc = self.lineTenNamHoc.text()
          addNH = NamHocDTO(None,lineTenNamHoc)
          if len(lineTenNamHoc)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if namhoc.Checkten(lineTenNamHoc):
                    QMessageBox.information(self,"Thông báo","Loại năm học này đã có trong danh sách!")
               else:
                    if namhoc.insert(addNH):
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu thành công!")
                         self.loadlistHKNH()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")

     def updateNamHoc(self):
          namhoc = NamHocBUS()
          numRows = self.tableNamHoc.rowCount()
          flag = True
          for i in range(numRows):
               maNH= self.tableNamHoc.item(i,0).text()
               tenNH= self.tableNamHoc.item(i,1).text()
               update = NamHocDTO(maNH,tenNH)
               if not namhoc.update(update):
                    flag = False
          if flag :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistHKNH()
          else :
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")
     def deleteNamHoc(self):
          selected = self.tableNamHoc.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableNamHoc.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa loại năm học có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              nh = NamHocBUS()
                              if nh.delete(mamon):
                                   #self.tableHocLuc.removeRow(row)
                                   for col in range(self.tableNamHoc.columnCount()):
                                        item = self.tableNamHoc.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistHKNH()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def fineSortASCMaInNH(self):
          nh = NamHocBUS()
          self.tableNamHoc.clearContents()
          order = self.cbSortCV_2.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = nh.findSortASCMa(order)
          #self.tableChucVu.clearContents()
          self.tableNamHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableNamHoc.setItem(i, j, QTableWidgetItem(str(item)))
     def fineSortASCTenInNH(self):
          nh = NamHocBUS()
          self.tableNamHoc.clearContents()
          order = self.cbSortCV_3.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = nh.findSortASCTen(order)
          #self.tableChucVu.clearContents()
          self.tableNamHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableNamHoc.setItem(i, j, QTableWidgetItem(str(item)))
     def findNH(self):
          nh = NamHocBUS()
          txtTimKiem = self.lineEdit_69.text()
          list = nh.find(txtTimKiem)
          rowcount = 0
          self.tableNamHoc.clearContents()
          self.tableNamHoc.rowCount()
          if list is not None:
               for row in list :
                    self.tableNamHoc.setItem(rowcount, 0, QTableWidgetItem(row[0]))
               #self.tableChucVu.item(i, 0).setFlags(self.tableChucVu.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               #self.tableChucVu.item(i, 0).setBackground(QtGui.QColor(200, 200, 200))
                    self.tableNamHoc.setItem(rowcount, 1, QTableWidgetItem(row[1]))
                    rowcount += 1
     def stackMonHoc(self):
          self.stackedWidget.setCurrentIndex(7)
          nguoiDung = NguoiDungBUS()
          tenDangNhap = global_username
          self.role = nguoiDung.get_role_code(tenDangNhap)
          if self.role == 'CV001':
          #monhoc
               self.btnThemMonHoc.clicked.connect(self.addMonHoc)
               self.btnCapNhatMonHoc.clicked.connect(self.updateMonHoc)
               self.btnXoaMonHoc.clicked.connect(self.deleteMonHoc)
               self.btnTimKiemCV_2.clicked.connect(self.findMon)
               self.cbSortMH.activated.connect(self.findSortMonHoc)
               self.cbSortHeSo.activated.connect(self.findHeSo)
               self.cbSortST.activated.connect(self.findSoTiet)
               self.pushButton_103.clicked.connect(self.clear)
               self.btnThemMonHoc_2.clicked.connect(self.addLoaiDiem)
               self.btnCapNhatMonHoc_2.clicked.connect(self.updateLoaiDiem)
               self.btnXoaMonHoc_2.clicked.connect(self.deleteLoaiDiem)
               self.pushButton_105.clicked.connect(self.clear)
               #diem
               self.comboBox_4.currentTextChanged.connect(self.Diem_lopHoc_combobox)
               self.comboBox_5.currentTextChanged.connect(self.Diem_lopHoc1_combobox)
               self.comboBox_6.currentTextChanged.connect(self.Diem_TenHocSinh_combobox)

               self.displayDanhSachDiem.clicked.connect(self.Display_Hsinh_Diem)
               self.btnDisplayListDiemHS.clicked.connect(self.display_list_Hsinh)
               self.btnExportExOFLH_2.clicked.connect(self.exportListDiem)

               self.btnLuuListDiemhs.clicked.connect(self.insertDiem)

               self.btnDisplayListDiemHS_2.clicked.connect(self.display_list_lop_hocsinh_monhoc)
               self.comboBox_9.currentTextChanged.connect(self.Diem_lopHoc2_combobox)
               self.btnExportExOFLH_3.clicked.connect(self.exportListDiem_MonHoc)
          elif self.role == 'CV004':
               self.comboBox_4.currentTextChanged.connect(self.Diem_lopHoc_combobox)
               self.comboBox_5.currentTextChanged.connect(self.Diem_lopHoc1_combobox)
               self.comboBox_6.currentTextChanged.connect(self.Diem_TenHocSinh_combobox)

               self.displayDanhSachDiem.clicked.connect(self.Display_Hsinh_Diem)
               self.btnDisplayListDiemHS.clicked.connect(self.display_list_Hsinh)
               self.btnExportExOFLH_2.clicked.connect(self.exportListDiem)
               self.btnLuuListDiemhs.clicked.connect(self.insertDiem)

               self.btnDisplayListDiemHS_2.clicked.connect(self.display_list_lop_hocsinh_monhoc)
               self.comboBox_9.currentTextChanged.connect(self.Diem_lopHoc2_combobox)
               self.btnExportExOFLH_3.clicked.connect(self.exportListDiem_MonHoc)

               self.btnThemMonHoc.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnCapNhatMonHoc.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnXoaMonHoc.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnTimKiemCV_2.clicked.connect(self.findMon)
               self.cbSortMH.activated.connect(self.findSortMonHoc)
               self.cbSortHeSo.activated.connect(self.findHeSo)
               self.cbSortST.activated.connect(self.findSoTiet)
               self.pushButton_103.clicked.connect(self.clear)
               self.btnThemMonHoc_2.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnCapNhatMonHoc_2.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.btnXoaMonHoc_2.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
               self.pushButton_105.clicked.connect(lambda: QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền truy cập chức năng này!"))
          self.loadlistMonHoc()
     def loadlistMonHoc(self):
          monhoc = MonHocBUS()
          self.lineMaMonHoc.setText(str(MonHocBUS.CheckgetID(self)))
          listmonHoc = monhoc.getListMonHoc()
          self.tableMonHoc.setRowCount(len(listmonHoc))
          #self.tableMonHoc.setColumnCount(len(listmonHoc[0]))

          for i,row in enumerate(listmonHoc): 
               for j,val in enumerate(row): 
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableMonHoc.rowCount() 
          for i in range(numRows):
               self.tableMonHoc.item(i, 0).setFlags(self.tableMonHoc.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableMonHoc.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          
          #LoaiDiem
          loaidiem = LoaiDiemBUS()
          self.lineLoaiDiem.setText(str(LoaiDiemBUS.CheckgetID(self)))
          listdiem = loaidiem.getListLoaiDiem()
          self.tableLoaiDiem.setRowCount(len(listdiem))
          for i,row in enumerate(listdiem): 
               for j,val in enumerate(row): 
                    self.tableLoaiDiem.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableLoaiDiem.rowCount() 
          for i in range(numRows):
               self.tableLoaiDiem.item(i, 0).setFlags(self.tableMonHoc.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableLoaiDiem.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))   
          #diem 
          namhoc = NamHocBUS()
          self.comboBox_4.clear() #cboxNamHoc
          self.comboBox_5.clear()
          self.comboBox_9.clear()
          list = namhoc.getlistNH()
          for row in list : 
               self.comboBox_4.addItem(row[1])
               self.comboBox_5.addItem(row[1])
               self.comboBox_9.addItem(row[1])
          hocky = HocKyBUS()
          self.comboBox_2.clear()
          self.comboBox_7.clear()
          self.comboBox_19.clear()
          list = hocky.getlistHocKy()
          for row in list:
               self.comboBox_2.addItem(row[1])
               self.comboBox_7.addItem(row[1])
               self.comboBox_19.addItem(row[1])
          
          monhoc = MonHocBUS()
          self.comboBox_3.clear()
          self.comboBox_20.clear()
          list = monhoc.getListMonHoc()
          for row in list:
               self.comboBox_3.addItem(row[1])
               self.comboBox_20.addItem(row[1])
     def Diem_lopHoc_combobox(self,namhoc):
          diem = DiemBUS()
          self.comboBox.clear() #cboxLopHoc
          self.comboBox_18.clear()
          listLop = diem.getLopDiem(namhoc)
          for lops in listLop:
               self.comboBox.addItem(lops)
               self.comboBox_18.addItem(lops)
     def Diem_lopHoc1_combobox(self,namhoc):
          diem = DiemBUS()
          self.comboBox_6.clear()
          listLop = diem.getLopDiem(namhoc)
          for lops in listLop:
               self.comboBox_6.addItem(lops)
     def Diem_lopHoc2_combobox(self,namhoc):
          diem = DiemBUS()
          self.comboBox_18.clear()#LOPHOC
          listLop = diem.getLopDiem(namhoc)
          for lops in listLop:
               self.comboBox_18.addItem(lops)
     def Diem_TenHocSinh_combobox(self,lop):
          hocsinh = HocSinhBUS()
          self.comboBox_8.clear()
          lisths = hocsinh.getTenHS(self.comboBox_5.currentText(),lop)
          for hs in lisths:
               self.comboBox_8.addItem(hs)
     def Display_Hsinh_Diem(self):
          cboxNamHocDiem = self.comboBox_4.currentText()
          cboxMonHoc = self.comboBox_3.currentText()
          cboxHocKy = self.comboBox_2.currentText()
          cboxLop = self.comboBox.currentText()
          diem = DiemBUS()
          list = diem.getHsDiem(cboxMonHoc,cboxHocKy,cboxNamHocDiem,cboxLop)
          self.tableListHsDiem.setRowCount(len(list))
          for i, row in enumerate(list):
               for j,val in enumerate(row):
                    self.tableListHsDiem.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableListHsDiem.rowCount() 
          for i in range(numRows):
               self.tableListHsDiem.item(i, 0).setFlags(self.tableListHsDiem.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListHsDiem.item(i, 1).setFlags(self.tableListHsDiem.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
     def display_list_Hsinh(self):
          ketquaMH = DiemTBMonHocBUS()
          cboxHocKy = self.comboBox_7.currentText()
          cboxLop = self.comboBox_6.currentText()
          cboxHS= self.comboBox_8.currentText()
          diem = DiemBUS()
          listDiemHS = diem.getListHSDiem(cboxHocKy, cboxLop, cboxHS)
          self.tableListDiemHS.setRowCount(len(listDiemHS))
          flag = True
          for i, row in enumerate(listDiemHS):
               for j,val in enumerate(row):
                    self.tableListDiemHS.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableListDiemHS.rowCount() 
          for i in range(numRows):
               self.tableListDiemHS.item(i, 0).setFlags(self.tableListDiemHS.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 1).setFlags(self.tableListDiemHS.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 2).setFlags(self.tableListDiemHS.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 3).setFlags(self.tableListDiemHS.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 4).setFlags(self.tableListDiemHS.item(i, 4).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 5).setFlags(self.tableListDiemHS.item(i, 5).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 6).setFlags(self.tableListDiemHS.item(i, 6).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListDiemHS.item(i, 7).setFlags(self.tableListDiemHS.item(i, 7).flags() & ~QtCore.Qt.ItemIsEditable)
          for row in range(numRows):
               cboxnamhoc = self.comboBox_5.currentText()
               getMaHocSinh = self.tableListDiemHS.item(row, 0).text()
               lophoc = LopHocBUS()
               monhoc = MonHocBUS()
               getMaMonHoc = monhoc.getMamon(self.tableListDiemHS.item(row, 2).text())
               hocky = HocKyBUS()
               getMaHocKy = hocky.getma(cboxHocKy)
               namhoc = NamHocBUS()
               getMaNH = namhoc.getma(cboxnamhoc)
               getMaLopHoc = lophoc.getma(cboxLop,getMaNH)

               diemMieng = self.tableListDiemHS.item(row, 3).text()
               diem15phut = self.tableListDiemHS.item(row, 4).text()
               diemGiuaKy = self.tableListDiemHS.item(row, 5).text()
               diemThi = self.tableListDiemHS.item(row, 6).text()
               diemTBMon = self.tableListDiemHS.item(row, 7).text()
               ketQuaMonHoc = KQMHDTO(getMaHocSinh,getMaLopHoc,getMaNH,getMaMonHoc,getMaHocKy,diemMieng,diem15phut,diemGiuaKy,diemThi,diemTBMon)
               if not ketquaMH.insertDiem(ketQuaMonHoc):
                    flag = False
          if flag :
               print("Thêm thành thông")
          else: 
               print("Không thành công")
     def display_list_lop_hocsinh_monhoc(self):
          comboBox_9 = self.comboBox_9.currentText() #namhoc
          comboBox_18 = self.comboBox_18.currentText()#lophoc
          comboBox_19 = self.comboBox_19.currentText()#hocky
          comboBox_20 = self.comboBox_20.currentText()#monhoc
          diemTBHK = DiemTBMonHocBUS()
          listDiemTB_Lop = diemTBHK.getListDiem_MonHoc(comboBox_19,comboBox_18,comboBox_9,comboBox_20)
          self.table_ListDiem_MonHoc_Lop.setRowCount(len(listDiemTB_Lop))
          flag = True
          for i, row in enumerate(listDiemTB_Lop):
               for j,val in enumerate(row):
                    self.table_ListDiem_MonHoc_Lop.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.table_ListDiem_MonHoc_Lop.rowCount() 
          for i in range(numRows):
               self.table_ListDiem_MonHoc_Lop.item(i, 0).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 1).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 1).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 2).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 2).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 3).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 3).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 4).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 4).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 5).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 5).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 6).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 6).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 7).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 7).flags() & ~QtCore.Qt.ItemIsEditable)
               self.table_ListDiem_MonHoc_Lop.item(i, 8).setFlags(self.table_ListDiem_MonHoc_Lop.item(i, 8).flags() & ~QtCore.Qt.ItemIsEditable)
     def exportListDiem_MonHoc(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.table_ListDiem_MonHoc_Lop.model().columnCount()):
               columnHeader.append(self.table_ListDiem_MonHoc_Lop.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.table_ListDiem_MonHoc_Lop.rowCount()):
               for col in range(self.table_ListDiem_MonHoc_Lop.columnCount()):
                    item = self.table_ListDiem_MonHoc_Lop.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenLop = self.comboBox_18.currentText()
          namhoc = self.comboBox_9.currentText()
          hocky = self.comboBox_19.currentText()
          monhoc = self.comboBox_20.currentText()
          tenFile = r"FileExcel\BangDiem\{}\NamHoc_{}\Lop_{}\{}_{}.xlsx".format(monhoc,namhoc,tenLop,hocky,currentTime)
          path = os.path.dirname(tenFile)

          # Kiểm tra nếu thư mục không tồn tại thì tạo mới
          if not os.path.exists(path):
               os.makedirs(path)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    

     def insertDiem(self):
          diem = DiemBUS()
          monhoc = MonHocBUS()
          #maMonHoc = monhoc.getMamon(self.comboBox_3.currentText())
          hocky = HocKyBUS()
          #maHocKy = hocky.getma(self.comboBox_2.currentText())
          namhoc = NamHocBUS()
          #maNamHoc = namhoc.getma(self.comboBox_4.currentText())
          lophoc = LopHocBUS()
          #maLop = lophoc.getma(self.comboBox.currentText())
          flag = False
    
          for row in range(self.tableListHsDiem.rowCount()):
               maHocSinh = self.tableListHsDiem.item(row, 0).text()
               diemMieng = self.tableListHsDiem.item(row, 2).text()
               diem15phut = self.tableListHsDiem.item(row, 3).text()
               diemGiuaKy = self.tableListHsDiem.item(row, 4).text()
               diemThi = self.tableListHsDiem.item(row, 5).text()

               maMonHoc = monhoc.getMamon(self.comboBox_3.currentText())
               maHocKy = hocky.getma(self.comboBox_2.currentText())
               maNamHoc = namhoc.getma(self.comboBox_4.currentText())
               maLop = lophoc.getma(self.comboBox.currentText(),maNamHoc)

               for loaiDiem, diemSo in [('LD003', diemMieng), ('LD001', diem15phut), ('LD002', diemGiuaKy), ('LD004', diemThi)]:
                    diemDTO = DiemDTO(maHocSinh, maMonHoc, maHocKy, maNamHoc, maLop, loaiDiem, diemSo)
                    print("Insert điểm cho học sinh", maHocSinh)
                    if not diem.insertDiem(diemDTO):
                         break
               else:
                    flag = True
    
          if flag:
               QMessageBox.information(self, "Thông báo", "Lưu dữ liệu thành công!")
          else:
               QMessageBox.information(self, "Thông báo", "Lưu dữ liệu không thành công!")
     def exportListDiem(self):
          columnHeader = []
          #Tạo danh sách tiêu đề cột 
          for j in range(self.tableListDiemHS.model().columnCount()):
               columnHeader.append(self.tableListDiemHS.horizontalHeaderItem(j).text())
               df = pd.DataFrame(columns = columnHeader)
          for row in range(self.tableListDiemHS.rowCount()):
               for col in range(self.tableListDiemHS.columnCount()):
                    item = self.tableListDiemHS.item(row,col)
                    if item is None:
                         df.at[row, columnHeader[col]] = ''
                    else:            
                         df.at[row,columnHeader[col]] = item.text()
          t = time.localtime()
          currentTime = time.strftime("%H-%M-%S",t)
          tenHocSinh = self.tableListDiemHS.item(0, 1).text()
          tenLop = self.comboBox_6.currentText()
          namhoc = self.comboBox_5.currentText()
          hocky = self.comboBox_7.currentText()
          tenFile = r"FileExcel\BangDiem\NamHoc_{}\Lop_{}\{}\{}_{}.xlsx".format(namhoc,tenLop,hocky,tenHocSinh,currentTime)
          path = os.path.dirname(tenFile)

          # Kiểm tra nếu thư mục không tồn tại thì tạo mới
          if not os.path.exists(path):
               os.makedirs(path)
          df.to_excel(tenFile,index = False)
          if(columnHeader != " "):
               QMessageBox.information(self,"Thông báo","Xuất ra tệp excel thành công!")
               dir_path = os.getcwd()
               #excel =os.startfile('Excel.Application')
               os.startfile(os.path.join(dir_path,tenFile))
              # excel.Visible = True 
               print('Excel file exported!') 
               
          else:
               QMessageBox.warning(self,"Lỗi","Xuất ra tệp excel không thành công!")                                    
     
     def addLoaiDiem(self):
          loaidiem = LoaiDiemBUS()
          lineTenLoaiDiem = self. lineTenLoaiDiem.text()
          cboxHeSo_2 = self.cboxHeSo_2.currentText()
          addDiem = LoaiDiemDTO(None,lineTenLoaiDiem,cboxHeSo_2)
          if len(lineTenLoaiDiem) == 0 :
               QMessageBox.information(self,"Thông báo","Bạn chưa nhập đủ dữ liệu!")
          else:
               if loaidiem.ChecktenTonTai(lineTenLoaiDiem):
                    QMessageBox.information(self,"Thông báo","Môn học này đã có trong danh sách!")
               else:
                    if loaidiem.insert(addDiem):
                         print("Inserted record:", addDiem.maLoaiDiem, addDiem.tenLoaiDiem,addDiem.heSo)
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu thành công!")
                         self.loadlistMonHoc()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")
     def updateLoaiDiem(self):
          loaidiem = LoaiDiemBUS()
          numRows = self.tableLoaiDiem.rowCount()
          flag = True
          for i in range(numRows):
               maLoaiDiem= self.tableLoaiDiem.item(i,0).text()
               tenLoaiDiem= self.tableLoaiDiem.item(i,1).text()
               heSoLoaiDiem= self.tableLoaiDiem.item(i,2).text()
               update = LoaiDiemDTO(maLoaiDiem,tenLoaiDiem,heSoLoaiDiem)
               if not loaidiem.update(update):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistMonHoc()
          else : 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")

     def deleteLoaiDiem(self):
          selected = self.tableLoaiDiem.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableLoaiDiem.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa loại điểm có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              loaidiem = LoaiDiemBUS()
                              #self.tableChucVu.removeRow(row)
                              if loaidiem.delete(mamon):
                                   for col in range(self.tableLoaiDiem.columnCount()):
                                        item = self.tableLoaiDiem.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistMonHoc()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     
     def addMonHoc(self):
          mon = MonHocBUS()
          lineTenMonHoc = self.lineTenMonHoc.text()
          lineSoTiet = self.lineSoTiet.text()
          cboxHeSo = self.cboxHeSo.currentText()

          #maMonHoc =self.maMonHoc
          addMon = MonHocDTO(None, lineTenMonHoc, lineSoTiet, cboxHeSo)
          if len(lineTenMonHoc) == 0 or len(lineSoTiet)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if mon.CheckTenMonHoc(lineTenMonHoc):
                    QMessageBox.information(self,"Thông báo","Môn học này đã có trong danh sách!")
               else:
                    if mon.inser(addMon):
                    # Hiển thị thông báo lỗi nếu truy vấn không thành công
                         print("Inserted record:", addMon.idMH, addMon.tenMH, addMon.soTiet,addMon.heSo)
                         QMessageBox.warning(self, "Thông báo", "Thêm dữ liệu thành công!")
                         self.loadlistMonHoc()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")
     def updateMonHoc(self):
          mon = MonHocBUS()
          numRows = self.tableMonHoc.rowCount()
          flag = True
          for i in range(numRows):
               maMonHoc= self.tableMonHoc.item(i,0).text()
               tenMonHoc = self.tableMonHoc.item(i,1).text()
               soTietMonHoc = self.tableMonHoc.item(i,2).text()
               heSoMonHoc = self.tableMonHoc.item(i,3).text()
               updateMon = MonHocDTO(maMonHoc,tenMonHoc,soTietMonHoc,heSoMonHoc)
               if not mon.updateMon(updateMon):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistMonHoc()
          else : 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")
     
     
     def deleteMonHoc(self):
          selected = self.tableMonHoc.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableMonHoc.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa môn học có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              mon = MonHocBUS()
                              #self.tableChucVu.removeRow(row)
                              if mon.deleteMon(mamon):
                                   for col in range(self.tableMonHoc.columnCount()):
                                        item = self.tableMonHoc.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistMonHoc()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def findMon(self):
          mon = MonHocBUS()
          txtTimKiem_2 = self.txtTimKiem_2.text()
          list = mon.find(txtTimKiem_2)
          self.tableMonHoc.clearContents()
          self.tableMonHoc.setRowCount(len(list))
          for i, row in enumerate(list):
               for j, item in enumerate(row):
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(item)))
     
     def findSortMonHoc(self):
          mon = MonHocBUS()
          self.tableMonHoc.clearContents()
          order = self.cbSortMH.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = mon.findASC(order)
          #self.tableChucVu.clearContents()
          self.tableMonHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(item)))
     
     def findHeSo(self):
          mon = MonHocBUS()
          self.tableMonHoc.clearContents()
          order = self.cbSortHeSo.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = mon.findHeSo(order)
          #self.tableChucVu.clearContents()
          self.tableMonHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(item)))
     
     def findSoTiet(self):
          mon = MonHocBUS()
          self.tableMonHoc.clearContents()
          order = self.cbSortST.currentText()
          #sort_order = "Giảm dần" if self.cbSortCV.currentIndex() == 0 else "Tăng dần"  # determine sorting order based on selected index
          data = mon.findSoTiet(order)
          #self.tableChucVu.clearContents()
          self.tableMonHoc.setRowCount(len(data))
          for i, row in enumerate(data):
               for j, item in enumerate(row):
                    self.tableMonHoc.setItem(i, j, QTableWidgetItem(str(item)))
     
     def stackKetQua(self):
          self.stackedWidget.setCurrentIndex(8)
          #KetQua
          self.btnThemKQ.clicked.connect(self.addKetQua)
          self.btnCapNhatKetQua.clicked.connect(self.updateKetQua)
          self.btnXoaKetQua.clicked.connect(self.deleteKetQua)
          self.pushButton_96.clicked.connect(self.clear)

          #HocLuc
          self.btnThemHocLuc.clicked.connect(self.addHocLuc)
          self.btnCapNhatHocLuc.clicked.connect(self.updateHocLuc)
          self.btnXoaHocLuc.clicked.connect(self.deleteHocLuc)
          self.pushButton_97.clicked.connect(self.clear)
          #HanhKiem
          self.btnThemHanhKiem.clicked.connect(self.addHanhKiem)
          self.btnCapNhatHanhKiem.clicked.connect(self.updateHanhKiem)
          self.btnXoaHanhKiem.clicked.connect(self.deleteHanhKiem)
          self.pushButton_99.clicked.connect(self.clear)
          #QuyDinh
          self.btnQuyDinh.clicked.connect(self.quyDinh)
          self.btnResetQuyDinh.clicked.connect(self.resetQuyDinh)

          self.loadlistKQ()
     def loadlistKQ(self):
          #ketqua
          ketqua = KetQuaBUS()
          self.lineMaKetQua.setText(str(KetQuaBUS.CheckgetID(self)))
          listmonHoc = ketqua.getlistKetQua()
          self.tableKetQua.setRowCount(len(listmonHoc))
          #self.tableMonHoc.setColumnCount(len(listmonHoc[0]))

          for i,row in enumerate(listmonHoc): 
               for j,val in enumerate(row): 
                    self.tableKetQua.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableKetQua.rowCount() 
          for i in range(numRows):
               self.tableKetQua.item(i, 0).setFlags(self.tableKetQua.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableKetQua.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          #hocluc
          hocluc = HocLucBUS()
          self.lineMaHocLuc.setText(str(HocLucBUS.CheckgetID(self)))
          listmonHoc = hocluc.getlistHocLuc()
          self.tableHocLuc.setRowCount(len(listmonHoc))

          for i,row in enumerate(listmonHoc): 
               for j,val in enumerate(row): 
                    self.tableHocLuc.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableHocLuc.rowCount() 
          for i in range(numRows):
               self.tableHocLuc.item(i, 0).setFlags(self.tableHocLuc.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableHocLuc.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          #HanhKiem
          hanhkiem = HanhKiemBUS()
          self.lineMaHanhKiem.setText(str(HanhKiemBUS.CheckgetID(self)))
          listHK = hanhkiem.getlistHK()
          self.tableHanhKiem.setRowCount(len(listHK))
          for i,row in enumerate(listHK): 
               for j,val in enumerate(row): 
                    self.tableHanhKiem.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableHanhKiem.rowCount() 
          for i in range(numRows):
               self.tableHanhKiem.item(i, 0).setFlags(self.tableHanhKiem.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableHanhKiem.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          #QuyDinh 
          qd = QuyDinhBUS()
          quydinhlist = qd.get()
          self.spinTuoitToiThieu.setValue(quydinhlist[0][0])
          self.spinTuoiToiDa.setValue(quydinhlist[0][1])
          self.spinLopToiThieu.setValue(quydinhlist[0][2])
          self.spinLopToiDa.setValue(quydinhlist[0][3])
          self.spinDiem.setValue(quydinhlist[0][4])     
     def addKetQua(self):
          kq = KetQuaBUS()
          lineTenKetQua = self.lineTenKetQua.text()
          addKQ = KetQuaDTO(None,lineTenKetQua)
          if len(lineTenKetQua)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if kq.Checkten(lineTenKetQua):
                    QMessageBox.information(self,"Thông báo","Môn học này đã có trong danh sách!")
               else:
                    if kq.inser(addKQ):
                         print("Inserted record:", addKQ.maKetQua, addKQ.tenKetQua)
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
                         self.loadlistKQ()
                         self.clear()
                    else:
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu không thành công!")
     
     def updateKetQua(self):
          kq = KetQuaBUS()
          numRows = self.tableKetQua.rowCount()
          flag = True
          for i in range(numRows):
               ma= self.tableKetQua.item(i,0).text()
               ten= self.tableKetQua.item(i,1).text()
               update = KetQuaDTO(ma,ten)
               if not kq.update(update):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistKQ()
          else : 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")

     def deleteKetQua(self):
          selected = self.tableKetQua.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableKetQua.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa loại điểm có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              loaidiem = KetQuaBUS()
                              #self.tableChucVu.removeRow(row)
                              if loaidiem.delete(mamon):
                                   for col in range(self.tableKetQua.columnCount()):
                                        item = self.tableKetQua.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistKQ()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")

          
     def addHocLuc(self):
          hl = HocLucBUS()
          lineTenHocLuc = self.lineTenHocLuc.text()
          lineDiemCD = self.lineDiemCD.text()
          lineDiemCT = self.lineDiemCT.text()
          lineDiemKhongChe = self.lineDiemKhongChe.text()
          addHocLuc = HocLucDTO(None,lineTenHocLuc,lineDiemCD,lineDiemCT,lineDiemKhongChe)
          if len(lineTenHocLuc)==0 or len(lineDiemCD)==0 or len(lineDiemCT)==0 or len(lineDiemKhongChe)==0:
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if hl.Checkten(lineTenHocLuc):
                    QMessageBox.information(self,"Thông báo","Loại học lực này đã có trong danh sách!")
               else:
                    if hl.insert(addHocLuc):
                         print("Inserted record:", addHocLuc.maHL, addHocLuc.tenHL, addHocLuc.diemCanDuoi,addHocLuc.diemCanTren, addHocLuc.diemKhongChe)
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu thành công!")
                         self.loadlistKQ()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")
     
     def updateHocLuc(self):
          hl = HocLucBUS()
          numRows = self.tableHocLuc.rowCount()
          flag = True
          for i in range(numRows):
               maHocLuc= self.tableHocLuc.item(i,0).text()
               tenHocLuc= self.tableHocLuc.item(i,1).text()
               diemCD = self.tableHocLuc.item(i,2).text()
               diemCT = self.tableHocLuc.item(i,3).text()
               diemKhongChe = self.tableHocLuc.item(i,4).text()
               update = HocLucDTO(maHocLuc,tenHocLuc,diemCD,diemCT,diemKhongChe)
               if not hl.update(update):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistKQ()
          else : 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")

     def deleteHocLuc(self):
          selected = self.tableHocLuc.selectedItems()
          
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableHocLuc.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa loại điểm có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              hl = HocLucBUS()
                              if hl.delete(mamon):
                                   #self.tableHocLuc.removeRow(row)
                                   for col in range(self.tableHocLuc.columnCount()):
                                        item = self.tableHocLuc.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistKQ()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def addHanhKiem(self):
          hk = HanhKiemBUS()
          lineTenHanhKiem = self.lineTenHanhKiem.text()
          addKQ = HanhKiemDTO(None,lineTenHanhKiem)
          if len(lineTenHanhKiem)==0 :
               QMessageBox.warning(self,"Thông báo","Bạn chưa nhập dữ liệu")
          else: 
               if hk.Checkten(lineTenHanhKiem):
                    QMessageBox.information(self,"Thông báo","Loại hạnh kiểm này đã có trong danh sách!")
               else:
                    if hk.inser(addKQ):
                         print("Inserted record:", addKQ.maHanhKiem, addKQ.tenHanhKiem)
                         QMessageBox.warning(self, "Lỗi", "Thêm dữ liệu thành công!")
                         self.loadlistKQ()
                         self.clear()
                    else:
                         QMessageBox.information(self,"Thông báo","Thêm vào danh sách không thành công!")
     
     def updateHanhKiem(self):
          hk = HanhKiemBUS()
          numRows = self.tableHanhKiem.rowCount()
          flag = True
          for i in range(numRows):
               ma= self.tableHanhKiem.item(i,0).text()
               ten= self.tableHanhKiem.item(i,1).text()
               update = HanhKiemDTO(ma,ten)
               if not hk.update(update):
                    flag = False
          if flag:
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistKQ()
          else : 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu không thành công!")

     def deleteHanhKiem(self):
          selected = self.tableHanhKiem.selectedItems()
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         mamon = self.tableHanhKiem.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa loại hạnh kiểm có mã {mamon} ?", QMessageBox.Yes| QMessageBox.Cancel)
                         if ret == QMessageBox.Yes:
                              hk = HanhKiemBUS()
                              #self.tableChucVu.removeRow(row)
                              if hk.delete(mamon):
                                   for col in range(self.tableHanhKiem.columnCount()):
                                        item = self.tableHanhKiem.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {mamon} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistKQ()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def quyDinh(self):
          qd = QuyDinhBUS()
          spinTuoitToiThieu = self.spinTuoitToiThieu.value()
          spinTuoiToiDa = self.spinTuoiToiDa.value()
          spinLopToiThieu = self.spinLopToiThieu.value()
          spinLopToiDa = self.spinLopToiDa.value()
          spinDiem = self.spinDiem.value()
          addQuyDinh = QuyDinhDTO(spinTuoitToiThieu,spinTuoiToiDa,spinLopToiThieu,spinLopToiDa,spinDiem)
          if qd.insert(addQuyDinh):
               print("Insert record:",addQuyDinh.tuoiCD,addQuyDinh.tuoiCT,addQuyDinh.siSoCD,addQuyDinh.tuoiCT,addQuyDinh.diemDat)
               QMessageBox.information(self,"Thông báo","Cập nhật quy định mới thành công!")
               self.loadlistKQ()
          else:
               QMessageBox.information(self,"Thông báo","Cập nhật quy định mới không thành công!")
     def resetQuyDinh(self):
          self.spinTuoitToiThieu.setValue(0)
          self.spinTuoiToiDa.setValue(0)
          self.spinLopToiThieu.setValue(0)
          self.spinLopToiDa.setValue(0)
          self.spinDiem.setValue(0)

     def stackHocPhi(self):
          self.stackedWidget.setCurrentIndex(9)
          maPhieu = "HD" + str(random.randint(0, 9999)).zfill(5)
          self.lineMaPhieu.setText(maPhieu)
          self.maPhieu = maPhieu
          self.btnThemKhoanPhi.clicked.connect(self.addKhoanPhi)
          self.btnCapNhatKhoanPhi.clicked.connect(self.updateKhoanPhi)
          self.btnXoaKhoanPhi.clicked.connect(self.deleteKhoanPhi)
          self.btnClearPhi.clicked.connect(self.clear)
          self.btnTimKiemPhi.clicked.connect(self.findPhi)
          self.loadlistPhi()
     def loadlistPhi(self):
          phi = CacKhoanPhiBUS()
          self.lineMaPhi.setText(str(CacKhoanPhiBUS.CheckgetID(self)))
          listPhi = phi.getListPhi()
          self.tableKhoanPhi.setRowCount(len(listPhi))
          self.tableKhoanPhi.setColumnCount(len(listPhi[0]))

          for i,row in enumerate(listPhi): 
               for j,val in enumerate(row): 
                    self.tableKhoanPhi.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableKhoanPhi.rowCount()
          for i in range(numRows):
               self.tableKhoanPhi.item(i, 0).setFlags(self.tableKhoanPhi.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableKhoanPhi.item(i, 0).setBackground(QtGui.QColor(200, 200, 150))     
          self.tableListKhoanPhi.setRowCount(len(listPhi))
          self.tableListKhoanPhi.setColumnCount(len(listPhi[0]))
          for i, row in enumerate(listPhi):
               for j, val in enumerate(row):
                    self.tableListKhoanPhi.setItem(i, j, QTableWidgetItem(str(val)))
          numRows = self.tableListKhoanPhi.rowCount()
          for i in range(numRows):
               self.tableListKhoanPhi.item(i, 0).setFlags(self.tableListKhoanPhi.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               self.tableListKhoanPhi.item(i, 1).setFlags(self.tableListKhoanPhi.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
          self.tableListKhoanPhi.itemSelectionChanged.connect(self.displayItemData)    
     def displayItemData(self):     
          selected = self.tableListKhoanPhi.selectedItems()
          if selected and len(selected) >= 2: 
               maPhi = selected[0].text()
               tenPhi = selected[1].text()
               soTien = selected[2].text()
               self.lineListMaPhi.setText(maPhi)
               self.lineListTenKhoanPhi.setText(tenPhi)
               self.lineTienDong.setText(soTien)
     def addKhoanPhi(self):
          #lineMaPhi
          phi = CacKhoanPhiBUS()
          lineTenKhoanPhi = self.lineTenMaPhi.text()
          lineTienPhi = self.lineTienPhi.text()
          #maPhi = self.maPhi
          addphi = CacKhoanPhi(None, lineTenKhoanPhi,lineTienPhi)
          if len(lineTenKhoanPhi)==0:
               QMessageBox.warning(self,"Cảnh báo","Bạn chưa nhập dữ liệu")
          else: 
               if phi.checkPhiTonTai(lineTenKhoanPhi):
                    QMessageBox.information(self,"Thông báo","Loại phí này đã có trong danh sách!")
               else : 
                    if phi.insertPhi(addphi):
                         # The above code is printing a message that includes the ID and details of a
                         # record that has been inserted into a database table or data structure. The
                         # specific details of the record are contained in the variable `addphi`, and
                         # the message is printed using the `print()` function in Python.
                         print("Inserted record:", addphi.idCacKhoanPhi, addphi.tenPhi)
                         QMessageBox.information(self,"Thông báo",f"Thêm phí có tên {lineTenKhoanPhi} vào danh sách thành công!")
                         self.loadlistPhi()
                         self.lineTienPhi.clear()
                         self.clear()
                    else: 
                         QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
     def updateKhoanPhi(self):
          phi = CacKhoanPhiBUS()
          numRows = self.tableKhoanPhi.rowCount()
          flag = True
          for i in range(numRows):
               maPhi= self.tableKhoanPhi.item(i,0).text()
               tenPhi = self.tableKhoanPhi.item(i,1).text()
               tienPhi = self.tableKhoanPhi.item(i,2).text()
               updatephi = CacKhoanPhi(maPhi,tenPhi,tienPhi)
               
               if not phi.updateListPhi(updatephi):
                    flag = False
          if flag: 
               QMessageBox.information(self,"Thông báo","Cập nhật dữ liệu thành công!")
               self.loadlistPhi()
          else : 
               QMessageBox.warning(self, "Lỗi", "Cập nhật dữ liệu không thành công!")
     def deleteKhoanPhi(self):
          selected = self.tableKhoanPhi.selectedItems()
          
          if selected:
               for item in selected:
                    row = item.row()
                    col = item.column()
                    if col == 0: 
                         # Kiểm tra xem ô đầu tiên (cột mã chức vụ) đã được chọn hay chưa
                         maPhi = self.tableKhoanPhi.item(row, col).text()
                         ret = QMessageBox.question(self, 'MessageBox', f"Bạn muốn xóa chức vụ có mã {maPhi} ?", QMessageBox.Yes| QMessageBox.Cancel)
               
                         if ret == QMessageBox.Yes:
                              phi = CacKhoanPhiBUS()
                              #self.tableChucVu.removeRow(row)
                              if phi.deletePhi(maPhi):
                                   for col in range(self.tableKhoanPhi.columnCount()):
                                        item = self.tableKhoanPhi.takeItem(row, col)
                                        del item
                                   QMessageBox.information(self,"Thông báo",f"Xóa {maPhi} thành công")
                                   # Xóa đối tượng QTableWidgetItem khỏi bảng và danh sách đối tượng tương ứng
                                   self.loadlistPhi()
                              else:
                                   QMessageBox.warning(self, "Lỗi", "Xóa dữ liệu không thành công!")
          else:
                    QMessageBox.warning(self,"Cảnh báo","Bạn chưa chọn đối tượng cần xóa!")
     def findPhi(self):
          phi = CacKhoanPhiBUS()
          txtTimKiem = self.lineTimKiemPhi.text()
          list = phi.find(txtTimKiem)
          rowcount = 0
          self.tableKhoanPhi.clearContents()
          self.tableKhoanPhi.rowCount()
          if list is not None:
               for row in list :
                    self.tableKhoanPhi.setItem(rowcount, 0, QTableWidgetItem(row[0]))
               #self.tableChucVu.item(i, 0).setFlags(self.tableChucVu.item(i, 0).flags() & ~QtCore.Qt.ItemIsEditable)
               #self.tableChucVu.item(i, 0).setBackground(QtGui.QColor(200, 200, 200))
                    self.tableKhoanPhi.setItem(rowcount, 1, QTableWidgetItem(row[1]))
                    rowcount += 1
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
               #widget.setCurrentIndex(0)
          #formLogin.show()
               #widget.setFixedSize(800,500)
               global global_username
               global_username = None  # đặt giá trị của biến global_username thành None     
               #widget.setCurrentIndex(0)
               self.deleteLater()
               widget.setCurrentIndex(0)  # chuyển đến trang đầu tiên (FormLogin)
               widget.setFixedSize(800,500)
               formLogin.show()  # hiển thị FormLogin trên màn hình




app = QtWidgets.QApplication(sys.argv)
formLogin = FormLogin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(formLogin)
#widget.setFixedHeight(500)
#widget.setFixedWidth(800)
widget.resize(formLogin.width(),formLogin.height())
widget.show()
formLogin.setParent(widget)
#formLogin.show()
try:
     sys.exit(app.exec_())
except:
     print("Exiting!")
#app.exec()
query.close()
     