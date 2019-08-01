import xlrd
import os.path
from xlrd.sheet import empty_cell
import shutil
#Reading all excel files one by one from repository
def file_copy(path):
folder_list=os.listdir(path)
print folder_list
#Reading the last column from each excel and create file with that each field name
for fname in folder_list:
if fname.endswith(".xlsx"):
print fname
wb = xlrd.open_workbook(os.path.join(path,fname))
sname = wb.sheet_names()
print type(sname)
sh = wb.sheet_by_index(0)
#i = 1
#fname = []
rcount = sh.nrows
#print rcount
try:
for i in range(1,rcount+1):
#sh.cell(i,85).value != "":
name = sh.cell(i,85).value
if name is not empty_cell and name != '':
print os.getcwd()
#path = os.getcwd()
#print os.listdir(path)
shutil.copy('MASTER.doc','E:/1439/Training_task/New folder')
os.chdir('E:/1439/Training_task/New folder')
os.rename('MASTER.doc',name)
os.chdir(path)
i = i + 1
except IndexError:
exit
path = ''
print file_copy(path)
#I dont how manage this files 
# i will learn this

