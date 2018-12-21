from threading import Thread
class X(Thread):
    def run(self):
        for i in range(1,50):
            print(i)
class Y(Thread):
    def run(self):
        for j in range(50,100):
            print(j)
#calling block
x=X()
y=Y()
x.start()
y.start()
#by using sub class object of thread class(superclass) here no need to create threads why because already X,Y classes are in thread class only.