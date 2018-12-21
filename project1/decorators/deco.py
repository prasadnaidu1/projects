def add(fun):
    def inner(x,y):
        price=fun(x,y)
        if price>=4000:
            price=price-price*0.10
            return price
    return inner
@add
def purchase(no_of_items,price_per_item):
    return no_of_items*price_per_item
k=purchase(12,3000)
print(k)
