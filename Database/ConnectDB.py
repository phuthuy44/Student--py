import mysql.connector
mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database ="studentmanager"
)
mycursor = mydb.cursor()
"""
mycursor.execute('''
                 CREATE TABLE loaiNguoiDung(
                    maLoai VARCHAR(6) NOT NULL PRIMARY KEY,
                    tenLoaiNguoiDung VARCHAR(255) NOT NULL
                 )
                 ''')
mycursor.execute('''
               CREATE TABLE nguoiDung(
               maNguoiDung VARCHAR(6) NOT NULL  PRIMARY KEY,
               maLoai VARCHAR(6) NOT NULL,
               tenNguoiDung VARCHAR(30) NOT NULL,
               tenDangNhap VARCHAR(30) NOT NULL,
               matKhau VARCHAR(64) NOT NULL,
               CONSTRAINT FK_NguoiDung_LoaiNguoiDung FOREIGN KEY (maLoai) REFERENCES loaiNguoiDung (maLoai)
               )
               ''')
mycursor.execute('''
                    CREATE TABLE namHoc(
                    maNamHoc VARCHAR(6) NOT NULL PRIMARY KEY,
                    tenNamHoc VARCHAR(30) NOT NULL
                    )
               ''')
mycursor.execute('''
                    CREATE TABLE hocKy(
                    maHocKy VARCHAR(6) NOT NULL PRIMARY KEY,
                    tenHocKy VARCHAR(30) NOT NULL,
                    heSo INT,
                    CONSTRAINT CK_HOCKY CHECK(CAST(RIGHT(maHocKy,1) AS INT) BETWEEN 1 AND 1 AND 3)
                    )
               ''')
mycursor.execute('''
               CREATE TABLE khoiLop(
               maKhoiLop VARCHAR(6) NOT NULL PRIMARY KEY,
               tenKhoiLop VARCHAR(30) NOT NULL
               )
               ''')
mycursor.execute('''
               CREATE TABLE MonHoc(
               maMonHoc VARCHAR(6) NOT NULL PRIMARY KEY,
               tenMonHoc VARCHAR(30) NOT NULL,
               soTiet INT NOT NULL,
               heSo INT NOT NULL
               )
               ''')
mycursor.execute('''
               CREATE TABLE hocLuc(
               maHocLuc VARCHAR(6) NOT NULL PRIMARY KEY,
               tenHocLuc VARCHAR(30) NOT NULL,
               diemCanDuoi FLOAT NOT NULL,
               diemCanTren FLOAT NOT NULL,
               diemKhongChe FLOAT NOT NULL,
               CONSTRAINT CK_DIEMCANDUOI CHECK (diemCanDuoi BETWEEN 0 AND 10),
               CONSTRAINT CK_DIEMCANTREN CHECK(diemCanTren BETWEEN 0 AND 10),
               CONSTRAINT CK_DIEMKHONGCHE CHECK (diemKhongChe BETWEEN 0 AND 10)
               )
                    ''')
mycursor.execute('''
               CREATE TABLE hanhKiem(
               maHanhKiem VARCHAR(6) NOT NULL PRIMARY KEY,
               tenHanhKiem VARCHAR(30) NOT NULL
               )
                ''')
mycursor.execute('''
               CREATE TABLE ketQua(
               maKetQua VARCHAR(6) NOT NULL PRIMARY KEY,
               tenKetQua VARCHAR(30) NOT NULL
               )
               ''')
mycursor.execute('''
               CREATE TABLE giaoVien(
               maGiaoVien VARCHAR(6) NOT NULL PRIMARY KEY,
               tenGiaoVien VARCHAR(30) NOT NULL,
               ngaySinh DATETIME NOT NULL,
               gioiTinh BIT,
               diaChi VARCHAR(50) NOT NULL,
               email VARCHAR(50) NOT NULL UNIQUE,
               soDienThoai VARCHAR(15) NOT NULL,
               maMonHoc VARCHAR(6) NOT NULL,
               hinhAnh VARCHAR(255),
               CONSTRAINT fk_GIAOVIEN_MONHOC FOREIGN KEY (maMonHoc) REFERENCES monHoc(maMonHoc)
               )
                     ''')
mycursor.execute(''' 
               CREATE TABLE hocSinh(
               maHocSinh VARCHAR(6) NOT NULL PRIMARY KEY,
               tenHocSinh VARCHAR(30) NOT NULL,
               ngaySinh DATETIME NOT NULL,
               gioiTinh BIT,
               email VARCHAR(50) NOT NULL UNIQUE ,
               diaChi VARCHAR(50) NOT NULL,
               tenPhuHuynh VARCHAR(30) NOT NULL,
               soDienThoai VARCHAR(15) NOT NULL,
               hinhAnh VARCHAR(255)

               )
               ''')
mycursor.execute('''
               CREATE TABLE LOP(
               maLop VARCHAR(30) NOT NULL PRIMARY KEY,
               tenLop VARCHAR(30) NOT NULL,
               maKhoiLop VARCHAR(6) NOT NULL,
               maNamHoc VARCHAR(6) NOT NULL,
               siSo INT NOT NULL,
               maGiaoVien VARCHAR(6) NOT NULL,
               CONSTRAINT fk_LOP_KHOILOP FOREIGN KEY (maKhoiLop) REFERENCES khoiLop(maKhoiLop),
               CONSTRAINT fk_LOP_NAMHOC FOREIGN KEY (maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fK_LOP_GIAOVIEN FOREIGN KEY (maGiaoVien) REFERENCES giaoVien(maGiaoVien)
               )
               ''')
mycursor.execute('''
               CREATE TABLE phanLop(
               maNamHoc VARCHAR(6) NOT NULL,
               maKhoiLop VARCHAR(6) NOT NULL,
               maLop VARCHAR(6) NOT NULL,
               maHocSinh VARCHAR(6) NOT NULL,
               PRIMARY KEY (maNamHoc,maKhoiLop,maLop,maHocSinh),
               CONSTRAINT fk_PHANLOP_NAMHOC FOREIGN KEY (maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_PHANLOP_KHOILOP FOREIGN KEY (maKhoiLop) REFERENCES khoiLop(maKhoiLop),
               CONSTRAINT fk_PHANLOP_LOP FOREIGN KEY (maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_PHANLOP_HocSinh FOREIGN KEY (maHocSinh) REFERENCES hocSinh(maHocSinh)
               )
       ''')
mycursor.execute('''
               CREATE TABLE phanCong(
               maNamHoc VARCHAR(6) NOT NULL,
               maLop VARCHAR(6) NOT NULL,
               maMonHoc VARCHAR(6) NOT NULL,
               maGiaoVien VARCHAR(6) NOT NULL,
               PRIMARY KEY (maNamHoc,maLop,maMonHoc,maGiaoVien),
               CONSTRAINT fk_PHANCONG_NAMHOC FOREIGN KEY (maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_PHANCONG_LOP FOREIGN KEY (maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_PHANCONG_MONHOC FOREIGN KEY (maMonHoc) REFERENCES monHoc(maMonHoc),
               CONSTRAINT fk_PHANCONG_GIAOVIEN FOREIGN KEY (maGiaoVien) REFERENCES giaoVien(maGiaoVien)
               )
                    ''')
mycursor.execute('''
               CREATE TABLE loaiDiem(
               maLoaiDiem VARCHAR(6) NOT NULL PRIMARY KEY,
               tenLoai VARCHAR(30) NOT NULL,
               heSo INT NOT NULL
               )
               ''')
mycursor.execute('''
               CREATE TABLE Diem(
               maHocSinh VARCHAR(6) NOT NULL,
               maMonHoc VARCHAR(6) NOT NULL,
               maHocKy VARCHAR(6) NOT NULL,
               maNamHoc VARCHAR(6) NOT null,
               maLop VARCHAR(6) NOT NULL,
               maLoaiDiem VARCHAR(6) NOT NULL,
               diem FLOAT NOT NULL,
               PRIMARY KEY (maHocSinh, maMonHoc,maHocKy, maNamHoc, maLop, maLoaiDiem),
               CONSTRAINT fk_DIEM_HOCSINH FOREIGN KEY (maHocSinh) REFERENCES hocSinh (maHocSinh),
               CONSTRAINT fk_DIEM_MONHOC FOREIGN KEY (maMonHoc) REFERENCES monHoc (maMonHoc),
               CONSTRAINT fk_DIEM_NAMHOC FOREIGN KEY (maNamhoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_DIEM_LOP FOREIGN KEY (maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_DIEM_LOAIDIEM FOREIGN KEY (maLoaiDiem) REFERENCES loaiDiem(maLoaiDiem),
               CONSTRAINT fk_DIEM CHECK(diem BETWEEN 0 AND 10)
               )
                    ''')
mycursor.execute('''
               CREATE TABLE KQ_HOCSINH_MONHOC(
               maHocSinh VARCHAR(6) NOT NULL,
               maLop VARCHAR(6) NOT NULL,
               maNamHoc VARCHAR(6) NOT NULL,
               maMonHoc VARCHAR(6) NOT NULL,
               maHocKy VARCHAR(6) NOT NULL,
               diemMieng FLOAT NOT NULL,
               diem15phut FLOAT NOT NULL,
               diem45phut FLOAT NOT NULL,
               diemThi FLOAT NOT NULL,
               diemTBHK FLOAT NOT NULL,
               PRIMARY KEY (maHocSinh,maLop,maNamHoc,maMonHoc,maHocKy),
               CONSTRAINT fk_HSMN_HOCSINH FOREIGN KEY (maHocSinh) REFERENCES hocSinh (maHocSinh),
               CONSTRAINT fk_HSMN_LOP FOREIGN KEY (maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_HSMN_NAMHOC FOREIGN KEY (maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_HSMH_MONHOC FOREIGN KEY (maMonHoc) REFERENCES monHoc(maMonHoc),
               CONSTRAINT fk_HSMH_HOCKY FOREIGN KEY (maHocky) REFERENCES hocky(maHocky),
               CONSTRAINT ck_DIEMMIENG CHECK(diemMieng BETWEEN 0 AND 10),
               CONSTRAINT ck_DIEM15PHUT CHECK(diem15PHUT BETWEEN 0 AND 10),
               CONSTRAINT ck_Diem45PHUT CHECK(diem45phut BETWEEN 0 AND 10),
               CONSTRAINT ck_DIEMTHI CHECK(diemThi BETWEEN 0 AND 10),
               CONSTRAINT ck_DiemTBHK CHECK(diemTBHK BETWEEN 0 AND 10)
               )
               ''')
mycursor.execute('''
               CREATE TABLE KQ_HOCSINH_CANAM(
               maHocSinh VARCHAR(6) NOT NULL,
               maLop VARCHAR(6) NOT NULL,
               maNamHoc VARCHAR(6) NOT NULL,
               maHocLuc VARCHAR(6) NOT NULL,
               maHanhKiem VARCHAR(6) NULL,
               maKetQua VARCHAR(6) NOT NULL,
               diemTBHK1 FLOAT NOT NULL,
               diemTBHK2 FLOAT NOT NULL,
               diemTBCN FLOAT NOT NULL,
               PRIMARY KEY (maHocSinh, maLop, maNamHoc, maHocLuc, maHanhKiem,maKetQua),
               CONSTRAINT fk_HSNH_HOCSINH FOREIGN KEY (maHocSinh) REFERENCES hocSinh(maHocSinh),
               CONSTRAINT fk_HSNH_LOP FOREIGN KEY (maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_HSNH_NAMHOC FOREIGN KEY (maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_HSNH_HOCLUC FOREIGN KEY (maHocLuc) REFERENCES hocLuc(maHocLuc),
               CONSTRAINT fk_HSNM_HANHKIEM FOREIGN KEY (maHanhKiem) REFERENCES hanhKiem(maHanhKiem),
               CONSTRAINT ck_DiemTBHK1 CHECK (diemTBHK1 BETWEEN 0 AND 10),
               CONSTRAINT ck_DiemTBHK2 CHECK (diemTBHK2 BETWEEN 0 AND 10),
               CONSTRAINT ck_DiemTBCN CHECK (diemTBCN BETWEEN 0 AND 10)
               )
''')
mycursor.execute('''
               CREATE TABLE KQ_LOPHOC_MONHOC(
               maLop VARCHAR(6) NOT NULL,
               maNamHoc VARCHAR(6) NOT NULL,
               maMonHoc VARCHAR(6) NOT NULL,
               maHocKy VARCHAR(6) NOT NULL,
               soLuongDat INT NOT NULL,
               PRIMARY KEY (maLop,maNamHoc,maMonHoc,maHocKy),
               CONSTRAINT fk_LHMH FOREIGN KEY (maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_LHNH FOREIGN KEY (maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_LHMH_MONHOC FOREIGN KEY (maMonHoc) REFERENCES monHoc(maMonHoc),
               CONSTRAINT fk_LHMH_HOCKY FOREIGN KEY (maHocKy) REFERENCES hocKy(maHocKy)
               )
''')
mycursor.execute('''
               CREATE TABLE KQ_LOPHOC_HOCKY(
               maLop VARCHAR(6) NOT NULL,
               maNamHoc VARCHAR(6) NOT NULL,
               maHocKy VARCHAR(6) NOT NULL,
               soLuongDat INT NOT NULL,
               PRIMARY KEY (maLop,maNamHoc,maHocKy,soLuongDat),
               CONSTRAINT fk_LHHK_LOP FOREIGN KEY(maLop) REFERENCES lop(maLop),
               CONSTRAINT fk_LHHK_NAMHOC FOREIGN KEY(maNamHoc) REFERENCES namHoc(maNamHoc),
               CONSTRAINT fk_LHHK_HOCKY FOREIGN KEY(maHocky) REFERENCES hocKy(maHocKy)

               )
''')
mycursor.execute('''
               CREATE TABLE quyDinh(
               tuoiCanDuoi INT NOT NULL,
               tuoiCanTren INT NOT NULL,
               siSoCanDuoi INT NOT NULL,
               siSoCanTren INT NOT NULL,
               diemDat INT NOT NULL
               )
''')
mycursor.execute('''
               ALTER TABLE KQ_HOCSINH_CANAM
               ADD FOREIGN KEY (maKetQua) REFERENCES ketQua(maKetQua)

                    ''')
mycursor.execute('''
               CREATE TABLE chucVu(
               maChucVu VARCHAR(6) NOT NULL PRIMARY KEY,
               tenChucVu VARCHAR(30) NOT NULL
               )
''')
mycursor.execute('''
               CREATE TABLE cacKhoanPhi(
               maPhi VARCHAR(6) NOT NULL PRIMARY KEY,
               tenPhi VARCHAR(30) NOT NULL
               )
''')
mycursor.execute('''
               CREATE TABLE nhanVien(
               maNhanVien VARCHAR(6) NOT NULL PRIMARY KEY,
               tenNhanVien VARCHAR(30) NOT NULL,
               ngaySinh DATETIME NOT NULL,
               gioiTinh BIT,
               diaChi VARCHAR(50) NOT NULL,
               email VARCHAR(50) NOT NULL UNIQUE,
               soDienThoai VARCHAR(15) NOT NULL,
               maChucVu VARCHAR(6) NOT NULL,
               hinhAnh VARCHAR(255),
               CONSTRAINT fk_NHANVIEN_CHUCVU FOREIGN KEY (maChucVu) REFERENCES chucVu(maChucVu)
               )
                     ''')
mycursor.execute('''
               CREATE TABLE PhieuThanhToan(
               maPhieu VARCHAR(6) NOT NULL PRIMARY KEY,
               maNhanVien VARCHAR(6) NOT NULL,
               maHocSinh varchar(6) NOT NULL,
               maLop varchar(6) NOT NULL,
               ngayDong DATETIME NOT NULL,
               nguoiDong VARCHAR(50) NOT NULL,
               thanhToan INT NOT NULL,
               CONSTRAINT FK_PTT_NHANVIEN FOREIGN KEY (maNhanVien) REFERENCES nhanVien(maNhanVien),
               CONSTRAINT FK_PTT_HOCSINH FOREIGN KEY (maHocSinh) REFERENCES hocSinh(maHocSinh),
               CONSTRAINT FK_PTT_LOPHOC FOREIGN KEY (maLop) REFERENCES lop(maLop)
               )
''')
mycursor.execute('''
               CREATE TABLE chiTietPhieu(
               maPhi VARCHAR(6) NOT NULL,
               maPhieu VARCHAR(6) NOT NULL,
               soTienDong INT NOT NULL,
               PRIMARY KEY (maPhi,maPhieu),
               CONSTRAINT fk_CTPHIEU_CACKHOANPHI FOREIGN KEY (maPhi) REFERENCES cacKhoanPhi(maPhi),
               CONSTRAINT fk_CTPHIEU_PHIEU FOREIGN KEY (maPhieu) REFERENCES PhieuThanhToan(maPhieu)
               )
''')
mycursor.execute('''ALTER TABLE hocky DROP CONSTRAINT CK_HOCKY''')
mycursor.execute('''ALTER TABLE hocsinh MODIFY gioitinh VARCHAR(30)''')
mycursor.execute('''ALTER TABLE hocsinh MODIFY hinhAnh BLOB''')"""
mycursor.execute('''ALTER TABLE hocsinh MODIFY ngaySinh DATE''')
mydb.close()