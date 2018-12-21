def ticket_cost(adult,child):
    print('amount=', amount)
    print('discount=', discount)
    print('service_tax=', service_tax)
    print('total_cost=', total_cost)
x=int(input('enter adults no:'))
y=int(input('enter childs no:'))
adult_cost=37555.0
child_cost=adult_cost/3
amount = adult_cost+ child_cost
discount = (adult_cost + child_cost) * 10 / 100
service_tax = amount* 7 / 100
total_cost = (adult_cost+ child_cost + service_tax) - discount
ticket_cost(x,y)

