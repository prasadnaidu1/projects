#print current system date and time separately and combined.
import datetime
td=datetime.datetime.today()
print(td)
tdt=datetime.datetime.today()
print('date:',tdt.date())
print('time:',tdt.time())
