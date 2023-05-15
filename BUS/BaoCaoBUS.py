import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.BaoCaoDAO import BaoCaoDAO
from DAO.KetQuaLopHocMonHocDAO import KetQuaLopHocMonHocDAO
from DTO.KetQuaLopHocMonHocDTO import KetQuaLopHocMonHocDTO
class BaoCaoBUS :
    def getListHSDiem(self,lop,hocky,namhoc):
        return BaoCaoDAO.getListMonHocLop(self,lop,hocky,namhoc)
    def getListHocKyLop(self,lop,hocky,namhoc):
        return BaoCaoDAO.getListHocKyLop(self,lop,hocky,namhoc)
    def insertDiem(self, KetQuaLopHocMonHocDTO):
        # Kiểm tra xem bản ghi đã tồn tại trong cơ sở dữ liệu hay chưa
          if KetQuaLopHocMonHocDAO.checkExist(KetQuaLopHocMonHocDTO):
            # Nếu bản ghi đã tồn tại, cập nhật bản ghi đó
               return KetQuaLopHocMonHocDAO.updateDiem(self,KetQuaLopHocMonHocDTO)
          else:
            # Nếu bản ghi chưa tồn tại, thêm bản ghi mới vào cơ sở dữ liệu
               return KetQuaLopHocMonHocDAO.LuuDiem(self,KetQuaLopHocMonHocDTO)
