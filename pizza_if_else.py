print("Welcome to Pizzajoy!!")
pizza_type=input("There are 3 types of pizzas, select s, m, l:\n")
pepperoni=input("Need pepperoni select y or n:\n")
extra_chesse=input("Need Extra Chesse select y or n:\n")
bill=0

if pizza_type=="s":
    bill=120
    print(f"The small pizza is Rs.{bill}")
elif pizza_type=="m":
    bill=160
    print(f"The medium pizza is Rs.{bill}")
elif pizza_type=="l":
    bill=200
    print(f"The large pizza is Rs.{bill}")
if pepperoni=="y":
    bill= bill+10
    print(f"The Bill after adding pepperoni is Rs.{bill}")
elif extra_chesse=="y":
     bill+=15
     print(f"The bill after adding chesse is Rs.{bill}")
     print(f"The amount after adding chesse and pepperoni is Rs.{bill}")
else:
    print(f"The bill amount for selected pizza is Rs.{bill}")
