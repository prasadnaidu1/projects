def dadecor(fun):
    def inner():
        sal=fun()
        daily_allowences=sal*0.10
        sal+=daily_allowences
        print('daily_allowences=',daily_allowences)
        return sal

    return inner
def hradecor(fun):
    def inner():
        sal=fun()
        human_resource=sal*0.20
        sal+=human_resource
        print('human_resource=',human_resource)
        return sal
    return inner
def tradecor(fun):
    def inner():
        sal=fun()
        travelling_allowences=sal*0.05
        sal+=travelling_allowences
        print('travelling_allowences=',travelling_allowences)
        return sal
    return inner
@dadecor
@hradecor
@tradecor

def salary():
    return 30000
totalsalary=salary()
print('totalsalary=',totalsalary)
