import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.CacKhoanPhiDAO import CacKhoanPhiDAO
from DTO.CacKhoanPhi import CacKhoanPhi
class CacKhoanPhiBUS:
     def __init__(self):
          pass
     def getListPhi(self):
          list = CacKhoanPhiDAO()
          return list.getlistDanhSach()
     def updateListPhi(self,dd:CacKhoanPhi):
          return CacKhoanPhiDAO.updatePhi(dd)
     def deletePhi(self,maPhi):
          return CacKhoanPhiDAO.deletePhi(maPhi)
     def insertPhi(self,dd:CacKhoanPhi):
          return CacKhoanPhiDAO.insertPhi(self,dd)
     def checkPhiTonTai(self,tenPhi):
          return CacKhoanPhiDAO.CheckTenTonTai(tenPhi)
     def CheckgetID(self):
          return CacKhoanPhiDAO.CheckgetID(self)
     def find(self,key):
          return CacKhoanPhiDAO.find(self,key)
          

phi = CacKhoanPhiBUS()
phi.getListPhi()