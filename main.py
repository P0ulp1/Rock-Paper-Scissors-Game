# Pre Requirements
import random

# ASCII Art
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

# Real Code
ascii = [rock, paper, scissors]

player_choice = int(input("What do you choose ? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(f'''{ascii[player_choice]}''')

print("Computer choose :")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if player_choice == computer_choice:
    print("Tie.")
elif player_choice == 0 and computer_choice == 1:
    print("You loose.")
elif player_choice == 0 and computer_choice == 2:
    print("You Win !")
elif player_choice == 1 and computer_choice == 0:
    print("You Win !")
elif player_choice == 1 and computer_choice == 2:
    print("You loose.")
elif player_choice == 2 and computer_choice == 0:
    print("You loose.")
elif player_choice == 2 and computer_choice == 1:
    print("You Win !")
else:
    print("This line can't be printed.")
