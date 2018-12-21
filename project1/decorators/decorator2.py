def increment(fun):
    def inner(x):
        value=fun(x)
        value+=1
        return value
    return inner
@increment
def calculate(i):
    return i
@increment
def squere(j):
    return j*j
#calling block
m=calculate(23)
print(m)
n=squere(23)
print(n)

