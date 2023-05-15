import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.DiemTBMonHocDAO import DiemTBMonHocDAO
from DTO.KQMHDTO import KQMHDTO
class DiemTBMonHocBUS:
      def __init__(self):
        pass
      def insertDiem(self, KQMHDTO):
        # Kiểm tra xem bản ghi đã tồn tại trong cơ sở dữ liệu hay chưa
          if DiemTBMonHocDAO.checkExist(KQMHDTO):
            # Nếu bản ghi đã tồn tại, cập nhật bản ghi đó
               return DiemTBMonHocDAO.updateDiem(self,KQMHDTO)
          else:
            # Nếu bản ghi chưa tồn tại, thêm bản ghi mới vào cơ sở dữ liệu
               return DiemTBMonHocDAO.insertDiem(self,KQMHDTO)
      def getListDiem_MonHoc(self,hocky,lop,namhoc,monhoc):
          return DiemTBMonHocDAO.getListDiem_MonHoc(self,hocky,lop,namhoc,monhoc)