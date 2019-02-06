import xlwt
a=xlt.Workbook
y=xlwt.easyxf('font:chillar,bold on,height 300;')
w=a.add_sheet("sheet 1")

w.write(0,0,"s.n.")
w.erite(0,1,"name")
w.write(0,2,"attendance")
a.save("attandance.xls")

