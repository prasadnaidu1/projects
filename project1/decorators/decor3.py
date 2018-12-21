def decor(fun):
    def inner(x,y):
        purchase=fun(x,y)
        if purchase>4000:
            purchase-=purchase*0.10
            return purchase
    return inner
@decor
def add(no_of_item,price_per_item):
    return no_of_item*price_per_item
#calling block
k=add(1000,500)
print(k)


