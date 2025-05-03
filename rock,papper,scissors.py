import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissors!")
choices = [rock, paper, scissors]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print("You have choosen:", choices)
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    print("coomputer choosen:",computer_choice)
    if user_choice==computer_choice:
         print("It's Draw Match")
    elif user_choice == "rock":
        if computer_choice == "scissors":
             print("You have win!")
        else:
             print("computer choose paper. So, you have lost")
    elif user_choice == "paper":
        if computer_choice == "rock":
             print("You have win!")
        else:
             print(" computer choose scissors. So, you have lost")
    elif user_choice == "scissors":
        if computer_choice == "paper":
             print("You have win")
        else:
         print("computer choose rock. So, you have lost")