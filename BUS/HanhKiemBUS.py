import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.HanhKiemDAO import HanhKiemDAO
from DTO.HanhKiemDTO import HanhKiemDTO
class HanhKiemBUS:
     def __init__(self):
          pass
     def getlistHK(self):
          hk = HanhKiemDAO()
          return hk.getlistdanhsach()
     def inser(self,dd:HanhKiemDTO):
          return HanhKiemDAO.insert(self,dd)
     def update(self,dd:HanhKiemDTO):
          return HanhKiemDAO.update(dd)
     def delete(self,ma):
          return HanhKiemDAO.delete(ma)
     def CheckgetID(self):
          return HanhKiemDAO.CheckgetID(self)
     def Checkten(self,ten):
          return HanhKiemDAO.CheckTenTonTai(ten)
hk = HanhKiemBUS()
hk.getlistHK()