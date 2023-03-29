class KetQuaCTDTO:
     def __init__(self,id,idMonHoc,diemKT1,diemKT2,diemGK,diemCuoiKy):
          self.id = id
          self.idMonHoc = idMonHoc
          self.diemKT1 = diemKT1
          self.diemKT2 = diemKT2
          self.diemGK = diemGK
          self.diemCuoiKy = diemCuoiKy
     def getID(self):
          return self.id
     def getIdMonHoc(self):
          return self.idMonHoc
     def setDiemKT1(self, diemKT1):
          self.diemKT1 = diemKT1
     def getDiemKT1(self):
          return self.diemKT1
     def setDiemKT2(self, diemKT2):
          self.diemKT2 = diemKT2
     def getDiemKT2(self):
          return self.diemKT2
     def setDiemGK(self, diemGK):
          self.diemGK = diemGK
     def getDiemGK(self):
          return self.diemGK
     def setDiemCuoiKy(self, diemCuoiKy):
          self.diemCuoiKy = diemCuoiKy
     def getDiemCuoiKy(self):
          return self.diemCuoiKy