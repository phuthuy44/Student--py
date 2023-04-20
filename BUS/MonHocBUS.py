import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector
from DAO.MonHocDAO import MonHocDAO
from DTO.MonHocDTO import MonHocDTO
class MonHocBUS:
     def __init__(self):
          pass
     def getListMonHoc(self):
          mon = MonHocDAO()
          return mon.getlistDanhSach()
     def CheckgetID(self):
          return MonHocDAO.CheckgetID(self)
     def CheckTenMonHoc(self,tenmon):
          return MonHocDAO.CheckTenTonTai(tenmon)
     def updateMon(self,dd:MonHocDTO):
          return MonHocDAO.updateMon(dd)
     def findMon(self,key):
          return MonHocDAO.find(key)
     def deleteMon(self,maMon):
          return MonHocDAO.deleteMon(maMon)
     def inser(self,dd:MonHocDTO):
          return MonHocDAO.insertMon(self,dd)
     def find(self,key):
          return MonHocDAO.find(self,key)
     def findASC(self,order):
          print("order:", order)
          return MonHocDAO.findSortASC(self,order=order)
     def findHeSo(self,order):
          return MonHocDAO.findHeSo(self,order = order)
     def findSoTiet(self,order):
          return MonHocDAO.findSoTiet(self,order = order)
     def getMamon(self,ma):
          return MonHocDAO.getMaMon(ma)
monhoc = MonHocBUS()
monhoc.getListMonHoc()