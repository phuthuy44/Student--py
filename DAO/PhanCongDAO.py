import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.PhanCongDTO import PhanCongDTO
class PhanCongDAO:
     def __init__(self):
        pass
     def  getlist(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT namhoc.tenNamHoc,lop.tenLop,monhoc.tenMonHoc, giaovien.tenGiaoVien FROM namhoc,lop,monhoc,giaovien,phancong WHERE phanCONG.maNamHoc = namhoc.maNamHoc AND phancong.maLop= LOP.maLop AND phancong.maMonHoc = monhoc.maMonHoc AND phancong.maGiaoVien = giaovien.maGiaoVien"
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def getLop(self,khoi):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT lop.tenLop FROM lop INNER JOIN namhoc ON lop.maNamHoc = namhoc.maNamHoc WHERE namhoc.tenNamHoc = %s"
               val = (khoi,)
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
     def getMonHoc(self,nam,mon):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT monhoc.tenMonHoc FROM monhoc WHERE NOT EXISTS ( SELECT * FROM phancong,lop,namhoc WHERE phancong.maMonHoc = monhoc.maMonHoc AND phancong.maLop = lop.maLop AND phancong.maNamHoc = namhoc.maNamHoc And namhoc.tenNamHoc =%s AND lop.tenLop = %s )"
               val = (nam,mon)
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
     def getGiaoVien(self,mon):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT giaovien.tenGiaoVien FROM giaovien INNER JOIN monhoc ON monhoc.maMonHoc = giaovien.maMonHoc AND monhoc.tenMonHoc = %s"
               val = (mon,)
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
     def insert(self,dd:PhanCongDTO):
          sqlInsert ="INSERT INTO phancong(maNamHoc,maLop,maMonHoc,maGiaoVien) VALUES (%s, %s,%s,%s)"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.maNamHoc,dd.maLop,dd.maMonHoc,dd.maGiaoVien)
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
     def delete(ma,lop):
          sql = "DELETE FROM phancong WHERE phancong.maGiaoVien = %s AND phancong.maLop IN (SELECT maLop FROM lop WHERE maLop = %s)"
          val = (ma,lop)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sql,val)
               print(sql,val)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def getlistGV(self,lop):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT giaovien.maGiaoVien,giaovien.tenGiaoVien,giaovien.gioitinh,giaovien.ngaySinh,monhoc.tenMonHoc,lop.tenLop FROM giaovien,monhoc,lop,phancong WHERE phancong.maGiaoVien = giaovien.maGiaoVien AND giaovien.maMonHoc = monhoc.maMonHoc AND phancong.maLop = LOP.maLop AND lop.tenLop = %s"
               val = (lop,)
               query.execute(sqlChucVu,val)
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