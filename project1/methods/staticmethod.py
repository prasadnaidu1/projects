class emp:
    def __init__(self):
        self.empno=123
        self.empname='prasad'
    def display(self):
        print('empno=',self.empno)
        print('empname=',self.empname)
class sample:
    x=200
    def __init__(self,i):
        self.y=i
    @staticmethod
    def modify(e):
        sample.x+=100
        e.empno=223

    def show(self):
        print('x=',sample.x)
        print('y=',self.y)
#calling block
s1=sample(25)
e=emp()
sample.modify(e)
s1.show()
e.display()

