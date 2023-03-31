class StudentDTO:
     def __init__(self,idHocSinh,hoTen,ngaySinh,gioiTinh,idLopHoc,diaChi,soDienThoai,tenPhuHuynh,soDienThoaiPH,hinhAnh):
          self.id = idHocSinh
          self.hoTen = hoTen
          self.ngaySinh = ngaySinh
          self.gioiTinh = gioiTinh
          self.idLopHoc = idLopHoc
          self.diaChi = diaChi
          self.soDienThoai = soDienThoai
          self.tenPhuHuynh = tenPhuHuynh
          self.soDienThoaiPH = soDienThoaiPH
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
     def setTenPH(self, tenPH):
          self.tenPhuHuynh=tenPH
     def getTenPH(self):
          return self.tenPhuHuynh
     def setSDTPH(self, sdTPH):
          self.soDienThoaiPH = sdTPH
     def getSDTPH(self):
          return self.soDienThoaiPH
     def setHinhAnh(self, hinhAnh):
          self.hinhAnh = hinhAnh
     def getHinhAnh(self):
          return self.hinhAnh