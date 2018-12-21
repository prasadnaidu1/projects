import filehandling.item
from pickle import dump
x=int(input('enter how many objects you want to serilize'))
fobj=open("items.txt","wb")
for i in range(1,x+1):
    l=int(input('enter item id'))
    m=input('enter item name')
    n=int(input('enter price'))
    itemobj=filehandling.item.Item(l,m,n)
    dump(itemobj,fobj)
    print('serilize is completed')
fobj.close()


