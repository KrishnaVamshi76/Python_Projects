from random import choice
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("welcome to Hangman game")

words_list=["ashok","yashwantha","sujatha","vamshi","krishna","chinna"]

guess=choice(words_list)
lives=6
print(guess)
display=[]
for _ in range(len(guess)):
    display+="_"
print("".join(display))

while lives!=0:
    
    user_guess=input("Enter the letter to guess:\t").lower()
    if user_guess not in guess:
        lives-=1
    else:
     for i in range(len(guess)):
        if guess[i] == user_guess and display[i] == "_":
            display[i]=user_guess
            break
    print(f"*********Remaining lives: {lives}/6*********\nGuess the letter correctly")    
    print("".join(display))
    print(stages[lives])

    if lives==0:
        print("****************************YOU LOSE****************************")
        break  
    if "_" not in display:
        print("****************************YOU WIN****************************")