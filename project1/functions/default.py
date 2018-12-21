def add(x, y, z=400):
    i = x + y + z
    j = x - y + z
    k = x * y * z
    print('x=', x)
    print('y=', y)
    print('z=', z)
    print('x+y+z=', x + y + z)
    print('x-y+z=', x + y + z)
    print('x*y*z=', x * y * z)


a = int(input('enter a value:'))
b = int(input('enter b value:'))
c = int(input('enter c value:'))
add(b,a)