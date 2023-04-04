class GiaoVienDTO :
     def __init__(self,maGiaoVien,tenGV,gioiTinh,ngaySinh,diaChi,email,soDienThoai,chuyenMon,hinhAnh):
          self.maGiaoVien = maGiaoVien
          self.tenGV = tenGV
          self.gioiTinh =gioiTinh
          self.ngaySinh = ngaySinh
          self.diaChi = diaChi
          self.email = email
          self.soDienThoai = soDienThoai
          self.chuyenMon = chuyenMon
          self.hinhAnh = hinhAnh
     def getidGiaoVien(self):
          return self.idGiaoVien
     def setTenGV(self, tenGV):
          self.tenGiaoVien = tenGV
     def gettenGiaoVien(self):
          return self.tenGiaoVien
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
     def setChuyenMon(self, chuyenMon):
          self.chuyenMon = chuyenMon
     def getChuyenMon(self):
          return self.chuyenMon
     def setHinhANh(self,hinhAnh):
          self.hinhAnh = hinhAnh
     def getHinhANh(self):
          return self.hinhAnh