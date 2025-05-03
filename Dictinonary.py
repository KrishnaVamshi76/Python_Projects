def highest_bid(dic_bids):
    highest_bidder=0 
    winner=''
    for bidder in dic_bids:
            bidder_amount=dic_bids[bidder]
            if bidder_amount>highest_bidder:
              highest_bidder=bidder_amount
              winner=bidder
    print(f"Congrats {winner} have highest bid of Rs.{highest_bidder}")

dic={}
should_conti=True

while should_conti:

    user_input=input("Enter Your name:\t")
    user_price=int(input("Enter the amount: \t"))

    dic[user_input]=user_price
    i=0
    continue_play=input("Wanna Bid more then type \'y\' else \'n\':").lower()

    if continue_play=="n":  
        should_conti=False
        highest_bid(dic)
    else:
        continue_play=="y"
        print("\n"*20)