
def get_ticket_price():
    price = float(input('Enter the price of one ticket: '))
    if price <= 0:
        print('The price of one ticket must be greater than zero. Try again!')
        return get_ticket_price()
    return price

ticket_price = get_ticket_price()

total = 0
for ticket_count in range (1, 21):
    price = ticket_price
    if ticket_count >= 10:
        price = ticket_price - (ticket_price * .1)
    total = total + price

print(total)



