from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_maker.report()
my_money_machine.report()

is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What item would you like? ({option}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
