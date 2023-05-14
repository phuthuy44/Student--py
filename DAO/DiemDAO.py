import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DTO.DiemDTO import DiemDTO
class DiemDAO:
     def __init__(self) -> None:
          pass
     def getList(self,monhoc,hocky,namhoc,tenlop):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT hs.MaHocSinh,hs.TenHocSinh, IFNULL(dm.Diem, 0) , IFNULL(d15p.Diem, 0) ,IFNULL(dgk.Diem, 0),IFNULL(dt.Diem, 0) FROM HocSinh hs LEFT JOIN PhanLop pl ON hs.MaHocSinh = pl.MaHocSinh LEFT JOIN Lop l ON pl.MaLop = l.MaLop LEFT JOIN MonHoc mh ON mh.tenMonHoc = %s LEFT JOIN hocky hk ON hk.tenHocKy = %s LEFT JOIN namhoc nh ON nh.tenNamHoc = %s LEFT JOIN Diem dm ON hs.MaHocSinh = dm.MaHocSinh AND dm.MaMonHoc = mh.maMonHoc AND dm.MaHocKy = hk.maHocKy AND dm.MaLop = l.maLop AND dm.maNamHoc = nh.maNamHoc AND dm.MaLoaiDiem = 'LD003' LEFT JOIN Diem d15p ON hs.MaHocSinh = d15p.MaHocSinh AND d15p.MaMonHoc = mh.maMonHoc AND d15p.MaHocKy = hk.maHocKy AND d15p.MaLop = l.maLop AND d15p.maNamHoc = nh.maNamHoc AND d15p.MaLoaiDiem = 'LD001' LEFT JOIN Diem dgk ON hs.MaHocSinh = dgk.MaHocSinh AND dgk.MaMonHoc =  mh.maMonHoc AND dgk.MaHocKy =  hk.maHocKy AND dgk.MaLop = l.maLop AND dgk.maNamHoc = nh.maNamHoc AND dgk.MaLoaiDiem = 'LD002' LEFT JOIN Diem dt ON hs.MaHocSinh = dt.MaHocSinh AND dt.MaMonHoc = mh.maMonHoc AND dt.MaHocKy = hK.maHocKy AND dt.MaLop = l.maLop AND dt.maNamHoc = nh.maNamHoc AND dt.MaLoaiDiem = 'LD004' WHERE l.TenLop = %s AND l.maNamHoc = nh.maNamHoc ORDER BY hs.MaHocSinh"
               val = (monhoc,hocky,namhoc,tenlop)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list    
     def getLop(self,namhoc):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT TenLop FROM Lop,namhoc WHERE lop.maNamHoc = namhoc.maNamHoc AND namhoc.tenNamHoc = %s ORDER BY TenLop ASC"
               val = (namhoc,)
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
     def insertDiem(self,dd:DiemDTO):
          sqlInsert ="INSERT INTO diem(maHocSinh, maMonHoc, maHocKy, maNamHoc, maLop, maLoaiDiem, Diem) VALUES (%s, %s,%s,%s,%s,%s,%s)"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.maHocSinh,dd.maMonHocSinh,dd.maHocKy,dd.maNamHoc,dd.maLop,dd.maLoaiDiem,dd.diem)
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
     def updateDiem(self,dd:DiemDTO):
          sqlInsert ="UPDATE Diem SET diem = %s WHERE maHocSinh = %s AND maMonHoc = %s AND maHocKy = %s AND maNamHoc = %s AND maLop = %s AND maLoaiDiem = %s"
          #id = self.CheckgetID()  # generate new unique ID
          val = (dd.diem,dd.maHocSinh,dd.maMonHocSinh,dd.maHocKy,dd.maNamHoc,dd.maLop,dd.maLoaiDiem)
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
     def checkExist(dd:DiemDTO):
          sqlCheckExist = "SELECT COUNT(*) FROM Diem WHERE MaHocSinh = %s AND MaMonHoc = %s AND MaHocKy = %s AND MaNamHoc = %s AND MaLop = %s AND maLoaiDiem = %s"
          val = (dd.maHocSinh,dd.maMonHocSinh,dd.maHocKy,dd.maNamHoc,dd.maLop,dd.maLoaiDiem)
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
     def getlistDiemHS(self,hocky,lop,tenHS):
          list = []
          try : 
               mydb = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="",
                    database ="studentmanager"
               )
               query = mydb.cursor()
               sqlChucVu  = "SELECT hs.MaHocSinh, hs.TenHocSinh, mh.TenMonHoc, IFNULL(dm.Diem, 0), IFNULL(d15p.Diem, 0), IFNULL(dgk.Diem, 0), IFNULL(dt.Diem, 0),(SUM(dm.Diem * ld3.heso) + SUM(d15p.Diem * ld1.heSo) + SUM(dgk.Diem * ld2.heSo) + SUM(dt.Diem * ld4.heSo)) / SUM(ld3.heSo+ ld1.heSo + ld2.heSo + ld4.heSo) FROM HocSinh hs LEFT JOIN PhanLop pl ON hs.MaHocSinh = pl.MaHocSinh LEFT JOIN Lop l ON pl.MaLop = l.MaLop LEFT JOIN MonHoc mh ON TRUE LEFT JOIN HocKy hk ON hk.tenHocKy = %s LEFT JOIN Diem dm ON hs.MaHocSinh = dm.MaHocSinh AND dm.MaMonHoc = mh.MaMonHoc AND dm.MaHocKy = hk.MaHocKy AND dm.MaLop = l.MaLop AND dm.MaLoaiDiem = 'LD003' LEFT JOIN Diem d15p ON hs.MaHocSinh = d15p.MaHocSinh AND d15p.MaMonHoc = mh.MaMonHoc AND d15p.MaHocKy = hk.MaHocKy AND d15p.MaLop = l.MaLop AND d15p.MaLoaiDiem = 'LD001' LEFT JOIN Diem dgk ON hs.MaHocSinh = dgk.MaHocSinh AND dgk.MaMonHoc =  mh.MaMonHoc AND dgk.MaHocKy =  hk.MaHocKy AND dgk.MaLop = l.MaLop AND dgk.MaLoaiDiem = 'LD002' LEFT JOIN Diem dt ON hs.MaHocSinh = dt.MaHocSinh AND dt.MaMonHoc = mh.MaMonHoc AND dt.MaHocKy = hk.MaHocKy AND dt.MaLop = l.MaLop AND dt.MaLoaiDiem = 'LD004' LEFT JOIN LoaiDiem ld1 ON d15p.MaLoaiDiem = ld1.MaLoaiDiem LEFT JOIN LoaiDiem ld2 ON dgk.MaLoaiDiem = ld2.MaLoaiDiem LEFT JOIN LoaiDiem ld3 ON dm.maLoaiDiem = ld3.maLoaiDiem LEFT JOIN LoaiDiem ld4 ON dt.MaLoaiDiem = ld4.MaLoaiDiem WHERE l.TenLop = %s AND hs.TenHocSinh = %s GROUP BY hs.MaHocSinh, mh.MaMonHoc ORDER BY hs.MaHocSinh"
               val = (hocky,lop,tenHS)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    list.append(chucvu)
               print(list)
          except mysql.connector.errors.InternalError as e:
               print("Error executing MySQL query:", e)
          finally : 
               query.close()
               mydb.close()
          return list