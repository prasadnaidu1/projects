class amountoverflowException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
class Bank:
    def __init__(self,balance):
        self.bal=balance
    def withdraw(self,amount):
        try:
            if amount>20000:
                raise amountoverflowException('amount is invalid,max is 20000')
        except amountoverflowException as ae:
            print(ae)
        else:
            self.bal -= amount
            print('remaining  amount after withdraw', self.bal)
#outside of the class
b=Bank(balance=90000)
b.withdraw(12000)


