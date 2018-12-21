class toomanyvaluesException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
class test:
    def fun1(self,mylist):
        try:
            if len(mylist)>5:
                raise toomanyvaluesException('list has more than 5 values')
        except toomanyvaluesException as e:
            print(e)
        else:
            print('list accepted')
            print(mylist)
#ouyside of the class
t=test()
mylist=[10,20,30,40,50]
t.fun1(mylist)