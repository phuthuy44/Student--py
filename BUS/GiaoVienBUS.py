import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.GiaoVienDAO import GiaoVienDAO
from DTO.GiaoVienDTO import GiaoVienDTO
class GiaoVienBUS:
     def __init__(self):
          pass
     def getlistGV(self):
          gv = GiaoVienDAO()
          return gv.getlistGV()
     def CheckgetID(self):
         return GiaoVienDAO.CheckgetID(self)
     def Checkten(self, ten):
         return GiaoVienDAO.CheckTenTonTai(ten)
     def ChecksoDT(self,so):
          return GiaoVienDAO.CheckSoDT(so)
     def insert(self,dd:GiaoVienDTO):
          return GiaoVienDAO.insert(self,dd)
     def update(self,dd:GiaoVienDTO):
          return GiaoVienDAO.update(dd)
     def delete(self,ma):
          return GiaoVienDAO.delete(ma)
     def findsort(self,order):
          return GiaoVienDAO.findSortASC(self,order=order)
     def findGT(self,order):
          return GiaoVienDAO.findGioiTinh(self,order=order)
     def get_giaovien(self,year):
          return GiaoVienDAO.get_teachers_not_incharge(self,year)
     def getma(self,ten):
          return GiaoVienDAO.getma(ten)

gv = GiaoVienBUS()
gv.getlistGV()