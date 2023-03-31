class StudentDTO:
     def __init__(self,idHocSinh,hoTen,ngaySinh,gioiTinh,idLopHoc,diaChi,soDienThoai,tenCha,tenMe,soDienThoaiCha, soDienThoaiMe,hinhAnh):
          self.id = idHocSinh
          self.hoTen = hoTen
          self.ngaySinh = ngaySinh
          self.gioiTinh = gioiTinh
          self.idLopHoc = idLopHoc
          self.diaChi = diaChi
          self.soDienThoai = soDienThoai
          self.tenCha = tenCha
          self.tenMe = tenMe
          self.soDienThoaiCha = soDienThoaiCha
          self.soDienThoaiMe = soDienThoaiMe
          self.hinhAnh = hinhAnh
     def getMssv(self):
          return self.id
     def setHoTen(self,HoTen):
          self.hoTen = HoTen
     def getHoTen(self):
          return self.hoTen
     def setNgaySinh(self,NgaySinh):
          self.ngaySinh = NgaySinh
     def getNgaySinh(self):
          return self.ngaySinh
     def setGioiTinh(self,GioiTinh):
          self.gioiTinh = GioiTinh
     def getIdLopHoc(self):
          return self.idLopHoc
     def getGioiTinh(self):
          return self.gioiTinh
     def setDiaChi(self,DiaChi):
          self.diaChi = DiaChi
     def getDiaChi(self):
          return self.diaChi
     def setSoDienThoai(self,SoDienThoai):
          self.soDienThoai = SoDienThoai
     def getSoDienThoai(self):
          return self.soDienThoai
     '''def setDiemTB(self, diemTB):
          self.diemTB = diemTB'''
     def setTenCha(self, tenCha):
          self.tenCha = tenCha
     def getTenCha(self):
          return self.tenCha
     def setTenMe(self, tenMe):
          return self.tenMe
     def setSoDienThoaiCha(self, soDienThoaiCha):
          self.soDienThoaiCha = soDienThoaiCha
     def setSoDienThoaiMe(self, soDienThoaiMe):
          self.soDienThoaiMe = soDienThoaiMe
     def setHinhAnh(self, hinhAnh):
          self.hinhAnh = hinhAnh
     def getHinhAnh(self):
          return self.hinhAnh