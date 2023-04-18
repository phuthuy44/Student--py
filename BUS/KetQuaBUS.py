import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DAO.KetQuaDAO import KetQuaDAO
from DTO.KetQuaDTO import KetQuaDTO
class KetQuaBUS :
     def __init__(self):
        pass
     def getlistKetQua(self):
         kq = KetQuaDAO()
         return kq.getlistdanhsach()
     def inser(self,dd:KetQuaDTO):
         return KetQuaDAO.insert(self,dd)
     def update(self,dd:KetQuaDTO):
         return KetQuaDAO.update(dd)
     def CheckgetID(self):
         return KetQuaDAO.CheckgetID(self)
     def Checkten(self, ten):
         return KetQuaDAO.CheckTenTonTai(ten)
     def delete(self,ma):
         return KetQuaDAO.delete(ma)
         
ketqua = KetQuaBUS()
ketqua.getlistKetQua()