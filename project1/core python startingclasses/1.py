def ticket_cost(adults,childs):
    ad_q=adults
    ch_q=childs
    print('cost=',cost)
    print('discount=',discount)
    print('service_tax=',service_tax)
    print('total_cost=',total_cost)

x=int(input('enter adults no:'))
y=int(input('enter childs no:'))
adults=37555.0
childs=adults/3
adults_cost=adults*ad_q
childs_cost=childs*ch_q
cost = adults + childs
discount = (adults + childs) * 10 / 100
service_tax = cost * 7 / 100
total_cost = (adults + childs + service_tax) - discount
ticket_cost(x,y)




