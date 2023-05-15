import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
class BaoCaoDAO :
     def __init__(self):
          pass
     def getListMonHocLop(self,lop,hocky,namhoc):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT monhoc.tenMonHoc,phanlop_count.count,COUNT(CASE WHEN diem.diemTBHK >= quydinh.diemDat THEN 1 ELSE NULL END), CONCAT(FORMAT((COUNT(CASE WHEN diem.diemTBHK >= quydinh.diemDat THEN 1 ELSE NULL END) * 100.0 / phanlop_count.count), 1), '%') FROM lop INNER JOIN namhoc ON namhoc.maNamHoc = lop.maNamHoc INNER JOIN phanlop ON phanlop.maLop = lop.maLop AND phanlop.maNamHoc = namhoc.maNamHoc INNER JOIN hocsinh ON hocsinh.maHocSinh = phanlop.maHocSinh LEFT JOIN kq_hocsinh_monhoc diem ON diem.maNamHoc = namhoc.maNamHoc AND diem.maLop = lop.maLop AND diem.maHocSinh = hocsinh.maHocSinh INNER JOIN hocky ON hocky.maHocKy = diem.maHocKy INNER JOIN monhoc ON diem.maMonHoc = monhoc.maMonHoc INNER JOIN quydinh INNER JOIN (SELECT COUNT(phanlop.maHocSinh) AS count FROM phanlop, hocsinh, lop, namhoc  WHERE phanlop.maNamHoc = namhoc.maNamHoc AND phanlop.maLop = lop.maLop AND phanlop.maHocSinh = hocsinh.maHocSinh AND lop.maNamHoc = namhoc.maNamHoc AND lop.tenLop = %s AND namhoc.tenNamHoc = %s AND phanlop.maHocSinh IS NOT NULL) AS phanlop_count ON lop.tenLop = %s AND hocky.tenHocKy = %s AND namhoc.tenNamHoc = %s GROUP BY monhoc.tenMonHoc;"
               val = (lop,namhoc,lop,hocky,namhoc)
               query.execute(sqlChucVu,val)
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
     def getListHocKyLop(self,lop,hocky,namhoc):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT hocky.tenHocKy,lop.tenLop,COUNT(CASE WHEN d.diemTBHK >= quydinh.diemDat THEN 1 ELSE NULL END), CONCAT(FORMAT((COUNT(CASE WHEN d.diemTBHK >= quydinh.diemDat THEN 1 ELSE NULL END) * 100.0 / phanlop_count.count), 1), '%')FROM lop INNER JOIN namhoc ON namhoc.maNamHoc = lop.maNamHoc INNER JOIN phanlop ON phanlop.maLop = lop.maLop AND phanlop.maNamHoc = namhoc.maNamHoc INNER JOIN hocsinh ON hocsinh.maHocSinh = phanlop.maHocSinh LEFT JOIN kq_hocsinh_monhoc d ON d.maNamHoc = namhoc.maNamHoc AND d.maLop = lop.maLop AND d.maHocSinh = hocsinh.maHocSinh INNER JOIN hocky ON hocky.maHocKy = d.maHocKy INNER JOIN quydinh ON quydinh.diemDat <= d.diemTBHK INNER JOIN(SELECT COUNT(phanlop.maHocSinh) AS count FROM phanlop, hocsinh, lop, namhoc WHERE phanlop.maNamHoc = namhoc.maNamHoc AND phanlop.maLop = lop.maLop AND phanlop.maHocSinh = hocsinh.maHocSinh AND lop.maNamHoc = namhoc.maNamHoc AND lop.tenLop = %s AND namhoc.tenNamHoc = %s AND phanlop.maHocSinh IS NOT NULL) AS phanlop_count ON lop.tenLop = %s AND hocky.tenHocKy = %s AND namhoc.tenNamHoc = %s GROUP BY hocky.tenHocKy;"
               val = (lop,namhoc,lop,hocky,namhoc)
               query.execute(sqlChucVu,val)
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