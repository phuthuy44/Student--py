import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.DiemDAO import DiemDAO
from DTO.DiemDTO import DiemDTO
class DiemBUS:
     def __init__(self):
          pass
     def getHsDiem(self,monhoc,hocky,lophoc):
          return DiemDAO.getList(self,monhoc,hocky,lophoc)
     def getLopDiem(self,namhoc):
          return DiemDAO.getLop(self,namhoc)
     #def insertDiem(self,dd:DiemDTO):
          #return DiemDAO.insertDiem(self,dd)
     def insertDiem(self, diemDTO):
        # Kiểm tra xem bản ghi đã tồn tại trong cơ sở dữ liệu hay chưa
          if DiemDAO.checkExist(diemDTO):
            # Nếu bản ghi đã tồn tại, cập nhật bản ghi đó
               return DiemDAO.updateDiem(self,diemDTO)
          else:
            # Nếu bản ghi chưa tồn tại, thêm bản ghi mới vào cơ sở dữ liệu
               return DiemDAO.insertDiem(self,diemDTO)
     def getListHSDiem(self,hocky,lop,tenHS):
          return DiemDAO.getlistDiemHS(self,hocky,lop,tenHS)