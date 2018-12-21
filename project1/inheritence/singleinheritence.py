class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def  show(self):
        print('x=',self.x)
        print('y=',self.y)
class B(A):
    def display(self):
        print('prasad')
#calling block
bobj=B(2000,300000)
bobj.show()
bobj.display()
