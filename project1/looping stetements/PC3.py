units=int(input('enter the no of units'))
if units<=150:
    price=0
elif units>150 and units<=300:
    price=units*5.46
elif units>300 and units<=700:
    price=units*12.0
else:
    price=units*20.0
discount=(price*10)/100
total=price-discount
print('price=',price)
print('discout=',discount)
print('total=',total)