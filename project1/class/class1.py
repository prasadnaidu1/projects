class sample():
    def assign(self,m):
        self.msg=m
    def show(self,m):
        print(self.msg)
s1=sample()
s1.assign('HELLO')
s2=sample()
s2.assign('PRASAD')
s1.show(sample)
s2.show(sample)