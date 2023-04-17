def fineSortASC(self):
          cv = ChucVuBUS()
          self.tableChucVu.clearContents()
          self.tableChucVu.setRowCount(0)
          rowcount = 0
          macv = cv.findSortASC(self.cbSortCV.currentText())
          self.tableChucVu.setRowCount(len(macv))
          for row in macv :
                    self.tableChucVu.setItem(rowcount, 0, QTableWidgetItem(row[0]))
                    self.tableChucVu.setItem(rowcount, 1, QTableWidgetItem(row[1]))
                    rowcount += 1