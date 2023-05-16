import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.PhanLopDAO import PhanLopDAO
from DTO.PhanLopDTO import PhanLopDTO
class PhanLopBUS:
     def __init__(self):
          pass
     def getlist(self):
          phanlop = PhanLopDAO()
          return phanlop.getlist()
     def getKhoi(self,year):
          return PhanLopDAO.getKhoi(self,year)
     def getLop(self,khoi,namhoc):
          return PhanLopDAO.getLop(self,khoi,namhoc)
     def getHocSinh(self,year):
          return PhanLopDAO.getHocSinh(self,year)
     def insert(self,dd:PhanLopDTO):
          return PhanLopDAO.insert(self,dd)
     def delete(self,ma,namhoc):
          return PhanLopDAO.delete(ma,namhoc)
     def getlisths(self,lop,namhoc):
          return PhanLopDAO.getlistHS(self,lop,namhoc)
     