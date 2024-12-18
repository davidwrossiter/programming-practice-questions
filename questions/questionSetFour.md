# Pizza Shop Calculator

Create a program that calculates the total cost and preparation time for pizza orders.

Base Prices:

    Small: £8.99
    Medium: £11.99
    Large: £14.99

Toppings (£0.80 each):

    Pepperoni
    Mushrooms
    Onions
    Peppers
    Extra Cheese

Special Rules:

    Happy Hour (5PM-7PM): 20% discount
    Prep Time: 15 mins base + 2 mins per topping
    Large Order Bonus: Orders over £30 get free delivery (normally £2.50)
    Combo Deal: When ordering 2+ pizzas, apply 10% discount

Example input:
```
order = {
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
    "time": "17:30",  # 5:30 PM
    "delivery": True
}
```

Expected output:
```
{
    "subtotal": 22.78,
    "discount": 4.56,  # (20% happy hour + 10% combo)
    "delivery_fee": 2.50,
    "total": 20.72,
    "prep_time": 19  # minutes
}
```
