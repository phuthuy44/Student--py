import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DTO.PhieuThanhToanDTO import PhieuThanhToanDTO
from DAO.PhieuThanhToanDAO import PhieuThanhToanDAO
from DAO.PhieuThanhToanCTDAO import PhieuThanhToanCTDAO
from DTO.PhieuThanhToanCTDTO import PhieuThanhToanCTDTO
class PhieuThanhToanBUS:
     def __init__(self):
          pass
     def insertPhieuThanhToan(self,dd:PhieuThanhToanDTO):
          return PhieuThanhToanDAO.insertPhieuThanhToan(self,dd)
     def insertPhieuTTCT(self,dd:PhieuThanhToanCTDTO):
          return PhieuThanhToanCTDAO.insertPhieuTTCT(self,dd)
     def CheckgetID(self):
         return PhieuThanhToanDAO.CheckgetID(self)
     def getNhanVien(self):
          return PhieuThanhToanDAO.getnhanvien(self)
     def getHocSinh(self,year,lop):
          return PhieuThanhToanDAO.getHocSinh(self,year,lop)
     def getlistPhieu(self):
          return PhieuThanhToanDAO.getlistPhieu(self)
     def getlistPhi(self,phieu):
          return PhieuThanhToanDAO.getlistPhi(self,phieu)