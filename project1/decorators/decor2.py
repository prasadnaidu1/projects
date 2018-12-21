def dadecor(fun):
    def inner():
        sal=fun()
        sal+=sal*0.10
        return sal
    return inner
def hradecor(fun):
    def inner():
        sal=fun()
        sal+=sal*0.20
        return sal
    return inner
def tadecor(fun):
    def inner():
        sal=fun()
        sal+=sal*0.05
        return sal
    return inner

@dadecor
@hradecor
@tadecor
def salary():
    return 30000
#calling block
m=salary()
print(m)