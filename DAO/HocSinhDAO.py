import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.HocSinhDTO import HocSinhDTO
class HocSinhDAO:
     def __init__(self):
          pass
     def getlistHS(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT * FROM hocsinh  "
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
          sqlGetMa = "SELECT CONCAT('HS', LPAD(COALESCE(MAX(SUBSTR(maHocSinh, 3)), 0) + 1, 3, '0')) FROM hocsinh"
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
          sqlCheck = "SELECT * FROM hocsinh WHERE email = %s"
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
     def insert(self,dd:HocSinhDTO):
          sqlInsert ="INSERT INTO hocsinh (maHocSinh , tenHocSinh,ngaySinh,gioitinh,email,diaChi,tenPhuHuynh,soDienThoai,hinhAnh) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.hoTen,dd.ngaySinh,dd.gioiTinh,dd.email,dd.diaChi,dd.tenPhuHuynh,dd.soDienThoaiPH,dd.hinhAnh)
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
          sqlDelete = "DELETE FROM hocsinh WHERE maHocSinh= %s"
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
     def update(dd:HocSinhDTO):
          sqlCapNhat = "UPDATE hocsinh SET tenHocSinh = %s, ngaySinh = %s, gioitinh =%s, email= %s, diaChi = %s, tenPhuHuynh = %s,soDienThoai = %s WHERE maHocSinh =%s"
          data = (dd.hoTen,dd.ngaySinh,dd.gioiTinh,dd.email,dd.diaChi,dd.tenPhuHuynh,dd.soDienThoaiPH,dd.id)
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
               query.execute("SELECT * FROM hocsinh ORDER BY maHocSinh ASC")
          elif order == "Giảm dần":
               query.execute("SELECT * FROM hocsinh ORDER BY maHocSinh DESC")
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
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
               query.execute("SELECT * from hocsinh WHERE hocsinh.gioitinh = 'Nam'")
          elif order == "Nữ":
               query.execute("SELECT * from hocsinh WHERE hocsinh.gioitinh = 'Nữ'")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list 
     def find(self,key):
          list = []
          sqlTimkiem = "SELECT * FROM `hocsinh` WHERE maHocSinh LIKE '%{}%' OR LOWER(hocsinh.tenHocSinh) LIKE LOWER('%{}%') OR LOWER(hocsinh.gioiTinh) LIKE LOWER('%{}%') OR LOWER(hocsinh.diaChi) LIKE LOWER('%{}%') ORDER BY maHocSinh ASC LIMIT 10".format(key.lower(), key.lower(),key.lower(), key.lower())
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlTimkiem)
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