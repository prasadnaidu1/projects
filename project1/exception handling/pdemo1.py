class cashoverflowException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
class Bank:
    def __init__(self,balance):
        self.bal=balance
    def deposite(self,amount):
        try:
            if amount>100000:
                raise cashoverflowException('Exception:your bank deposited is not more than 100000.please visit your branch and exceed the your bank deposited money')
        except cashoverflowException as cf:
            print(cf)
        else:
            self.bal+=amount
            print('total  deposited money',self.bal)
        finally:
            print('this is final value')
#outside of the class
b=Bank(balance=40000)
b.deposite(120000)
