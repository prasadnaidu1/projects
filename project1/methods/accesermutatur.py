class customer:
    def __init__(self,id,name,address):
        self.custid=id
        self.custname=name
        self.custaddress=address
    def setCustid(self,id):#using settermethod
        self.custid=id
    def getCustid(self):# using getter method
        print(self.custid)
    def setCustname(self,name):
        self.custname=name
    def getCustname(self):
        print(self.custname)
    def setCustaddress(self,address):
        self.custaddress=address
    def getCustaddress(self):
        return self.custaddress
    def show(self):
        print('customer details {},{},{} '.format(self.custid,self.custname,self.custaddress))
#calling block
c=customer(1011,'prasad','hyd')
print('customer details before changing')
c.show()
c.setCustname('ramu')#set thhe value
c.setCustaddress('bangalore')
c.setCustid(4455)
print('customer details after changing')
c.show()
c1=customer(1022,'reddy','chennai')
print('after second time customer details')
c1.show()
c1.setCustname('raju')
c1.setCustaddress('madanapalli')
print('-------------------------')
c1.show()