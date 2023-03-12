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


def kahve_tercih_et():
    coffe_choice = input("Ne tür kahve istersiniz? (espresso/latte/cappuccino): ")
    if coffe_choice.casefold() == "espresso":
        malzemeleri_kontrol_et("espresso")
    elif coffe_choice.casefold() == "latte":
        malzemeleri_kontrol_et("latte")
    elif coffe_choice.casefold() == "cappuccino":
        malzemeleri_kontrol_et("cappuccino")
    elif coffe_choice == "report":
        rapor_ver()
    elif coffe_choice.casefold() == "off":
        return False
    return True

def malzeme_azalt(kahve_turu):
    if kahve_turu == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif kahve_turu == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif kahve_turu == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["cappuccino"] -= 24
    return True

def malzemeleri_kontrol_et(kahve_turu):
    if kahve_turu == "espresso":
        if resources.get("water") >= 50 and resources.get("coffee") >= 18:
            malzeme_azalt("espresso")
            para_yukle("espresso")
        elif resources.get("water") < 50:
            print("Sorry there is not enough water.")
        if resources.get("coffee") < 18:
            print("Sorry there is not enough coffee.")
        
    elif kahve_turu == "latte":
        if (resources.get("water") >= 200) and (resources.get("coffee") >= 24) and (resources.get("milk") >= 150):
            malzeme_azalt("latte")
            para_yukle("latte")
        elif resources.get("water") < 200:
            print("Sorry there is not enough water.")
        if  resources.get("coffee") < 24:
            print("Sorry there is not enogh coffee.")
        if resources.get("milk") < 150:
            print("Sorry there is not enough milk.")
        
    elif kahve_turu == "cappuccino":
        if (resources.get("water") >= 250) and (resources.get("coffee") >= 24) and (resources.get("milk") >= 100):
            malzeme_azalt("cappuccino")
            para_yukle("cappuccino")
        elif resources.get("water") < 250:
            print("Sorry there is not enough water.")
        if  resources.get("coffee") < 24:
            print("Sorry there is not enogh coffee.")
        if resources.get("milk") < 100:
            print("Sorry there is not enough milk.")
    return True

def para_yukle(kahve_turu):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    parayi_kontrol_et(pennies=pennies, nickels=nickles, dimes=dimes, quarters=quarters, kahve_turu=kahve_turu)
    return True

def parayi_kontrol_et(pennies, nickels, dimes, quarters, kahve_turu):
    inserted_money = pennies*0.01 + nickels*0.05 + dimes*0.1 + quarters*0.25
    if kahve_turu == "espresso":
        if inserted_money > MENU.get("espresso").get("cost"):
            print("Here is ${} in change.".format(round(inserted_money - MENU.get("espresso").get("cost"),2)))
            print("Here is your espresso ☕. Enjoy!")
        elif inserted_money == MENU.get("espresso").get("cost"):
            print("Here is your espresso ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded.")
    elif kahve_turu == "latte":
        if inserted_money > MENU.get("latte").get("cost"):
            print("Here is ${} in change.".format(round(inserted_money - MENU.get("latte").get("cost"),2)))
            print("Here is your latte ☕. Enjoy!")
        elif inserted_money == MENU.get("latte").get("cost"):
            print("Here is your latte ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded.")
    elif kahve_turu == "cappuccino":
        if inserted_money > MENU.get("cappuccino").get("cost"):
            print("Here is ${} in change.".format(round(inserted_money - MENU.get("cappuccino").get("cost"),2)))
            print("Here is your cappuccino ☕. Enjoy!")
        elif inserted_money == MENU.get("cappuccino").get("cost"):
            print("Here is your cappuccino ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded.")
    return True

def rapor_ver():
    print("Mevcut su miktarı: {} mL.". format(resources.get("water")))
    print("Mevcut süt miktarı: {} mL.". format(resources.get("milk")))
    print("Mevcut kahve miktarı: {} g.". format(resources.get("coffee")))
    return True


while True:
    returning = kahve_tercih_et()
    if returning == False:
        break

print("Makine kapatıldı.")