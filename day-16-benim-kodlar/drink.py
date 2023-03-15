class Drink:
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.cost = cost
    
    
    
    
class Menu:
    def __init__(self):
        self.menu_list = []
        self.menu_list.append(Drink("espresso", 200, 18, 0, 1.5))
        self.menu_list.append(Drink("latte", 200, 24, 150, 2.5))
        self.menu_list.append(Drink("cappuccino", 250, 24, 100, 3.0))
        return self.menu_list
    
    def find_drink(self, order_name):
        for drink in self.menu_list:
            if drink.name == order_name:
                return True
        return False
    