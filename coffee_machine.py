MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit=0

def check_resources(ordered):
    for make in ordered:
     if ordered[make]>resources[make]:
        print(f"Sorry there is not enough {make}.")
        return False
    return True

def process():
    print("Please input the coins")
    total = int(input("how many Rs.1 coins?: ")) * 1
    total += int(input("how many Rs.2 coins?: ")) * 2
    total += int(input("how many Rs.5 coins?: ")) * 5
    total += int(input("how many Rs.10 notes?: ")) * 10
    return total

def compareprice(money_recieved,costed):
   
   if money_recieved>costed:
      change=round(money_recieved-costed,2)
      print("Here is your change:",change)
      global profit
      profit+=costed      
      return True
   else:
      print("Sorry that's not enough money. Money refunded.")
      return False
   

def makecoffee(drink_name,remaining):
    for item in remaining:
       resources[item]-=remaining[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

stop=True
print("Welcome to Krishna\'s Coffee Machine")

while stop:

    user_input=input("What would you like to have (latte/expresso/cappuccino) or else to exit press \'no\':\n").lower()

    if user_input=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_input=="no":
       print("Ok Bye!")
       stop=False
    else:
       if user_input in MENU:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
         payment = process()
         if compareprice(payment,drink["cost"]):
            makecoffee(user_input,drink["ingredients"])
         else:
            print("you have entered wrong coffee list")
            stop=False
        
    
        