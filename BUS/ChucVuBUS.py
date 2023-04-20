import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.ChucVuDAO import ChucVuDAO
from DTO.ChucVuDTO import ChucVuDTO

class ChucVuBUS:
     def __init__(self):
          pass
     def getListCV(self):
          listCV = ChucVuDAO()
          return listCV.getlistDanhSach()
     def updateChucVu(self,dd:ChucVuDTO):
          return ChucVuDAO.updateChucVu(dd)
     def deleteChucVu(self,maChucVu):
          return ChucVuDAO.deleteChucVu(maChucVu)
     def addChucVu(self,dd:ChucVuDTO):
          return ChucVuDAO.insertChucVu(self,dd)
     def checkChucVuTonTai(self,tenchucvu):
          return ChucVuDAO.CheckChucVuTonTai(tenchucvu)
     def checkidChucVu(self):
          return ChucVuDAO.CheckgetID(self)
     def CheckgetID(self):
          return ChucVuDAO.CheckgetID(self)
     def find(self,key):
          return ChucVuDAO.find(self,key)
     def findSortASC(self,order):
          print("order:", order)
          return ChucVuDAO.findSortASC(self,order=order)
     def getmaMon(self,mamon):
          return ChucVuDAO.getMaMon(mamon)

chucvu = ChucVuBUS()
chucvu.getListCV()