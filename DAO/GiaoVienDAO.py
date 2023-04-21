import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.GiaoVienDTO import GiaoVienDTO
class GiaoVienDAO:
     def __init__(self):
          pass
     def getlistGV(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT maGiaoVien,tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,monhoc.tenMonHoc,chucvu.tenChucVu,hinhAnh FROM giaovien,monhoc,chucvu WHERE giaovien.maMonHoc = monhoc.maMonHoc AND giaovien.maChucVu = chucvu.maChucVu ORDER BY giaovien.maGiaoVien ASC "
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def update(dd:GiaoVienDTO):
          sqlCapNhat = "UPDATE giaovien SET tenGiaoVien= %s,ngaySinh =%s,gioiTinh =%s,diaChi = %s,email = %s,soDienThoai=%s,maMonHoc = %s,maChucVu=%s WHERE maGiaoVien=%s"
          data = (dd.tenGV,dd.ngaySinh,dd.gioiTinh,dd.diaChi,dd.email,dd.soDienThoai,dd.chuyenMon,dd.chucVu,dd.maGiaoVien)
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
     def CheckgetID(self):
          sqlGetMa = "SELECT CONCAT('GV', LPAD(COALESCE(MAX(SUBSTR(maGiaoVien, 3)), 0) + 1, 3, '0')) FROM giaovien"
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
          sqlCheck = "SELECT * FROM giaovien WHERE email = %s"
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
          sqlCheck = "SELECT * FROM giaovien WHERE soDienThoai = %s"
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
     def insert(self,dd:GiaoVienDTO):
          sqlInsert ="INSERT INTO giaovien (maGiaoVien , tenGiaoVien,ngaySinh,gioitinh,diaChi,email,soDienThoai,maMonHoc,maChucVu,hinhAnh) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.tenGV,dd.ngaySinh,dd.gioiTinh,dd.diaChi,dd.email,dd.soDienThoai,dd.chuyenMon,dd.chucVu,dd.hinhAnh)
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
     def delete(ma):
          sqlDelete = "DELETE FROM giaovien WHERE maGiaoVien= %s"
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
     def findSortASC(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "Tăng dần":
               query.execute("SELECT maGiaoVien,tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,monhoc.tenMonHoc,chucvu.tenChucVu,hinhAnh FROM giaovien,monhoc,chucvu WHERE giaovien.maMonHoc = monhoc.maMonHoc AND giaovien.maChucVu = chucvu.maChucVu ORDER BY maGiaoVien ASC")
          elif order == "Giảm dần":
               query.execute("SELECT maGiaoVien,tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,monhoc.tenMonHoc,chucvu.tenChucVu,hinhAnh FROM giaovien,monhoc,chucvu WHERE giaovien.maMonHoc = monhoc.maMonHoc AND giaovien.maChucVu = chucvu.maChucVu ORDER BY maGiaoVien DESC")
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list
     def findGioiTinh(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "Nam":
               query.execute("SELECT maGiaoVien,tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,monhoc.tenMonHoc,chucvu.tenChucVu,hinhAnh FROM giaovien,monhoc,chucvu WHERE giaovien.gioiTinh = 'Nam' AND giaovien.maMonHoc = monhoc.maMonHoc AND giaovien.maChucVu = chucvu.maChucVu ORDER BY maGiaoVien ASC")
          elif order == "Nữ":
               query.execute("SELECT maGiaoVien,tenGiaoVien,ngaySinh,gioiTinh,diaChi,email,soDienThoai,monhoc.tenMonHoc,chucvu.tenChucVu,hinhAnh FROM giaovien,monhoc,chucvu WHERE giaovien.gioiTinh = 'Nữ' AND giaovien.maMonHoc = monhoc.maMonHoc AND giaovien.maChucVu = chucvu.maChucVu ORDER BY maGiaoVien ASC")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list 
     def get_teachers_not_incharge(self,year):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT giaovien.tenGiaoVien FROM giaovien WHERE giaovien.maGiaoVien NOT IN ( SELECT lop.maGiaoVien FROM lop,namhoc WHERE namhoc.tenNamHoc = %s AND lop.maNamHoc = namhoc.maNamHoc) "
               val = (year,)
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
     def getma(ten):
          sql  = "SELECT maGiaoVien FROM giaovien WHERE tenGiaoVien = %s"
          val = (ten,)
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sql,val)
               rows = query.fetchone()[0]
               print(sql,val)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return rows
     