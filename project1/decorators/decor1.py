def decor(fun):
    def inner(x,y):
        price=fun(x,y)
        if price>=10000:
            price=price-price*0.10
            return price

        else:
            price<=10000
            price=price-price*0.05
            return price
    return inner
@decor
def calculate(no_of_item,price_per_item):
    return no_of_item*price_per_item
m=calculate(10,1000)
print(m)

