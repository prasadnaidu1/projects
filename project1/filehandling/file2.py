try:
 fobj=open('prasad','r')
 print('the file is opened')
 for line in fobj:
    print(line)
except:
    print('the file is closed')
