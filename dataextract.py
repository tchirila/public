# extracts values from files (excel)
import xlrd

list = []
test = xlrd.open_workbook('D:\\Program Files\\Anaconda Python 2.7\\projects\\filetest\\data\\data1.xlsx')
testsheet = test.sheet_by_index(0)
r = testsheet.row(0) #returns all the CELLS of row 0,
c = testsheet.col_values(0) #returns all the VALUES of row 0, 
for i in xrange(testsheet.nrows):
  list.append(testsheet.row_values(i)) #drop all the values in the rows into data
print list

#y = 0
#while testsheet.cell(0,y).value != xlrd.empty_cell.value:
#    number = testsheet.cell(0,y).value
#    list.append(number)
#    y = y + 1
#    break
#print list
