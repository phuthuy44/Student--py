import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.KQMHDTO import KQMHDTO
class DiemTBMonHocDAO:
     def __init__(self):
         pass
     def checkExist(dd:KQMHDTO):
          sqlCheckExist = "SELECT COUNT(*) FROM kq_hocsinh_monhoc WHERE MaHocSinh = %s AND maLop =%s AND MaNamHoc = %s AND MaMonHoc = %s AND MaHocKy = %s "
          val = (dd.maHocSinh,dd.maLop,dd.maNamHoc,dd.maMonHoc,dd.maHocKy)
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
     def insertDiem(self,dd:KQMHDTO):
          sqlInsert ="INSERT INTO kq_hocsinh_monhoc(maHocSinh,maLop,maNamHoc,maMonHoc, maHocKy,diemMieng,diem15phut,diem45phut,diemThi,diemTBHK) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
          val = (dd.maHocSinh,dd.maLop,dd.maNamHoc,dd.maMonHoc,dd.maHocKy,dd.diemMieng,dd.diem15phut,dd.diem45phut,dd.diemThi,dd.diemTBHK)
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
     def updateDiem(self,dd:KQMHDTO):
          sqlInsert ="UPDATE kq_hocsinh_monhoc SET diemMieng = %s ,diem15phut= %s,diem45phut=%s,diemThi= %s,diemTBHK= %s WHERE MaHocSinh = %s AND maLop =%s AND MaNamHoc = %s AND MaMonHoc = %s AND MaHocKy = %s "
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.diemMieng,dd.diem15phut,dd.diem45phut,dd.diemThi,dd.diemTBHK,dd.maHocSinh,dd.maLop,dd.maNamHoc,dd.maMonHoc,dd.maHocKy)
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