# Student Score Analyser

Write a function that takes a list of student test scores (numbers between 0-100) and performs the following tasks:

1. Calculate the class average
2. Find the highest and lowest scores
3. Count how many students passed (score >= 50)
4. Return these values in a suitable format

Example Input:

scores = [45, 78, 92, 33, 65, 89, 54, 23]

Expected Output:

{
    "average": 59.875,
    "highest": 92,
    "lowest": 23,
    "passes": 5
}

# Vending Machine Simulator

A vending machine company wants to write a function that simulates its products. The function takes a list of products with their names and prices, and a specific amount of money inserted by the user. The function needs to determine:

1. Whether the user has enough money to buy each product
2. If so, calculate the change owed to the user
3. Return a list of products that the user can afford, along with the change owed

Example input:

products = [
    {"name": "Soda", "price": 1.50},
    {"name": "Chips", "price": 2.00},
    {"name": "Candy", "price": 0.75}
]
money_inserted = 5.00

Expected Output:

[
    {"product": "Soda", "change": 3.50},
    {"product": "Chips", "change": 3.00},
    {"product": "Candy", "change": 4.25}
]
