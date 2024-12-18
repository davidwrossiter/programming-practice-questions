def costfinder(order):
    subtotal=0.00
    prep=0
    delivery=0.00
    discount=0.00
    for i in order["pizzas"]:
        prep+=15
        if i["size"] == "small":
            subtotal += 8.99
        elif i["size"] == "medium":
            subtotal += 11.99
        else:
            subtotal += 14.99
        for j in i["toppings"]:
            subtotal += 0.80
            prep+=2
    if subtotal <= 30.00 and order["delivery"]==True:
        delivery=2.50
    if len(order["pizzas"]) >= 2:
        discount=round(subtotal/10,2)
    receipt={
        "subtotal":round(subtotal,2),
        "discount":discount,
        "delivery":delivery,
        "total":round(subtotal+delivery-discount,2),
        "preptime":prep
    }
    return receipt

cost = costfinder({
    "pizzas": [
        {
            "size": "medium",
            "toppings": ["pepperoni", "mushrooms"]
        },
        {
            "size": "small",
            "toppings": ["extra cheese"]
        }
    ],
    "delivery": True
})

print(cost)