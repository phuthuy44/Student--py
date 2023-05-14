import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAO.BaoCaoDAO import BaoCaoDAO
class BaoCaoBUS :
    def getListHSDiem(self,lop,hocky,namhoc):
          return BaoCaoDAO.getListMonHocLop(self,lop,hocky,namhoc)