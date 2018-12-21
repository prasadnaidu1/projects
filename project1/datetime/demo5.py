import datetime
d1,m1,y1=[int(x) for x in input('enter first date(dd/mm/yyy)').split('/')]
d2,m2,y2=[int(x) for x in input('enter second date(dd/mm/yyy)').split('/')]
firstdate=datetime.date(day=d1,year=y1,month=m1)
seconddate=datetime.date(day=d2,year=y2,month=m2)
delta=firstdate-seconddate
days=int(delta.days)
print('difference between two dates in years:',days//365)
print('difference between two dates in months:',days//30)
print('difference between two dates in weeks:',days//7)
print('difference between two dates in days:',days)