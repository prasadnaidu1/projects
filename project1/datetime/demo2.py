#print object of date
import datetime
d1,m1,y1=[int(x) for x in input('enter the date of birth(dd/mm/yyy)').split('/')]
td=datetime.date(y1,m1,d1)
print('ypur datebirth is:',td)