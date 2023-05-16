import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.PhieuThanhToanCTDTO import PhieuThanhToanCTDTO
class PhieuThanhToanCTDAO:
     def __init__(self):
          pass
     def insertPhieuTTCT(self,dd:PhieuThanhToanCTDTO):
          sqlInsert ="INSERT INTO ctphieuthanhtoan(maPhieu, maPhi) VALUES (%s,%s)"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.maPhieu,dd.maPhi)
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
     