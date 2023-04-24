import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.PhanLopDTO import PhanLopDTO
class PhanLopDAO:
     def __init__(self):
          pass
     def getlist(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT namhoc.tenNamHoc,khoilop.tenKhoiLop,lop.tenLop,hocsinh.tenHocSinh FROM namhoc,khoilop,lop,hocsinh,phanlop WHERE phanlop.maNamHoc=namhoc.maNamHoc AND phanlop.maKhoiLop=khoilop.maKhoiLop AND phanlop.maLop = lop.maLop AND phanlop.maHocSinh = hocsinh.maHocSinh"
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
     def getKhoi (self,year):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT kl.tenKhoiLop FROM lop l JOIN khoilop kl ON l.maKhoiLop = kl.maKhoiLop JOIN namhoc n ON l.maNamHoc = n.maNamHoc WHERE n.tenNamHoc = %s"
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
               sqlChucVu  = "SELECT DISTINCT lop.tenLop FROM lop JOIN khoilop ON lop.maKhoiLop = khoilop.maKhoiLop WHERE khoilop.tenKhoiLop = %s"
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
     def getHocSinh(self,year):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT hocsinh.tenHocSinh FROM hocsinh WHERE hocsinh.maHocSinh NOT IN (SELECT phanlop.maHocSinh FROM phanlop, lop,namhoc WHERE phanlop.maLop = lop.maLop AND lop.maNamHoc= namhoc.maNamHoc AND namhoc.tenNamHoc= %s)"
               val=(year,)
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
     def insert(self,dd:PhanLopDTO):
          sqlInsert ="INSERT INTO phanlop (maNamHoc,maKhoiLop,maLop,maHocSinh) VALUES (%s, %s,%s,%s)"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.maNamHoc,dd.maKhoi,dd.maLop,dd.maHocSinh)
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
          sql = "DELETE FROM phanlop WHERE phanlop.maHocSinh = %s"
          val = (ma,)
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
     def getlistHS(self,lop):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT hocsinh.maHocSinh,hocsinh.tenHocSinh,hocsinh.gioitinh,hocsinh.ngaySinh,lop.tenLop FROM hocsinh,lop,phanlop WHERE lop.maLop = phanlop.maLop AND lop.tenLop = %s AND hocsinh.maHocSinh = phanlop.maHocSinh"
               val = (lop,)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list