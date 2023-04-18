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
     def insert(self,dd:QuyDinhDTO):
          return QuyDinhDAO.insert(self,dd)

qd = QuyDinhBUS()
qd.get()