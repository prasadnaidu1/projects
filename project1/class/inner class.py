class mobile:  #outer class
    def __init__(self):  #outerconstructer
        self.mobilemodel='samsung'  #instance variable
        self.s=self.sim() #object of inner class
    def displaymodel(self):  #inner class
        print('mobile model is:',self.mobilemodel)
    class sim:
        def __init__(self): #inner constructer
            self.provider='jio'# inner instance variable
        def displaysim(self):
            print('sim provider is:',self.provider)
#calling block
m=mobile()
m.displaymodel()
x=m.s #reading innerclass object from outerclass
x.displaysim()

