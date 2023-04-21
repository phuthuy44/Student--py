import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.LopHocDAO import LopHocDAO
from DTO.LopHocDTO import LopHocDTO
class LopHocBUS:
     def __init__(self):
          pass
     def getListLH(self):
          lh = LopHocDAO()
          return lh.getlistLH()
     def insert(self,dd: LopHocDTO):
          return LopHocDAO.insert(self,dd)
     def update(self,dd:LopHocDAO):
          return LopHocDAO.update(dd)
     def delete(self,ma):
          return LopHocDAO.delete(ma)
     def CheckgetID(self):
         return LopHocDAO.CheckgetID(self)
     def Checkten(self, tennam,tenlop):
         return LopHocDAO.CheckTenTonTai(tennam,tenlop)
     def CheckGV(self,nam):
          return LopHocDAO.CheckGV(self,nam)
     def findLH(self,key):
          return LopHocDAO.find(self,key)
     def findSortMa(self,order):
          return LopHocDAO.findSortASC(self,order=order)
     def findSortTen(self,order):
          return LopHocDAO.findTenLop(self,order=order)
     