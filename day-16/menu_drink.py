class Drink:
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.cost = cost


class Menu:
    def __init__(self):
        self.menu_list = [Drink("espresso", water=50, milk=0, coffee=18, cost=1.5),
                          Drink("latte", water=200, milk=150, coffee=24, cost=2.5),
                          Drink("cappuccino", water=250, milk=50, coffee=24, cost=3)]
        
    def show_menu(self):
        for drink in self.menu_list:
            print(f"{drink.name}, {drink.cost}")
        
    def find_drink(self, order_name):
        for drink in self.menu_list:
            if drink.name == order_name.casefold():
                return drink
        return False
    
    def show_ingredients(self):
        for drink in self.menu_list:
            print(f"{drink.name.upper()} water: {drink.water}, milk: {drink.milk}, coffee: {drink.coffee}$")
    
    