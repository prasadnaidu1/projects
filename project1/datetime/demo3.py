#take two dates from user as input and compare two dates.
import datetime
d1,m1,y1=[int(x) for x in input('enter your date of birth(dd/mm/yyy)').split('/')]
d2,m2,y2=[int(x) for x in input('enter your life partner date of birth(dd/mm/yyy').split('/')]
bd1=datetime.date(day=d1,year=y1,month=m1)
bd2=datetime.date(day=d2,month=m2,year=y2)
if bd1==bd2:
    print('you and your life partner ages are same')
elif bd1>bd2:
    print('your life partner more than age of yours')
else:
    print('you have more age than your life partner')