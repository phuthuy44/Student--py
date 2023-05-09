import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.LopHocDTO import LopHocDTO
class LopHocDAO:
     def __init__(self):
          pass
     def getlistLH(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT maLop, tenLop,khoilop.tenKhoiLop,namhoc.tenNamHoc,siSo,giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE lop.maKhoiLop = khoilop.maKhoiLop AND namhoc.maNamHoc = lop.maNamHoc AND giaovien.maGiaoVien = lop.maGiaoVien"
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def CheckgetID(self):
          sqlGetMa = "SELECT CONCAT('LH', LPAD(COALESCE(MAX(SUBSTR(maLop, 3)), 0) + 1, 3, '0')) FROM lop"
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
     def CheckTenTonTai(tenNamHoc,tenLopHoc):
          sqlCheck = "SELECT lop.tenLop FROM lop JOIN namhoc ON lop.maNamHoc = namhoc.maNamHoc WHERE namhoc.tenNamHoc = %s AND lop.tenLop =%s"
          val = (tenNamHoc,tenLopHoc)
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
     def CheckGV(tenGV,namHoc):
          sqlCheck = "SELECT COUNT(*) FROM lop WHERE maGiaoVien = %s AND maNamHoc = %s"
          val = (tenGV,namHoc)
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
     def insert(self,dd:LopHocDTO):
          sqlInsert ="INSERT INTO lop (maLop,tenLop,maKhoiLop,maNamHoc,siSo,maGiaoVien) VALUES (%s,%s,%s,%s,%s,%s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.tenLop,dd.maKhoiLop,dd.maNamHoc,dd.siSo,dd.maGiaoVien)
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
     def update(dd:LopHocDTO):
          sqlCapNhat = "UPDATE lop SET tenLop= %s, maKhoiLop = %s,maNamHoc = %s, siSo = %s,maGiaoVien=%s WHERE  maLop = %s"
          data = (dd.tenLop,dd.maKhoiLop,dd.maNamHoc,dd.siSo,dd.maGiaoVien,dd.idLopHoc)
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
          sqlDelete = "DELETE FROM lop WHERE maLop= %s"
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
               query.execute("SELECT maLop, tenLop , khoilop.tenKhoiLop, namhoc.tenNamHoc,siSo,giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE lop.maKhoiLop = khoilop.maKhoiLop AND lop.maNamHoc = namhoc.maNamHoc AND lop.maGiaoVien = giaovien.maGiaoVien ORDER BY maLop ASC")
          elif order == "Giảm dần":
               query.execute("SELECT maLop, tenLop , khoilop.tenKhoiLop, namhoc.tenNamHoc,siSo,giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE lop.maKhoiLop = khoilop.maKhoiLop AND lop.maNamHoc = namhoc.maNamHoc AND lop.maGiaoVien = giaovien.maGiaoVien ORDER BY maLop DESC")
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list
     def findTenLop(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "Tăng dần":
               query.execute("SELECT maLop, tenLop , khoilop.tenKhoiLop, namhoc.tenNamHoc,siSo,giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE lop.maKhoiLop = khoilop.maKhoiLop AND lop.maNamHoc = namhoc.maNamHoc AND lop.maGiaoVien = giaovien.maGiaoVien ORDER BY tenLop ASC")
          elif order == "Giảm dần":
               query.execute("SELECT maLop, tenLop , khoilop.tenKhoiLop, namhoc.tenNamHoc,siSo,giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE lop.maKhoiLop = khoilop.maKhoiLop AND lop.maNamHoc = namhoc.maNamHoc AND lop.maGiaoVien = giaovien.maGiaoVien ORDER BY tenLop DESC")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5])
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
          sqlTimkiem = "SELECT maLop, tenLop , khoilop.tenKhoiLop, namhoc.tenNamHoc,LOP.siSo,giaovien.tenGiaoVien FROM lop,khoilop,namhoc,giaovien WHERE  lop.maKhoiLop = khoilop.maKhoiLop AND LOP.maNamHoc = namhoc.maNamHoc AND LOP.maGiaoVien = giaovien.maGiaoVien AND maLop LIKE '%{}%' OR LOWER(lop.tenLop) LIKE LOWER('%{}%') ".format(key.lower(), key.lower())
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
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def getma(tenLop,maNamHoc):
          sql  = "SELECT maLop FROM lop,namhoc WHERE tenLop = %s and lop.maNamHoc = namhoc.maNamHoc and namhoc.maNamHoc = %s"
          val = (tenLop,maNamHoc)
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
