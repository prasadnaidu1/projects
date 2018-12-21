class personal:
    def getStudent(self):
        self.name=input('Name:')
        self.age=input('Age:')
        self.gender=input('Gender:')


class marks(personal):
    def getMarks(self):
        self.studentclass=input('enter class')
        print('enter student marks memo')
        self.telugu=int(input('telugu marks'))
        self.english=int(input('english marks'))
        self.hindhi=int(input('hindhi marks'))
        self.maths=int(input('maths marks'))
        self.science=int(input('science marks'))
        self.social=int(input('social marks'))
class results(marks):
    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)
        print('student class:',self.studentclass)
        print('telugu:',self.telugu)
        print('english:',self.english)
        print('hindhi:',self.hindhi)
        print('maths:',self.maths)
        print('science:',self.science)
        print('social:',self.social)
        print('totalmarks:',self.telugu+self.english+self.hindhi+self.maths+self.science+self.social)
        print('----------------------------------')

#calling block
r=results()
r.getStudent()
r.getMarks()
r.display()
