import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.MonHocDTO import MonHocDTO
class MonHocDAO:
     def __init__(self):
          pass
     def getlistDanhSach(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sql  = "SELECT *FROM monhoc"
               query.execute(sql)
               rows = query.fetchall()
               for row in rows:
                    mon= (row[0],row[1],row[2],row[3])
                    list.append(mon)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def CheckgetID(self):
          sqlGetMa = "SELECT CONCAT('MH', LPAD(COALESCE(MAX(SUBSTR(maMonHoc, 3)), 0) + 1, 3, '0')) FROM monhoc"
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
     def CheckTenTonTai(tenMon):
          sqlCheck = "SELECT * FROM monhoc WHERE tenMonHoc = %s"
          val = (tenMon,)
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
     def updateMon(dd: MonHocDTO):
          sqlCapNhat = "UPDATE monhoc SET tenMonHoc = %s, soTiet = %s, heSo = %s WHERE maMonHoc =%s"
          data = (dd.tenMH,dd.soTiet,dd.heSo,dd.idMH)
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
     def find(self,key):
          list = []
          sqlTimkiem = "SELECT maMonHoc, tenMonHoc, soTiet,heSo FROM `monhoc` WHERE maMonHoc LIKE '%{}%' OR LOWER(tenMonHoc) LIKE LOWER('%{}%') OR LOWER(soTiet) LIKE LOWER('%{}%') OR LOWER(heSo) LIKE LOWER('%{}%')".format(key.lower(), key.lower(),key.lower(), key.lower())
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
                    chucvu = (row[0],row[1],row[2],row[3])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def deleteMon(maMon):
          sqlDelete = "DELETE FROM monhoc WHERE maMonHoc= %s"
          val = (maMon,)
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
     def insertMon(self,dd:MonHocDTO):
          sqlInsert ="INSERT INTO monhoc (maMonHoc, tenMonHoc,soTiet,heSo) VALUES (%s, %s,%s,%s)"
          idPhi = self.CheckgetID()  # generate new unique ID
          val = (idPhi,dd.tenMH,dd.soTiet,dd.heSo)
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
               query.execute(f"SELECT * FROM monhoc ORDER BY maMonHoc ASC")
          elif order == "Giảm dần":
               query.execute(f"SELECT * FROM monHOC ORDER BY maMonHoc DESC")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list 
     def findHeSo(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "Hệ số 2":
               query.execute("SELECT * FROM monhoc WHERE monhoc.heso = 2")
          elif order == "Hệ số 1":
               query.execute("SELECT * FROM monhoc WHERE monhoc.heso = 1")
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list 
     def findSoTiet(self,order):
          print("order:", order)
          mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
          query = mydb.cursor()
          if order == "30":
               query.execute("SELECT * from monhoc WHERE soTiet= 30")
          elif order == "45":
               query.execute("SELECT * from monhoc WHERE soTiet= 45")
          elif order == "60":
               query.execute("SELECT * from monhoc WHERE soTiet= 60")
          elif order == "90":
               query.execute("SELECT * from monhoc WHERE soTiet= 90")
          
          #sqlfindSortASC ="SELECT * FROM chucvu ORDER BY maChucVu DESC"
          try:
               #query.execute(sqlfindSortASC)
               result = query.fetchall()
               list = []
               for row in result:
                    chucvu = (row[0],row[1],row[2],row[3])
                    list.append(chucvu)
               print(list)
               mydb.commit()
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return list
     def getMaMon(ten):
          sql  = "SELECT maMonHoc FROM monhoc WHERE tenMonHoc = %s"
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
               ma = query.fetchone()[0]
               print(ma)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return ma