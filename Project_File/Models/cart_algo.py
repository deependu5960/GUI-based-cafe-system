cart_detail = {}
def add_to_cart(name, price, img_url, quantity=1):
    cart_detail.update({name : {"price": price, "img_url": img_url, "quantity": quantity}})
    # print(cart_detail)
    return cart_detail

def total_price():
    sum = 0
    for i in cart_detail:
        sum = sum + cart_detail[i]["price"]
    return sum
