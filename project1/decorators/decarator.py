def decor(fun):
    def inner():
        value=fun()
        value+=39
        return value
    return inner()
@decor
def calculate():
    return 20
print('calculate=',calculate)