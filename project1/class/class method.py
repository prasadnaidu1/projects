class sample:
    x=100
    def __init__(self,i):
        self.y=i
    @classmethod
    def modify(cls):
        cls.x+=1000
    def show(self):
        print('x=',sample.x)
        print('y=',self.y)
#calling block
s1=sample(25)
s1.modify()
s1.show()
print('----------------')
s2=sample(32)
s2.modify()
s2.show()