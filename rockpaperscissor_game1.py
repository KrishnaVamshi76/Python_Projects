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
user_choice = int(input("Enter your choice 0 for rock, 1 for paper, 2 for scissors): \n").lower())

if user_choice >= 0 and user_choice <= 2:
 print("You have choosen:", user_choice)
 print(choices[user_choice])
computer_choice = random.randint(0,2)
print("Computer choose: ",computer_choice)
print(choices[computer_choice])
if user_choice>=3:
 print("you have enter invalid input, so you have lose!")
elif user_choice==0 and computer_choice==2:
    print("You Win!!")
elif user_choice == 2 and computer_choice == 0:
   print("You lost!!")
elif computer_choice>user_choice:
    print("You lose!")
elif user_choice==computer_choice:
    print("It's a Draw")
elif computer_choice<user_choice:
    print("You win!")
