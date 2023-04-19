import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.NamHocDTO import NamHocDTO
class NamHocDAO:
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
               sqlChucVu  = "SELECT * FROM namhoc"
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def update(dd:NamHocDTO):
          sqlCapNhat = "UPDATE namhoc SET tenNamHoc= %s WHERE maNamHoc=%s"
          data = (dd.tenNamHoc,dd.maNamHoc)
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
          sqlGetMa = "SELECT CONCAT('NH', LPAD(COALESCE(MAX(SUBSTR(maNamHoc, 3)), 0) + 1, 3, '0')) FROM namhoc"
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
          sqlCheck = "SELECT * FROM namhoc WHERE tenNamHoc= %s"
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
     def delete(ma):
          sqlDelete = "DELETE FROM namhoc WHERE maNamHoc= %s"
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
     def insert(self,dd:NamHocDTO):
          sqlInsert ="INSERT INTO namhoc (maNamHoc, tenNamHoc) VALUES (%s, %s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.tenNamHoc)
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
     def find(self,key):
          list = []
          sqlTimkiem = "SELECT maNamHoc, tenNamHoc FROM `namhoc` WHERE maNamHoc LIKE '%{}%' OR LOWER(tenNamHoc) LIKE LOWER('%{}%')".format(key.lower(), key.lower())
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
                    chucvu = (row[0],row[1])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def findSortASCMa(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "Tăng dần":
               query.execute(f"SELECT * FROM namhoc ORDER BY maNamHoc ASC")
          elif order == "Giảm dần":
               query.execute(f"SELECT * FROM namhoc ORDER BY maNamHoc DESC")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list
     def findSortASCTen(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "Tăng dần":
               query.execute(f"SELECT * FROM namhoc ORDER BY tenNamHoc ASC")
          elif order == "Giảm dần":
               query.execute(f"SELECT * FROM namhoc ORDER BY tenNamHoc DESC")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list