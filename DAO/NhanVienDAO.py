import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.NhanVienDTO import NhanVienDTO
class NhanVienDAO : 
     def __init__(self):
          pass
     def getlistNV(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT maNhanVien,tenNhanVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,chucvu.tenChucVu,hinhAnh FROM nhanvien,chucvu WHERE nhanvien.maChucVu = chucvu.maChucVu"
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def CheckgetID(self):
          sqlGetMa = "SELECT CONCAT('NV', LPAD(COALESCE(MAX(SUBSTR(maNhanVien, 3)), 0) + 1, 3, '0')) FROM nhanvien"
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
     def CheckTenTonTai(ten):
          sqlCheck = "SELECT * FROM nhanvien WHERE email = %s"
          val = (ten,)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlCheck,val)
               result = query.fetchone()
               print(sqlCheck,val)
               mydb.commit()
               return result is not None

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def CheckSoDT(so):
          sqlCheck = "SELECT * FROM nhanvien WHERE soDienThoai = %s"
          val = (so,)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlCheck,val)
               result = query.fetchone()
               print(sqlCheck,val)
               mydb.commit()
               return result is not None

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def insert(self,dd:NhanVienDTO):
          sqlInsert ="INSERT INTO nhanvien (maNhanVien, tenNhanVien,ngaySinh,gioitinh,diaChi,email,soDienThoai,maChucVu,hinhAnh) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.tenNV,dd.ngaySinh,dd.gioiTinh,dd.diaChi,dd.email,dd.soDienThoai,dd.chucVu,dd.hinhAnh)
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
     def update(dd:NhanVienDTO):
          sqlCapNhat = "UPDATE nhanvien SET tenNhanVien= %s,ngaySinh =%s,gioiTinh =%s,diaChi = %s,email = %s,soDienThoai=%s,maChucVu=%s WHERE maNhanVien=%s"
          data = (dd.tenNV,dd.ngaySinh,dd.gioiTinh,dd.diaChi,dd.email,dd.soDienThoai,dd.chucVu,dd.hinhAnh,dd.maNhanVien)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlCapNhat,data)
               print(sqlCapNhat, data)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def delete(ma):
          sqlDelete = "DELETE FROM nhanvien WHERE maNhanVien= %s"
          val = (ma,)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlDelete,val)
               print(sqlDelete,val)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def find(self,key):
          pass
     def findSortASC(self,order):
          pass
     def finSortOfGT(self,order):
          pass
     