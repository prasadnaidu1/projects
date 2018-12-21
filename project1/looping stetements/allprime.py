n=int(input('enter a n value:'))
for i in range(1,n):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
      print(i,end='  ')
print('all prime numbers are between 1-50')