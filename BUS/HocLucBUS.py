import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.HocLucDAO import HocLucDAO
from DTO.HocLucDTO import HocLucDTO
class HocLucBUS():
     def __init__(self):
        pass
     def getlistHocLuc(self):
         hl = HocLucDAO()
         return hl.getlistdanhsach()
     def insert(self,dd: HocLucDTO):
         return HocLucDAO.insert(self,dd)
     def update(self,dd: HocLucDTO):
         return HocLucDAO.update(dd)
     def delete(self,ma):
         return HocLucDAO.delete(ma)
     def CheckgetID(self):
         return HocLucDAO.CheckgetID(self)
     def Checkten(self,ten):
         return HocLucDAO.CheckTenTonTai(ten)
     
hl = HocLucBUS()
hl.getlistHocLuc()