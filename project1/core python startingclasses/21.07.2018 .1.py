def ticket_cost(adult,child):
    ad_q=adult
    ch_q=child
    adult_cost=37555
    child_cost=adult_cost/3
    adult_amount=adult_cost*ad_q
    child_amount=child_cost*ch_q
    amount=adult_amount+ch
dis_count= amount*10/100
sub_total=amount-dis_count
service_tax=sub_total*7/100
tootal_amount=sub_total+service_tax
x = int(input('enter adult:'))
y = int(input('enter child:'))
print('amount:')
print('dis_count10%')
print('service _tax7%')
print('total_amount:')
ticket_cost(x,y)


