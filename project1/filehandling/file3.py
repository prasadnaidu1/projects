
fobj=open('prasad','r')
print('the is opened')
c1=0
c2=0
c3=0
for line in fobj:
    c1+=1
    wordslist=line.split()
    c2+=len(wordslist)
    c3+=len(line)
print('no of lines:',c1)
print('no of words:',c2)
print('no of characters:',c3)
fobj.close()