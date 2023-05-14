import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.CacKhoanPhi import CacKhoanPhi
class CacKhoanPhiDAO:
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
               sqlPhi  = "SELECT *FROM cackhoanphi"
               query.execute(sqlPhi)
               rows = query.fetchall()
               for row in rows:
                    phi= (row[0],row[1],row[2])
                    list.append(phi)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def updatePhi(dd: CacKhoanPhi):
          sqlCapNhat = "UPDATE cackhoanphi SET soTien = %s , tenPhi = %s WHERE maPhi =%s"
          data = (dd.soTien,dd.tenPhi,dd.idCacKhoanPhi)
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
          sqlGetMa = "SELECT CONCAT('PH', LPAD(COALESCE(MAX(SUBSTR(maPhi, 3)), 0) + 1, 3, '0')) FROM cackhoanphi"
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
     def CheckTenTonTai(tenPhi):
          sqlCheck = "SELECT * FROM cackhoanphi WHERE tenPhi = %s"
          val = (tenPhi,)
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
     def find(self,key):
          list = []
          sqlTimkiem = "SELECT maPhi, tenPhi FROM `cackhoanphi` WHERE maPhi LIKE '%{}%' OR LOWER(tenPhi) LIKE LOWER('%{}%')".format(key.lower(), key.lower())
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
     def deletePhi(maPhi):
          sqlDelete = "DELETE FROM cackhoanphi WHERE maPhi = %s"
          val = (maPhi,)
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
     def insertPhi(self,dd:CacKhoanPhi):
          sqlInsert ="INSERT INTO cackhoanphi (maPhi, tenPhi,soTien) VALUES (%s, %s,%s)"
          idPhi = self.CheckgetID()  # generate new unique ID
          val = (idPhi, dd.tenPhi,dd.soTien)
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