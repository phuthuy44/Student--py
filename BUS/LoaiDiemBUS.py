import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DAO.LoaiDiemDAO import LoaiDiemDAO
from DTO.LoaiDiemDTO import LoaiDiemDTO
class LoaiDiemBUS:
     def __init__(self):
          pass
     def getListLoaiDiem(self):
          loai = LoaiDiemDAO()
          return loai.getlistDanhSach()
     def CheckgetID(self):
          return LoaiDiemDAO.CheckgetID(self)
     def ChecktenTonTai(self,ten):
          return LoaiDiemDAO.CheckTenTonTai(ten)
     def update(self,dd : LoaiDiemDTO):
          return LoaiDiemDAO.update(dd)
     def delete(self,ma):
          return LoaiDiemDAO.delete(ma)
     def insert(self,dd: LoaiDiemDTO):
          return LoaiDiemDAO.insertMon(self,dd)

loaidiem = LoaiDiemBUS()
loaidiem.getListLoaiDiem()