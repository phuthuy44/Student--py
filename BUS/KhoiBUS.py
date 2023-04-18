import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.KhoiDAO import KhoiDAO
from DTO.KhoiDTO import KhoiDTO
class KhoiBUS:
     def __init__(self):
          pass
     def getKhoi(self):
          khoi = KhoiDAO()
          return khoi.getlistKhoi()
     def insert(self,dd:KhoiDTO):
          return KhoiDAO.insert(self,dd)
     def update(self,dd:KhoiDTO):
          return KhoiDAO.update(dd)
     def delete(self,ma):
          return KhoiDAO.delete(ma)
     def CheckgetID(self):
         return KhoiDAO.CheckgetID(self)
     def Checkten(self, ten):
         return KhoiDAO.CheckTenTonTai(ten)
khoi = KhoiBUS()
khoi.getKhoi()