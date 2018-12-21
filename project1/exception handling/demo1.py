class totalamountException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
try:
    x=int(input('enter the amount'))
    if x%100!=0:
        raise totalamountException('enter the amount multiples,100 only')

except totalamountException as tae:
    print(tae)
else:
    print("amount accepted")
finally:
    print('i am finally')

