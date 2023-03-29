class KetQuaDTO:
     def __init__(self,id,idHocSinh,idLopHoc,hocKy,namHoc,diemTB):
          self.id = id
          self.idHocSinh = idHocSinh
          self.idLopHoc = idLopHoc
          self.hocKy = hocKy
          self.namHoc = namHoc
          self.diemTB = diemTB
     def getId(self):
          return self.id
     def getIdLopHoc(self):
          return self.idLopHoc
     def setHocKy(self, hocKy):
          self.hocKy = hocKy
     def getHocKy(self):
          return self.hocKy
     def setNamHoc(self, namHoc):
          self.namHoc = namHoc
     def getNamHoc(self):
          return self.namHoc
     def setDiemTB( self, diemTB):
          self.diemTB = diemTB
     def getDiemTB(self):
          return self.diemTB;