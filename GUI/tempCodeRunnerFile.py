def insertNguoiDung(self):
          chucvu = ChucVuBUS()
          maChucVu = chucvu.getmaMon(self.cboxChucVuList.currentText())
          cboxTenNguoiDung = self.cboxTenNguoiDung.currentText()
          LineTenDangNhap = self.LineTenDangNhap.text()
          lineMatKhau = self.lineMatKhau.text()
          addNguoiDung = NguoiDungDTO(maChucVu,LineTenDangNhap,cboxTenNguoiDung,lineMatKhau)
          nguoiDung = NguoiDungBUS()
          if nguoiDung.insert(addNguoiDung):
               QMessageBox.information(self,"Thông báo","Thêm vào danh sách thành công!")
               self.loadlistNguoiDung()
          else:
               QMessageBox.warning(self,"Lỗi","Thêm vào danh sách không thành công!")
