from zipfile import ZipFile, ZIP_DEFLATED
z=ZipFile('E:/test2.zip','w',ZIP_DEFLATED)
z.write('file.py')
z.write('file2.py')
z.write('file3.py')
z.close()