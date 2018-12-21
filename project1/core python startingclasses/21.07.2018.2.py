def calculate_find(enternumberofadults ,enternumberofchilds):
    aduldsprice = 37555.0
    childsprice = 12518.3
    cost = aduldsprice + childsprice
    tax = (cost * 7) / 100
    discount = (cost+tax)*10 / 100
    d=(aduldsprice+childsprice+tax)-discount
    return d
x=input('enteradults,enter chids:')
print(x)