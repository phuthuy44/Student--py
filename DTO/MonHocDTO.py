class MonHocDTO:
     def __init__(self,idMH,tenMH,soTiet):
          self.idMH = idMH
          self.tenMH = tenMH
          self.soTiet = soTiet
     def getIdMH(self):
          return self.idMH
     def setSoTiet(self,soTiet):
          self.soTiet = soTiet
     def getSoTiet(self):
          return self.soTiet
     def setTenMH(self,tenMH):
          self.tenMH = tenMH
     def getTenMH(self):
          return self.tenMH