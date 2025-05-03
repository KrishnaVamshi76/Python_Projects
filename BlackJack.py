from random import choice

def play_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=choice(cards)
    return card 

def sumofcards(alt):
    if sum(alt) == 21 and len(alt) == 2:

        return 0 

    if 11 in alt:
        alt.remove(11)
        alt.append(1)

    return sum(alt)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return"Its a draw Play Again"
    elif user_score==0:
        return "You Won the Black Jack"
    elif user_score>21:
        return "You Have crossed 21, So you will lose!!"
    elif computer_score>21:
        return "Computer Crossed 21, You Win!!"
    elif user_score > computer_score:
        return "You win!!"
    else:
        return "You lose!!"


def game():
    user_cards=[]
    computer_cards=[]
    user_score=0
    computer_score=0

    for i in range(2):
        user_cards.append(play_cards())
        computer_cards.append(play_cards())
    game_over=False
    while not game_over:
        user_score=sumofcards(user_cards)
        computer_score=sumofcards(computer_cards)
        print(f"You Have{user_cards} cards\n and current score is {user_score} ")
        print(f"computer has [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_play = input("Enter 'y' to draw a card, 'n' to pass: ").lower()
            if user_play == "y":
                user_cards.append(play_cards())
            else:
                game_over = True

    # Computer's turn (draws until at least 17)
    while computer_score < 20 and computer_score != 0:
        computer_cards.append(play_cards())
        computer_score = sumofcards(computer_cards)
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))        

while True:
    again=input("Wanna Play again type y or else type n:\t").lower()

    if again=="y":
        print("\n"*30)
        game()
    else:
        print("sad to see you go!!")
        break    
