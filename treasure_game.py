print("Welcome to Treasure Yashwantha island game")
direction=input("Choose Left or Right: ").lower()

if direction=="left":
    print("okay!")
    wait_or_swim=input("Choose wait or swim: ").lower()
    if wait_or_swim=="wait":
        print("okay! you are waiting, hey there is a boat \n now choose the color")
        colour_1=input("select red, yellow, blue:").lower()
        if colour_1=="yellow":
         print("Yess! you won the teasure!!!")
        elif colour_1=="red": 
         print("sorry, Here there are red monsters, Game over!")
        elif colour_1=="blue":
            print("Sorry, You have fell into water, Game Over!")
    else :
        print("You should have wait rather than swimming, Go and do your work now!!")
else:
    print("Game Over!! you have choosen wrong Direction")