import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.HocSinhDAO import HocSinhDAO
from DTO.HocSinhDTO import HocSinhDTO
class HocSinhBUS:
     def __init__(self):
          pass
     def getlistHS(self):
          hs = HocSinhDAO()
          return hs.getlistHS()
     def CheckgetID(self):
         return HocSinhDAO.CheckgetID(self)
     def Checkten(self, ten):
         return HocSinhDAO.CheckTenTonTai(ten)
     def insert(self,dd:HocSinhDTO):
          return HocSinhDAO.insert(self,dd)
     def update(self,dd:HocSinhDAO):
          return HocSinhDAO.update(dd)
     def delete(self,ma):
          return HocSinhDAO.delete(ma)
     def findsort(self,order):
          return HocSinhDAO.findSortASC(self,order=order)
     def findGT(self,order):
          return HocSinhDAO.findGioiTinh(self,order=order)
     def find(self,key):
          return HocSinhDAO.find(self,key)
     def getma(self,ma):
          return HocSinhDAO.getma(ma)
     def getTenHS(self,lop):
          return HocSinhDAO.getListTenHS(self,lop)
     
hs = HocSinhBUS()
hs.getlistHS()