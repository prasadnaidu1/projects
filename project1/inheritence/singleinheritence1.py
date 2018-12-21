class sample:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print('x=', self.x)
        print('y=', self.y)
class demo(sample):
    def __init__(self,a,b,c):
        self.z=c
        super().__init__(a,b)
    def show(self):
        super().show()
        print('z=',self.z)

#calling block
d=demo(100,200,300)
d.show()
