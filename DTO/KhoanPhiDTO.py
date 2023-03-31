class KhoanPhiDTO:
     def __init__(self,idPhieu,idNhanVien,idHocSinh,idLopHoc,ngayDong,nguoiDong,thanhTien):
          self.idPhieu = idPhieu
          self.idNhanVien = idNhanVien
          self.idHocSinh = idHocSinh
          self.idLopHoc = idLopHoc
          self.ngayDong = ngayDong
          self.nguoiDong = nguoiDong
          self.thanhTien = thanhTien
     def getIdPhieu(self):
          return self.idPhieu