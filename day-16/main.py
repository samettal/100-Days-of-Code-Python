from menu_drink import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    order_name = input("Which coffee do you want?(espresso, latte, cappuccino): ")
    if order_name.casefold() == "r":
        money_machine.report()
        continue
    if order_name.casefold() == "s":
        coffe_maker.report()
        continue
    drink = menu.find_drink(order_name)
    if drink != False:
        if coffe_maker.is_resource_sufficient(drink) == True:
            inserted_money = money_machine.insert_money()
            if money_machine.is_money_enough(inserted_money=inserted_money, drinks_cost=drink.cost) == True:
                coffe_maker.make_coffee(drink)
                money_machine.money_reserve -= drink.cost
            else:
                print(f"There is not enough money! Please insert {drink.cost - money_machine.money_reserve}$")
                continue
    else:
        print("Lütfen doğru bir içecek ismi giriniz\n")
        continue