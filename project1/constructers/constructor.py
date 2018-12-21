class reservation:
    availableseats=200
    def __init__(self,requiredseats):
        self.requiredseats=requiredseats
    def reserve(self):
        if reservation.availableseats>=self.requiredseats:
            reservation.availableseats-=self.requiredseats
            return 'seats are reserved'
        else:
            return 'sorry {} seats are only available'.format(reservation.availableseats)
#calling block
r1=reservation(78)
msg=r1.reserve()
print(msg)
print('-------')
r2=reservation(200)
msg=r2.reserve()
print(msg)