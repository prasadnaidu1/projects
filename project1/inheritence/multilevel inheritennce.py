class A:
    def __init__(self,x):
        self.x=x

class B(A):
    def __init__(self,x,y):
        self.y=y
        super().__init__(x)
class C(B):
    def __init__(self,x,y,z):
        self.z=z
        super().__init__(x,y)
    def show(self):
        print('x=',self.x)
        print('y=',self.y)
        print('z=',self.z)
#calling block
cobj=C(123,456,789)
cobj.show()