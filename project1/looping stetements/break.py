import random
while True:
    i=int(input('guess a number from 0-20:'))
    j=random.randint(0,20)
    if i!=j:
       print('your no=',i)
       print('random no:',j)
       print('guess is wrong')
       continue
    print('your no=',i)
    print('random number=',j)
    print('guess is correct')
    break
print('*******end********')

