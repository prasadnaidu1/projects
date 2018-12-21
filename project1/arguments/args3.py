x=222
y=999
def increment():
    x=100
    dict=globals()['x']
    print(dict)
increment()
print('x in function=',x)
print('y in function=',y)
