import random

choices = "Paper \n Rock \n Scissors \n Lizard \n Phoenix \n Match \n Scientist"

while True:
  actions = ["paper","rock","scissors", "lizard", "phoenix", "match", "scientist"]
  human_action = input(f'Please select one of the following: \n {choices} \n').lower()
  
  if human_action not in actions:
    print(f'Your choice of {human_action.capitalize()} is not a valid choice.')
    print('Please select again.')
    break
  computer_action = random.choice(actions)
  print(f'You selected {human_action.capitalize()}. Your opponent selected {computer_action.capitalize()}.')
  
  if human_action == computer_action:
    print(f"Both players selected {human_action}. It is a tie game!")
  elif (human_action == 'rock' and computer_action == 'lizard' or computer_action == 'match' or computer_action == 'scissors'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  elif (human_action == 'paper' and computer_action == 'rock' or computer_action == 'phoenix' or computer_action == 'scientist'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  elif (human_action == 'scissors' and computer_action == 'paper' or computer_action == 'lizard' or computer_action == 'match'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  elif (human_action == 'scientist' and computer_action == 'phoenix' or computer_action == 'rock' or computer_action == 'scissors'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  elif (human_action == 'match' and computer_action == 'lizard' or computer_action == 'paper' or computer_action == 'burns'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  elif (human_action == 'phoenix' and computer_action == 'rock' or computer_action == 'scissors' or computer_action == 'match'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  elif (human_action == 'lizard' and computer_action == 'phoenix' or computer_action == 'paper' or computer_action == 'scientist'):
    print(f"{human_action.capitalize()} beats {computer_action.capitalize()}. You win!")
  else:
    print(f"{computer_action.capitalize()} beats {human_action.capitalize()}. Sorry, you lose!")

  replay = input("Do you want to play again? (y/n)")
  if replay.lower() == 'n':
    break
