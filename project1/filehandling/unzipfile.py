from zipfile import ZipFile,ZIP_DEFLATED
z=ZipFile("E:/test2.zip","r")
names=z.namelist()
print(names)
for name in names:
    f=open(name,'r')
    print(f.read())
    f.close()
    print()
