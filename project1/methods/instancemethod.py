class sample:
    x=10
    def __init__(self,i):
        self.y=i
    def modify(self):
        sample.x+=100
        self.y+=25
    def show(self):
        print('x=',sample.x)
        print('y=',self.y)
#calling block
s1=sample(25)
s1.modify()
s1.show()
print('--------------------')
s2=sample(34)
s2.modify()
s2.show()