import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.PhieuThanhToanDTO import PhieuThanhToanDTO
class PhieuThanhToanDAO : 
     def __init__(self):
          pass
     def CheckgetID(self):
          sqlGetMa = "SELECT CONCAT('HD', LPAD(COALESCE(MAX(SUBSTR(maPhieu, 3)), 0) + 1, 3, '0')) FROM phieuthanhtoan"
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlGetMa)
               ma = query.fetchone()[0]
               print(sqlGetMa)
               mydb.commit()
               return ma

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def insertPhieuThanhToan(self,dd:PhieuThanhToanDTO):
          sqlInsert ="INSERT INTO phieuthanhtoan(maPhieu,maNhanVien,maHocSinh,maLop,ngayDong,nguoiDong,thanhToan) VALUES (%s, %s,%s,%s,%s,%s,%s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.maNhanVien,dd.maHocSinh,dd.maLop,dd.ngayDong,dd.nguoiDong,dd.thanhToan)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlInsert,val)
               print(sqlInsert,val)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def getnhanvien(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT nhanvien.maNhanVien FROM nhanvien,chucvu WHERE nhanvien.maChucVu = chucvu.maChucVu AND chucvu.maChucVu ='CV003'"
               #val = (namhoc,)
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def getHocSinh(self,year,lop):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT hocsinh.maHocSinh FROM hocsinh WHERE hocsinh.maHocSinh IN (SELECT phanlop.maHocSinh FROM phanlop, lop,namhoc WHERE phanlop.maLop = lop.maLop AND lop.maNamHoc= namhoc.maNamHoc AND namhoc.tenNamHoc= %s AND LOP.tenLop = %s )"
               val=(year,lop)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def getlistPhieu(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT phieuthanhtoan.maPhieu,phieuthanhtoan.maNhanVien,phieuthanhtoan.maHocSinh,lop.tenLop,phieuthanhtoan.ngayDong,phieuthanhtoan.nguoiDong,phieuthanhtoan.thanhToan FROM phieuthanhtoan,lop WHERE phieuthanhtoan.maLop = LOP.maLop "
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def getlistPhi(self,phieu):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT cackhoanphi.maPhi,cackhoanphi.tenPhi,cackhoanphi.soTien FROM cackhoanphi,ctphieuthanhtoan,phieuthanhtoan where ctphieuthanhtoan.maPhieu = phieuthanhtoan.maPhieu AND ctphieuthanhtoan.maPhi = cackhoanphi.maPhi AND phieuthanhtoan.maPhieu = %s "
               val = (phieu,)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list