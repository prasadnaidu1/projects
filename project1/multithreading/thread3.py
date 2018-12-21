from threading import Thread
from time import sleep
class X:
    def fun1(self):
        for i in range(1,41):
            print(i)
            sleep(3)


class Y:
    def fun2(self):
        for j in range(41,61):
            print(j)
            sleep(3)
#calling block
x=X()
y=Y()
t1=Thread(target=x.fun1)
t2=Thread(target=y.fun2)
t1.start()
t2.start()
