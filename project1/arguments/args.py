x=100
y=300
def increment():
    x=200
    y=123
    x=x+1
    y=y+1
    print('x in increment=',x)
    print('x in increment=',y)


#calling block
increment()
print('x in function=',x )
print('y in function=',y)