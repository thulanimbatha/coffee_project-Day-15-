# Day project - coffee machine
from data import MENU, resources

money = 0
machine_off = False

#  TODO 2: Check if user entered 'report' or 'off'
def button_off():
    '''Stops application'''
    print("Turning machine off...")
    return

# TODO 3: Print report
def button_report():
    '''Prints resources'''
    global money
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: R{money}")

# # TODO 4: Check is resources are sufficient
def resource_check(selection_ingredients):
    '''Returns True if there are resources available for selection, else Returns False'''
    for item in selection_ingredients:
        if selection_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO 6: check if there is enough money
def is_enough_money(total, bev_cost):
    '''Returns True if total >= the price of the beverage'''
    if total >= bev_cost:
        global money
        money += bev_cost
        print(f"The change is: R{round(total - bev_cost, 2)}")
        return True
    else:
        print("Sorry. Not enough money. Money refunded")
        return False

# TODO 7: Make beveage
def make_beverage(selection_ingredients):
    for item in selection_ingredients:
        resources[item] -= selection_ingredients[item]

while not machine_off:
    # TODO 1: PROMPT USER
    user_input = input("what would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        button_off()
        machine_off = True
    elif user_input == "report":
        button_report()
    else:
        # Check if resources are sufficient
        if resource_check(MENU[user_input]['ingredients']):
            # TODO 5: process coins
            coins = int(input("Please enter number of 10 cents: ")) * 0.1
            coins += int(input("Please enter number of 20 cents: ")) * 0.2
            coins += int(input("Please enter number of 50 cents: ")) * 0.5
            coins += int(input("Please enter number of 1 rands: ")) * 1
            # check if theres enough money
            is_enough_money(coins, MENU[user_input]['cost'])
            # make beverage
            make_beverage(MENU[user_input]['ingredients'])
            print(f"Dankie! Enjoy your {user_input}!")


