class subject:
    def __init__(self,sub_name):
        self.sub_name=sub_name
class maths(subject):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        super().__init__(self)
class physics(subject):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        super().__init__(self)

#calling block
s1=subject(physics)
s2=subject(maths)
p1=physics("prasad",80)
p2=physics("`raju",89)

m1=maths("prasad",100)
m2=maths("raju",89)

print('student 1 record')
print(p1.name,p1.marks)
print(p2.name,p2.marks)

print('student 2 record')
print(m1.name,m2.marks)
print(m2.name,m2.marks)
