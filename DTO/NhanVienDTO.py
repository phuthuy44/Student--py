class NhanVienDTO :
     def __init__(self,maNhanVien,tenNV,gioiTinh,ngaySinh,diaChi,email,soDienThoai,chucVu,hinhAnh):
          self.maNhanVien  = maNhanVien
          self.tenNV= tenNV
          self.gioiTinh =gioiTinh
          self.ngaySinh = ngaySinh
          self.diaChi = diaChi
          self.email = email
          self.soDienThoai = soDienThoai
          self.chucVu= chucVu
          self.hinhAnh = hinhAnh
     def getMaNhanVien(self):
          return self.maNhanVien
     def setTenNV(self, tenNV):
          self.tenNV = tenNV
     def getTenNV(self):
          return self.tenNV
     def setGioiTinh(self, gioiTinh):
          self.gioiTinh = gioiTinh
     def getGioiTinh(self):
          return self.gioiTinh
     def setNgaySinh(self,ngaySinh):
          self.ngaySinh = ngaySinh
     def getNgaySinh(self):
          return self.ngaySinh
     def setDiaChi(self,diaChi):
          self.diaChi = diaChi
     def getDiaChi(self):
          return self.diaChi
     def setEmail(self,email):
          self.email = email
     def getEmail(self):
          return self.email
     def setSoDienThoai(self,soDienThoai):
          self.soDienThoai = soDienThoai
     def getSoDienThoai(self):
          return self.soDienThoai
     def setChucVu(self, chucVu):
          self.chucVu = chucVu
     def getChucVu(self):
          return self.chucVu
     def setHinhANh(self,hinhAnh):
          self.hinhAnh = hinhAnh
     def getHinhANh(self):
          return self.hinhAnh