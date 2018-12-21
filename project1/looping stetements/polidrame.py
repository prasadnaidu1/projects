number=int(input('enter a number'))
temp=number
reverse=0
while number!=0:
    i=number%10
    reverse=reverse*10+i
    number=number//10
if reverse==temp:
    print(temp,'is a polindrame')
else:
    print(temp,'is not polindrame')