from pickle import load
fobj=open("items.txt","rb")
while True:
    try:
        i=load(fobj)
        print(i)
    except EOFError:
        fobj.close()
        break

