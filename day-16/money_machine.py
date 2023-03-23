class MoneyMachine:
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    
    def __init__(self):
        pass
    
    def insert_money(self):
        inserted_money = 0.0
        for coin in self.COIN_VALUES:
            inserted_money += int(input(f"How many {coin}? ")) * self.COIN_VALUES[coin]
        return inserted_money
        
    def is_money_enough(self, inserted_money, drinks_cost):
        if inserted_money >= drinks_cost:
            return True