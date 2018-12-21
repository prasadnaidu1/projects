class computer:
    def __init__(self):
        self.computermodels='acer one 14,lenovo'
        self.m=self.mouse()
    def displaymodels(self):
        print('computer models are:',self.computermodels)
    class mouse:
        def __init__(self):
            self.requires='mouse'
        def displaymouse(self):
            print('computer requirement is:',self.requires)
#calling block
c=computer()
c.displaymodels()
y=c.m
y.displaymouse()