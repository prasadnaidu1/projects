class employee:
    def __init__(self):
        self.empname=input('name:')
        self.empid=input('id:')
        self.gender=input('gender:')
    def show(self):
        print('empname=',self.empname)
        print('empid=',self.empid)
        print('gender=',self.gender)
class salary(employee):
    def monthly(self,x):
        self.sal=x
        self.da=(x*0.10)
        self.hra=(x*0.05)
        self.tra=(x*0.10)
    def display(self):
        print('dailyallowences:',self.da)
        print('human resourse allowence:',self.hra)
        print('travelling allowence:',self.tra)
        print('total salary',self.sal+self.da+self.hra+self.tra)
#calling block
s=salary()
s.show()
s.monthly(30000)
s.display()