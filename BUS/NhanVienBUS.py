import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.NhanVienDAO import NhanVienDAO
from DTO.NhanVienDTO import NhanVienDTO
class NhanVienBUS:
     def __init__(self):
          pass
     def CheckgetID(self):
         return NhanVienDAO.CheckgetID(self)
     def Checkten(self, ten):
          return NhanVienDAO.CheckTenTonTai(ten)
     def CheckSDT(self, sdt):
          return NhanVienDAO.CheckSoDT(sdt)
     def getlistNV(self):
          nv = NhanVienDAO()
          return nv.getlistNV()
     def insert(self,dd:NhanVienDTO):
          return NhanVienDAO.insert(self,dd)
     def update(self,dd:NhanVienDTO):
          return NhanVienDAO.update(dd)
     def delete(self,ma):
          return NhanVienDAO.delete(ma)
     def findSortNV(self,order):
          return NhanVienDAO.findSortASC(self,order=order)
     def findSortGT(self,order):
          return NhanVienDAO.findGioiTinh(self,order=order)
     
      