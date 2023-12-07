MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

prompt = input("What would you like? (espresso/latte/cappuccino): ")

if prompt == "off":
    quit("Thanks for visiting, see you next time!")
money = 0
if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
    print("Insert money, please")
    q = int(input("How many quarters? "))
    q = q * 0.25
    d = int(input("How many dimes? "))
    d = d * 0.10
    n = int(input("How many nickels? "))
    n = n * 0.05
    p = int(input("How many pennies? "))
    p = p * 0.01
    money = q + d + n + p
    if prompt == "espresso":
        if money < MENU["espresso"]["cost"]:
            print("Sorry, you're to poor! Money returned")
            print(f"You inserted ${money} and espresso is ${MENU['espresso']['cost']}")
        else:
            print(f"You inserted ${money}.")
            money = money - MENU["espresso"]["cost"]
            print(f"Here is your change: ${money}")
    if prompt == "latte":
        if money < MENU["latte"]["cost"]:
            print("Sorry, you're to poor! Money returned")
            print(f"You inserted ${money} and latte is ${MENU['latte']['cost']}")
        else:
            print(f"You inserted ${money}.")
            money = money - MENU["latte"]["cost"]
            print(f"Here is your change: ${money}")
    if prompt == "cappuccino":
        if money < MENU["cappuccino"]["cost"]:
            print("Sorry, you're to poor! Money returned")
            print(f"You inserted ${money} and cappuccino is ${MENU['cappuccino']['cost']}")
        else:
            print(f"You inserted ${money}.")
            money = money - MENU["cappuccino"]["cost"]
            print(f"Here is your change: ${money}")
if prompt == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
    print(resources)
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
