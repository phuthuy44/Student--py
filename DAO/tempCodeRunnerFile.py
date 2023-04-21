sqlChucVu  = "SELECT DISTINCT giaovien.tenGiaoVien FROM giaovien LEFT JOIN lop ON giaovien.maGiaoVien = lop.maGiaoVien AND lop.maNamHoc = %s WHERE lop.maLop IS NULL "
               val = (year,)
               query.execute(sqlChucVu,val)
               rows = query.fetchall()
               for row in rows:
                    chucvu = (row[0])
                    list.append(chucvu)
               print(list)