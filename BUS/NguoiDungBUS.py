import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DTO.NguoiDungDTO import NguoiDungDTO
from DAO.NguoiDungDAO import NguoiDungDAO
class NguoiDungBUS:
     def __init__(self):
          pass
     def getList(self):
          nguoidung = NguoiDungDAO()
          return nguoidung.getlist()
     def getTenDN(self,tenChucVu):
          return NguoiDungDAO.getListTenDangNhap(self,tenChucVu)
     def getMa(self,ma):
          return NguoiDungDAO.getMa(self,ma)
     def insert(self,dd:NguoiDungDTO):
          return NguoiDungDAO.insert(self,dd)
     def update(self,dd:NguoiDungDTO):
          return NguoiDungDAO.update(self,dd)
     def delete(self,ma):
          return NguoiDungDAO.delete(ma)