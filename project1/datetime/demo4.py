#using date formating codes write a program
import datetime
td=datetime.datetime.today()
print(td)
mystr=td.strftime('%a,%d %b,%Y')
print(mystr)
mystr2=td.strftime('%I:%M:%S %p')
print(mystr2)