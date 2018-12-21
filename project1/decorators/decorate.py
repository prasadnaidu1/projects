def dadecor(fun):
    def inner():
        sal=fun()
        daily_allowence=sal*0.10
        sal+=daily_allowence
        print('daily_allowence=',daily_allowence)



        return sal
    return inner
def hrdecor(fun):
        def inner():
            sal=fun()
            human_resourse=sal*0.20
            sal+=human_resourse
            print('human_resourse=',human_resourse)
            return sal
        return inner

def tadecor(fun):
        def inner():
            sal=fun()
            travelling_allowence=sal*0.05
            sal+=travelling_allowence
            print('travelling_allowence=',travelling_allowence)
            return sal
        return inner
@tadecor

@hrdecor
@dadecor



def salary():
    return 20000
m=salary()
print(m)

