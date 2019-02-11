import os
#取得目前工作資料夾或目錄
print(os.getcwd())
#變更工作目錄
os.chdir('D:\\')
new=os.getcwd()
print(new)

mydir =os.path.join('elaine','date')
print(mydir)

fulldir = os.path.join('D:\\' , mydir)
print(fulldir)
os.makedirs(fulldir)
myFiles= ['0211.txt','0212.xlsx','0213,docx']
for filename in myFiles:
    subdir = os.path.join(fulldir, filename)
    print(subdir)
    os.makedirs(subdir)



