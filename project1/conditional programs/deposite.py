class amount:
    def deposite(self,accno,amount):
        self.accno=accno
        self.amount=amount
        print(amount,'deposited to',accno)
    def withdraw(self,accno,amount):
        print(amount,'withdraw from to',accno)
acc=amount()
acc.deposite(112222,30000)
acc.withdraw(2223333,400000)
