import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.PhanCongDAO import PhanCongDAO
from DTO.PhanCongDTO import PhanCongDTO
class PhanCongBUS:
     def __init__(self):
          pass
     def getlist(self):
          PhanCong = PhanCongDAO()
          return PhanCong.getlist()
     def getLop(self,year):
          return PhanCongDAO.getLop(self,year)
     def getMon(self,year):
          return PhanCongDAO.getMonHoc(self,year)
     def getGiaoVien(self,mon):
          return PhanCongDAO.getGiaoVien(self,mon)
     def insert(self,dd:PhanCongDTO):
          return PhanCongDAO.insert(self,dd)
     def delete(self,ma,lop):
          return PhanCongDAO.delete(ma,lop)
     def getlistGV(self,lop):
          return PhanCongDAO.getlistGV(self,lop)