import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from  DTO.ChucVuDTO import ChucVuDTO
class ChucVuDAO:
     def __init__(self):
        pass
     def getlistDanhSach(self):
          listChucVu = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT maChucVu, tenChucVu FROM chucvu"
               query.execute(sqlChucVu)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1])
                    listChucVu.append(chucvu)
               print(listChucVu)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return listChucVu
     def updateChucVu(dd: ChucVuDTO):
          sqlCapNhatChucVu = "UPDATE chucvu SET tenChucVu = %s WHERE maChucVu =%s"
          data = (dd.tenChucVu,dd.idChucVu)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlCapNhatChucVu,data)
               print(sqlCapNhatChucVu, data)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def deleteChucVu(maChucVu):
          sqlDeleteChucVu = "DELETE FROM chucvu WHERE maChucVu = %s"
          val = (maChucVu,)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlDeleteChucVu,val)
               print(sqlDeleteChucVu,val)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def insertChucVu(self,dd:ChucVuDTO):
          sqlInsertChucVu ="INSERT INTO chucvu (maChucVu,tenChucVu) VALUES (%s,%s)"
          idChucVu = self.CheckgetID()  # generate new unique ID
          val = (idChucVu, dd.tenChucVu)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlInsertChucVu,val)
               print(sqlInsertChucVu,val)
               mydb.commit()
               return True

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def CheckgetID(self):
          sqlGetMaCV = "SELECT CONCAT('CV', LPAD(COUNT(*) + 1, 3, '0')) FROM chucvu"
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlGetMaCV)
               ma = query.fetchone()[0]
               print(sqlGetMaCV)
               mydb.commit()
               return ma

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def CheckChucVuTonTai(tenChucVu):
          sqlCheckChucVuTonTai = "SELECT * FROM chucvu WHERE tenChucVu = %s"
          val = (tenChucVu,)
          try:
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               query.execute(sqlCheckChucVuTonTai,val)
               result = query.fetchone()
               print(sqlCheckChucVuTonTai,val)
               mydb.commit()
               return result is not None

          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally :
               query.close()
               mydb.close()
          return False
     def find(self,key):
          list = []
          sqlTimkiem = "SELECT chucvu.maChucVu, chucvu.tenChucVu FROM `chucvu` WHERE chucvu.maChucVu LIKE '%{}%' OR LOWER(chucvu.tenChucVu) LIKE LOWER('%{}%')".format(key.lower(), key.lower())
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
               query.execute(f"SELECT * FROM chucvu ORDER BY maChucVu ASC")
          elif order == "Giảm dần":
               query.execute(f"SELECT * FROM chucvu ORDER BY maChucVu DESC")
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