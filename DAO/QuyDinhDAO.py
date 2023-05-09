import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.QuyDinhDTO import QuyDinhDTO
class QuyDinhDAO:
     def __init__(self):
          pass
     def get(self):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sql = "SELECT MAX(tuoiCanDuoi),MAX(tuoiCanTren),MAX(siSoCanDuoi),MAX(siSoCanTren),MAX(diemDat) FROM quydinh"
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
     def insert(self,dd:QuyDinhDTO):
          sqlInsert ="INSERT INTO quydinh (tuoiCanDuoi, tuoiCanTren,siSoCanDuoi,siSoCanTren,diemDat) VALUES (%s, %s,%s,%s,%s)"
          val = (dd.tuoiCD,dd.tuoiCT,dd.siSoCD,dd.siSOCT,dd.diemDat)
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
     def updateDiem(self,dd:QuyDinhDTO):
          sqlInsert ="UPDATE quydinh SET tuoiCanDuoi = %s, tuoiCanTren =%s,siSoCanDuoi =%s,siSoCanTren=%s,diemDat=%s"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.tuoiCD,dd.tuoiCT,dd.siSoCD,dd.siSOCT,dd.diemDat)
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
     def checkExist(dd:QuyDinhDTO):
          sqlCheckExist = "SELECT COUNT(*) FROM quydinh"
          #val = ()
          try:
               mydb = mysql.connector.connect(
               host ="localhost",
            user ="root",
            password ="",
            database ="studentmanager"
        )
               query = mydb.cursor()
               query.execute(sqlCheckExist)
               count = query.fetchone()[0]
               if count > 0:
                    return True
               else:     
                    return False
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally:
               query.close()
               mydb.close()