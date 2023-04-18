import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.HocLucDTO import HocLucDTO
class HocLucDAO:
     def __init__(self):
          pass
     def getlistdanhsach(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sql = "SELECT *FROM hocluc"
               query.execute(sql)
               rows = query.fetchall()
               for row in rows:
                    phi= (row[0],row[1],row[2],row[3],row[4])
                    list.append(phi)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def CheckgetID(self):
          sqlGetMa = "SELECT CONCAT('HL', LPAD(COALESCE(MAX(SUBSTR(maHocLuc, 3)), 0) + 1, 3, '0')) FROM hocluc"
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
          sqlCheck = "SELECT * FROM hocluc WHERE tenHocLuc = %s"
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
     def update(dd: HocLucDTO):
          sqlCapNhat = "UPDATE hocluc SET tenHocLuc= %s,diemCanDuoi = %s, diemCanTren = %s, diemKhongChe =%s WHERE maHocLuc=%s"
          data = (dd.tenHL,dd.diemCanDuoi,dd.diemCanTren,dd.diemKhongChe,dd.maHL)
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
          sqlDelete = "DELETE FROM hocluc WHERE maHocLuc= %s"
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
     def insert(self,dd:HocLucDTO):
          sqlInsert ="INSERT INTO hocluc (maHocLuc, tenHocLuc,diemCanDuoi,diemCanTren,diemKhongChe) VALUES (%s, %s,%s,%s,%s)"
          id = self.CheckgetID()  # generate new unique ID
          val = (id,dd.tenHL, dd.diemCanDuoi, dd.diemCanTren, dd.diemKhongChe)
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