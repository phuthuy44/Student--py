import mysql.connector
mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database ="studentmanager"
)
#print(mydb)
#mydb.close()
mycursor = mydb.cursor()
'''
mycursor.execute("""CREATE TABLE Khoi(
                 idKhoi INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                 tenKhoi VARCHAR(255) NOT NULL)""")'''
'''mycursor.execute("""CREATE TABLE lop(
                idLop INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                tenLop VARCHAR(255) NOT NULL,
                idKhoi INT not null,
                FOREIGN KEY (idKhoi) REFERENCES Khoi (idKhoi)
                            )""")'''
'''mycursor.execute("""
                CREATE TABLE Monhoc(
                idMonHoc INT AUTO_INCREMENT PRIMARY KEY,
                tenMonHoc VARCHAR(255) NOT NULL,
                soTiet INT NOT NULL
                                                )""")
mycursor.execute("""
                CREATE TABLE ChucVu(
                idChucVu INT AUTO_INCREMENT PRIMARY KEY,
                tenChucVu VARCHAR(255) NOT NULL
                )
                            """)
mycursor.execute("""
                CREATE TABLE CacKhoanPhi(
                idCacKhoanPhi INT AUTO_INCREMENT PRIMARY KEY,
                tenCacKhoanPhi VARCHAR(255) NOT NULL
                )
                    """)
mycursor.execute("""
                CREATE TABLE IF NOT EXISTS XEPLOAI(
                idXepLoai INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                tenXepLoai VARCHAR(255) NOT NULL
                )
                """)
mycursor.execute("""
                CREATE TABLE IF NOT EXISTS QuyenHan(
                idQuyenHan INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                tenQuyenHan VARCHAR(255) NOT NULL
                )
                    """)
mycursor.execute("""
                    ALTER TABLE LopHoc
                    MODIFY COLUMN idLopHoc VARCHAR(255)
                    """)'''
'''mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS HocSinh(
                    idHocSinh INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    hoTen VARCHAR(255) NOT NULL,
                    ngaySinh datetime NOT NULL,
                    gioiTinh VARCHAR(255) NOT NULL,
                    diaChi VARCHAR(255) NOT NULL,
                    idLopHoc VARCHAR(255) NOT NULL,
                    soDienThoai varchar(255) NOT NULL,
                    tenPhuHuynh VARCHAR(255) NOT NULL,
                    soDine 
                    
                    )
                """)'''
mycursor.execute('''
                DROP DATABASE studentmanager
                ''')

mydb.close()