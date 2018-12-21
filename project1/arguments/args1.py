x=223
y=223
def increment():
    global x
    global y
    x=x+100
    y=y+1
    print('x in increment=',x)
    print('y in incremnt=',y)
increment()
print('x in main function=',x)
print('y in function=',y)
