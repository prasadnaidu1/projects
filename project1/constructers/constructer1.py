class deposite:
    minimumdeposite=100000
    def __init__(self,depositedmoney):
        self.depositedmoney=depositedmoney
    def cash(self):
        if deposite.minimumdeposite>=self.depositedmoney:
            deposite.minimumdeposite-=self.depositedmoney
            return 'cash are deposited'
        else:
            return 'sorry {} cash is available'.format(deposite.minimumdeposite)
#calling block
d1=deposite(10000)
msg=d1.cash()
print(msg)
print('----------------------')
d2=deposite(200000)
msg=d2.cash()
print(msg)