class sample:
    x=100 #public  static variable
    __y=200  #private stattic variable
    def m1(self):     #instance method
        print('i am m1')
    def __m2(self):
        print('i am m2')
#callingblock
print(sample.x)
s=sample()
s.m1()
s.__m2__()
