import random
n=int(input('enter a number 1-10'))
i=(random.randint(1,10))
if n==i:
    print('your no=',n)
    print('random no=',i)
    print('yes')

else:
    print('yourrno=',n)
    print('random no=',i)
    print('wrong')
