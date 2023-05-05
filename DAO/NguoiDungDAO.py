import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.NguoiDungDTO import NguoiDungDTO
class NguoiDungDAO:
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
               sqlChucVu  = "SELECT chucvu.tenChucVu, nguoidung.tenDangNhap,nguoidung.tenNguoiDung,nguoidung.matKhau FROM chucvu,nguoidung WHERE chucvu.maChucVu = nguoidung.maChucVu"
               query.execute(sqlChucVu)
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
     def getListTenDangNhap(self,tenChucVu):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT DISTINCT tenGiaoVien FROM GiaoVien WHERE giaovien.maChucVu = (SELECT chucvu.MaChucVu FROM ChucVu WHERE TenChucVu = %s)AND giaovien.maGiaoVien NOT IN (SELECT nguoidung.tenDangNhap FROM nguoidung) UNION ALL SELECT DISTINCT nhanvien.tenNhanVien FROM nhanvien WHERE nhanvien.maChucVu = (SELECT chucvu.maChucVu FROM chucvu WHERE chucvu.tenChucVu = %s) AND nhanvien.maNhanVien NOT IN (SELECT nguoidung.tenDangNhap FROM nguoidung)"
               val = (tenChucVu,tenChucVu)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     def getMa(self,ten):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT giaovien.maGiaoVien FROM giaovien WHERE giaovien.tenGiaoVien = %s UNION ALL SELECT nhanvien.maNhanVien FROM nhanvien WHERE nhanvien.tenNhanVien =%s"
               val = (ten,ten)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list
     