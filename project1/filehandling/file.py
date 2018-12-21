#open a file
fobj=open('prasad','r')
str=fobj.read()
print(str)
print('-----------------')
fobj.seek(0)#will move cursor to first character of file
str1=fobj.read()
print(str1)