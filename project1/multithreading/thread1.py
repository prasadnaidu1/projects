
from threading import Thread
def fun1():
    for i in range(1,11):
        print(i)
def fun2():
    for j in  range(11,21):
        print(j)
#calling block
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()  #this method is used to  actuaylly thread in newborn state whenever we call the start() method thenn only the thread will go to rrunnable state