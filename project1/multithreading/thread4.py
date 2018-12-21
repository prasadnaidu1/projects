from threading import Thread
from time import sleep
class X(Thread):
    def run(self):
        for i in range(1,21):
            print(i)
            sleep(3)
class Y(Thread):
    def run(self):
        x=X()
        x.start()
        for j in range(21,41):
            print(j)
            sleep(3)
            if j==31:
              x.join()
#calling block
y=Y()
y.start()

