import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.KetQuaLopHocMonHocDTO import KetQuaLopHocMonHocDTO
class KetQuaLopHocMonHocDAO:
     def __init__(self):
          pass
     def LuuDiem(self,dd:KetQuaLopHocMonHocDTO):
          sqlInsert ="INSERT INTO kq_lophoc_monhoc(maLop, maNamHoc, maMonHoc, maHocKy,soLuongDat) VALUES (%s, %s,%s,%s,%s)"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.maLop,dd.maNamHoc,dd.maMonHoc,dd.maHocKy,dd.soLuongDat)
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
     def checkExist(dd:KetQuaLopHocMonHocDTO):
          sqlCheckExist = "SELECT COUNT(*) FROM kq_lophoc_monhoc WHERE maLop = %s AND maNamHoc= %s AND maMonHoc = %s AND maHocKy = %s"
          val = (dd.maLop,dd.maNamHoc,dd.maMonHoc,dd.maHocKy)
          try:
               mydb = mysql.connector.connect(
               host ="localhost",
            user ="root",
            password ="",
            database ="studentmanager"
        )
               query = mydb.cursor()
               query.execute(sqlCheckExist, val)
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
     def updateDiem(self,dd:KetQuaLopHocMonHocDTO):
          sqlInsert ="UPDATE kq_lophoc_monhoc SET soLuongDat = %s WHERE maLop = %s AND maNamHoc = %s AND maMonHoc= %s AND maHocKy = %s"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.soLuongDat,dd.maLop,dd.maNamHoc,dd.maMonHoc,dd.maHocKy)
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