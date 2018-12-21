def mobile(x):
    def sim():
        return 'AIRTEL'
    return 'mobile{} is inserted with sim{}'format(x,sim())
#calling block
n=mobile('vivo')
print(n)