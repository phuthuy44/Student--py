import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.HocKyDAO import HocKyDAO
from DTO.HocKyDTO import HocKyDTO
class HocKyBUS:
     def __init__(self):
          pass
     def getlistHocKy(self):
          hk = HocKyDAO()
          return hk.getlist()
     def insert(self,dd: HocKyDTO):
          return HocKyDAO.insert(self,dd)
     def update(self,dd: HocKyDTO):
          return HocKyDAO.update(dd)
     def delete(self,ma):
          return HocKyDAO.delete(ma)
     def Checkten(self, ten):
         return HocKyDAO.CheckTenTonTai(ten)
     def CheckgetID(self):
         return HocKyDAO.CheckgetID(self)
     def getma(self,ten):
          return HocKyDAO.getMa(ten)

hk = HocKyBUS()
hk.getlistHocKy()
