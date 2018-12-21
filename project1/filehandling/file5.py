
fobj=open('prasad1.txt','w')
print('file is opened')
while True:
    line=input()
    if line!='stop':
        fobj.write(line)
        fobj.write('\n')
    else:
        break;
fobj.close()