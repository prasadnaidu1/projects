units=int(input('enter  no of units:'))
price=0
if units<=150:
    pass
elif units>150 and units<=300:
    price=units*5.4
else:
    price=units*9.46
print('price=',price)