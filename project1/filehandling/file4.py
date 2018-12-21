fobj=open('prasad','r')
print('this is opened')
count=0
for line in fobj:
    count+=line.count('this')
print('the no of line repeated is:',count)
fobj.close()