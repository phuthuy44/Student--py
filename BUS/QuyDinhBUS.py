import sys
import os 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.QuyDinhDAO import QuyDinhDAO
from DTO.QuyDinhDTO import QuyDinhDTO
class QuyDinhBUS:
     def __init__(self):
          pass
     def get(self):
          qd = QuyDinhDAO()
          return qd.get()
     
     '''def insert(self,dd:QuyDinhDTO):
          return QuyDinhDAO.insert(self,dd)'''
     def insert(self, QuyDinhDTO):
        # Kiểm tra xem bản ghi đã tồn tại trong cơ sở dữ liệu hay chưa
          if QuyDinhDAO.checkExist(QuyDinhDTO):
            # Nếu bản ghi đã tồn tại, cập nhật bản ghi đó
               return QuyDinhDAO.updateDiem(self,QuyDinhDTO)
          else:
            # Nếu bản ghi chưa tồn tại, thêm bản ghi mới vào cơ sở dữ liệu
               return QuyDinhDAO.insert(self,QuyDinhDTO)

qd = QuyDinhBUS()
qd.get()