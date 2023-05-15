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
     def getListDiem_MonHoc(self,hocky,lop,namhoc,monhoc):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT hocsinh.maHocSinh, hocsinh.tenHocSinh, hocsinh.ngaySinh,hocsinh.gioitinh, kq_hocsinh_monhoc.diemMieng,kq_hocsinh_monhoc.diem15phut,kq_hocsinh_monhoc.diem45phut,kq_hocsinh_monhoc.diemThi,kq_hocsinh_monhoc.diemTBHK FROM hocsinh, kq_hocsinh_monhoc,lop,phanlop,namhoc,hocky,monhoc WHERE hocsinh.maHocSinh = kq_hocsinh_monhoc.maHocSinh AND namhoc.maNamHoc = kq_hocsinh_monhoc.maNamHoc and phanlop.maNamHoc = namhoc.maNamHoc AND phanlop.maLop = lop.maLop and LOP.maNamHoc = namhoc.maNamHoc and hocsinh.maHocSinh = phanlop.maHocSinh and hocky.maHocKy = kq_hocsinh_monhoc.maHocKy and kq_hocsinh_monhoc.maNamHoc = namhoc.maNamHoc and monhoc.maMonHoc = kq_hocsinh_monhoc.maMonHoc and hocky.tenHocKy=%s AND lop.tenLop =%s and namhoc.tenNamHoc =%s and monhoc.tenMonHoc=%s"
               val = (hocky,lop,namhoc,monhoc)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list