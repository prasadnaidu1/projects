def get_ticket_price(adulsprice,childsprice):
    aduldsprice = 37555.0
    childsprice = 12518.3
    totalcost = aduldsprice + childsprice
    discount = (totalcost ) * 10 / 100
    servicetax = (totalcost * 7) / 100
    ticketprice = (aduldsprice + childsprice + discount) - servicetax
    return ticketprice
x=int(input('enter adulds'))
y=int(input('enter child'))
print('totalcost')
print('discount')
print('servicetax')
print('ticketprice')



