# from menu_drink import Drink

class CoffeeMaker:
    INGREDIENT_CONSUMPTION = {"espresso": {"water": 50,
                                           "milk": 0,
                                           "coffee": 18},
                              "latte": {"water": 200,
                                        "milk": 150,
                                        "coffee": 24},
                              "cappuccino": {"water": 250,
                                             "milk": 50,
                                             "coffee": 24}}
    
    def __init__(self):
        self.initial_resources = {"water": 300, "milk": 200, "coffee": 100}
        self.resource_list = ["water", "milk", "coffee"]
    
    def is_resource_sufficient(self, drink) -> bool:
        if (drink.water > self.initial_resources.get("water")) or (drink.coffee > self.initial_resources.get("coffee")) or (drink.milk > self.initial_resources.get("milk")):
            print("There is not enough resources")
            return False
        else:
            return True
    
    def make_coffee(self, drink):
        for resource in self.resource_list:
            self.initial_resources[resource] -= self.INGREDIENT_CONSUMPTION[drink.name][resource]
        print(f"Here is your {drink.name}☕")