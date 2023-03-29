class LopHocDTO:
     def __init__(self,idLopHoc,tenLop,nienKhoa):
          self.idLopHoc = idLopHoc
          self.tenLop = tenLop
          self.nienKhoa = nienKhoa
     def getIdLopHoc(self):
          return self.idLopHoc
     def setTenLop(self,tenLop):
          self.tenLop = tenLop
     def getTenLop(self):
          return self.tenLop 
     def setNienKhoa(self,nienKhoa):
          self.nienKhoa = nienKhoa
     def getNienKhoa(self):
          return self.nienKhoa         