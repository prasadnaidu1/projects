def discount(fun):
    def inner(x,y):
        price=fun(x,y)
        if price>=10000:
            price=price-price*0.10
            return price
    return inner

@discount
def calculate(no_of_items,price_per_amount):
    return no_of_items*price_per_amount
#calling block
final_value=calculate(16,1000)
print('fanal_value=',final_value)
