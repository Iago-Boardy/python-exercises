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

#Write your code below this line 👇

import random

computer_choose = random.randint(0, 2)

print("Welcome to the Rock, Paper, Scissors Game!")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if choose == 0:
  print(rock)
elif choose == 1:
  print(paper)
elif choose == 2:
  print(scissors)

print("Computer choose:")

if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose == 2:
    print(scissors)

if choose == 0 and computer_choose == 2:
    print("You win!")
elif choose == 1 and computer_choose == 0:
    print("You win!")
elif choose == 2 and computer_choose == 1:
    print("You win!")
elif choose == computer_choose:
    print("It's a draw")
elif choose >= 3 or choose < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You lose the game!")
