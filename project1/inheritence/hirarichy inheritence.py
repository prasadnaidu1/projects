class subject:
    def __init__(self,sub_name):
        self.sub_name=sub_name
class maths(subject):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        subject.__init__(self,maths)
        def display(self):
            print('name=',self.name)
            print('marks=',self.marks)
            print('sub_name=',self.sub_name)

class physics(subject):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        subject.__init__(self,physics)
    def dispaly1(self):
        print('name=', self.name)
        print('marks=', self.marks)
        print('sub_name=', self.sub_name)
#calling block
p1=physics('prasad',89)
p2=physics('naidu',90)
p1.dispaly1()
p2.dispaly1()
m1=maths('prasad',89)
m2=maths('naidu',89)
