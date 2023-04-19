import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.NamHocDAO import NamHocDAO
from DTO.NamHocDTO import NamHocDTO
class NamHocBUS:
     def __init__(self):
        pass
     def getlistNH(self):
         namhoc = NamHocDAO()
         return namhoc.getlist()
     def insert(self,dd:NamHocDTO):
         return NamHocDAO.insert(self,dd)
     def update(self,dd:NamHocDTO):
         return NamHocDAO.update(dd)
     def CheckgetID(self):
         return NamHocDAO.CheckgetID(self)
     def Checkten(self, ten):
         return NamHocDAO.CheckTenTonTai(ten)
     def delete(self,ma):
         return NamHocDAO.delete(ma)
     def find(self,key):
          return NamHocDAO.find(self,key)
     def findSortASCMa(self,order):
          print("order:", order)
          return NamHocDAO.findSortASCMa(self,order=order)
     def findSortASCTen(self,order):
          print("order:", order)
          return NamHocDAO.findSortASCTen(self,order=order)
NH = NamHocBUS()
NH.getlistNH()