number=int(input('enter a number'))
sum=0
n=len(str(number))
temp=number
while number!=0:
    i=number%10
    sum=sum+(i**n)
    number=number//10
if sum==temp:
    print(temp,'is a armstrong')
else:
    print(temp,'is not armstrong')


