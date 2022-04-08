MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0
change = 0
continue_serving = True

def print_report(resources, money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def coffee_choice(MENU, resources):
    for x in resources:
        resources[x] = resources[x] - MENU[choice]['ingredients'][x]
    return resources


def process_money():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money



while continue_serving == True:
    choice = input(" What would you like? (espresso, latte, cappucino): ")
    enough_ingredients = True
    if choice == 'report':
        print_report(resources, money)
    elif choice == 'off':
        continue_serving = False
    else:
        if resources['water'] >= MENU[choice]['ingredients']['water'] and resources['milk'] >= MENU[choice]['ingredients']['milk'] and resources['coffee'] >= MENU[choice]['ingredients']['coffee']:
            total_money = float(process_money())
            if total_money < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded")
            else:
                coffee_choice(MENU, resources)
                money += MENU[choice]['cost']
                change = round(total_money - MENU[choice]['cost'], 2)
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {choice}. Enjoy")
        else:
            for x in resources:
                if resources[x] <= 0:
                    print(f"Not enough {x}")
            enough_ingredients = False

