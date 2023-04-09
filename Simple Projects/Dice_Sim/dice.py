import random

print("""
Let's Play a Game of Chance

1: Dice Rolls
2: Coin Flips
3: Guessing a number

""")

user_choice = input("Select Your Choice (1 - 3):  ")


if user_choice == '1':
    sides = int(input("How Many Sides? "))
    rolls = int(input("How Many Rolls? "))
    for i in range(1,rolls+1):
        x = random.randint(1,sides)
        print(f'On Roll {i}: {x}')


if user_choice == '2':
    toss = int(input("How Many Tosses? "))
    coins = ['Heads', 'Tails']
    for i in range(1,toss+1):
        x = random.choice(coins)
        print(f'On Flip {i}: {x}')


if user_choice == '3':

    print("""
    I will pick a number between 1 and 50. 
    The goal is to pick the number that I am thinking.
    You will have five attempts to guess?
    Are you ready?
    """)

    computer_guess = random.randint(1,50)
    chance = 1

    while chance < 6:
        for i in range(1,6):
            user_guess = int(input(f'Guess {i} - What Is Your Guess?  '))
            if computer_guess != user_guess:
                if computer_guess < user_guess:
                    print(f'Your Guess of {user_guess} is high. Try again.')
                    chance += 1
                elif computer_guess > user_guess:
                    print(f'Your Guess of {user_guess} is low. Try again.')
                    chance += 1
                else:
                    break
            else:
                print(f'Great Job! Your Guess of {user_guess} Was Correct!')
                break
    print(f'Sorry, you have used all your chances. My choice was the number {computer_guess}')
