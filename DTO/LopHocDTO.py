class LopHocDTO:
     def __init__(self,idLopHoc,tenLop,maKhoiLop,maNamHoc,siSo,maGiaoVien):
          self.idLopHoc = idLopHoc
          self.tenLop = tenLop
          self.maKhoiLop = maKhoiLop
          self.maNamHoc = maNamHoc
          self.siSo = siSo
          self.maGiaoVien = maGiaoVien
     def getIdLopHoc(self):
          return self.idLopHoc
     def setTenLop(self,tenLop):
          self.tenLop = tenLop
     def getTenLop(self):
          return self.tenLop    